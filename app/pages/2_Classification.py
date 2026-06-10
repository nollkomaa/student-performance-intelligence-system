import streamlit as st
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="Classification Analysis", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 02 &nbsp;·&nbsp; Supervised Learning</p>
    <h1 class="page-title">Classification Analysis</h1>
    <p class="page-subtitle">
        Comparative evaluation of three classifiers — Logistic Regression, Random Forest, and XGBoost — on the three-class student performance task.
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Row ──────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("Best Model",  "XGBoost",  "Gradient boosting", "0s"),
    ("Accuracy",    "87.59%",   "Test set score",    "0.1s"),
    ("F1 Score",    "87.63%",   "Macro average",     "0.2s"),
    ("Models Tested","3",       "Compared",          "0.3s"),
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

# ── Model Comparison Table ───────────────────────────────────────

comparison_df = pd.DataFrame({
    "Model":     ["Logistic Regression", "Random Forest", "XGBoost"],
    "Accuracy":  ["80.11%",              "80.56%",        "87.59%"],
    "Precision": ["80.33%",              "80.85%",        "87.86%"],
    "Recall":    ["80.11%",              "80.56%",        "87.59%"],
    "F1 Score":  ["80.20%",              "80.66%",        "87.63%"],
})

col_c, col_t = st.columns([2, 2])

# ── Left Side : Why XGBoost Leads ────────────────────────────────

with col_c:

    st.markdown(
        '<div class="section-card" style="height:100%;">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Why XGBoost Leads</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="font-size:13px;color:#CBD5E1;line-height:1.8;">
        XGBoost captures complex non-linear relationships between study behavior,
        attendance patterns, and academic outcomes more effectively than traditional
        machine learning models.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    accuracy_df = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Random Forest",
            "XGBoost"
        ],
        "Accuracy": [
            80.11,
            80.56,
            87.59
        ]
    })

    st.markdown(
        '<div class="section-title">Relative Accuracy</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        accuracy_df.set_index("Model")
    )

    st.markdown("""
    <div class="insight-box" style="margin-top:14px;">
        XGBoost consistently achieves the highest predictive performance,
        outperforming both baseline models across all evaluation metrics.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ── Right Side : Leaderboard ─────────────────────────────────────

with col_t:

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Model Leaderboard</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        comparison_df,
        width=500,
        hide_index=True
    )

    st.markdown("""
    <div class="insight-box" style="margin-top:14px;">
        <strong>Performance Gap</strong><br>
        XGBoost achieves a 7–8 percentage point improvement over both baseline
        models across every evaluation metric, demonstrating a substantial gain
        in predictive reliability.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

st.markdown('<hr class="divider">', unsafe_allow_html=True)
    # ── Model Comparison Chart ───────────────────────────────────────

col_chart, col_insight = st.columns([3, 2])

with col_chart:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Visual Model Comparison</div>',
        unsafe_allow_html=True
    )

    st.image(
        "app/assets/images/classification_model_comparison.png",
        width=550
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_insight:
    st.markdown(
        '<div class="section-card" style="height:100%;">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Key Findings</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="insight-highlight">
        <strong>XGBoost Leads Across All Metrics</strong><br>
        Accuracy, Precision, Recall, and F1 Score consistently outperform
        both baseline models.
    </div>

    <div class="insight-box">
        The performance advantage exceeds 7 percentage points,
        indicating a substantial improvement in predictive capability.
    </div>

    <div class="insight-box insight-warn">
        Consistency across all metrics suggests the model improvement
        is genuine rather than driven by a single evaluation measure.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Confusion Matrix Analysis ────────────────────────────────────

st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Confusion Matrix Analysis</div>',
    unsafe_allow_html=True
)

selected_model = st.selectbox(
    "Select Model",
    [
        "XGBoost",
        "Random Forest",
        "Logistic Regression"
    ]
)

if selected_model == "XGBoost":

    img_path = "app/assets/images/classification_confusion_matrix_xgb.png"
    accuracy = "87.59%"

    notes = """
    Strong diagonal dominance indicates highly accurate classification.
    Most prediction errors occur between adjacent performance categories,
    while critical Low-to-High misclassifications are extremely rare.
    """

elif selected_model == "Random Forest":

    img_path = "app/assets/images/classification_confusion_matrix_rf.png"
    accuracy = "80.56%"

    notes = """
    The model demonstrates solid classification performance, although
    confusion within the Medium category remains more noticeable than
    in XGBoost.
    """

else:

    img_path = "app/assets/images/classification_confusion_matrix_lr.png"
    accuracy = "80.11%"

    notes = """
    Logistic Regression struggles with non-linear decision boundaries,
    resulting in more frequent errors around borderline student profiles.
    """

col_img, col_txt = st.columns([3, 2])

with col_img:

    st.image(
        img_path,
        width=500
    )
with col_txt:

    st.markdown(
        '<div class="section-card" style="height:100%;">',
        unsafe_allow_html=True
    )

    st.metric(
        label="Selected Model",
        value=selected_model
    )

    st.metric(
        label="Accuracy",
        value=accuracy
    )
    st.markdown(f"""
    <div class="insight-box">
    <strong>Model Interpretation</strong><br>
    {notes.strip()}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="insight-box" style="margin-top:12px;">
            The confusion matrix provides a detailed view of classification
            performance by comparing actual labels against predicted labels.
            Strong diagonal values indicate accurate predictions, while
            off-diagonal values represent misclassification errors.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)