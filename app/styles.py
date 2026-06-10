GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background-color: #080C14 !important;
    color: #E2E8F0;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: #0D1117 !important;
    border-right: 1px solid #1A2235 !important;
}

[data-testid="stSidebar"] * {
    color: #CBD5E1 !important;
}

[data-testid="stSidebarNavLink"][aria-current="page"] {
    background: rgba(56, 139, 253, 0.1) !important;
    border-left: 2px solid #388BFD !important;
}

[data-testid="stSidebar"] {
    background: #0D1117 !important;
    border-right: 1px solid #1A2235 !important;
    min-width: 280px !important;
    max-width: 280px !important;
}

.main .block-container {
    padding: 2.5rem 3rem 4rem 3rem;
    max-width: 1400px;
}

/* ── Page Header ── */
.page-header {
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #1A2235;
    animation: fadeSlideDown 0.5s ease both;
}

.page-eyebrow {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #388BFD;
    margin-bottom: 0.5rem;
}

.page-title {
    font-size: 28px;
    font-weight: 700;
    color: #F1F5F9;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.02em;
}

.page-subtitle {
    font-size: 14px;
    color: #CBD5E1;
    margin: 0;
    line-height: 1.6;
}

/* ── KPI Cards ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 2rem;
    animation: fadeSlideUp 0.5s ease 0.1s both;
}

.kpi-card {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 12px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    cursor: default;
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #388BFD, #7C3AED);
    opacity: 0;
    transition: opacity 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    border-color: #388BFD;
    box-shadow: 0 12px 32px rgba(56, 139, 253, 0.15);
}

.kpi-card:hover::before { opacity: 1; }

.kpi-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #CBD5E1;
    margin-bottom: 10px;
}

.kpi-value {
    font-size: 30px;
    font-weight: 700;
    color: #F1F5F9;
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 4px;
}

.kpi-sub {
    font-size: 12px;
    color: #388BFD;
    font-weight: 500;
}

.kpi-card-sm {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 12px;
    padding: 18px 20px;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}

.kpi-card-sm:hover {
    transform: translateY(-3px);
    border-color: #7C3AED;
    box-shadow: 0 8px 24px rgba(124, 58, 237, 0.12);
}

.kpi-card-sm .kpi-label { margin-bottom: 6px; }
.kpi-card-sm .kpi-value { font-size: 22px; }

/* ── Section Cards ── */
.section-card {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 14px;
    padding: 0;
    margin-bottom: 0.5rem;
}
    animation: fadeSlideUp 0.4s ease both;
    transition: border-color 0.25s ease;
}

.section-card:hover { border-color: #1E293B; }

.section-title {
    font-size: 14px;
    font-weight: 600;
    color: #F1F5F9;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1A2235;
}

/* ── Insight Box ── */
.insight-box {
    background: #0A0F1A;
    border: 1px solid #1A2235;
    border-left: 3px solid #388BFD;
    border-radius: 0 10px 10px 0;
    padding: 16px 18px;
    margin-top: 12px;
    font-size: 13px;
    color: #94A3B8;
    line-height: 1.7;
}

.insight-box strong {
    color: #E2E8F0;
    display: block;
    margin-bottom: 6px;
    font-size: 13px;
}

.insight-highlight {
    background: #0A0F1A;
    border: 1px solid #1A2235;
    border-left: 3px solid #10B981;
    border-radius: 0 10px 10px 0;
    padding: 16px 18px;
    margin-top: 12px;
    font-size: 13px;
    color: #E2E8F0;
    line-height: 1.7;
}

.insight-warn {
    border-left-color: #F59E0B;
}

/* ── Table styling ── */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* ── Badge ── */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.05em;
}

