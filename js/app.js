// VidyaSetu - Core Application Engine (Notebook Edition)
// Designed for plain, clear, honest access to educational opportunities.

(function () {
  'use strict';

  // Global State
  const state = {
    opportunities: [],
    meta: null,
    loading: true,
    error: null,

    // Active Filters
    section: 'all', // 'all', 'india', 'abroad', 'providers'
    level: 'all',
    status: 'all',
    category: 'all',
    country: 'all',
    stateFilter: 'all',
    target: 'all',
    income: 'all',
    searchQuery: '',
    sort: 'deadline',

    // Hero selections
    heroStage: 'After 12th',
    heroPlace: 'all',
    heroKind: 'all',

    // Provider filter
    providerKind: 'all',
    providerSearch: '',
    selectedProviderSlug: null,

    // User preferences & Bookmarks
    lang: safeLocalStorage('get', 'vidyasetu_lang') || 'en',
    theme: safeLocalStorage('get', 'vidyasetu_theme') || 'light',
    bookmarks: JSON.parse(safeLocalStorage('get', 'vidyasetu_bookmarks') || '[]'),
    compare: []
  };

  let activeModalItem = null;

  // Safe localStorage helper
  function safeLocalStorage(action, key, val) {
    try {
      if (action === 'get') return localStorage.getItem(key);
      if (action === 'set') localStorage.setItem(key, val);
      if (action === 'remove') localStorage.removeItem(key);
    } catch (e) {
      console.warn('localStorage access failed:', e);
      return null;
    }
  }

  // DOM Elements Cache
  const els = {
    // Nav & Theme
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    langToggleBtn: document.getElementById('langToggleBtn'),
    mobileMenuBtn: document.getElementById('mobileMenuBtn'),
    mainNavLinks: document.getElementById('mainNavLinks'),
    logoBrand: document.getElementById('logoBrand'),
    savedCountBadge: document.getElementById('savedCountBadge'),
    navLinkIndia: document.getElementById('navLinkIndia'),
    navLinkAbroad: document.getElementById('navLinkAbroad'),
    btnOpenCalendar: document.getElementById('btnOpenCalendar'),
    btnSavedBookmarks: document.getElementById('btnSavedBookmarks'),
    btnOpenWizard: document.getElementById('btnOpenWizard'),

    // Hero
    heroStage: document.getElementById('heroStage'),
    heroPlace: document.getElementById('heroPlace'),
    heroKind: document.getElementById('heroKind'),
    heroLiveSummary: document.getElementById('heroLiveSummary'),
    btnHeroShowAll: document.getElementById('btnHeroShowAll'),
    btnResetHero: document.getElementById('btnResetHero'),
    closingSoonList: document.getElementById('closingSoonList'),
    btnOpenCalendarLink: document.getElementById('btnOpenCalendarLink'),

    // Road Track
    roadStops: document.querySelectorAll('.road-stop'),
    roadCountAfter12: document.getElementById('roadCountAfter12'),
    roadCountBachelor: document.getElementById('roadCountBachelor'),
    roadCountMaster: document.getElementById('roadCountMaster'),
    roadCountPhD: document.getElementById('roadCountPhD'),
    roadCountPostdoc: document.getElementById('roadCountPostdoc'),

    // Columns
    colIndiaCount: document.getElementById('colIndiaCount'),
    colAbroadCount: document.getElementById('colAbroadCount'),
    statePillsContainer: document.getElementById('statePillsContainer'),
    abroadCountriesList: document.getElementById('abroadCountriesList'),

    // Results & Sidebar
    resultsSection: document.getElementById('resultsSection'),
    filtersSidebar: document.getElementById('filtersSidebar'),
    filterLevel: document.getElementById('filterLevel'),
    filterSection: document.getElementById('filterSection'),
    filterStatus: document.getElementById('filterStatus'),
    filterCategory: document.getElementById('filterCategory'),
    filterCountry: document.getElementById('filterCountry'),
    filterTarget: document.getElementById('filterTarget'),
    filterSort: document.getElementById('filterSort'),
    btnResetFilters: document.getElementById('btnResetFilters'),
    btnMobileFilterToggle: document.getElementById('btnMobileFilterToggle'),
    btnCloseMobileFilters: document.getElementById('btnCloseMobileFilters'),

    // Search & Lists
    searchInput: document.getElementById('searchInput'),
    resultsCountText: document.getElementById('resultsCountText'),
    btnViewProviders: document.getElementById('btnViewProviders'),
    opportunitiesListContainer: document.getElementById('opportunitiesListContainer'),
    loadingState: document.getElementById('loadingState'),
    errorState: document.getElementById('errorState'),
    errorMessage: document.getElementById('errorMessage'),
    noResultsState: document.getElementById('noResultsState'),
    btnResetNoResults: document.getElementById('btnResetNoResults'),

    // Providers View
    providersContainer: document.getElementById('providersContainer'),
    providersGrid: document.getElementById('providersGrid'),
    providerSearchInput: document.getElementById('providerSearchInput'),
    btnBackToOpportunities: document.getElementById('btnBackToOpportunities'),

    // Compare Drawer
    compareDrawer: document.getElementById('compareDrawer'),
    compareBadgeCount: document.getElementById('compareBadgeCount'),
    btnLaunchComparison: document.getElementById('btnLaunchComparison'),
    btnClearComparison: document.getElementById('btnClearComparison'),

    // Modals
    detailModal: document.getElementById('detailModal'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalTitle: document.getElementById('modalTitle'),
    modalAgency: document.getElementById('modalAgency'),
    modalEligibility: document.getElementById('modalEligibility'),
    modalLevelsAndStreams: document.getElementById('modalLevelsAndStreams'),
    modalAmount: document.getElementById('modalAmount'),
    modalCoverage: document.getElementById('modalCoverage'),
    modalDocChecklist: document.getElementById('modalDocChecklist'),
    modalApplicationSteps: document.getElementById('modalApplicationSteps'),
    modalDeadline: document.getElementById('modalDeadline'),
    modalEvidenceContainer: document.getElementById('modalEvidenceContainer'),
    modalEvidenceText: document.getElementById('modalEvidenceText'),
    modalVerificationTimestamp: document.getElementById('modalVerificationTimestamp'),
    modalOfficialLink: document.getElementById('modalOfficialLink'),
    modalBookmarkBtn: document.getElementById('modalBookmarkBtn'),
    modalReportBrokenBtn: document.getElementById('modalReportBrokenBtn'),
    btnModalGoogleCal: document.getElementById('btnModalGoogleCal'),
    btnModalICS: document.getElementById('btnModalICS'),

    calendarModal: document.getElementById('calendarModal'),
    calendarCloseBtn: document.getElementById('calendarCloseBtn'),
    dynamicCalendarBody: document.getElementById('dynamicCalendarBody'),
    btnCloseCalendarFooter: document.getElementById('btnCloseCalendarFooter'),

    wizardModal: document.getElementById('wizardModal'),
    wizardCloseBtn: document.getElementById('wizardCloseBtn'),
    wizLevel: document.getElementById('wizLevel'),
    wizStream: document.getElementById('wizStream'),
    wizDestination: document.getElementById('wizDestination'),
    btnCancelWizard: document.getElementById('btnCancelWizard'),
    btnApplyWizard: document.getElementById('btnApplyWizard'),

    compareModal: document.getElementById('compareModal'),
    compareCloseBtn: document.getElementById('compareCloseBtn'),
    compareTableContainer: document.getElementById('compareTableContainer'),
    btnCloseCompareFooter: document.getElementById('btnCloseCompareFooter'),

    bookmarksModal: document.getElementById('bookmarksModal'),
    bookmarksCloseBtn: document.getElementById('bookmarksCloseBtn'),
    bookmarksListBody: document.getElementById('bookmarksListBody'),
    btnClearAllBookmarks: document.getElementById('btnClearAllBookmarks'),
    btnCloseBookmarksFooter: document.getElementById('btnCloseBookmarksFooter'),

    footerUpdatedDate: document.getElementById('footerUpdatedDate')
  };

  // --------------------------------------------------------------------------
  // Application Initialization
  // --------------------------------------------------------------------------
  async function init() {
    applyTheme(state.theme);
    updateBookmarkBadge();
    bindEvents();
    loadSavedHeroSelections();

    try {
      const [oppRes, metaRes] = await Promise.all([
        fetch('data/opportunities.json'),
        fetch('data/meta.json')
      ]);

      if (!oppRes.ok) throw new Error(`HTTP ${oppRes.status} loading opportunities`);
      
      state.opportunities = await oppRes.json();
      if (metaRes.ok) {
        state.meta = await metaRes.json();
      }

      state.loading = false;
      renderInitialView();
      handleHashRouting();
    } catch (err) {
      console.error('Initialization error:', err);
      state.loading = false;
      state.error = err.message;
      if (els.loadingState) els.loadingState.style.display = 'none';
      if (els.errorState) {
        els.errorState.style.display = 'block';
        if (els.errorMessage) els.errorMessage.textContent = err.message;
      }
    }
  }

  // Render initial page elements once data loads
  function renderInitialView() {
    if (els.loadingState) els.loadingState.style.display = 'none';

    // Populate metadata & footer
    if (state.meta && els.footerUpdatedDate) {
      const d = state.meta.lastVerifiedDate || 'October 2026';
      els.footerUpdatedDate.textContent = `Updated ${d}`;
    }

    updateHeroSummary();
    renderClosingSoonNote();
    renderRoadCounts();
    renderColumnsSummary();
    renderCards();
    renderProviders();
  }

  // --------------------------------------------------------------------------
  // Hero: Sentence & Live Matching
  // --------------------------------------------------------------------------
  function loadSavedHeroSelections() {
    const savedStage = safeLocalStorage('get', 'vidyasetu_hero_stage');
    const savedPlace = safeLocalStorage('get', 'vidyasetu_hero_place');
    const savedKind = safeLocalStorage('get', 'vidyasetu_hero_kind');

    if (savedStage && els.heroStage) els.heroStage.value = savedStage;
    if (savedPlace && els.heroPlace) els.heroPlace.value = savedPlace;
    if (savedKind && els.heroKind) els.heroKind.value = savedKind;
  }

  function saveHeroSelections() {
    if (els.heroStage) safeLocalStorage('set', 'vidyasetu_hero_stage', els.heroStage.value);
    if (els.heroPlace) safeLocalStorage('set', 'vidyasetu_hero_place', els.heroPlace.value);
    if (els.heroKind) safeLocalStorage('set', 'vidyasetu_hero_kind', els.heroKind.value);
  }

  function getHeroMatches() {
    if (!state.opportunities.length) return [];

    const stage = els.heroStage ? els.heroStage.value : 'After 12th';
    const place = els.heroPlace ? els.heroPlace.value : 'all';
    const kind = els.heroKind ? els.heroKind.value : 'all';

    return state.opportunities.filter(item => {
      // Stage match
      if (!item.educationLevel || !item.educationLevel.includes(stage)) return false;

      // Location match
      if (place === 'india' && item.section !== 'india') return false;
      if (place === 'abroad' && item.section !== 'abroad') return false;

      // Kind match
      if (kind === 'funds') {
        if (!['Scholarship', 'Fellowship', 'Fund/Grant'].includes(item.category)) return false;
      } else if (kind === 'internships_projects') {
        if (!['Internship', 'Project Position (JRF/SRF/RA)'].includes(item.category)) return false;
      }

      return true;
    });
  }

  function updateHeroSummary() {
    saveHeroSelections();
    const matches = getHeroMatches();
    const total = matches.length;

    if (!els.heroLiveSummary) return;

    if (total === 0) {
      els.heroLiveSummary.innerHTML = `
        No opportunities directly match that combination right now. 
        <span style="color: var(--text-muted); display: block; font-size: 0.9rem; margin-top: 4px;">
          Tip: Most summer research internships require students to be in their 2nd or 3rd year of a bachelor's degree.
        </span>
      `;
      if (els.btnHeroShowAll) {
        els.btnHeroShowAll.textContent = 'Show all opportunities';
      }
      return;
    }

    const govCount = matches.filter(m => m.type === 'government').length;
    const otherCount = total - govCount;

    let details = '';
    if (govCount > 0 && otherCount > 0) {
      details = ` <strong>${govCount}</strong> come from the government and <strong>${otherCount}</strong> from trusts, companies and universities.`;
    } else if (govCount > 0) {
      details = ` All <strong>${govCount}</strong> come from central and state governments.`;
    } else {
      details = ` Offered by universities and philanthropic trusts.`;
    }

    els.heroLiveSummary.innerHTML = `
      <strong>${total}</strong> opportunities fit that.${details}
    `;

    if (els.btnHeroShowAll) {
      els.btnHeroShowAll.textContent = `Show me all ${total}`;
    }
  }

  // --------------------------------------------------------------------------
  // Closing Soon Note Card
  // --------------------------------------------------------------------------
  function renderClosingSoonNote() {
    if (!els.closingSoonList || !state.opportunities.length) return;

    // Pick top confirmed closing first, then active cycles
    const candidates = state.opportunities
      .filter(it => it.status === 'open' || it.dateConfidence === 'confirmed')
      .slice(0, 5);

    els.closingSoonList.innerHTML = candidates.map(it => {
      let dateHtml = '';
      if (it.dateConfidence === 'confirmed' && it.deadline) {
        dateHtml = `<span class="highlighter">closes ${formatShortDate(it.deadline)}</span>`;
      } else {
        dateHtml = `<span class="highlighter">usually ${it.deadlineText || 'mid-cycle'}</span>`;
      }

      return `
        <li class="pinned-item">
          <a href="#/opportunity/${it.id}" onclick="window.VidyaSetu.openDetailModal('${it.id}'); return false;">
            ${it.title}
          </a>
          <span class="pinned-item-date">${dateHtml} • ${it.provider.name}</span>
        </li>
      `;
    }).join('');
  }

  // --------------------------------------------------------------------------
  // Road Track & Columns Counts
  // --------------------------------------------------------------------------
  function renderRoadCounts() {
    const opps = state.opportunities;
    const countStage = (lvl) => opps.filter(o => o.educationLevel && o.educationLevel.includes(lvl)).length;

    if (els.roadCountAfter12) els.roadCountAfter12.textContent = `${countStage('After 12th')}`;
    if (els.roadCountBachelor) els.roadCountBachelor.textContent = `${countStage('Bachelor')}`;
    if (els.roadCountMaster) els.roadCountMaster.textContent = `${countStage('Master')}`;
    if (els.roadCountPhD) els.roadCountPhD.textContent = `${countStage('PhD')}`;
    if (els.roadCountPostdoc) els.roadCountPostdoc.textContent = `${countStage('Postdoc')}`;
  }

  function renderColumnsSummary() {
    const opps = state.opportunities;
    const indiaCount = opps.filter(o => o.section === 'india').length;
    const abroadCount = opps.filter(o => o.section === 'abroad').length;

    if (els.colIndiaCount) els.colIndiaCount.textContent = `${indiaCount}`;
    if (els.colAbroadCount) els.colAbroadCount.textContent = `${abroadCount}`;

    // Render Abroad Countries Table (Wikipedia style)
    if (els.abroadCountriesList) {
      const countryMap = new Map();
      opps.filter(o => o.section === 'abroad').forEach(o => {
        const c = o.country || 'International';
        countryMap.set(c, (countryMap.get(c) || 0) + 1);
      });

      const sorted = Array.from(countryMap.entries())
        .sort((a, b) => b[1] - a[1]);

      els.abroadCountriesList.innerHTML = sorted.map(([country, count]) => `
        <a class="country-row" href="#section-abroad" data-country="${country}">
          <span>${country}</span>
          <span class="country-count">${count}</span>
        </a>
      `).join('');

      // Add click events to country rows
      els.abroadCountriesList.querySelectorAll('.country-row').forEach(row => {
        row.addEventListener('click', (e) => {
          e.preventDefault();
          const country = row.getAttribute('data-country');
          state.section = 'abroad';
          state.country = country;
          if (els.filterSection) els.filterSection.value = 'abroad';
          if (els.filterCountry) els.filterCountry.value = country;
          renderCards();
          scrollToResults();
        });
      });
    }
  }

  // --------------------------------------------------------------------------
  // Main Calm Opportunities List
  // --------------------------------------------------------------------------
  function getFilteredOpportunities() {
    return state.opportunities.filter(it => {
      // Section
      if (state.section !== 'all' && it.section !== state.section) return false;

      // Education Level
      if (state.level !== 'all' && it.educationLevel && !it.educationLevel.includes(state.level)) return false;

      // Status
      if (state.status !== 'all') {
        if (state.status === 'open' && (it.status !== 'open' || it.dateConfidence !== 'confirmed')) return false;
        if (state.status === 'expected' && it.dateConfidence !== 'expected') return false;
        if (state.status === 'closed' && it.status !== 'closed') return false;
      }

      // Category
      if (state.category !== 'all' && it.category !== state.category) return false;

      // Country
      if (state.country !== 'all' && it.country !== state.country) return false;

      // State Filter (for Indian State Schemes)
      if (state.stateFilter !== 'all') {
        const matchState = (it.state && it.state.toLowerCase() === state.stateFilter.toLowerCase()) ||
                           it.title.toLowerCase().includes(state.stateFilter.toLowerCase()) ||
                           it.provider.name.toLowerCase().includes(state.stateFilter.toLowerCase());
        if (!matchState) return false;
      }

      // Target Group
      if (state.target !== 'all') {
        if (state.target === 'women' && it.targetGroup !== 'Girls' && !it.tags.includes('women-only')) return false;
        if (['sc', 'st', 'obc', 'minority', 'pwd'].includes(state.target)) {
          if (!it.tags.some(t => t.includes(state.target)) && !it.targetGroup.toLowerCase().includes(state.target)) return false;
        }
      }

      // Search Query
      if (state.searchQuery.trim() !== '') {
        const q = state.searchQuery.toLowerCase();
        const haystack = `${it.title} ${it.provider.name} ${it.eligibility} ${it.fundingAmount} ${it.country || ''} ${it.tags.join(' ')}`.toLowerCase();
        if (!haystack.includes(q)) return false;
      }

      return true;
    }).sort((a, b) => {
      if (state.sort === 'deadline') {
        // Confirmed open deadlines first
        if (a.dateConfidence === 'confirmed' && b.dateConfidence !== 'confirmed') return -1;
        if (b.dateConfidence === 'confirmed' && a.dateConfidence !== 'confirmed') return 1;
        if (a.deadline && b.deadline) return a.deadline.localeCompare(b.deadline);
      } else if (state.sort === 'title') {
        return a.title.localeCompare(b.title);
      }
      return 0;
    });
  }

  function renderCards() {
    if (state.section === 'providers') {
      if (els.opportunitiesListContainer) els.opportunitiesListContainer.style.display = 'none';
      if (els.resultsSection) els.resultsSection.style.display = 'none';
      if (els.providersContainer) els.providersContainer.style.display = 'block';
      return;
    } else {
      if (els.opportunitiesListContainer) els.opportunitiesListContainer.style.display = 'flex';
      if (els.resultsSection) els.resultsSection.style.display = 'block';
      if (els.providersContainer) els.providersContainer.style.display = 'none';
    }

    const list = getFilteredOpportunities();

    if (els.resultsCountText) {
      els.resultsCountText.innerHTML = `Showing <strong>${list.length}</strong> ${
        state.section === 'india' ? 'opportunities in India' :
        state.section === 'abroad' ? 'opportunities abroad' :
        'opportunities'
      }`;
    }

    if (list.length === 0) {
      if (els.opportunitiesListContainer) els.opportunitiesListContainer.innerHTML = '';
      if (els.noResultsState) els.noResultsState.style.display = 'block';
      return;
    } else {
      if (els.noResultsState) els.noResultsState.style.display = 'none';
    }

    if (!els.opportunitiesListContainer) return;

    els.opportunitiesListContainer.innerHTML = list.map(item => {
      const bookmarked = isBookmarked(item.id);
      const compared = isInCompare(item.id);
      const levelsText = (item.educationLevel || []).join(', ');

      // Status Badge Logic
      let statusHtml = '';
      if (item.dateConfidence === 'confirmed' && item.status === 'open' && item.deadline) {
        statusHtml = `<span class="status-badge open">Open, closes ${formatShortDate(item.deadline)}</span>`;
      } else if (item.status === 'closed') {
        statusHtml = `<span class="status-badge closed">Closed. Next round expected ${item.deadlineText || 'next cycle'}</span>`;
      } else if (item.deadlineText && item.deadlineText.toLowerCase().includes('rolling')) {
        statusHtml = `<span class="status-badge open">Rolling, open year-round</span>`;
      } else {
        statusHtml = `<span class="status-badge expected">Expected: ${item.deadlineText || 'Check official site'}</span>`;
      }

      // Verification note
      let verifyNote = '';
      if (item.lastVerified) {
        verifyNote = `<span class="verification-note">• Checked for 2026/27 cycle</span>`;
      } else {
        verifyNote = `<span class="verification-note">• Not yet checked for this cycle</span>`;
      }

      return `
        <article class="opportunity-row" data-id="${item.id}">
          <div class="row-main">
            <div class="row-provider-line">
              <a href="#/provider/${item.provider.slug}" class="provider-link">
                ${item.provider.name}
              </a>
              <span>•</span>
              <span>${item.section === 'india' ? 'India' : (item.country || 'Abroad')}</span>
              <span>•</span>
              <span style="text-transform: capitalize;">${item.type}</span>
            </div>

            <h3 class="row-title">
              <a href="#/opportunity/${item.id}" onclick="window.VidyaSetu.openDetailModal('${item.id}'); return false;">
                ${item.title}
              </a>
            </h3>

            <div class="row-meta-line">
              <span class="meta-for">For ${levelsText}</span>
              <span>•</span>
              <span class="meta-amount">${item.fundingAmount}</span>
            </div>

            <div class="row-status-line">
              ${statusHtml}
              ${verifyNote}
            </div>
          </div>

          <div class="row-side-actions">
            <button 
              class="pill-btn small ${bookmarked ? 'primary' : 'secondary'}" 
              onclick="window.VidyaSetu.toggleBookmark('${item.id}')"
            >
              ${bookmarked ? 'Saved' : 'Save'}
            </button>

            <button 
              class="pill-btn small text-only" 
              onclick="window.VidyaSetu.toggleCompare('${item.id}')"
            >
              ${compared ? 'In compare' : 'Compare'}
            </button>

            <a 
              href="${item.officialLink}" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="pill-btn small text-only"
              title="Visit official portal"
            >
              Official site
            </a>
          </div>
        </article>
      `;
    }).join('');
  }

  // --------------------------------------------------------------------------
  // Opportunity Detail Reader Guide
  // --------------------------------------------------------------------------
  function openDetailModal(id) {
    const item = state.opportunities.find(o => o.id === id);
    if (!item) return;

    activeModalItem = item;

    // Set URL Hash for sharing
    window.location.hash = `/opportunity/${item.id}`;

    if (els.modalTitle) els.modalTitle.textContent = item.title;
    if (els.modalAgency) els.modalAgency.textContent = `${item.provider.name} (${item.section === 'india' ? 'India' : (item.country || 'Abroad')})`;

    // Question 1: Who can apply?
    if (els.modalEligibility) els.modalEligibility.textContent = item.eligibility;
    if (els.modalLevelsAndStreams) {
      els.modalLevelsAndStreams.textContent = `Target stages: ${(item.educationLevel || []).join(', ')} • Streams: ${(item.streams || []).join(', ')}`;
    }

    // Question 2: How much do you get?
    if (els.modalAmount) els.modalAmount.textContent = item.fundingAmount;
    if (els.modalCoverage) els.modalCoverage.textContent = `Provider Website: ${item.provider.website || 'Official portal'}`;

    // Question 3: Documents Checklist with real checkboxes & persistence
    if (els.modalDocChecklist) {
      const savedChecks = JSON.parse(safeLocalStorage('get', `vidyasetu_docs_${item.id}`) || '{}');
      const docs = item.documentsRequired || [
        'Aadhaar card linked to bank account (for DBT)',
        'Bonafide student certificate from current institution',
        'Previous academic marksheets',
        'Income certificate issued by competent authority (if means-based)'
      ];

      els.modalDocChecklist.innerHTML = docs.map((doc, idx) => {
        const isChecked = !!savedChecks[idx];
        return `
          <li class="doc-check-item">
            <input 
              type="checkbox" 
              id="docCheck_${item.id}_${idx}" 
              ${isChecked ? 'checked' : ''} 
              onchange="window.VidyaSetu.toggleDocCheck('${item.id}', ${idx}, this.checked)"
            >
            <label for="docCheck_${item.id}_${idx}">${doc}</label>
          </li>
        `;
      }).join('');
    }

    // Question 4: How do you apply?
    if (els.modalApplicationSteps) {
      els.modalApplicationSteps.textContent = item.applicationProcess || 'Submit your application directly through the official provider portal.';
    }

    // Question 5: When?
    if (els.modalDeadline) {
      if (item.dateConfidence === 'confirmed') {
        els.modalDeadline.textContent = `Confirmed application window: Opens ${item.openDate || 'start of cycle'}, closes ${item.deadline || item.deadlineText}.`;
      } else {
        els.modalDeadline.textContent = `Expected timeline: ${item.deadlineText || 'Annual cycle'}. (Always confirm on official site before applying).`;
      }
    }

    // Calendar Export Links
    setupCalendarExport(item);

    // Evidence quote box
    if (els.modalEvidenceContainer && els.modalEvidenceText) {
      if (item.evidence) {
        els.modalEvidenceContainer.style.display = 'block';
        els.modalEvidenceText.textContent = `“${item.evidence}” — Official circular verification`;
      } else {
        els.modalEvidenceContainer.style.display = 'none';
      }
    }

    // Verification timestamp
    if (els.modalVerificationTimestamp) {
      if (item.lastVerified) {
        els.modalVerificationTimestamp.textContent = `Last checked against official guidelines on ${item.lastVerified}.`;
      } else {
        els.modalVerificationTimestamp.textContent = `Not yet verified for this cycle. Dates are from historical patterns.`;
      }
    }

    // Buttons
    if (els.modalOfficialLink) {
      els.modalOfficialLink.href = item.officialLink;
    }

    if (els.modalReportBrokenBtn) {
      els.modalReportBrokenBtn.href = `https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/issues/new?title=Date+Check+${encodeURIComponent(item.title)}&template=wrong_date.yml`;
    }

    updateModalBookmarkBtn(item.id);

    if (els.detailModal) els.detailModal.style.display = 'flex';
  }

  function closeDetailModal() {
    if (els.detailModal) els.detailModal.style.display = 'none';
    activeModalItem = null;
    if (window.location.hash.startsWith('#/opportunity/')) {
      history.replaceState(null, '', ' ');
    }
  }

  // --------------------------------------------------------------------------
  // Calendar Export (.ics & Google Calendar)
  // --------------------------------------------------------------------------
  function setupCalendarExport(item) {
    if (!item.deadline) {
      if (els.btnModalGoogleCal) els.btnModalGoogleCal.style.display = 'none';
      if (els.btnModalICS) els.btnModalICS.style.display = 'none';
      return;
    }

    if (els.btnModalGoogleCal) els.btnModalGoogleCal.style.display = 'inline-flex';
    if (els.btnModalICS) els.btnModalICS.style.display = 'inline-flex';

    const dStr = item.deadline.replace(/-/g, '');
    const gUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(item.title + ' Deadline')}&dates=${dStr}T000000Z/${dStr}T235959Z&details=${encodeURIComponent('Apply on: ' + item.officialLink)}&location=${encodeURIComponent(item.provider.name)}`;

    if (els.btnModalGoogleCal) els.btnModalGoogleCal.href = gUrl;

    if (els.btnModalICS) {
      els.btnModalICS.onclick = () => {
        const icsContent = [
          'BEGIN:VCALENDAR',
          'VERSION:2.0',
          'BEGIN:VEVENT',
          `SUMMARY:${item.title} Deadline`,
          `DESCRIPTION:Apply at ${item.officialLink}`,
          `DTSTART;VALUE=DATE:${dStr}`,
          `DTEND;VALUE=DATE:${dStr}`,
          'END:VEVENT',
          'END:VCALENDAR'
        ].join('\r\n');

        const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${item.id}-deadline.ics`;
        a.click();
        URL.revokeObjectURL(url);
      };
    }
  }

  // --------------------------------------------------------------------------
  // Month-by-Month Calendar Modal
  // --------------------------------------------------------------------------
  function openCalendarModal() {
    if (!els.dynamicCalendarBody || !state.opportunities.length) return;

    const months = [
      'January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'
    ];

    const monthMap = new Map();
    months.forEach((m, idx) => monthMap.set(idx + 1, []));

    state.opportunities.forEach(it => {
      let mIdx = null;
      if (it.deadline) {
        const parts = it.deadline.split('-');
        if (parts.length >= 2) mIdx = parseInt(parts[1], 10);
      }
      if (mIdx && monthMap.has(mIdx)) {
        monthMap.get(mIdx).push(it);
      }
    });

    els.dynamicCalendarBody.innerHTML = months.map((monthName, idx) => {
      const items = monthMap.get(idx + 1) || [];
      if (items.length === 0) return '';

      return `
        <div class="month-block">
          <h4>${monthName} (${items.length})</h4>
          <ul class="month-items-list">
            ${items.map(it => `
              <li class="month-item">
                <a href="#/opportunity/${it.id}" onclick="window.VidyaSetu.openDetailModal('${it.id}'); return false;">
                  ${it.title}
                </a>
                <span style="color: var(--text-muted); font-size: 0.85rem;">
                  ${it.deadline ? formatShortDate(it.deadline) : it.deadlineText}
                </span>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }).join('');

    if (els.calendarModal) els.calendarModal.style.display = 'flex';
  }

  function closeCalendarModal() {
    if (els.calendarModal) els.calendarModal.style.display = 'none';
  }

  // --------------------------------------------------------------------------
  // Profile Matcher Wizard Modal
  // --------------------------------------------------------------------------
  function openWizardModal() {
    if (els.wizardModal) els.wizardModal.style.display = 'flex';
  }

  function closeWizardModal() {
    if (els.wizardModal) els.wizardModal.style.display = 'none';
  }

  function applyWizard() {
    const stage = els.wizLevel ? els.wizLevel.value : 'all';
    const place = els.wizDestination ? els.wizDestination.value : 'all';

    state.level = stage;
    state.section = place;

    if (els.filterLevel) els.filterLevel.value = stage;
    if (els.filterSection) els.filterSection.value = place;
    if (els.heroStage) els.heroStage.value = stage;
    if (els.heroPlace) els.heroPlace.value = place;

    closeWizardModal();
    updateHeroSummary();
    renderCards();
    scrollToResults();
  }

  // --------------------------------------------------------------------------
  // Side by Side Comparison
  // --------------------------------------------------------------------------
  function isInCompare(id) {
    return state.compare.includes(id);
  }

  function toggleCompare(id) {
    const idx = state.compare.indexOf(id);
    if (idx > -1) {
      state.compare.splice(idx, 1);
    } else {
      if (state.compare.length >= 4) {
        alert('You can compare up to 4 opportunities side by side.');
        return;
      }
      state.compare.push(id);
    }
    updateCompareDrawer();
    renderCards();
  }

  function updateCompareDrawer() {
    if (!els.compareDrawer) return;
    if (state.compare.length > 0) {
      els.compareDrawer.style.display = 'flex';
      if (els.compareBadgeCount) els.compareBadgeCount.textContent = state.compare.length;
    } else {
      els.compareDrawer.style.display = 'none';
    }
  }

  function openCompareModal() {
    if (!els.compareTableContainer || !state.compare.length) return;

    const items = state.opportunities.filter(o => state.compare.includes(o.id));

    els.compareTableContainer.innerHTML = `
      <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
        <thead>
          <tr style="border-bottom: 2px solid var(--border);">
            <th style="padding: 10px; width: 140px;">Feature</th>
            ${items.map(it => `
              <th style="padding: 10px; min-width: 200px;">
                <div style="font-weight: 700;">${it.title}</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">${it.provider.name}</div>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 10px; font-weight: 600;">Amount</td>
            ${items.map(it => `<td style="padding: 10px; font-weight: 700; color: var(--ink-blue);">${it.fundingAmount}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 10px; font-weight: 600;">Location</td>
            ${items.map(it => `<td style="padding: 10px;">${it.section === 'india' ? 'India' : (it.country || 'Abroad')}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 10px; font-weight: 600;">Eligibility</td>
            ${items.map(it => `<td style="padding: 10px; font-size: 0.88rem;">${it.eligibility}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 10px; font-weight: 600;">Stages</td>
            ${items.map(it => `<td style="padding: 10px;">${(it.educationLevel || []).join(', ')}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 10px; font-weight: 600;">Deadline</td>
            ${items.map(it => `<td style="padding: 10px;">${it.deadline || it.deadlineText}</td>`).join('')}
          </tr>
          <tr>
            <td style="padding: 10px;"></td>
            ${items.map(it => `
              <td style="padding: 10px;">
                <a href="${it.officialLink}" target="_blank" rel="noopener noreferrer" class="pill-btn small primary">
                  Official page
                </a>
              </td>
            `).join('')}
          </tr>
        </tbody>
      </table>
    `;

    if (els.compareModal) els.compareModal.style.display = 'flex';
  }

  function closeCompareModal() {
    if (els.compareModal) els.compareModal.style.display = 'none';
  }

  // --------------------------------------------------------------------------
  // Bookmarks / Saved Opportunities
  // --------------------------------------------------------------------------
  function isBookmarked(id) {
    return state.bookmarks.includes(id);
  }

  function toggleBookmark(id) {
    const idx = state.bookmarks.indexOf(id);
    if (idx > -1) {
      state.bookmarks.splice(idx, 1);
    } else {
      state.bookmarks.push(id);
    }
    safeLocalStorage('set', 'vidyasetu_bookmarks', JSON.stringify(state.bookmarks));
    updateBookmarkBadge();
    updateModalBookmarkBtn(id);
    renderCards();
  }

  function updateBookmarkBadge() {
    if (els.savedCountBadge) {
      els.savedCountBadge.textContent = state.bookmarks.length;
    }
  }

  function updateModalBookmarkBtn(id) {
    if (!els.modalBookmarkBtn) return;
    const bookmarked = isBookmarked(id);
    els.modalBookmarkBtn.textContent = bookmarked ? 'Saved' : 'Save';
    els.modalBookmarkBtn.onclick = () => toggleBookmark(id);
  }

  function openBookmarksModal() {
    if (!els.bookmarksListBody) return;

    const saved = state.opportunities.filter(o => state.bookmarks.includes(o.id));

    if (saved.length === 0) {
      els.bookmarksListBody.innerHTML = `
        <div class="empty-state-box">
          <h3>No opportunities saved yet</h3>
          <p>Click "Save" on any opportunity to keep it here for quick access.</p>
        </div>
      `;
    } else {
      els.bookmarksListBody.innerHTML = `
        <div class="opportunities-list">
          ${saved.map(it => `
            <div class="opportunity-row">
              <div class="row-main">
                <div class="row-provider-line">
                  <span>${it.provider.name}</span>
                </div>
                <h4 class="row-title">
                  <a href="#/opportunity/${it.id}" onclick="window.VidyaSetu.openDetailModal('${it.id}'); return false;">
                    ${it.title}
                  </a>
                </h4>
                <div class="row-meta-line">
                  <span>${it.fundingAmount}</span>
                  <span>•</span>
                  <span>${it.deadline || it.deadlineText}</span>
                </div>
              </div>
              <div class="row-side-actions">
                <button class="pill-btn small text-only" onclick="window.VidyaSetu.toggleBookmark('${it.id}'); window.VidyaSetu.openBookmarksModal();">
                  Remove
                </button>
              </div>
            </div>
          `).join('')}
        </div>
      `;
    }

    if (els.bookmarksModal) els.bookmarksModal.style.display = 'flex';
  }

  function closeBookmarksModal() {
    if (els.bookmarksModal) els.bookmarksModal.style.display = 'none';
  }

  // --------------------------------------------------------------------------
  // Providers Directory View
  // --------------------------------------------------------------------------
  function renderProviders() {
    if (!els.providersGrid || !state.opportunities.length) return;

    const map = new Map();
    state.opportunities.forEach(it => {
      const slug = it.provider.slug;
      if (!map.has(slug)) {
        map.set(slug, {
          name: it.provider.name,
          slug: it.provider.slug,
          kind: it.provider.kind,
          website: it.provider.website,
          section: it.section,
          opportunities: []
        });
      }
      map.get(slug).opportunities.push(it);
    });

    const providers = Array.from(map.values()).sort((a, b) => a.name.localeCompare(b.name));

    els.providersGrid.innerHTML = providers.map(p => `
      <div class="opportunity-row">
        <div class="row-main">
          <div class="row-provider-line">
            <span>${p.section === 'india' ? 'India' : 'Abroad'}</span>
            <span>•</span>
            <span style="text-transform: capitalize;">${p.kind}</span>
          </div>
          <h3 class="row-title">
            <a href="#/provider/${p.slug}">
              ${p.name}
            </a>
          </h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">
            ${p.opportunities.length} listed opportunity / research position(s).
          </p>
        </div>
        <div class="row-side-actions">
          <a href="#/provider/${p.slug}" class="pill-btn small primary">
            View schemes (${p.opportunities.length})
          </a>
          <a href="${p.website}" target="_blank" rel="noopener noreferrer" class="pill-btn small text-only">
            Provider site
          </a>
        </div>
      </div>
    `).join('');
  }

  // --------------------------------------------------------------------------
  // Document Check Persistence
  // --------------------------------------------------------------------------
  function toggleDocCheck(oppId, docIdx, checked) {
    const key = `vidyasetu_docs_${oppId}`;
    const saved = JSON.parse(safeLocalStorage('get', key) || '{}');
    if (checked) {
      saved[docIdx] = true;
    } else {
      delete saved[docIdx];
    }
    safeLocalStorage('set', key, JSON.stringify(saved));
  }

  // --------------------------------------------------------------------------
  // Hash Routing
  // --------------------------------------------------------------------------
  function handleHashRouting() {
    window.addEventListener('hashchange', checkHashDeepLink);
    checkHashDeepLink();
  }

  function checkHashDeepLink() {
    const hash = window.location.hash;
    if (hash.startsWith('#/opportunity/')) {
      const oppId = hash.replace('#/opportunity/', '');
      openDetailModal(oppId);
    } else if (hash.startsWith('#/provider/')) {
      const slug = hash.replace('#/provider/', '');
      state.section = 'all';
      state.searchQuery = slug.replace(/-/g, ' ');
      if (els.searchInput) els.searchInput.value = state.searchQuery;
      renderCards();
      scrollToResults();
    } else if (hash === '#/providers') {
      state.section = 'providers';
      renderCards();
    }
  }

  // --------------------------------------------------------------------------
  // Theme Toggle (Dark / Light)
  // --------------------------------------------------------------------------
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    state.theme = theme;
    safeLocalStorage('set', 'vidyasetu_theme', theme);
  }

  function toggleTheme() {
    const next = state.theme === 'dark' ? 'light' : 'dark';
    applyTheme(next);
  }

  // --------------------------------------------------------------------------
  // Language Switch
  // --------------------------------------------------------------------------
  function toggleLanguage() {
    const next = state.lang === 'hi' ? 'en' : 'hi';
    state.lang = next;
    safeLocalStorage('set', 'vidyasetu_lang', next);
    if (els.langToggleBtn) {
      els.langToggleBtn.textContent = next === 'hi' ? 'Read in English' : 'हिंदी में पढ़ें';
    }
  }

  // --------------------------------------------------------------------------
  // Helpers & Utility
  // --------------------------------------------------------------------------
  function formatShortDate(isoDate) {
    if (!isoDate) return '';
    try {
      const parts = isoDate.split('-');
      if (parts.length === 3) {
        const d = parseInt(parts[2], 10);
        const m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][parseInt(parts[1], 10) - 1];
        return `${d} ${m}`;
      }
    } catch (e) {}
    return isoDate;
  }

  function scrollToResults() {
    if (els.resultsSection) {
      els.resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
  }

  // --------------------------------------------------------------------------
  // Event Listeners Binding
  // --------------------------------------------------------------------------
  function bindEvents() {
    // Theme & Lang
    if (els.themeToggleBtn) els.themeToggleBtn.addEventListener('click', toggleTheme);
    if (els.langToggleBtn) els.langToggleBtn.addEventListener('click', toggleLanguage);

    // Mobile Navigation Menu Toggle
    if (els.mobileMenuBtn && els.mainNavLinks) {
      els.mobileMenuBtn.addEventListener('click', () => {
        els.mainNavLinks.classList.toggle('mobile-open');
      });
    }

    // Logo click resets to home
    if (els.logoBrand) {
      els.logoBrand.addEventListener('click', () => {
        window.location.hash = '';
        state.section = 'all';
        state.level = 'all';
        state.searchQuery = '';
        if (els.searchInput) els.searchInput.value = '';
        renderCards();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Hero selects
    if (els.heroStage) els.heroStage.addEventListener('change', updateHeroSummary);
    if (els.heroPlace) els.heroPlace.addEventListener('change', updateHeroSummary);
    if (els.heroKind) els.heroKind.addEventListener('change', updateHeroSummary);

    // Hero Show All Button
    if (els.btnHeroShowAll) {
      els.btnHeroShowAll.addEventListener('click', () => {
        const stage = els.heroStage ? els.heroStage.value : 'After 12th';
        const place = els.heroPlace ? els.heroPlace.value : 'all';
        const kind = els.heroKind ? els.heroKind.value : 'all';

        state.level = stage;
        state.section = place;

        if (kind === 'funds') {
          state.category = 'Scholarship';
        } else if (kind === 'internships_projects') {
          state.category = 'Internship';
        } else {
          state.category = 'all';
        }

        if (els.filterLevel) els.filterLevel.value = stage;
        if (els.filterSection) els.filterSection.value = place;
        if (els.filterCategory) els.filterCategory.value = state.category;

        renderCards();
        scrollToResults();
      });
    }

    // Reset Hero
    if (els.btnResetHero) {
      els.btnResetHero.addEventListener('click', () => {
        if (els.heroStage) els.heroStage.value = 'After 12th';
        if (els.heroPlace) els.heroPlace.value = 'all';
        if (els.heroKind) els.heroKind.value = 'all';
        updateHeroSummary();
      });
    }

    // Road Track stops
    if (els.roadStops) {
      els.roadStops.forEach(stop => {
        stop.addEventListener('click', () => {
          const lvl = stop.getAttribute('data-level');
          state.level = lvl;
          if (els.heroStage) els.heroStage.value = lvl;
          if (els.filterLevel) els.filterLevel.value = lvl;
          updateHeroSummary();
          renderCards();
          scrollToResults();
        });
      });
    }

    // State Pills in Column 1
    if (els.statePillsContainer) {
      els.statePillsContainer.querySelectorAll('.state-pill-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const st = btn.getAttribute('data-state');
          state.section = 'india';
          state.stateFilter = st;
          if (els.filterSection) els.filterSection.value = 'india';
          renderCards();
          scrollToResults();
        });
      });
    }

    // Nav Links
    if (els.navLinkIndia) {
      els.navLinkIndia.addEventListener('click', (e) => {
        e.preventDefault();
        state.section = 'india';
        if (els.filterSection) els.filterSection.value = 'india';
        renderCards();
        scrollToResults();
      });
    }

    if (els.navLinkAbroad) {
      els.navLinkAbroad.addEventListener('click', (e) => {
        e.preventDefault();
        state.section = 'abroad';
        if (els.filterSection) els.filterSection.value = 'abroad';
        renderCards();
        scrollToResults();
      });
    }

    // Search Input with debounce
    let searchTimer = null;
    if (els.searchInput) {
      els.searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => {
          state.searchQuery = e.target.value;
          renderCards();
        }, 200);
      });
    }

    // Filters Sidebar Selects
    if (els.filterLevel) {
      els.filterLevel.addEventListener('change', (e) => {
        state.level = e.target.value;
        renderCards();
      });
    }

    if (els.filterSection) {
      els.filterSection.addEventListener('change', (e) => {
        state.section = e.target.value;
        renderCards();
      });
    }

    if (els.filterStatus) {
      els.filterStatus.addEventListener('change', (e) => {
        state.status = e.target.value;
        renderCards();
      });
    }

    if (els.filterCategory) {
      els.filterCategory.addEventListener('change', (e) => {
        state.category = e.target.value;
        renderCards();
      });
    }

    if (els.filterCountry) {
      els.filterCountry.addEventListener('change', (e) => {
        state.country = e.target.value;
        renderCards();
      });
    }

    if (els.filterTarget) {
      els.filterTarget.addEventListener('change', (e) => {
        state.target = e.target.value;
        renderCards();
      });
    }

    if (els.filterSort) {
      els.filterSort.addEventListener('change', (e) => {
        state.sort = e.target.value;
        renderCards();
      });
    }

    // Reset Filters Button
    const resetAllFilters = () => {
      state.level = 'all';
      state.section = 'all';
      state.status = 'all';
      state.category = 'all';
      state.country = 'all';
      state.stateFilter = 'all';
      state.target = 'all';
      state.searchQuery = '';

      if (els.filterLevel) els.filterLevel.value = 'all';
      if (els.filterSection) els.filterSection.value = 'all';
      if (els.filterStatus) els.filterStatus.value = 'all';
      if (els.filterCategory) els.filterCategory.value = 'all';
      if (els.filterCountry) els.filterCountry.value = 'all';
      if (els.filterTarget) els.filterTarget.value = 'all';
      if (els.searchInput) els.searchInput.value = '';

      renderCards();
    };

    if (els.btnResetFilters) els.btnResetFilters.addEventListener('click', resetAllFilters);
    if (els.btnResetNoResults) els.btnResetNoResults.addEventListener('click', resetAllFilters);

    // Mobile Filters Toggle
    if (els.btnMobileFilterToggle && els.filtersSidebar) {
      els.btnMobileFilterToggle.addEventListener('click', () => {
        els.filtersSidebar.classList.toggle('mobile-open');
      });
    }

    if (els.btnCloseMobileFilters && els.filtersSidebar) {
      els.btnCloseMobileFilters.addEventListener('click', () => {
        els.filtersSidebar.classList.remove('mobile-open');
      });
    }

    // Provider view buttons
    if (els.btnViewProviders) {
      els.btnViewProviders.addEventListener('click', () => {
        window.location.hash = '#/providers';
      });
    }

    if (els.btnBackToOpportunities) {
      els.btnBackToOpportunities.addEventListener('click', () => {
        window.location.hash = '';
        state.section = 'all';
        renderCards();
        scrollToResults();
      });
    }

    if (els.providerSearchInput) {
      els.providerSearchInput.addEventListener('input', (e) => {
        state.providerSearch = e.target.value.toLowerCase();
        renderProviders();
      });
    }

    // Modal Triggers
    if (els.btnOpenCalendar) els.btnOpenCalendar.addEventListener('click', openCalendarModal);
    if (els.btnOpenCalendarLink) els.btnOpenCalendarLink.addEventListener('click', openCalendarModal);
    if (els.calendarCloseBtn) els.calendarCloseBtn.addEventListener('click', closeCalendarModal);
    if (els.btnCloseCalendarFooter) els.btnCloseCalendarFooter.addEventListener('click', closeCalendarModal);

    if (els.modalCloseBtn) els.modalCloseBtn.addEventListener('click', closeDetailModal);

    if (els.btnOpenWizard) els.btnOpenWizard.addEventListener('click', openWizardModal);
    if (els.wizardCloseBtn) els.wizardCloseBtn.addEventListener('click', closeWizardModal);
    if (els.btnCancelWizard) els.btnCancelWizard.addEventListener('click', closeWizardModal);
    if (els.btnApplyWizard) els.btnApplyWizard.addEventListener('click', applyWizard);

    if (els.btnSavedBookmarks) els.btnSavedBookmarks.addEventListener('click', openBookmarksModal);
    if (els.bookmarksCloseBtn) els.bookmarksCloseBtn.addEventListener('click', closeBookmarksModal);
    if (els.btnCloseBookmarksFooter) els.btnCloseBookmarksFooter.addEventListener('click', closeBookmarksModal);
    if (els.btnClearAllBookmarks) {
      els.btnClearAllBookmarks.addEventListener('click', () => {
        state.bookmarks = [];
        safeLocalStorage('set', 'vidyasetu_bookmarks', '[]');
        updateBookmarkBadge();
        openBookmarksModal();
        renderCards();
      });
    }

    if (els.btnLaunchComparison) els.btnLaunchComparison.addEventListener('click', openCompareModal);
    if (els.compareCloseBtn) els.compareCloseBtn.addEventListener('click', closeCompareModal);
    if (els.btnCloseCompareFooter) els.btnCloseCompareFooter.addEventListener('click', closeCompareModal);
    if (els.btnClearComparison) {
      els.btnClearComparison.addEventListener('click', () => {
        state.compare = [];
        updateCompareDrawer();
        renderCards();
      });
    }

    // Close Modals on Overlay Click or Esc Key
    window.addEventListener('click', (e) => {
      if (e.target === els.detailModal) closeDetailModal();
      if (e.target === els.calendarModal) closeCalendarModal();
      if (e.target === els.wizardModal) closeWizardModal();
      if (e.target === els.compareModal) closeCompareModal();
      if (e.target === els.bookmarksModal) closeBookmarksModal();
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeDetailModal();
        closeCalendarModal();
        closeWizardModal();
        closeCompareModal();
        closeBookmarksModal();
      }
    });
  }

  // --------------------------------------------------------------------------
  // Global API
  // --------------------------------------------------------------------------
  window.VidyaSetu = {
    openDetailModal,
    closeDetailModal,
    toggleBookmark,
    toggleCompare,
    openBookmarksModal,
    toggleDocCheck
  };

  // Launch on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
