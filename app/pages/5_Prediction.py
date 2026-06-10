import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="Performance Predictor", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

st.markdown("""
<style>
.form-section {
    background: #0D1117;
    border: 1px solid #1A2235;
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 1.5rem;
    transition: border-color 0.25s;
}
.form-section:hover { border-color: #1E293B; }
.form-label-group {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #388BFD;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.form-label-group::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1A2235;
}
.result-wrap {
    animation: fadeSlideUp 0.5s ease both;
}
.prob-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 05 &nbsp;·&nbsp; Predictive Inference</p>
    <h1 class="page-title">Student Performance Predictor</h1>
    <p class="page-subtitle">
        Enter a student's academic profile and the XGBoost model will classify predicted performance
        as Low, Medium, or High with confidence scores and tailored recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load model ───────────────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    model    = joblib.load("model/xgboost_model.pkl")
    metadata = joblib.load("model/metadata.pkl")
    return model, metadata

model, metadata = load_artifacts()

# ── Layout ───────────────────────────────────────────────────────
form_col, result_col = st.columns([3, 2])

with form_col:

    # Academic Behavior ──────────────────────────────────────────
    st.markdown('<div class="form-label-group">Academic Behavior</div>', unsafe_allow_html=True)

    a1, a2 = st.columns(2)
    with a1:
        hours_studied   = st.slider("Hours Studied per Week", 1, 44, 20)
        attendance      = st.slider("Attendance (%)", 50, 100, 80)
        previous_scores = st.slider("Previous Scores", 40, 100, 70)
    with a2:
        tutoring_sessions  = st.slider("Tutoring Sessions (monthly)", 0, 8, 2)
        physical_activity  = st.slider("Physical Activity (hrs/week)", 0, 6, 3)
        sleep_hours        = st.slider("Sleep Hours per Night", 4, 10, 7)

    st.markdown('</div>', unsafe_allow_html=True)

    # Personal Profile ───────────────────────────────────────────
    st.markdown('<div class="form-label-group">Personal Profile</div>', unsafe_allow_html=True)

    p1, p2 = st.columns(2)
    with p1:
        motivation_level            = st.selectbox("Motivation Level",           ["High", "Medium", "Low"])
        extracurricular_activities  = st.selectbox("Extracurricular Activities", ["Yes", "No"])
        internet_access             = st.selectbox("Internet Access",            ["Yes", "No"])
    with p2:
        gender               = st.selectbox("Gender",               ["Male", "Female"])
        learning_disabilities= st.selectbox("Learning Disabilities",["No", "Yes"])
        peer_influence       = st.selectbox("Peer Influence",       ["Positive", "Neutral", "Negative"])

    st.markdown('</div>', unsafe_allow_html=True)

    # Family & Environment ───────────────────────────────────────
    st.markdown('<div class="form-label-group">Family and Environment</div>', unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        parental_involvement = st.selectbox("Parental Involvement",      ["High", "Medium", "Low"])
        family_income        = st.selectbox("Family Income Level",        ["High", "Medium", "Low"])
        parental_education   = st.selectbox("Parental Education",         ["Postgraduate", "College", "High School"])
    with f2:
        access_to_resources  = st.selectbox("Access to Resources",        ["High", "Medium", "Low"])
        teacher_quality      = st.selectbox("Teacher Quality",            ["High", "Medium", "Low"])
        school_type          = st.selectbox("School Type",                ["Private", "Public"])

    distance_from_home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])

    st.markdown('</div>', unsafe_allow_html=True)

    # Predict Button ─────────────────────────────────────────────
    predict_btn = st.button("Run Prediction", use_container_width=True, type="primary")


# ── Sidebar Result Panel ─────────────────────────────────────────
with result_col:

    if not predict_btn:
        st.markdown("""
        <div class="section-card" style="text-align:center;padding:40px 24px;">
            <div style="font-size:40px;margin-bottom:16px;color:#1A2235;">◎</div>
            <div style="font-size:16px;font-weight:600;color:#374151;margin-bottom:8px;">
                Awaiting Input
            </div>
            <div style="font-size:13px;color:#4B5563;line-height:1.7;">
                Fill in the student profile on the left, then click
                <strong style="color:#388BFD;">Run Prediction</strong> to generate
                a performance forecast with confidence breakdown and recommendations.
            </div>
        </div>

        <div class="section-card" style="margin-top:16px;">
            <div class="section-title">Model Details</div>
            <div style="font-size:13px;color:#94A3B8;line-height:1.8;">
                The predictor uses XGBoost trained on 6,607 student records across 20 features.
                Probability outputs are derived from calibrated class probability estimates
                and reflect uncertainty across all three performance categories.
            </div>
            <div style="margin-top:14px;">
                <div class="metric-pill" style="margin-bottom:8px;">
                    <div class="mp-label">Classifier</div>
                    <div class="mp-value" style="font-size:14px;">XGBoost</div>
                </div>
                <div class="metric-pill" style="margin-bottom:8px;">
                    <div class="mp-label">Accuracy</div>
                    <div class="mp-value" style="font-size:14px;">87.59%</div>
                </div>
                <div class="metric-pill">
                    <div class="mp-label">Classes</div>
                    <div class="mp-value" style="font-size:14px;">Low / Medium / High</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        mapping = {
            "High": 0, "Low": 1, "Medium": 2,
            "No": 0,  "Yes": 1,
            "Private": 0, "Public": 1,
            "Negative": 0, "Neutral": 1, "Positive": 2,
            "College": 0, "High School": 1, "Postgraduate": 2,
            "Far": 0, "Moderate": 1, "Near": 2,
            "Female": 0, "Male": 1,
        }

        input_data = pd.DataFrame([{
            "Hours_Studied":           hours_studied,
            "Attendance":              attendance,
            "Parental_Involvement":    mapping[parental_involvement],
            "Access_to_Resources":     mapping[access_to_resources],
            "Extracurricular_Activities": mapping[extracurricular_activities],
            "Sleep_Hours":             sleep_hours,
            "Previous_Scores":         previous_scores,
            "Motivation_Level":        mapping[motivation_level],
            "Internet_Access":         mapping[internet_access],
            "Tutoring_Sessions":       tutoring_sessions,
            "Family_Income":           mapping[family_income],
            "Teacher_Quality":         mapping[teacher_quality],
            "School_Type":             mapping[school_type],
            "Peer_Influence":          mapping[peer_influence],
            "Physical_Activity":       physical_activity,
            "Learning_Disabilities":   mapping[learning_disabilities],
            "Parental_Education_Level":mapping[parental_education],
            "Distance_from_Home":      mapping[distance_from_home],
            "Gender":                  mapping[gender],
        }])

        input_data  = input_data[metadata["feature_names"]]
        prediction  = int(model.predict(input_data)[0])
        probabilities = model.predict_proba(input_data)[0]
        result      = metadata["label_map"][prediction]
        confidence  = round(float(np.max(probabilities)) * 100, 2)

        cat_class = result.lower()
        cat_color = {"high": "#10B981", "medium": "#FBBF24", "low": "#EF4444"}.get(cat_class, "#388BFD")
        cat_icon  = {"high": "↑", "medium": "→", "low": "↓"}.get(cat_class, "")

        st.markdown(f"""
        <div class="result-wrap">
            <div class="pred-result">
                <div class="pred-label">Predicted Performance</div>
                <div class="pred-category {cat_class}">{cat_icon} {result}</div>
                <div style="font-size:13px;color:#4B5563;margin-top:6px;">
                    Confidence: <strong style="color:{cat_color};">{confidence}%</strong>
                </div>
                <div class="conf-bar-wrap" style="margin-top:10px;">
                    <div class="conf-bar" style="width:{confidence}%;background:{cat_color};"></div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

        # Probability breakdown ──────────────────────────────────
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Class Probabilities</div>', unsafe_allow_html=True)

        class_labels = ["Low", "Medium", "High"]
        class_colors = ["#EF4444", "#FBBF24", "#10B981"]

        for label, prob, color in zip(class_labels, probabilities, class_colors):
            pct = round(prob * 100, 1)
            st.markdown(f"""
            <div style="margin-bottom:12px;">
                <div class="prob-bar-label">
                    <span style="color:#E2E8F0;font-size:13px;font-weight:500;">{label}</span>
                    <span style="color:{color};font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:600;">{pct}%</span>
                </div>
                <div class="conf-bar-wrap">
                    <div class="conf-bar" style="width:{pct}%;background:{color};opacity:.8;"></div>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Recommendations ────────────────────────────────────────
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Recommendations</div>', unsafe_allow_html=True)

        recs = []
        if attendance < 75:
            recs.append(("Attendance is critically low. Regular classroom presence is the single highest-leverage intervention.", "#EF4444"))
        if hours_studied < 15:
            recs.append(("Weekly study hours are below the threshold associated with Medium performance. A structured study schedule would help.", "#F59E0B"))
        if previous_scores < 70:
            recs.append(("Prior academic results indicate foundational gaps. Targeted tutoring in core subjects is recommended.", "#F59E0B"))
        if motivation_level == "Low":
            recs.append(("Low motivation correlates strongly with underperformance. Goal-setting workshops and mentoring programs have shown measurable impact.", "#7C3AED"))
        if internet_access == "No":
            recs.append(("No internet access limits access to supplementary learning materials. School-provided resource access can bridge this gap.", "#388BFD"))
        if parental_involvement == "Low":
            recs.append(("Low parental involvement is a risk factor. Family engagement programs can improve student accountability.", "#388BFD"))
        if tutoring_sessions == 0 and result in ["Low", "Medium"]:
            recs.append(("No tutoring sessions recorded. Even monthly supplementary instruction correlates with improved outcomes.", "#10B981"))
        if not recs:
            recs.append(("Current indicators are strong across all monitored dimensions. Maintaining consistency is the primary recommendation.", "#10B981"))

        for text, color in recs:
            st.markdown(f"""
            <div class="rec-card" style="border-left:3px solid {color};">
                <div style="width:8px;height:8px;border-radius:50%;background:{color};flex-shrink:0;margin-top:4px;"></div>
                <div>{text}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Input Summary ──────────────────────────────────────────
        with st.expander("Input Summary", expanded=False):
            summary = {
                "Hours Studied":        hours_studied,
                "Attendance":           f"{attendance}%",
                "Previous Scores":      previous_scores,
                "Sleep Hours":          sleep_hours,
                "Tutoring Sessions":    tutoring_sessions,
                "Motivation Level":     motivation_level,
                "Internet Access":      internet_access,
                "Parental Involvement": parental_involvement,
                "Family Income":        family_income,
                "School Type":          school_type,
            }
            summary_df = pd.DataFrame(summary.items(), columns=["Factor", "Value"])
            st.dataframe(summary_df, use_container_width=True, hide_index=True)