.badge-blue { background: rgba(56,139,253,0.15); color: #388BFD; }
.badge-green { background: rgba(16,185,129,0.15); color: #10B981; }
.badge-purple { background: rgba(124,58,237,0.15); color: #A78BFA; }
.badge-amber { background: rgba(245,158,11,0.15); color: #FBBF24; }

/* ── Metric row ── */
.metric-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
}

.metric-pill {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 8px;
    padding: 12px 18px;
    flex: 1;
    min-width: 120px;
    transition: transform 0.2s, border-color 0.2s;
}

.metric-pill:hover {
    transform: translateY(-2px);
    border-color: #388BFD;
}

.metric-pill .mp-label {
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4B5563;
    margin-bottom: 4px;
}

.metric-pill .mp-value {
    font-size: 18px;
    font-weight: 700;
    color: #F1F5F9;
}

/* ── Cluster card ── */
.cluster-card {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 12px;
    padding: 18px;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
}

.cluster-card:hover {
    transform: translateY(-4px);
    border-color: #7C3AED;
    box-shadow: 0 10px 28px rgba(124,58,237,0.12);
}

/* ── Prediction result card ── */
.pred-result {
    background: linear-gradient(135deg, #0D1117 0%, #0A1628 100%);
    border: 1px solid #388BFD;
    border-radius: 16px;
    padding: 28px;
    text-align: center;
    animation: pulseGlow 2s ease-in-out infinite;
}

@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 20px rgba(56,139,253,0.1); }
    50% { box-shadow: 0 0 40px rgba(56,139,253,0.25); }
}

.pred-category {
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 8px 0;
}

.pred-category.high { color: #10B981; }
.pred-category.medium { color: #FBBF24; }
.pred-category.low { color: #EF4444; }

.pred-label {
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4B5563;
}

/* ── Confidence bar ── */
.conf-bar-wrap {
    background: #111827;
    border-radius: 6px;
    height: 8px;
    overflow: hidden;
    margin-top: 8px;
}

.conf-bar {
    height: 100%;
    border-radius: 6px;
    background: linear-gradient(90deg, #388BFD, #7C3AED);
    transition: width 1s ease;
}

/* ── Recommendation card ── */
.rec-card {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    transition: transform 0.2s, border-color 0.2s;
    font-size: 13.5px;
    color: #CBD5E1;
    line-height: 1.6;
}

.rec-card:hover {
    transform: translateX(4px);
    border-color: #10B981;
}

.rec-icon {
    font-size: 16px;
    margin-top: 1px;
    flex-shrink: 0;
}

/* ── About timeline ── */
.tech-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.tech-item {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 13px;
    color: #CBD5E1;
    font-weight: 500;
    transition: transform 0.2s, border-color 0.2s, color 0.2s;
}

.tech-item:hover {
    transform: translateY(-3px);
    border-color: #388BFD;
    color: #E2E8F0;
}

.dashboard-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:20px;
}
.insight-card{
    background:#0A0F1A;
    border:1px solid #1A2235;
    border-radius:12px;
    padding:20px;
    height:100%;
    transition:all .25s ease;
}

.insight-card:hover{
    border-color:#388BFD;
}
img{
    border-radius:12px;
}
.section-card img{
    transition:all .3s ease;
}

.section-card img:hover{
    transform:scale(1.01);
}
.hero-card{
    background:linear-gradient(
        135deg,
        #0D1117,
        #0F172A
    );
    border:1px solid #1A2235;
    border-radius:16px;
    padding:28px;
}
.chart-card{
    background:#0D1117;
    border:1px solid #1A2235;
    border-radius:14px;
    padding:20px;
    transition:all .25s ease;
}

.chart-card:hover{
    border-color:#388BFD;
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #1A2235;
    margin: 0.5rem 0;
}
/* ── Animations ── */
@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* ── Staggered animation delays ── */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }

/* ── Streamlit overrides ── */
[data-testid="metric-container"] {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 12px;
    padding: 16px;
}

[data-testid="stMetricValue"] {
    color: #F1F5F9 !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #4B5563 !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}

button[kind="primary"], [data-testid="stButton"] > button {
    background: linear-gradient(135deg, #388BFD, #7C3AED) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.4rem !important;
    transition: opacity 0.2s, transform 0.2s !important;
    letter-spacing: 0.02em !important;
}

button[kind="primary"]:hover, [data-testid="stButton"] > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

[data-testid="stSelectbox"] > div, [data-testid="stSlider"] {
    color: #E2E8F0;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #388BFD !important;
}

/* ── Tab overrides ── */
[data-baseweb="tab"] {
    color: #94A3B8 !important;
}

.section-card:empty{
    display:none;
}

[aria-selected="true"] {
    color: #388BFD !important;
}
</style>
"""
