import streamlit as st
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="Dataset Overview", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 01 &nbsp;·&nbsp; Data Foundation</p>
    <h1 class="page-title">Dataset Overview</h1>
    <p class="page-subtitle">
        Structural exploration of the Student Performance Factors dataset — records, schema, distributions, and inter-feature relationships.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load data ────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("dataset/StudentPerformanceFactors.csv")

df = load_data()

# ── KPI Row ──────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("Total Records",    f"{df.shape[0]:,}", "Student entries"),
    ("Total Features",   str(df.shape[1]),   "Input variables"),
    ("Missing Values",   str(int(df.isnull().sum().sum())), "Across all columns"),
    ("Numeric Features", str(df.select_dtypes(include="number").shape[1]), "Continuous variables"),
]
delays = ["0s", "0.1s", "0.2s", "0.3s"]
for col, (label, val, sub), delay in zip([c1, c2, c3, c4], kpis, delays):
    with col:
        st.markdown(f"""
        <div class="kpi-card" style="animation: fadeSlideUp 0.5s ease {delay} both;">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{val}</div>
            <div class="kpi-sub">{sub}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Dataset Preview ──────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Dataset Preview</div>', unsafe_allow_html=True)
st.markdown("""
<p style="font-size:13px;color:#94A3B8;margin-bottom:14px;">
    First 10 records. The dataset covers academic habits, personal background, and environmental conditions for each student.
</p>""", unsafe_allow_html=True)
st.dataframe(df.head(10),    width=550, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Feature Schema ───────────────────────────────────────────────
col_l, col_r = st.columns([3, 2])

with col_l:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Feature Schema</div>', unsafe_allow_html=True)

    feature_info = pd.DataFrame({
        "Feature":        df.columns.tolist(),
        "Data Type":      df.dtypes.astype(str).tolist(),
        "Missing Values": df.isnull().sum().values,
        "Unique Values":  [df[c].nunique() for c in df.columns],
    })
    st.dataframe(feature_info,    width=550, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_r:
    st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Feature Categories</div>', unsafe_allow_html=True)

    categories = {
        "Academic Behavior": ["Hours_Studied", "Attendance", "Tutoring_Sessions", "Physical_Activity"],
        "Personal Profile":  ["Motivation_Level", "Extracurricular_Activities", "Gender", "Learning_Disabilities", "Peer_Influence", "Sleep_Hours"],
        "Family & Environment": ["Parental_Involvement", "Family_Income", "Parental_Education_Level", "Internet_Access", "Access_to_Resources", "Distance_from_Home", "School_Type", "Teacher_Quality"],
        "Historical Record": ["Previous_Scores"],
        "Target Variable":   ["Exam_Score"],
    }
    color_map = {
        "Academic Behavior":   "#388BFD",
        "Personal Profile":    "#7C3AED",
        "Family & Environment":"#10B981",
        "Historical Record":   "#F59E0B",
        "Target Variable":     "#EF4444",
    }
    for cat, feats in categories.items():
        color = color_map[cat]
        st.markdown(f"""
        <div style="margin-bottom:14px;">
            <div style="font-size:11px;text-transform:uppercase;letter-spacing:.09em;
                        color:{color};margin-bottom:6px;font-weight:600;">{cat}</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px;">
                {"".join(f'<span class="badge" style="background:rgba(255,255,255,0.04);color:#CBD5E1;border:1px solid #1A2235;">{f}</span>' for f in feats)}
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── EDA Charts ───────────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Exploratory Data Analysis</div>', unsafe_allow_html=True)

eda_col1, eda_col2 = st.columns([3, 2])

with eda_col1:
    st.image(
        "app/assets/images/eda_exam_score_distribution.png",
           width=550
    )

with eda_col2:
    st.markdown("""
    <div style="padding:8px 0;">
        <div style="font-size:13px;font-weight:600;color:#E2E8F0;margin-bottom:10px;">
            Exam Score Distribution
        </div>
        <div style="font-size:13px;color:#CBD5E1;line-height:1.8;">
            The distribution of exam scores reveals the spread of academic outcomes across the student population.
            A roughly bell-shaped curve centered around the mid-range suggests most students perform at a moderate level,
            with meaningful tails at both extremes indicating at-risk and high-achieving populations.
        </div>
    </div>
    <div class="insight-box" style="margin-top:16px;">
        <strong>Key Observation</strong>
        Score distribution shapes the class boundaries for Low, Medium, and High — making threshold selection
        a critical preprocessing decision.
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Correlation Heatmap ──────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Correlation Heatmap</div>', unsafe_allow_html=True)

h1, h2 = st.columns([3, 2])

with h1:
    st.image(
        "app/assets/images/eda_correlation_heatmap.png",
           width=550
    )

with h2:
    st.markdown("""
    <div style="font-size:13px;color:#CBD5E1;line-height:1.8;padding:8px 0;">
        The heatmap quantifies pairwise linear relationships between all numeric features.
        Strong correlations suggest potential multicollinearity, while weak correlations point
        to independent information sources that collectively improve model performance.
    </div>
    <div class="insight-highlight" style="margin-top:16px;">
        <strong>Actionable Insight</strong>
        Hours Studied and Attendance show the strongest positive correlation with Exam Score,
        validating their dominance in feature importance analyses.
    </div>
    <div class="insight-box insight-warn" style="margin-top:12px;">
        <strong>Watch for Collinearity</strong>
        Highly correlated predictor pairs may inflate coefficient estimates in linear models.
        Tree-based methods like XGBoost are naturally robust to this.
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Bivariate Charts ─────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Bivariate Relationships</div>', unsafe_allow_html=True)

b1, b2 = st.columns(2)

with b1:
    st.image(
        "app/assets/images/eda_hours_studied_vs_exam_score.png",
           width=550
    )
    st.markdown("""
    <div class="insight-box" style="margin-top:10px;">
        <strong>Hours Studied vs Exam Score</strong>
        A clear positive trend — students investing more study time consistently achieve higher scores.
        The relationship plateaus beyond ~35 hours, suggesting diminishing returns.
    </div>""", unsafe_allow_html=True)

with b2:
    st.image(
        "app/assets/images/eda_attendance_vs_exam_score.png",
           width=550
    )
    st.markdown("""
    <div class="insight-box" style="margin-top:10px;">
        <strong>Attendance vs Exam Score</strong>
        Higher attendance rates are strongly associated with better academic outcomes.
        Students below 75% attendance form the majority of the Low performance class.
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Descriptive Statistics ───────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Descriptive Statistics</div>', unsafe_allow_html=True)
st.markdown("""
<p style="font-size:13px;color:#94A3B8;margin-bottom:14px;">
    Summary statistics for all numeric features — count, mean, standard deviation, quartiles, and range.
</p>""", unsafe_allow_html=True)
st.dataframe(df.describe().round(2),    width=550)
st.markdown('</div>', unsafe_allow_html=True)