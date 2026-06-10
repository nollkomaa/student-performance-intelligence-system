import streamlit as st
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="Explainable AI", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 04 &nbsp;·&nbsp; Model Interpretability</p>
    <h1 class="page-title">Explainable AI — SHAP Analysis</h1>
    <p class="page-subtitle">
        SHapley Additive exPlanations (SHAP) deconstructs each XGBoost prediction into per-feature contributions,
        enabling transparent, auditable decision-making.
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Row ──────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("XAI Method",       "SHAP",         "Game-theoretic attribution", "0s"),
    ("Base Model",       "XGBoost",      "Explained model",            "0.1s"),
    ("Top Feature",      "Hours Studied","Highest SHAP impact",        "0.2s"),
    ("Features Ranked",  "20",           "All variables attributed",   "0.3s"),
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

# ── SHAP Importance Table ────────────────────────────────────────
shap_data = [
    ("Hours_Studied",       1.7580, 1),
    ("Attendance",          1.7365, 2),
    ("Previous_Scores",     0.7052, 3),
    ("Parental_Involvement",0.6285, 4),
    ("Family_Income",       0.4275, 5),
    ("Tutoring_Sessions",   0.4052, 6),
    ("Access_to_Resources", 0.3855, 7),
    ("Motivation_Level",    0.3614, 8),
    ("Distance_from_Home",  0.3405, 9),
    ("Peer_Influence",      0.3157, 10),
]

shap_df = pd.DataFrame(shap_data, columns=["Feature", "Mean |SHAP Value|", "Rank"])

col_tbl, col_chart = st.columns([2, 3])

with col_tbl:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">SHAP Feature Rankings</div>', unsafe_allow_html=True)

    max_val = shap_df["Mean |SHAP Value|"].max()
    for _, row in shap_df.iterrows():
        bar_w = f"{(row['Mean |SHAP Value|'] / max_val) * 100:.1f}%"
        color = "#388BFD" if row["Rank"] <= 2 else ("#7C3AED" if row["Rank"] <= 5 else "#4B5563")
        st.markdown(f"""
        <div style="margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                <span style="font-size:12px;color:#E2E8F0;font-weight:500;">{row['Feature']}</span>
                <span style="font-size:12px;color:{color};font-family:'JetBrains Mono',monospace;font-weight:600;">
                    {row['Mean |SHAP Value|']:.4f}
                </span>
            </div>
            <div class="conf-bar-wrap">
                <div class="conf-bar" style="width:{bar_w};background:{color};opacity:.8;"></div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col_chart:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">SHAP Feature Importance Bar Plot</div>', unsafe_allow_html=True)
    st.image("app/assets/images/shap_bar_plot.png",    width=550)
    st.markdown("""
    <div class="insight-box" style="margin-top:12px;">
        <strong>Consistent Signal</strong>
        Hours Studied (1.758) and Attendance (1.737) are nearly tied as the most impactful features,
        with a substantial drop to Previous Scores (0.705) in third place — indicating a two-factor
        dominance in predicting performance class.
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Summary Plot ─────────────────────────────────────────────────
col_sp, col_sp_txt = st.columns([3, 2])

with col_sp:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">SHAP Summary Plot — Global Attribution</div>', unsafe_allow_html=True)
    st.image("app/assets/images/shap_summary_plot.png",    width=550)
    st.markdown('</div>', unsafe_allow_html=True)

with col_sp_txt:
    st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">How to Interpret</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:13px;color:#CBD5E1;line-height:1.8;">
        Each dot represents one student-feature SHAP value.
        Position on the X-axis indicates the direction and magnitude of influence on the prediction.
        Color encodes the raw feature value — red is high, blue is low.
    </div>

    <div style="margin-top:18px;display:flex;flex-direction:column;gap:10px;">
        <div class="insight-highlight">
            <strong>Positive SHAP (right side)</strong>
            High feature values that push predictions toward High performance.
            Example: many study hours pulling the prediction upward.
        </div>
        <div class="insight-box">
            <strong>Negative SHAP (left side)</strong>
            Low feature values that push predictions toward Low performance.
            Example: poor attendance dragging the prediction downward.
        </div>
        <div class="insight-box insight-warn">
            <strong>Vertical spread</strong>
            Wide vertical spread indicates high variance in impact — the feature affects
            students very differently depending on their other characteristics.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Waterfall Plot ───────────────────────────────────────────────
col_wf, col_wf_txt = st.columns([3, 2])

with col_wf:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">SHAP Waterfall Plot — Individual Prediction</div>', unsafe_allow_html=True)
    st.image("app/assets/images/shap_waterfall_plot.png",    width=550)
    st.markdown('</div>', unsafe_allow_html=True)

with col_wf_txt:
    st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Local Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:13px;color:#CBD5E1;line-height:1.8;">
        The waterfall plot explains <em>a single student's prediction</em>. Starting from the
        base rate (average model output), each bar shows how one feature either increases
        or decreases the final predicted probability.
    </div>

    <div class="insight-highlight" style="margin-top:16px;">
        <strong>From Global to Local</strong>
        While the summary plot shows population-level patterns, the waterfall plot answers
        "why did this specific student receive a High/Medium/Low prediction?" — making the
        model auditable at the individual level.
    </div>

    <div class="insight-box" style="margin-top:12px;">
        <strong>Stakeholder Value</strong>
        Educators can use per-student waterfall explanations to identify which specific
        factors are working against a student and design targeted interventions.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Synthesis ────────────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Synthesis — What SHAP Tells Educators</div>', unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

findings = [
    ("Behavioral Factors Dominate", "#388BFD",
     "Study time and attendance — factors directly controllable by students and schools — "
     "contribute more than twice the SHAP weight of any demographic or socioeconomic variable."),
    ("Environment Matters", "#10B981",
     "Parental involvement, family income, and access to resources collectively contribute "
     "as much as Previous Scores, confirming that academic history alone is not destiny."),
    ("Model is Trustworthy", "#7C3AED",
     "SHAP values are consistent with domain knowledge and prior educational research, "
     "increasing confidence that XGBoost has learned genuine signal rather than dataset artifacts."),
]

for col, (title, color, body) in zip([s1, s2, s3], findings):
    with col:
        st.markdown(f"""
        <div class="cluster-card" style="border-top:3px solid {color};border-left:none;">
            <div style="font-size:13px;font-weight:600;color:{color};margin-bottom:10px;">{title}</div>
            <div style="font-size:13px;color:#CBD5E1;line-height:1.7;">{body}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)