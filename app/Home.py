import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from styles import GLOBAL_CSS

st.set_page_config(
    page_title="Student Performance Intelligence",
    page_icon="app/assets/icon/Students.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Hero Banner ──────────────────────────────────────────────────
st.markdown("""
<style>
.hero-wrap {
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 2.5rem;
    border: 1px solid #1A2235;
    animation: fadeIn 0.6s ease both;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.image("app/assets/images/home_banner.png",    use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Page Header ──────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Data Mining &nbsp;·&nbsp; Academic Intelligence</p>
    <h1 class="page-title">Student Performance Analysis &amp; Prediction System</h1>
    <p class="page-subtitle">
        End-to-end machine learning platform for classifying, clustering, and explaining academic outcomes across 6,607 student records.
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards ────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="kpi-card delay-1" style="animation: fadeSlideUp 0.5s ease both;">
        <div class="kpi-label">Dataset Size</div>
        <div class="kpi-value">6,607</div>
        <div class="kpi-sub">Student records</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="kpi-card delay-2" style="animation: fadeSlideUp 0.5s ease 0.1s both;">
        <div class="kpi-label">Input Variables</div>
        <div class="kpi-value">20</div>
        <div class="kpi-sub">Feature dimensions</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="kpi-card delay-3" style="animation: fadeSlideUp 0.5s ease 0.2s both;">
        <div class="kpi-label">Best Model</div>
        <div class="kpi-value">XGBoost</div>
        <div class="kpi-sub">Top classifier</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="kpi-card delay-4" style="animation: fadeSlideUp 0.5s ease 0.3s both;">
        <div class="kpi-label">Model Accuracy</div>
        <div class="kpi-value">87.59<span style="font-size:18px;font-weight:500">%</span></div>
        <div class="kpi-sub">Classification score</div>
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Executive Summary ────────────────────────────────────────────
st.markdown('<div class="section-card" style="animation: fadeSlideUp 0.5s ease 0.3s both;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)

col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.markdown("""
    <div style="padding:4px 0">
        <div style="font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#4B5563;margin-bottom:8px;">Classification</div>
        <div style="font-size:14px;color:#CBD5E1;line-height:1.7;">
            XGBoost outperformed all baselines, reaching 87.59% accuracy on the three-class student performance task.
            Logistic Regression and Random Forest served as competitive benchmarks.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
    <div style="padding:4px 0">
        <div style="font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#4B5563;margin-bottom:8px;">Feature Importance</div>
        <div style="font-size:14px;color:#CBD5E1;line-height:1.7;">
            Hours Studied and Attendance emerged as the dominant predictors, confirmed independently through
            both Random Forest importance scores and SHAP analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown("""
    <div style="padding:4px 0">
        <div style="font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#4B5563;margin-bottom:8px;">Clustering</div>
        <div style="font-size:14px;color:#CBD5E1;line-height:1.7;">
            K-Means segmented students into five distinct behavioral profiles, revealing patterns
            that raw performance scores alone cannot surface.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Model Performance Overview ───────────────────────────────────
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Model Performance Overview</div>', unsafe_allow_html=True)
    st.image("app/assets/images/classification_model_comparison.png",    width=550)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Best Model Metrics</div>', unsafe_allow_html=True)

    metrics = [
        ("Accuracy",  "87.59%"),
        ("Precision", "87.86%"),
        ("Recall",    "87.59%"),
        ("F1 Score",  "87.63%"),
    ]
    for label, val in metrics:
        st.markdown(f"""
        <div class="metric-pill" style="margin-bottom:10px;">
            <div class="mp-label">{label}</div>
            <div class="mp-value">{val}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <strong>Why XGBoost Wins</strong>
        XGBoost's gradient boosting mechanism handles class imbalance and non-linear
        feature interactions more effectively than both linear and tree-based baselines
        in this dataset.
    </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Confusion Matrix ─────────────────────────────────────────────

col_cm, col_cm_txt = st.columns([3, 2])

with col_cm:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">XGBoost Confusion Matrix</div>',
        unsafe_allow_html=True
    )

    st.image(
        "app/assets/images/classification_confusion_matrix_xgb.png",
        width=550
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_cm_txt:
    st.markdown(
        '<div class="section-card" style="height:100%;">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Interpretation</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="insight-highlight">
        <strong>Strong Classification Performance</strong><br>
        Most predictions fall on the diagonal, indicating correct classification
        across all performance categories.
    </div>

    <div class="insight-box">
        Misclassifications occur primarily between adjacent classes
        (Low ↔ Medium and Medium ↔ High), which is expected due to
        overlapping academic characteristics.
    </div>

    <div class="insight-box insight-warn">
        Critical errors between Low and High categories are extremely rare,
        demonstrating robust model discrimination.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Clustering Overview ──────────────────────────────────────────
col_c, col_d = st.columns([3, 2])

with col_c:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Student Clustering Overview</div>', unsafe_allow_html=True)
    st.image("app/assets/images/clustering_performance_by_cluster.png",    width=550)
    st.markdown('</div>', unsafe_allow_html=True)

with col_d:
    st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Cluster Findings</div>', unsafe_allow_html=True)

    cluster_items = [
        ("5", "Optimal clusters", "#388BFD"),
        ("2,208", "Largest segment", "#10B981"),
        ("499", "Smallest segment", "#F59E0B"),
    ]
    for val, label, color in cluster_items:
        st.markdown(f"""
        <div class="metric-pill" style="margin-bottom:10px;border-left:3px solid {color};">
            <div class="mp-label">{label}</div>
            <div class="mp-value" style="color:{color};">{val}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-highlight">
        <strong>Key Insight</strong>
        Cluster segmentation exposes student behavioral archetypes invisible to
        exam-score analysis alone — enabling more targeted academic interventions.
    </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── SHAP ─────────────────────────────────────────────────────────

col_shap, col_shap_txt = st.columns([3, 2])

with col_shap:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Top Features by SHAP Impact</div>',
        unsafe_allow_html=True
    )

    st.image(
        "app/assets/images/shap_bar_plot.png",
        width=550
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_shap_txt:
    st.markdown(
        '<div class="section-card" style="height:100%;">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Business Insight</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="insight-highlight">
        <strong>Top Predictors</strong><br>
        Attendance and Hours Studied contribute substantially more than any
        other feature.
    </div>

    <div class="insight-box">
        Academic behavior factors consistently outweigh demographic variables,
        suggesting performance can be improved through intervention and support.
    </div>

    <div class="insight-box">
        Agreement between SHAP and Random Forest feature importance increases
        confidence in the identified drivers of student success.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Navigation Guide ─────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Module Navigator</div>', unsafe_allow_html=True)

nav_cols = st.columns(5)
nav_items = [
    ("Dataset Overview",   "Explore raw data, distributions, and feature correlations.",            "#388BFD"),
    ("Classification",     "Compare model performance, confusion matrices, and feature importance.", "#7C3AED"),
    ("Clustering",         "Examine K-Means segments through elbow, silhouette, and PCA views.",    "#10B981"),
    ("Explainable AI",     "Interpret model decisions at global and individual prediction levels.",  "#F59E0B"),
    ("Prediction",         "Enter student parameters and receive a real-time performance forecast.", "#EF4444"),
]
for col, (title, desc, color) in zip(nav_cols, nav_items):
    with col:
        st.markdown(f"""
        <div class="cluster-card" style="border-left:3px solid {color};">
            <div style="font-size:13px;font-weight:600;color:{color};margin-bottom:8px;">{title}</div>
            <div style="font-size:12px;color:#94A3B8;line-height:1.6;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)