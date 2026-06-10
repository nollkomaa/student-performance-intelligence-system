import streamlit as st
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="About", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 06 &nbsp;·&nbsp; Project Documentation</p>
    <h1 class="page-title">About This Project</h1>
    <p class="page-subtitle">
        Academic background, technical methodology, dataset provenance, and tool stack
        for the Student Performance Analysis and Prediction System.
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Row ──────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("Student Records", "6,607",   "Dataset size",    "0s"),
    ("Input Features",  "20",      "Variables",       "0.1s"),
    ("Best Accuracy",   "87.59%",  "XGBoost",         "0.2s"),
    ("Modules Built",   "5",       "Analysis modules","0.3s"),
]
for col, (label, val, sub, delay) in zip([c1, c2, c3, c4], kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card" style="animation: fadeSlideUp 0.5s ease {delay} both;">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{val}</div>
            <div class="kpi-sub">{sub}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Project Overview ─────────────────────────────────────────────
col_ov, col_ds = st.columns(2)

with col_ov:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;">
        This system was developed as a final project for a Data Mining course, with the goal of
        building a credible, end-to-end analytical platform that goes beyond academic report formatting.
    </div>
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;margin-top:14px;">
        The project integrates classification, unsupervised clustering, explainability analysis,
        and interactive prediction into a single cohesive dashboard — designed to the standard
        of a professional analytics product, not a student submission.
    </div>

    <div style="margin-top:20px;">
        <div style="font-size:11px;text-transform:uppercase;letter-spacing:.09em;color:#4B5563;margin-bottom:10px;">
            Project Scope
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
            <div style="font-size:13px;color:#E2E8F0;padding:10px 14px;background:#0A0F1A;border:1px solid #1A2235;border-left:3px solid #388BFD;border-radius:0 8px 8px 0;">
                Supervised classification with three competing models
            </div>
            <div style="font-size:13px;color:#E2E8F0;padding:10px 14px;background:#0A0F1A;border:1px solid #1A2235;border-left:3px solid #7C3AED;border-radius:0 8px 8px 0;">
                Unsupervised K-Means segmentation into behavioral profiles
            </div>
            <div style="font-size:13px;color:#E2E8F0;padding:10px 14px;background:#0A0F1A;border:1px solid #1A2235;border-left:3px solid #10B981;border-radius:0 8px 8px 0;">
                SHAP-based global and local model interpretability
            </div>
            <div style="font-size:13px;color:#E2E8F0;padding:10px 14px;background:#0A0F1A;border:1px solid #1A2235;border-left:3px solid #F59E0B;border-radius:0 8px 8px 0;">
                Interactive prediction interface with tailored recommendations
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_ds:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Dataset</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;">
        The <strong style="color:#E2E8F0;">Student Performance Factors</strong> dataset contains
        academic, personal, and environmental variables collected across 6,607 students.
        The target variable is a three-class performance category derived from examination scores.
    </div>

    <div style="margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div class="metric-pill">
            <div class="mp-label">Total Records</div>
            <div class="mp-value" style="font-size:16px;">6,607</div>
        </div>
        <div class="metric-pill">
            <div class="mp-label">Input Features</div>
            <div class="mp-value" style="font-size:16px;">20</div>
        </div>
        <div class="metric-pill">
            <div class="mp-label">Target Classes</div>
            <div class="mp-value" style="font-size:16px;">3</div>
        </div>
        <div class="metric-pill">
            <div class="mp-label">Missing Values</div>
            <div class="mp-value" style="font-size:16px;">0</div>
        </div>
    </div>

    <div class="insight-box" style="margin-top:16px;">
        <strong>Feature Coverage</strong>
        Features span four domains: academic behavior (study time, attendance),
        personal profile (motivation, gender, peer influence), family and environment
        (income, parental education, school type), and academic history (prior scores).
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Methods ──────────────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Methodology</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
methods = [
    ("Classification", "#388BFD",
     "Logistic Regression, Random Forest, and XGBoost trained on an 80/20 train-test split. "
     "Evaluation via Accuracy, Precision, Recall, and macro F1."),
    ("Clustering", "#7C3AED",
     "K-Means with K selected via elbow method and validated through silhouette analysis. "
     "PCA used to project clusters into two dimensions for visual inspection."),
    ("Explainability", "#10B981",
     "SHAP TreeExplainer applied to the XGBoost model to generate global summary plots, "
     "feature importance rankings, and per-instance waterfall explanations."),
    ("Prediction", "#F59E0B",
     "The best-performing XGBoost model is deployed as a real-time inference engine, "
     "returning class label, probability vector, confidence score, and actionable recommendations."),
]
for col, (title, color, desc) in zip([m1, m2, m3, m4], methods):
    with col:
        st.markdown(f"""
        <div class="cluster-card" style="border-top:3px solid {color};border-left:none;height:100%;">
            <div style="font-size:13px;font-weight:600;color:{color};margin-bottom:10px;">{title}</div>
            <div style="font-size:12.5px;color:#94A3B8;line-height:1.75;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Results ──────────────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Results Summary</div>', unsafe_allow_html=True)

r1, r2 = st.columns([2, 3])

with r1:
    result_items = [
        ("XGBoost Accuracy",  "87.59%", "#388BFD"),
        ("XGBoost F1 Score",  "87.63%", "#388BFD"),
        ("RF Accuracy",       "80.56%", "#4B5563"),
        ("LR Accuracy",       "80.11%", "#4B5563"),
        ("Optimal Clusters",  "K = 5",  "#7C3AED"),
        ("Top Predictor",     "Hours Studied", "#10B981"),
    ]
    for label, val, color in result_items:
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
                    padding:10px 0;border-bottom:1px solid #1A2235;">
            <span style="font-size:13px;color:#CBD5E1;">{label}</span>
            <span style="font-size:14px;font-weight:600;color:{color};">{val}</span>
        </div>""", unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;padding:8px 0;">
        XGBoost demonstrated a clear and consistent performance advantage over both baseline models,
        improving accuracy by approximately seven to eight percentage points. The gap was uniform
        across all four evaluation metrics, indicating a genuine modeling advantage rather than
        a result of metric selection.
    </div>
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;margin-top:12px;">
        Clustering analysis revealed five behavioral archetypes among students — segments that
        exhibit meaningfully different combinations of study habits, family context, and institutional
        support. These profiles are actionable for educational administrators designing targeted
        intervention programs.
    </div>
    <div style="font-size:14px;color:#CBD5E1;line-height:1.85;margin-top:12px;">
        SHAP analysis confirmed that behavioral factors (study time, attendance) contribute more
        than twice the predictive weight of any demographic variable — a finding consistent with
        established educational research literature.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Tech Stack ───────────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)

tech_cats = {
    "Data Processing": ["Python 3.x", "Pandas", "NumPy"],
    "Machine Learning": ["Scikit-Learn", "XGBoost", "SHAP"],
    "Visualization": ["Matplotlib", "Seaborn", "Plotly"],
    "Application Layer": ["Streamlit", "Joblib"],
}
for cat, tools in tech_cats.items():
    st.markdown(f"""
    <div style="margin-bottom:16px;">
        <div style="font-size:11px;text-transform:uppercase;letter-spacing:.09em;color:#4B5563;margin-bottom:8px;">{cat}</div>
        <div class="tech-grid">
            {"".join(f'<div class="tech-item">{t}</div>' for t in tools)}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)