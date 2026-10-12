// VidyaSetu Core Application Engine - Self-Updating Edition

(function () {
  'use strict';

  // Global State
  const state = {
    opportunities: [],
    meta: null,
    loading: true,
    error: null,

    // Filter states
    section: 'all', // 'all', 'india', 'abroad', 'providers'
    level: 'all',
    status: 'all',
    category: 'all',
    country: 'all',
    stateFilter: 'all',
    target: 'all',
    income: 'all',
    searchQuery: '',
    sort: 'default',
    activeChip: null,

    // Provider filter
    providerKind: 'all',
    providerSearch: '',
    selectedProviderSlug: null,

    // Preferences & Features
    lang: localStorage.getItem('vidyasetu_lang') || 'en',
    theme: localStorage.getItem('vidyasetu_theme') || 'light',
    viewMode: 'grid', // 'grid' or 'compact'
    bookmarks: JSON.parse(localStorage.getItem('vidyasetu_bookmarks') || '[]'),
    compare: []
  };

  // Hindi Translations Dictionary
  const I18N = {
    en: {
      siteTagline: "National & Global Opportunities Portal",
      navWizardText: "Match My Profile",
      navCalendarText: "Deadline Calendar",
      navSavedText: "Saved",
      navSubmitText: "Submit Opportunity",
      heroBadgeLevels: "12th Pass • Bachelor's • Master's • PhD • Postdoc",
      verifiedBadge: "✓ Verified Daily by Official Sources",
      heroMainTitle: "Every Scholarship, Government Fund, Private Grant & Internship in One Place.",
      heroSubTitle: "150+ verified opportunities across MoE, DST, AICTE, CSIR, Indian state portals, Tata Trusts, Reliance, and fully funded global fellowships in Europe, USA, UK, Canada, Japan, and Australia.",
      lblMetricIndia: "Opportunities in India",
      lblMetricAbroad: "Opportunities Abroad",
      lblMetricGov: "Government Funds",
      lblMetricPvt: "Private & CSR Funds",
      lblMetricIntern: "Funded Internships",
      tabLabelAll: "All Opportunities",
      tabLabelIndia: "SECTION 1: India",
      tabLabelAbroad: "SECTION 2: Abroad",
      tabLabelProviders: "Providers Directory",
      btnFindEligibleText: "Find Eligible Opportunities",
      lblQuickFilters: "Quick Filters:",
      lblClearFilters: "Clear Filters",
      lblLoadingTitle: "Loading Verified Opportunities...",
      lblGuidesTitle: "Essential Guides & Preparation Resources",
      lblGuidesSub: "Everything you need to successfully win national and international scholarships"
    },
    hi: {
      siteTagline: "राष्ट्रीय एवं अंतर्राष्ट्रीय अवसर पोर्टल",
      navWizardText: "मेरी योग्यता जाँचें",
      navCalendarText: "आवेदन कैलेंडर",
      navSavedText: "सहेजे गए",
      navSubmitText: "नया अवसर जोड़ें",
      heroBadgeLevels: "12वीं पास • स्नातक • स्नातकोत्तर • पीएचडी • पोस्टडॉक",
      verifiedBadge: "✓ आधिकारिक स्रोतों द्वारा दैनिक सत्यापित",
      heroMainTitle: "सभी सरकारी व निजी छात्रवृत्तियां, रिसर्च प्रोजेक्ट और इंटर्नशिप एक ही स्थान पर।",
      heroSubTitle: "शिक्षा मंत्रालय, DST, AICTE, CSIR, राज्य पोर्टलों, टाटा ट्रस्ट्स, रिलायंस और यूरोप, अमेरिका, यूके, कनाडा, जापान की 150+ पूर्णतः वित्तपोषित छात्रवृत्तियां।",
      lblMetricIndia: "भारत में अवसर",
      lblMetricAbroad: "विदेश में अवसर",
      lblMetricGov: "सरकारी फंड्स",
      lblMetricPvt: "निजी व CSR फंड्स",
      lblMetricIntern: "सवेतन इंटर्नशिप",
      tabLabelAll: "सभी अवसर",
      tabLabelIndia: "भाग 1: भारत में अवसर",
      tabLabelAbroad: "भाग 2: विदेश में अवसर",
      tabLabelProviders: "संस्थान निर्देशिका",
      btnFindEligibleText: "पात्र अवसर खोजें",
      lblQuickFilters: "त्वरित फ़िल्टर:",
      lblClearFilters: "फ़िल्टर हटाएं",
      lblLoadingTitle: "सत्यापित अवसर लोड हो रहे हैं...",
      lblGuidesTitle: "महत्वपूर्ण मार्गदर्शिका एवं दस्तावेज़ चेकलिस्ट",
      lblGuidesSub: "राष्ट्रीय व वैश्विक छात्रवृत्तियों में सफलता पाने हेतु सम्पूर्ण विवरण"
    }
  };

  // DOM Elements
  const els = {
    // Top Bar
    closingSoonStrip: document.getElementById('closingSoonStrip'),
    closingSoonCarousel: document.getElementById('closingSoonCarousel'),
    langToggleBtn: document.getElementById('langToggleBtn'),
    currentLangLabel: document.getElementById('currentLangLabel'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeIcon: document.getElementById('themeIcon'),
    verifiedStatusBadge: document.getElementById('verifiedStatusBadge'),

    // Hero metrics
    metricIndiaCount: document.getElementById('metricIndiaCount'),
    metricAbroadCount: document.getElementById('metricAbroadCount'),
    metricGovCount: document.getElementById('metricGovCount'),
    metricPvtCount: document.getElementById('metricPvtCount'),
    metricInternCount: document.getElementById('metricInternCount'),

    // Section tabs
    tabSectionAll: document.getElementById('tabSectionAll'),
    tabSectionIndia: document.getElementById('tabSectionIndia'),
    tabSectionAbroad: document.getElementById('tabSectionAbroad'),
    tabSectionProviders: document.getElementById('tabSectionProviders'),
    badgeAll: document.getElementById('badgeAll'),
    badgeIndia: document.getElementById('badgeIndia'),
    badgeAbroad: document.getElementById('badgeAbroad'),
    badgeProviders: document.getElementById('badgeProviders'),

    // Filter controls
    filterSection: document.getElementById('filterSection'),
    searchInput: document.getElementById('searchInput'),
    btnHeroWizard: document.getElementById('btnHeroWizard'),
    filterLevel: document.getElementById('filterLevel'),
    filterStatus: document.getElementById('filterStatus'),
    filterCategory: document.getElementById('filterCategory'),
    filterCountry: document.getElementById('filterCountry'),
    filterState: document.getElementById('filterState'),
    filterTarget: document.getElementById('filterTarget'),
    filterIncome: document.getElementById('filterIncome'),
    chips: document.querySelectorAll('.chip-btn'),
    btnResetFilters: document.getElementById('btnResetFilters'),

    // Views & Containers
    loadingState: document.getElementById('loadingState'),
    errorState: document.getElementById('errorState'),
    errorMessage: document.getElementById('errorMessage'),
    resultsMeta: document.getElementById('resultsMeta'),
    resultsCountText: document.getElementById('resultsCountText'),
    cardsGridContainer: document.getElementById('cardsGridContainer'),
    providersContainer: document.getElementById('providersContainer'),
    providersGrid: document.getElementById('providersGrid'),
    providerSearchInput: document.getElementById('providerSearchInput'),
    providerKindFilter: document.getElementById('providerKindFilter'),
    noResultsState: document.getElementById('noResultsState'),
    btnResetNoResults: document.getElementById('btnResetNoResults'),

    viewModeGrid: document.getElementById('viewModeGrid'),
    viewModeCompact: document.getElementById('viewModeCompact'),

    // Modals
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
    modalReportBrokenBtn: document.getElementById('modalReportBrokenBtn'),
    btnModalGoogleCal: document.getElementById('btnModalGoogleCal'),
    btnModalICS: document.getElementById('btnModalICS'),

    // Wizard
    btnOpenWizard: document.getElementById('btnOpenWizard'),
    wizardModal: document.getElementById('wizardModal'),
    wizardCloseBtn: document.getElementById('wizardCloseBtn'),
    btnCancelWizard: document.getElementById('btnCancelWizard'),
    btnApplyWizard: document.getElementById('btnApplyWizard'),
    wizLevel: document.getElementById('wizLevel'),
    wizStream: document.getElementById('wizStream'),
    wizCategory: document.getElementById('wizCategory'),
    wizDestination: document.getElementById('wizDestination'),

    // Comparison Drawer & Modal
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
    dynamicCalendarGrid: document.getElementById('dynamicCalendarGrid'),

    // Bookmarks Modal
    btnSavedBookmarks: document.getElementById('btnSavedBookmarks'),
    savedCountBadge: document.getElementById('savedCountBadge'),
    bookmarksModal: document.getElementById('bookmarksModal'),
    bookmarksCloseBtn: document.getElementById('bookmarksCloseBtn'),
    btnCloseBookmarksFooter: document.getElementById('btnCloseBookmarksFooter'),
    bookmarksListBody: document.getElementById('bookmarksListBody'),
    btnClearAllBookmarks: document.getElementById('btnClearAllBookmarks')
  };

  let activeModalItem = null;

  // Initialize Application
  async function init() {
    applyTheme(state.theme);
    applyLanguage(state.lang);
    bindEvents();
    handleHashRouting();

    try {
      await loadData();
    } catch (err) {
      showError(err.message);
    }
  }

  // Fetch Data from JSON files (Phase 1)
  async function loadData() {
    els.loadingState.style.display = 'block';
    els.errorState.style.display = 'none';

    try {
      const [oppsRes, metaRes] = await Promise.all([
        fetch('data/opportunities.json'),
        fetch('data/meta.json').catch(() => null)
      ]);

      if (!oppsRes.ok) {
        throw new Error(`Failed to load opportunities data (HTTP ${oppsRes.status})`);
      }

      state.opportunities = await oppsRes.json();
      if (metaRes && metaRes.ok) {
        state.meta = await metaRes.json();
      }

      state.loading = false;
      els.loadingState.style.display = 'none';

      updateMetrics();
      renderClosingSoonStrip();
      renderCards();
      renderProviders();
      updateBookmarkBadge();

      // Check if hash points to specific opportunity
      checkHashDeepLink();
    } catch (e) {
      state.loading = false;
      showError(e.message || "Failed to load data/opportunities.json");
    }
  }

  function showError(msg) {
    els.loadingState.style.display = 'none';
    els.errorState.style.display = 'block';
    els.errorMessage.textContent = msg;
  }

  // Theme Management
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

  // Language Management (Phase 5)
  function applyLanguage(lang) {
    state.lang = lang;
    localStorage.setItem('vidyasetu_lang', lang);
    const dict = I18N[lang] || I18N.en;

    els.currentLangLabel.textContent = lang === 'en' ? 'हिंदी' : 'English';

    Object.keys(dict).forEach(key => {
      const el = document.getElementById(key);
      if (el) el.textContent = dict[key];
    });
  }

  function toggleLanguage() {
    applyLanguage(state.lang === 'en' ? 'hi' : 'en');
  }

  // Metrics & Badges
  function updateMetrics() {
    const total = state.opportunities.length;
    const india = state.opportunities.filter(o => o.section === 'india').length;
    const abroad = state.opportunities.filter(o => o.section === 'abroad').length;
    const gov = state.opportunities.filter(o => o.type === 'government').length;
    const pvt = state.opportunities.filter(o => o.type === 'private').length;
    const intern = state.opportunities.filter(o => o.category === 'Internship').length;

    // Unique providers count
    const providersSet = new Set(state.opportunities.map(o => o.provider.slug));

    els.metricIndiaCount.textContent = india;
    els.metricAbroadCount.textContent = abroad;
    els.metricGovCount.textContent = gov;
    els.metricPvtCount.textContent = pvt;
    els.metricInternCount.textContent = intern;

    els.badgeAll.textContent = total;
    els.badgeIndia.textContent = india;
    els.badgeAbroad.textContent = abroad;
    els.badgeProviders.textContent = providersSet.size;

    // Meta verification badge
    if (state.meta && state.meta.lastVerifiedDate) {
      els.verifiedStatusBadge.innerHTML = `<span>✓</span> Verified ${state.meta.lastVerifiedDate} (${total} Schemes)`;
    }
  }

  // Imminent Deadline / Closing Soon Strip (Phase 5)
  function renderClosingSoonStrip() {
    const today = new Date().toISOString().slice(0, 10);
    const withDeadlines = state.opportunities
      .filter(o => o.deadline && o.deadline >= today)
      .sort((a, b) => a.deadline.localeCompare(b.deadline))
      .slice(0, 8);

    if (withDeadlines.length === 0) {
      els.closingSoonStrip.style.display = 'none';
      return;
    }

    els.closingSoonCarousel.innerHTML = withDeadlines.map(it => `
      <div class="closing-pill" onclick="window.VidyaSetu.openDetailModal('${it.id}')">
        <span>⏰ ${it.deadline}</span>: <strong>${it.title.slice(0, 32)}...</strong>
      </div>
    `).join('');
  }

  // Bookmarking
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

  // Comparison
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
    const today = new Date().toISOString().slice(0, 10);

    return state.opportunities.filter(item => {
      // 1. Specific Provider slug filter
      if (state.selectedProviderSlug && item.provider.slug !== state.selectedProviderSlug) {
        return false;
      }

      // 2. Section (All, India, Abroad)
      if (state.section !== 'all' && state.section !== 'providers' && item.section !== state.section) {
        return false;
      }

      // 3. Education level
      if (state.level !== 'all' && !item.educationLevel.includes(state.level)) {
        return false;
      }

      // 4. Status Filter
      if (state.status !== 'all') {
        if (state.status === 'closing-soon') {
          if (!item.deadline || item.deadline < today) return false;
          const diffDays = (new Date(item.deadline) - new Date(today)) / (1000 * 60 * 60 * 24);
          if (diffDays > 30) return false;
        } else if (item.status !== state.status) {
          return false;
        }
      }

      // 5. Category Filter
      if (state.category !== 'all' && item.category !== state.category) {
        return false;
      }

      // 6. Country Filter
      if (state.country !== 'all') {
        if (!item.country || !item.country.toLowerCase().includes(state.country.toLowerCase())) {
          return false;
        }
      }

      // 7. State Filter
      if (state.stateFilter !== 'all') {
        if (!item.state || item.state !== state.stateFilter) {
          return false;
        }
      }

      // 8. Target Group / Quota
      if (state.target !== 'all') {
        const tgStr = item.targetGroup.join(' ').toLowerCase();
        if (state.target === 'women' && !tgStr.includes('women') && !tgStr.includes('girl')) return false;
        if (state.target === 'sc' && !tgStr.includes('sc') && !tgStr.includes('scheduled caste')) return false;
        if (state.target === 'st' && !tgStr.includes('st') && !tgStr.includes('scheduled tribe')) return false;
        if (state.target === 'obc' && !tgStr.includes('obc') && !tgStr.includes('backward')) return false;
        if (state.target === 'minority' && !tgStr.includes('minority')) return false;
        if (state.target === 'pwd' && !tgStr.includes('pwd') && !tgStr.includes('disab')) return false;
        if (state.target === 'merit' && !tgStr.includes('merit')) return false;
      }

      // 9. Income Limit
      if (state.income !== 'all') {
        const cap = parseInt(state.income, 10);
        if (item.incomeLimitINR !== null && item.incomeLimitINR > cap) {
          return false;
        }
      }

      // 10. Quick Chips
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
          case 'postdoc':
            if (!item.educationLevel.includes('Postdoc')) return false;
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
          case 'jrf':
            if (!item.category.includes('Project Position')) return false;
            break;
        }
      }

      // 11. Search Query
      if (state.searchQuery.trim() !== '') {
        const q = state.searchQuery.toLowerCase();
        const inTitle = item.title.toLowerCase().includes(q);
        const inAgency = item.provider.name.toLowerCase().includes(q);
        const inEligibility = item.eligibility.toLowerCase().includes(q);
        const inTags = item.tags.some(t => t.toLowerCase().includes(q));
        const inStreams = item.streams.some(s => s.toLowerCase().includes(q));

        if (!inTitle && !inAgency && !inEligibility && !inTags && !inStreams) {
          return false;
        }
      }

      return true;
    }).sort((a, b) => {
      if (state.sort === 'amount-high') {
        return (b.amountValINR || 0) - (a.amountValINR || 0);
      }
      if (state.sort === 'title-asc') {
        return a.title.localeCompare(b.title);
      }
      return 0;
    });
  }

  // Render Opportunities Cards
  function renderCards() {
    if (state.section === 'providers') {
      els.cardsGridContainer.style.display = 'none';
      els.filterSection.style.display = 'none';
      els.resultsMeta.style.display = 'none';
      els.providersContainer.style.display = 'block';
      return;
    } else {
      els.cardsGridContainer.style.display = 'grid';
      els.filterSection.style.display = 'block';
      els.resultsMeta.style.display = 'flex';
      els.providersContainer.style.display = 'none';
    }

    const list = getFilteredOpportunities();

    els.resultsCountText.innerHTML = `Showing <span>${list.length}</span> ${
      state.selectedProviderSlug ? `Opportunities from ${state.selectedProviderSlug}` :
      state.section === 'india' ? 'Opportunities in India' : 
      state.section === 'abroad' ? 'Opportunities Abroad' : 
      'Verified Opportunities'
    }`;

    if (list.length === 0) {
      els.cardsGridContainer.innerHTML = '';
      els.noResultsState.style.display = 'block';
      return;
    } else {
      els.noResultsState.style.display = 'none';
    }

    if (state.viewMode === 'compact') {
      els.cardsGridContainer.style.gridTemplateColumns = '1fr';
    } else {
      els.cardsGridContainer.style.gridTemplateColumns = 'repeat(auto-fill, minmax(400px, 1fr))';
    }

    els.cardsGridContainer.innerHTML = list.map(item => {
      const bookmarked = isBookmarked(item.id);
      const compared = isInCompare(item.id);
      const isIndia = item.section === 'india';

      const sectionBadge = isIndia 
        ? '<span class="badge badge-india">🇮🇳 India</span>'
        : `<span class="badge badge-abroad">🌍 ${item.country || 'Abroad'}</span>`;

      const typeBadge = item.type === 'government'
        ? '<span class="badge badge-gov">🏛️ Govt Fund</span>'
        : item.type === 'university'
        ? '<span class="badge badge-uni">🎓 University</span>'
        : '<span class="badge badge-pvt">💼 Private CSR</span>';

      const statusBadge = `<span class="badge badge-status-${item.status}">${item.status.toUpperCase()}</span>`;
      const levelPills = item.educationLevel.map(l => `<span class="level-tag">${l}</span>`).join('');

      return `
        <article class="opportunity-card" data-id="${item.id}">
          <div class="card-top-bar">
            <div class="badge-group">
              ${sectionBadge}
              ${typeBadge}
              ${statusBadge}
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
            <a href="#/provider/${item.provider.slug}" class="agency-label-link" title="View all from this provider">
              🏛️ ${item.provider.name} <span>→</span>
            </a>
            <h3 class="card-title" onclick="window.VidyaSetu.openDetailModal('${item.id}')">${item.title}</h3>

            <!-- Funding Highlight -->
            <div class="funding-highlight">
              <div class="funding-amount">
                <span>💰</span> ${item.fundingAmount}
              </div>
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
              <span class="deadline-label">Deadline / Timeline</span>
              <span class="deadline-val">📅 ${item.deadline || item.deadlineText}</span>
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

  // Render Providers Directory (Phase 4)
  function renderProviders() {
    const providersMap = new Map();

    state.opportunities.forEach(it => {
      const slug = it.provider.slug;
      if (!providersMap.has(slug)) {
        providersMap.set(slug, {
          name: it.provider.name,
          slug: it.provider.slug,
          kind: it.provider.kind,
          website: it.provider.website,
          section: it.section,
          opportunities: []
        });
      }
      providersMap.get(slug).opportunities.push(it);
    });

    const providers = Array.from(providersMap.values()).filter(p => {
      if (state.providerKind !== 'all' && p.kind !== state.providerKind) return false;
      if (state.providerSearch.trim() !== '') {
        const q = state.providerSearch.toLowerCase();
        if (!p.name.toLowerCase().includes(q)) return false;
      }
      return true;
    }).sort((a, b) => a.name.localeCompare(b.name));

    els.providersGrid.innerHTML = providers.map(p => `
      <div class="provider-card">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
            <span class="badge ${p.section === 'india' ? 'badge-india' : 'badge-abroad'}">${p.section === 'india' ? '🇮🇳 India' : '🌍 Abroad'}</span>
            <span class="badge badge-uni">${p.kind.toUpperCase()}</span>
          </div>
          <h3 style="font-size: 1.15rem; margin-bottom: 6px;">${p.name}</h3>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 14px;">
            ${p.opportunities.length} Total Verified Scheme(s) / Post(s)
          </p>
        </div>
        <div style="display: flex; gap: 8px; border-top: 1px solid var(--border-color); padding-top: 14px;">
          <a href="#/provider/${p.slug}" class="nav-btn primary" style="font-size: 0.82rem; flex: 1; text-align: center; justify-content: center;">
            View All Opportunities (${p.opportunities.length})
          </a>
          <a href="${p.website}" target="_blank" rel="noopener noreferrer" class="nav-btn" style="font-size: 0.82rem;" title="Official Website">
            Website ↗
          </a>
        </div>
      </div>
    `).join('');
  }

  // Open Full Detail Modal with Google Cal & .ics
  function openDetailModal(id) {
    const item = state.opportunities.find(o => o.id === id);
    if (!item) return;

    activeModalItem = item;

    // Badges
    const isIndia = item.section === 'india';
    els.modalBadgeGroup.innerHTML = `
      <span class="badge ${isIndia ? 'badge-india' : 'badge-abroad'}">${isIndia ? '🇮🇳 India' : '🌍 ' + item.country}</span>
      <span class="badge badge-gov">${item.type.toUpperCase()}</span>
      <span class="badge badge-intern">${item.category}</span>
      <span class="badge badge-status-${item.status}">${item.status.toUpperCase()}</span>
    `;

    els.modalTitle.textContent = item.title;
    els.modalAgency.textContent = item.provider.name;
    els.modalAmount.textContent = item.fundingAmount;
    els.modalCoverage.textContent = `Provider Website: ${item.provider.website}`;
    els.modalEligibility.textContent = item.eligibility;

    // Levels & Streams
    els.modalLevels.innerHTML = item.educationLevel.map(l => `<span class="level-tag" style="font-size: 0.82rem; padding: 5px 12px;">${l}</span>`).join('');
    els.modalStreams.innerHTML = item.streams.map(s => `<span class="level-tag" style="font-size: 0.82rem; padding: 5px 12px; background: rgba(37, 99, 235, 0.08); color: var(--brand-primary);">${s}</span>`).join('');

    // Document Checklist
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

    // Deadline & Calendar Links (Phase 5)
    els.modalDeadline.textContent = item.deadline ? `${item.deadline} (${item.deadlineText})` : item.deadlineText;
    setupCalendarExports(item);

    // Official and report broken links
    els.modalOfficialLink.href = item.officialLink;
    const reportUrl = `https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/issues/new?template=report_broken_link.yml&title=%5BReport%5D+Issue+with+${encodeURIComponent(item.title)}&opportunity_id=${encodeURIComponent(item.id)}&current_link=${encodeURIComponent(item.officialLink)}`;
    els.modalReportBrokenBtn.href = reportUrl;

    updateModalBookmarkBtn();

    els.detailModal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Update URL hash for sharing
    window.location.hash = `/opportunity/${item.id}`;
  }

  function setupCalendarExports(item) {
    if (!item.deadline) {
      els.btnModalGoogleCal.style.display = 'none';
      els.btnModalICS.style.display = 'none';
      return;
    }

    els.btnModalGoogleCal.style.display = 'inline-flex';
    els.btnModalICS.style.display = 'inline-flex';

    // Google Calendar URL
    const dateFormatted = item.deadline.replace(/-/g, '');
    const gCalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent('Deadline: ' + item.title)}&dates=${dateFormatted}/${dateFormatted}&details=${encodeURIComponent('Official Application Link: ' + item.officialLink + '\n\nEligibility: ' + item.eligibility)}&location=${encodeURIComponent(item.provider.name)}`;
    els.btnModalGoogleCal.href = gCalUrl;

    // .ics file generator
    els.btnModalICS.onclick = () => {
      const icsData = `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//VidyaSetu//Scholarship Deadlines//EN
BEGIN:VEVENT
SUMMARY:Application Deadline: ${item.title}
DESCRIPTION:Official Portal: ${item.officialLink}\\n\\nProvider: ${item.provider.name}
DTSTART;VALUE=DATE:${dateFormatted}
DTEND;VALUE=DATE:${dateFormatted}
LOCATION:${item.provider.name}
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR`;
      const blob = new Blob([icsData], { type: 'text/calendar;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `${item.id}-deadline.ics`;
      link.click();
      URL.revokeObjectURL(url);
    };
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
    if (window.location.hash.startsWith('#/opportunity/')) {
      window.location.hash = '';
    }
  }

  // Hash Routing & Deep Linking (Phase 5)
  function handleHashRouting() {
    window.addEventListener('hashchange', checkHashDeepLink);
  }

  function checkHashDeepLink() {
    const hash = window.location.hash;
    if (hash.startsWith('#/opportunity/')) {
      const oppId = hash.replace('#/opportunity/', '');
      openDetailModal(oppId);
    } else if (hash.startsWith('#/provider/')) {
      const slug = hash.replace('#/provider/', '');
      state.selectedProviderSlug = slug;
      state.section = 'all';
      updateSectionTabsUI();
      renderCards();
    } else if (hash === '#/providers') {
      state.section = 'providers';
      updateSectionTabsUI();
      renderCards();
    }
  }

  function updateSectionTabsUI() {
    [els.tabSectionAll, els.tabSectionIndia, els.tabSectionAbroad, els.tabSectionProviders].forEach(t => t.classList.remove('active'));
    if (state.section === 'india') els.tabSectionIndia.classList.add('active');
    else if (state.section === 'abroad') els.tabSectionAbroad.classList.add('active');
    else if (state.section === 'providers') els.tabSectionProviders.classList.add('active');
    else els.tabSectionAll.classList.add('active');
  }

  // Profile Matching Wizard
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

    state.level = level;
    els.filterLevel.value = level;

    if (stream !== 'All Disciplines') {
      state.searchQuery = stream;
      els.searchInput.value = stream;
    }

    if (destination !== 'all') {
      state.section = destination;
    } else {
      state.section = 'all';
    }

    if (category === 'women') {
      state.target = 'women';
      els.filterTarget.value = 'women';
    } else if (category === 'means') {
      state.income = '450000';
      els.filterIncome.value = '450000';
    }

    updateSectionTabsUI();
    closeWizardModal();
    renderCards();
    els.resultsCountText.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // Dynamic Deadline Calendar (Phase 5)
  function openCalendarModal() {
    const quarters = { Q1: [], Q2: [], Q3: [], Q4: [] };

    state.opportunities.forEach(it => {
      const text = (it.deadline || it.deadlineText || '').toLowerCase();
      if (text.includes('-01-') || text.includes('-02-') || text.includes('-03-') || text.includes('jan') || text.includes('feb') || text.includes('mar')) {
        quarters.Q1.push(it);
      } else if (text.includes('-04-') || text.includes('-05-') || text.includes('-06-') || text.includes('apr') || text.includes('may') || text.includes('jun')) {
        quarters.Q2.push(it);
      } else if (text.includes('-07-') || text.includes('-08-') || text.includes('-09-') || text.includes('jul') || text.includes('aug') || text.includes('sep')) {
        quarters.Q3.push(it);
      } else {
        quarters.Q4.push(it);
      }
    });

    els.dynamicCalendarGrid.innerHTML = `
      <div class="detail-box">
        <h4 style="color: #2563eb; margin-bottom: 8px;">❄️ Jan - Mar (Q1) - ${quarters.Q1.length} Schemes</h4>
        <ul style="font-size: 0.82rem; padding-left: 18px; line-height: 1.6; color: var(--text-secondary);">
          ${quarters.Q1.slice(0, 10).map(it => `<li><strong>${it.title.slice(0, 30)}...:</strong> ${it.deadline || it.deadlineText}</li>`).join('')}
        </ul>
      </div>
      <div class="detail-box">
        <h4 style="color: #059669; margin-bottom: 8px;">🌸 Apr - Jun (Q2) - ${quarters.Q2.length} Schemes</h4>
        <ul style="font-size: 0.82rem; padding-left: 18px; line-height: 1.6; color: var(--text-secondary);">
          ${quarters.Q2.slice(0, 10).map(it => `<li><strong>${it.title.slice(0, 30)}...:</strong> ${it.deadline || it.deadlineText}</li>`).join('')}
        </ul>
      </div>
      <div class="detail-box">
        <h4 style="color: #d97706; margin-bottom: 8px;">☀️ Jul - Sep (Q3) - ${quarters.Q3.length} Schemes</h4>
        <ul style="font-size: 0.82rem; padding-left: 18px; line-height: 1.6; color: var(--text-secondary);">
          ${quarters.Q3.slice(0, 10).map(it => `<li><strong>${it.title.slice(0, 30)}...:</strong> ${it.deadline || it.deadlineText}</li>`).join('')}
        </ul>
      </div>
      <div class="detail-box">
        <h4 style="color: #7c3aed; margin-bottom: 8px;">🍂 Oct - Dec (Q4) - ${quarters.Q4.length} Schemes</h4>
        <ul style="font-size: 0.82rem; padding-left: 18px; line-height: 1.6; color: var(--text-secondary);">
          ${quarters.Q4.slice(0, 10).map(it => `<li><strong>${it.title.slice(0, 30)}...:</strong> ${it.deadline || it.deadlineText}</li>`).join('')}
        </ul>
      </div>
    `;

    els.calendarModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCalendarModal() {
    els.calendarModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Side-by-Side Comparison
  function openComparisonModal() {
    if (state.compare.length === 0) return;
    const items = state.opportunities.filter(o => state.compare.includes(o.id));

    let html = `
      <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
        <thead>
          <tr style="background: var(--bg-primary); border-bottom: 2px solid var(--border-color);">
            <th style="padding: 14px; min-width: 140px;">Feature</th>
            ${items.map(it => `
              <th style="padding: 14px; min-width: 240px; vertical-align: top;">
                <div style="font-size: 1rem; font-weight: 700; margin-bottom: 6px;">${it.title}</div>
                <span class="badge ${it.section === 'india' ? 'badge-india' : 'badge-abroad'}">${it.section === 'india' ? 'India' : it.country}</span>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 12px 14px; font-weight: 700;">Funding Agency</td>
            ${items.map(it => `<td style="padding: 12px 14px;">${it.provider.name}</td>`).join('')}
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color); background: rgba(37, 99, 235, 0.04);">
            <td style="padding: 12px 14px; font-weight: 700; color: var(--brand-primary);">Amount & Stipend</td>
            ${items.map(it => `<td style="padding: 12px 14px; font-weight: 700; color: var(--brand-primary);">${it.fundingAmount}</td>`).join('')}
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
            ${items.map(it => `<td style="padding: 12px 14px; font-weight: 600;">${it.deadline || it.deadlineText}</td>`).join('')}
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
    const list = state.opportunities.filter(o => state.bookmarks.includes(o.id));
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
            <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">${item.provider.name}</div>
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

  // Reset Filters
  function resetAllFilters() {
    state.searchQuery = '';
    state.level = 'all';
    state.status = 'all';
    state.category = 'all';
    state.country = 'all';
    state.stateFilter = 'all';
    state.target = 'all';
    state.income = 'all';
    state.sort = 'default';
    state.activeChip = null;
    state.selectedProviderSlug = null;

    els.searchInput.value = '';
    els.filterLevel.value = 'all';
    els.filterStatus.value = 'all';
    els.filterCategory.value = 'all';
    els.filterCountry.value = 'all';
    els.filterState.value = 'all';
    els.filterTarget.value = 'all';
    els.filterIncome.value = 'all';

    els.chips.forEach(c => c.classList.remove('active'));
    renderCards();
  }

  // Event Listeners Binding
  function bindEvents() {
    els.themeToggleBtn.addEventListener('click', toggleTheme);
    els.langToggleBtn.addEventListener('click', toggleLanguage);

    // Section tabs
    els.tabSectionAll.addEventListener('click', () => {
      state.section = 'all';
      state.selectedProviderSlug = null;
      updateSectionTabsUI();
      renderCards();
    });
    els.tabSectionIndia.addEventListener('click', () => {
      state.section = 'india';
      state.selectedProviderSlug = null;
      updateSectionTabsUI();
      renderCards();
    });
    els.tabSectionAbroad.addEventListener('click', () => {
      state.section = 'abroad';
      state.selectedProviderSlug = null;
      updateSectionTabsUI();
      renderCards();
    });
    els.tabSectionProviders.addEventListener('click', () => {
      state.section = 'providers';
      updateSectionTabsUI();
      renderCards();
    });

    // Inputs
    els.searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderCards();
    });
    els.filterLevel.addEventListener('change', (e) => {
      state.level = e.target.value;
      renderCards();
    });
    els.filterStatus.addEventListener('change', (e) => {
      state.status = e.target.value;
      renderCards();
    });
    els.filterCategory.addEventListener('change', (e) => {
      state.category = e.target.value;
      renderCards();
    });
    els.filterCountry.addEventListener('change', (e) => {
      state.country = e.target.value;
      renderCards();
    });
    els.filterState.addEventListener('change', (e) => {
      state.stateFilter = e.target.value;
      renderCards();
    });
    els.filterTarget.addEventListener('change', (e) => {
      state.target = e.target.value;
      renderCards();
    });
    els.filterIncome.addEventListener('change', (e) => {
      state.income = e.target.value;
      renderCards();
    });

    // Provider search & filter
    els.providerSearchInput.addEventListener('input', (e) => {
      state.providerSearch = e.target.value;
      renderProviders();
    });
    els.providerKindFilter.addEventListener('change', (e) => {
      state.providerKind = e.target.value;
      renderProviders();
    });

    // Chips
    els.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        const val = chip.getAttribute('data-chip');
        if (state.activeChip === val) {
          state.activeChip = null;
          chip.classList.remove('active');
        } else {
          els.chips.forEach(c => c.classList.remove('active'));
          state.activeChip = val;
          chip.classList.add('active');
        }
        renderCards();
      });
    });

    // Resets
    els.btnResetFilters.addEventListener('click', resetAllFilters);
    els.btnResetNoResults.addEventListener('click', resetAllFilters);

    // View layout
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

    // Modals
    els.modalCloseBtn.addEventListener('click', closeDetailModal);
    els.detailModal.addEventListener('click', (e) => {
      if (e.target === els.detailModal) closeDetailModal();
    });
    els.modalBookmarkBtn.addEventListener('click', () => {
      if (activeModalItem) toggleBookmark(activeModalItem.id);
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
      if (confirm('Clear all saved scholarships?')) {
        state.bookmarks = [];
        localStorage.setItem('vidyasetu_bookmarks', '[]');
        updateBookmarkBadge();
        renderCards();
        openBookmarksModal();
      }
    });

    // Escape Key
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

  // Global methods for inline handlers
  window.VidyaSetu = {
    openDetailModal,
    closeDetailModal,
    toggleBookmark,
    toggleCompare,
    openBookmarksModal,
    closeBookmarksModal
  };

  // Run on ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
