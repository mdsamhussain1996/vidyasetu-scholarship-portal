// VidyaSetu Application Core Engine

(function () {
  'use strict';

  // State
  const state = {
    section: 'all', // 'all', 'india', 'abroad'
    searchQuery: '',
    level: 'all',
    type: 'all',
    category: 'all',
    stream: 'all',
    sort: 'default',
    activeChip: null,
    viewMode: 'grid', // 'grid' or 'compact'
    bookmarks: JSON.parse(localStorage.getItem('vidyasetu_bookmarks') || '[]'),
    compare: [],
    theme: localStorage.getItem('vidyasetu_theme') || 'light'
  };

  // DOM Elements Cache
  const els = {
    // Theme
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeIcon: document.getElementById('themeIcon'),

    // Metrics
    metricIndiaCount: document.getElementById('metricIndiaCount'),
    metricAbroadCount: document.getElementById('metricAbroadCount'),
    metricGovCount: document.getElementById('metricGovCount'),
    metricPvtCount: document.getElementById('metricPvtCount'),
    metricInternCount: document.getElementById('metricInternCount'),

    // Section Tabs
    tabSectionAll: document.getElementById('tabSectionAll'),
    tabSectionIndia: document.getElementById('tabSectionIndia'),
    tabSectionAbroad: document.getElementById('tabSectionAbroad'),
    badgeAll: document.getElementById('badgeAll'),
    badgeIndia: document.getElementById('badgeIndia'),
    badgeAbroad: document.getElementById('badgeAbroad'),

    // Filters
    searchInput: document.getElementById('searchInput'),
    filterLevel: document.getElementById('filterLevel'),
    filterType: document.getElementById('filterType'),
    filterCategory: document.getElementById('filterCategory'),
    filterStream: document.getElementById('filterStream'),
    sortOrder: document.getElementById('sortOrder'),
    chips: document.querySelectorAll('.chip-btn'),
    btnResetFilters: document.getElementById('btnResetFilters'),

    // View & Results
    cardsGridContainer: document.getElementById('cardsGridContainer'),
    noResultsState: document.getElementById('noResultsState'),
    btnResetNoResults: document.getElementById('btnResetNoResults'),
    resultsCountText: document.getElementById('resultsCountText'),
    viewModeGrid: document.getElementById('viewModeGrid'),
    viewModeCompact: document.getElementById('viewModeCompact'),

    // Bookmarks & Badges
    btnSavedBookmarks: document.getElementById('btnSavedBookmarks'),
    savedCountBadge: document.getElementById('savedCountBadge'),

    // Detail Modal
    detailModal: document.getElementById('detailModal'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalBadgeGroup: document.getElementById('modalBadgeGroup'),
    modalTitle: document.getElementById('modalTitle'),
    modalAgency: document.getElementById('modalAgency'),
    modalAmount: document.getElementById('modalAmount'),
    modalCoverage: document.getElementById('modalCoverage'),
    modalEligibility: document.getElementById('modalEligibility'),
    modalLevels: document.getElementById('modalLevels'),
    modalStreams: document.getElementById('modalStreams'),
    modalDocChecklist: document.getElementById('modalDocChecklist'),
    modalApplicationSteps: document.getElementById('modalApplicationSteps'),
    modalDeadline: document.getElementById('modalDeadline'),
    modalOfficialLink: document.getElementById('modalOfficialLink'),
    modalBookmarkBtn: document.getElementById('modalBookmarkBtn'),

    // Wizard
    btnOpenWizard: document.getElementById('btnOpenWizard'),
    btnHeroWizard: document.getElementById('btnHeroWizard'),
    wizardModal: document.getElementById('wizardModal'),
    wizardCloseBtn: document.getElementById('wizardCloseBtn'),
    btnCancelWizard: document.getElementById('btnCancelWizard'),
    btnApplyWizard: document.getElementById('btnApplyWizard'),
    wizLevel: document.getElementById('wizLevel'),
    wizStream: document.getElementById('wizStream'),
    wizCategory: document.getElementById('wizCategory'),
    wizDestination: document.getElementById('wizDestination'),

    // Compare Drawer & Modal
    compareDrawer: document.getElementById('compareDrawer'),
    compareBadgeCount: document.getElementById('compareBadgeCount'),
    btnLaunchComparison: document.getElementById('btnLaunchComparison'),
    btnClearComparison: document.getElementById('btnClearComparison'),
    compareModal: document.getElementById('compareModal'),
    compareCloseBtn: document.getElementById('compareCloseBtn'),
    btnCloseCompareFooter: document.getElementById('btnCloseCompareFooter'),
    compareTableContainer: document.getElementById('compareTableContainer'),

    // Calendar Modal
    btnOpenCalendar: document.getElementById('btnOpenCalendar'),
    calendarModal: document.getElementById('calendarModal'),
    calendarCloseBtn: document.getElementById('calendarCloseBtn'),
    btnCloseCalendarFooter: document.getElementById('btnCloseCalendarFooter'),

    // Bookmarks Modal
    bookmarksModal: document.getElementById('bookmarksModal'),
    bookmarksCloseBtn: document.getElementById('bookmarksCloseBtn'),
    btnCloseBookmarksFooter: document.getElementById('btnCloseBookmarksFooter'),
    bookmarksListBody: document.getElementById('bookmarksListBody'),
    btnClearAllBookmarks: document.getElementById('btnClearAllBookmarks')
  };

  let activeModalItem = null;

  // Initialize App
  function init() {
    applyTheme(state.theme);
    updateMetrics();
    updateBookmarkBadge();
    bindEvents();
    renderCards();
  }

  // Theme Handling
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('vidyasetu_theme', theme);
    if (els.themeIcon) {
      els.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
  }

  function toggleTheme() {
    applyTheme(state.theme === 'dark' ? 'light' : 'dark');
  }

  // Calculate & Display Header Metrics
  function updateMetrics() {
    if (typeof GET_METRICS === 'function') {
      const m = GET_METRICS();
      if (els.metricIndiaCount) els.metricIndiaCount.textContent = m.india;
      if (els.metricAbroadCount) els.metricAbroadCount.textContent = m.abroad;
      if (els.metricGovCount) els.metricGovCount.textContent = m.government;
      if (els.metricPvtCount) els.metricPvtCount.textContent = m.private;
      if (els.metricInternCount) els.metricInternCount.textContent = m.internships;

      if (els.badgeAll) els.badgeAll.textContent = m.total;
      if (els.badgeIndia) els.badgeIndia.textContent = m.india;
      if (els.badgeAbroad) els.badgeAbroad.textContent = m.abroad;
    }
  }

  // Bookmark Management
  function isBookmarked(id) {
    return state.bookmarks.includes(id);
  }

  function toggleBookmark(id) {
    if (isBookmarked(id)) {
      state.bookmarks = state.bookmarks.filter(bId => bId !== id);
    } else {
      state.bookmarks.push(id);
    }
    localStorage.setItem('vidyasetu_bookmarks', JSON.stringify(state.bookmarks));
    updateBookmarkBadge();
    renderCards();
    if (activeModalItem && activeModalItem.id === id) {
      updateModalBookmarkBtn();
    }
  }

  function updateBookmarkBadge() {
    if (els.savedCountBadge) {
      els.savedCountBadge.textContent = state.bookmarks.length;
    }
  }

  // Compare Management
  function isInCompare(id) {
    return state.compare.includes(id);
  }

  function toggleCompare(id) {
    if (isInCompare(id)) {
      state.compare = state.compare.filter(cId => cId !== id);
    } else {
      if (state.compare.length >= 3) {
        alert('You can compare a maximum of 3 opportunities at a time.');
        return;
      }
      state.compare.push(id);
    }
    updateCompareDrawer();
    renderCards();
  }

  function updateCompareDrawer() {
    if (state.compare.length > 0) {
      els.compareDrawer.classList.add('active');
      els.compareBadgeCount.textContent = state.compare.length;
    } else {
      els.compareDrawer.classList.remove('active');
    }
  }

  // Filtering Logic
  function getFilteredOpportunities() {
    return OPPORTUNITIES_DATA.filter(item => {
      // 1. Section match (All, India, Abroad)
      if (state.section !== 'all' && item.section !== state.section) {
        return false;
      }

      // 2. Education level filter
      if (state.level !== 'all' && !item.educationLevel.includes(state.level)) {
        return false;
      }

      // 3. Funding authority filter (government / private)
      if (state.type !== 'all' && item.type !== state.type) {
        return false;
      }

      // 4. Opportunity category (Scholarship, Fellowship, Internship)
      if (state.category !== 'all' && item.category !== state.category) {
        return false;
      }

      // 5. Academic Stream
      if (state.stream !== 'all') {
        const streamLower = state.stream.toLowerCase();
        const matchesStream = item.streams.some(s => 
          s.toLowerCase().includes(streamLower) || s.toLowerCase().includes('all disciplines')
        );
        if (!matchesStream) return false;
      }

      // 6. Quick Chips
      if (state.activeChip) {
        switch (state.activeChip) {
          case 'after12':
            if (!item.educationLevel.includes('After 12th')) return false;
            break;
          case 'bachelor':
            if (!item.educationLevel.includes('Bachelor')) return false;
            break;
          case 'master':
            if (!item.educationLevel.includes('Master')) return false;
            break;
          case 'phd':
            if (!item.educationLevel.includes('PhD')) return false;
            break;
          case 'women':
            if (!item.targetGroup.some(t => t.toLowerCase().includes('women') || t.toLowerCase().includes('girl'))) return false;
            break;
          case 'govt':
            if (item.type !== 'government') return false;
            break;
          case 'abroad':
            if (item.section !== 'abroad') return false;
            break;
          case 'intern':
            if (item.category !== 'Internship') return false;
            break;
        }
      }

      // 7. Text Search Query
      if (state.searchQuery.trim() !== '') {
        const q = state.searchQuery.toLowerCase();
        const inTitle = item.title.toLowerCase().includes(q);
        const inAgency = item.fundingAgency.toLowerCase().includes(q);
        const inCoverage = item.coverage.toLowerCase().includes(q);
        const inEligibility = item.eligibility.toLowerCase().includes(q);
        const inTags = item.tags.some(t => t.toLowerCase().includes(q));
        const inStreams = item.streams.some(s => s.toLowerCase().includes(q));

        if (!inTitle && !inAgency && !inCoverage && !inEligibility && !inTags && !inStreams) {
          return false;
        }
      }

      return true;
    }).sort((a, b) => {
      if (state.sort === 'amount-high') {
        return (b.amountVal || 0) - (a.amountVal || 0);
      }
      if (state.sort === 'title-asc') {
        return a.title.localeCompare(b.title);
      }
      return 0; // Default curated order
    });
  }

  // Render Opportunity Cards
  function renderCards() {
    const list = getFilteredOpportunities();

    // Update count text
    els.resultsCountText.innerHTML = `Showing <span>${list.length}</span> ${
      state.section === 'india' ? 'Opportunities in India' : 
      state.section === 'abroad' ? 'Opportunities Abroad' : 
      'Total Opportunities'
    }`;

    // Handle empty state
    if (list.length === 0) {
      els.cardsGridContainer.innerHTML = '';
      els.noResultsState.style.display = 'block';
      return;
    } else {
      els.noResultsState.style.display = 'none';
    }

    // Grid vs Compact layout
    if (state.viewMode === 'compact') {
      els.cardsGridContainer.style.gridTemplateColumns = '1fr';
    } else {
      els.cardsGridContainer.style.gridTemplateColumns = 'repeat(auto-fill, minmax(390px, 1fr))';
    }

    els.cardsGridContainer.innerHTML = list.map(item => {
      const bookmarked = isBookmarked(item.id);
      const compared = isInCompare(item.id);
      const isIndia = item.section === 'india';

      const sectionBadge = isIndia 
        ? '<span class="badge badge-india">🇮🇳 India</span>'
        : '<span class="badge badge-abroad">🌍 Abroad</span>';

      const typeBadge = item.type === 'government'
        ? '<span class="badge badge-gov">🏛️ Govt Fund</span>'
        : '<span class="badge badge-pvt">💼 Private / CSR</span>';

      const catBadge = item.category === 'Internship'
        ? '<span class="badge badge-intern">🔬 Internship</span>'
        : `<span class="badge badge-gov">${item.category}</span>`;

      const levelPills = item.educationLevel.map(l => `<span class="level-tag">${l}</span>`).join('');

      return `
        <article class="opportunity-card" data-id="${item.id}">
          <div class="card-top-bar">
            <div class="badge-group">
              ${sectionBadge}
              ${typeBadge}
              ${catBadge}
            </div>

            <div class="card-actions-quick">
              <button 
                class="action-icon-btn ${bookmarked ? 'bookmarked' : ''}" 
                onclick="window.VidyaSetu.toggleBookmark('${item.id}')" 
                title="${bookmarked ? 'Remove Bookmark' : 'Save Scheme'}"
              >
                ${bookmarked ? '★' : '☆'}
              </button>

              <button 
                class="action-icon-btn" 
                onclick="window.VidyaSetu.toggleCompare('${item.id}')" 
                title="${compared ? 'Remove from compare' : 'Add to compare'}"
                style="color: ${compared ? 'var(--brand-primary)' : 'inherit'}; font-weight: bold;"
              >
                ${compared ? '✓' : '⚖️'}
              </button>
            </div>
          </div>

          <div class="card-body">
            <div class="agency-label">${item.fundingAgency}</div>
            <h3 class="card-title" onclick="window.VidyaSetu.openDetailModal('${item.id}')">${item.title}</h3>

            <!-- Funding Highlight -->
            <div class="funding-highlight">
              <div class="funding-amount">
                <span>💰</span> ${item.fundingAmount}
              </div>
              <div class="funding-desc">${item.coverage}</div>
            </div>

            <!-- Target Levels -->
            <div class="levels-pills">
              ${levelPills}
            </div>

            <p class="card-snippet">
              <strong>Eligibility:</strong> ${item.eligibility}
            </p>
          </div>

          <div class="card-footer">
            <div class="deadline-indicator">
              <span class="deadline-label">Application Cycle</span>
              <span class="deadline-val">📅 ${item.deadline}</span>
            </div>

            <div class="card-buttons">
              <button class="btn-details" onclick="window.VidyaSetu.openDetailModal('${item.id}')">
                Details & Docs
              </button>
              <a href="${item.officialLink}" target="_blank" rel="noopener noreferrer" class="btn-apply-direct" title="Opens official portal">
                Apply <span>↗</span>
              </a>
            </div>
          </div>
        </article>
      `;
    }).join('');
  }

  // Open Full Detail Modal
  function openDetailModal(id) {
    const item = OPPORTUNITIES_DATA.find(o => o.id === id);
    if (!item) return;

    activeModalItem = item;

    // Badges
    const isIndia = item.section === 'india';
    els.modalBadgeGroup.innerHTML = `
      <span class="badge ${isIndia ? 'badge-india' : 'badge-abroad'}">${isIndia ? '🇮🇳 India' : '🌍 Abroad'}</span>
      <span class="badge ${item.type === 'government' ? 'badge-gov' : 'badge-pvt'}">${item.type === 'government' ? '🏛️ Govt Fund' : '💼 Private Trust'}</span>
      <span class="badge badge-intern">${item.category}</span>
    `;

    els.modalTitle.textContent = item.title;
    els.modalAgency.textContent = item.fundingAgency;
    els.modalAmount.textContent = item.fundingAmount;
    els.modalCoverage.textContent = item.coverage;
    els.modalEligibility.textContent = item.eligibility;

    // Levels & Streams
    els.modalLevels.innerHTML = item.educationLevel.map(l => `<span class="level-tag" style="font-size: 0.82rem; padding: 5px 12px;">${l}</span>`).join('');
    els.modalStreams.innerHTML = item.streams.map(s => `<span class="level-tag" style="font-size: 0.82rem; padding: 5px 12px; background: rgba(37, 99, 235, 0.08); color: var(--brand-primary);">${s}</span>`).join('');

    // Document Checklist (Interactive)
    els.modalDocChecklist.innerHTML = item.documentsRequired.map((doc, idx) => `
      <label class="checklist-item" id="docLabel_${idx}">
        <input type="checkbox" onchange="this.parentElement.style.opacity = this.checked ? '0.6' : '1'">
        <span>${doc}</span>
      </label>
    `).join('');

    // Application Steps
    els.modalApplicationSteps.innerHTML = item.applicationProcess.map((step, idx) => `
      <div class="step-card">
        <div class="step-number">${idx + 1}</div>
        <div style="font-size: 0.88rem; color: var(--text-secondary); padding-top: 2px;">${step}</div>
      </div>
    `).join('');

    // Deadline & Link
    els.modalDeadline.textContent = `${item.deadline} (Peak Window)`;
    els.modalOfficialLink.href = item.officialLink;

    updateModalBookmarkBtn();

    els.detailModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function updateModalBookmarkBtn() {
    if (!activeModalItem) return;
    const bookmarked = isBookmarked(activeModalItem.id);
    els.modalBookmarkBtn.innerHTML = bookmarked ? '★ Bookmarked' : '☆ Save Scheme';
    els.modalBookmarkBtn.style.color = bookmarked ? '#f59e0b' : 'inherit';
  }

  function closeDetailModal() {
    els.detailModal.classList.remove('active');
    document.body.style.overflow = '';
    activeModalItem = null;
  }

  // Profile Matching Wizard Logic
  function openWizardModal() {
    els.wizardModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeWizardModal() {
    els.wizardModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function applyWizard() {
    const level = els.wizLevel.value;
    const stream = els.wizStream.value;
    const category = els.wizCategory.value;
    const destination = els.wizDestination.value;

    // Set state
    state.level = level;
    els.filterLevel.value = level;

    if (stream !== 'All Disciplines') {
      state.stream = stream;
      els.filterStream.value = stream;
    } else {
      state.stream = 'all';
      els.filterStream.value = 'all';
    }

    if (destination !== 'all') {
      setSection(destination);
    } else {
      setSection('all');
    }

    if (category === 'women') {
      state.activeChip = 'women';
    } else if (category === 'means') {
      state.searchQuery = 'income';
      els.searchInput.value = 'income';
    } else {
      state.activeChip = null;
    }

    updateChipsUI();
    closeWizardModal();
    renderCards();

    // Scroll to results
    els.resultsCountText.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // Section Tab Switcher
  function setSection(sec) {
    state.section = sec;
    [els.tabSectionAll, els.tabSectionIndia, els.tabSectionAbroad].forEach(tab => {
      tab.classList.remove('active');
    });

    if (sec === 'india') {
      els.tabSectionIndia.classList.add('active');
    } else if (sec === 'abroad') {
      els.tabSectionAbroad.classList.add('active');
    } else {
      els.tabSectionAll.classList.add('active');
    }

    renderCards();
  }

  // Comparison View
  function openComparisonModal() {
    if (state.compare.length === 0) return;

    const items = OPPORTUNITIES_DATA.filter(o => state.compare.includes(o.id));

    let html = `
      <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
        <thead>
          <tr style="background: var(--bg-primary); border-bottom: 2px solid var(--border-color);">
            <th style="padding: 14px; min-width: 140px;">Feature</th>
            ${items.map(it => `
              <th style="padding: 14px; min-width: 240px; vertical-align: top;">
                <div style="font-size: 1rem; font-weight: 700; margin-bottom: 6px;">${it.title}</div>
                <span class="badge ${it.section === 'india' ? 'badge-india' : 'badge-abroad'}">${it.section === 'india' ? 'India' : 'Abroad'}</span>
                <span class="badge badge-gov">${it.category}</span>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Funding Agency</td>
            ${items.map(it => `<td style="padding: 12px 14px;">${it.fundingAgency}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color); background: rgba(37, 99, 235, 0.04);">
            <td style="padding: 12px 14px; font-weight: 700; color: var(--brand-primary);">Amount & Stipend</td>
            ${items.map(it => `<td style="padding: 12px 14px; font-weight: 700; color: var(--brand-primary);">${it.fundingAmount}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Coverage</td>
            ${items.map(it => `<td style="padding: 12px 14px;">${it.coverage}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Education Level</td>
            ${items.map(it => `<td style="padding: 12px 14px;">${it.educationLevel.join(', ')}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Eligibility</td>
            ${items.map(it => `<td style="padding: 12px 14px;">${it.eligibility}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Deadline</td>
            ${items.map(it => `<td style="padding: 12px 14px; font-weight: 600;">${it.deadline}</td>`).join('')}
          </tr>
          <tr>
            <td style="padding: 14px; font-weight: 700;">Official Link</td>
            ${items.map(it => `
              <td style="padding: 14px;">
                <a href="${it.officialLink}" target="_blank" rel="noopener noreferrer" class="btn-apply-direct" style="padding: 6px 14px;">
                  Apply Official <span>↗</span>
                </a>
              </td>
            `).join('')}
          </tr>
        </tbody>
      </table>
    `;

    els.compareTableContainer.innerHTML = html;
    els.compareModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeComparisonModal() {
    els.compareModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Bookmarks Modal
  function openBookmarksModal() {
    const list = OPPORTUNITIES_DATA.filter(o => state.bookmarks.includes(o.id));
    if (list.length === 0) {
      els.bookmarksListBody.innerHTML = `
        <div style="text-align: center; padding: 40px 20px;">
          <div style="font-size: 2.5rem; margin-bottom: 10px;">⭐</div>
          <h4>No schemes saved yet</h4>
          <p style="color: var(--text-secondary); font-size: 0.88rem; margin-top: 6px;">
            Click the star icon (☆) on any scholarship card to save it for quick review.
          </p>
        </div>
      `;
    } else {
      els.bookmarksListBody.innerHTML = list.map(item => `
        <div class="detail-box" style="margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; gap: 14px;">
          <div style="flex: 1;">
            <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">${item.fundingAgency}</div>
            <h4 style="font-size: 1rem; margin: 2px 0 6px;">${item.title}</h4>
            <div style="font-size: 0.85rem; font-weight: 700; color: var(--brand-primary);">${item.fundingAmount}</div>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn-details" onclick="window.VidyaSetu.openDetailModal('${item.id}'); window.VidyaSetu.closeBookmarksModal();">
              View
            </button>
            <button class="action-icon-btn bookmarked" onclick="window.VidyaSetu.toggleBookmark('${item.id}'); window.VidyaSetu.openBookmarksModal();" title="Remove">
              ✕
            </button>
          </div>
        </div>
      `).join('');
    }

    els.bookmarksModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeBookmarksModal() {
    els.bookmarksModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Calendar Modal
  function openCalendarModal() {
    els.calendarModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCalendarModal() {
    els.calendarModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Reset Filters
  function resetAllFilters() {
    state.searchQuery = '';
    state.level = 'all';
    state.type = 'all';
    state.category = 'all';
    state.stream = 'all';
    state.sort = 'default';
    state.activeChip = null;

    els.searchInput.value = '';
    els.filterLevel.value = 'all';
    els.filterType.value = 'all';
    els.filterCategory.value = 'all';
    els.filterStream.value = 'all';
    els.sortOrder.value = 'default';

    updateChipsUI();
    renderCards();
  }

  function updateChipsUI() {
    els.chips.forEach(chip => {
      if (chip.getAttribute('data-chip') === state.activeChip) {
        chip.classList.add('active');
      } else {
        chip.classList.remove('active');
      }
    });
  }

  // Event Bindings
  function bindEvents() {
    // Theme
    els.themeToggleBtn.addEventListener('click', toggleTheme);

    // Section switcher
    els.tabSectionAll.addEventListener('click', () => setSection('all'));
    els.tabSectionIndia.addEventListener('click', () => setSection('india'));
    els.tabSectionAbroad.addEventListener('click', () => setSection('abroad'));

    // Search input
    els.searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderCards();
    });

    // Dropdowns
    els.filterLevel.addEventListener('change', (e) => {
      state.level = e.target.value;
      renderCards();
    });
    els.filterType.addEventListener('change', (e) => {
      state.type = e.target.value;
      renderCards();
    });
    els.filterCategory.addEventListener('change', (e) => {
      state.category = e.target.value;
      renderCards();
    });
    els.filterStream.addEventListener('change', (e) => {
      state.stream = e.target.value;
      renderCards();
    });
    els.sortOrder.addEventListener('change', (e) => {
      state.sort = e.target.value;
      renderCards();
    });

    // Chips
    els.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        const chipVal = chip.getAttribute('data-chip');
        if (state.activeChip === chipVal) {
          state.activeChip = null;
        } else {
          state.activeChip = chipVal;
        }
        updateChipsUI();
        renderCards();
      });
    });

    // Reset buttons
    els.btnResetFilters.addEventListener('click', resetAllFilters);
    els.btnResetNoResults.addEventListener('click', resetAllFilters);

    // View toggles
    els.viewModeGrid.addEventListener('click', () => {
      state.viewMode = 'grid';
      els.viewModeGrid.classList.add('active');
      els.viewModeCompact.classList.remove('active');
      renderCards();
    });
    els.viewModeCompact.addEventListener('click', () => {
      state.viewMode = 'compact';
      els.viewModeCompact.classList.add('active');
      els.viewModeGrid.classList.remove('active');
      renderCards();
    });

    // Modal details
    els.modalCloseBtn.addEventListener('click', closeDetailModal);
    els.detailModal.addEventListener('click', (e) => {
      if (e.target === els.detailModal) closeDetailModal();
    });
    els.modalBookmarkBtn.addEventListener('click', () => {
      if (activeModalItem) {
        toggleBookmark(activeModalItem.id);
      }
    });

    // Wizard
    els.btnOpenWizard.addEventListener('click', openWizardModal);
    els.btnHeroWizard.addEventListener('click', openWizardModal);
    els.wizardCloseBtn.addEventListener('click', closeWizardModal);
    els.btnCancelWizard.addEventListener('click', closeWizardModal);
    els.wizardModal.addEventListener('click', (e) => {
      if (e.target === els.wizardModal) closeWizardModal();
    });
    els.btnApplyWizard.addEventListener('click', applyWizard);

    // Compare
    els.btnLaunchComparison.addEventListener('click', openComparisonModal);
    els.compareCloseBtn.addEventListener('click', closeComparisonModal);
    els.btnCloseCompareFooter.addEventListener('click', closeComparisonModal);
    els.compareModal.addEventListener('click', (e) => {
      if (e.target === els.compareModal) closeComparisonModal();
    });
    els.btnClearComparison.addEventListener('click', () => {
      state.compare = [];
      updateCompareDrawer();
      renderCards();
    });

    // Calendar
    els.btnOpenCalendar.addEventListener('click', openCalendarModal);
    els.calendarCloseBtn.addEventListener('click', closeCalendarModal);
    els.btnCloseCalendarFooter.addEventListener('click', closeCalendarModal);
    els.calendarModal.addEventListener('click', (e) => {
      if (e.target === els.calendarModal) closeCalendarModal();
    });

    // Bookmarks
    els.btnSavedBookmarks.addEventListener('click', openBookmarksModal);
    els.bookmarksCloseBtn.addEventListener('click', closeBookmarksModal);
    els.btnCloseBookmarksFooter.addEventListener('click', closeBookmarksModal);
    els.bookmarksModal.addEventListener('click', (e) => {
      if (e.target === els.bookmarksModal) closeBookmarksModal();
    });
    els.btnClearAllBookmarks.addEventListener('click', () => {
      if (confirm('Are you sure you want to remove all saved scholarships?')) {
        state.bookmarks = [];
        localStorage.setItem('vidyasetu_bookmarks', '[]');
        updateBookmarkBadge();
        renderCards();
        openBookmarksModal();
      }
    });

    // Escape key closes modals
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeDetailModal();
        closeWizardModal();
        closeComparisonModal();
        closeCalendarModal();
        closeBookmarksModal();
      }
    });
  }

  // Expose global methods for inline card onclick handlers
  window.VidyaSetu = {
    openDetailModal,
    closeDetailModal,
    toggleBookmark,
    toggleCompare,
    openBookmarksModal,
    closeBookmarksModal,
    setSection
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
