import streamlit as st
import pandas as pd
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from styles import GLOBAL_CSS

st.set_page_config(page_title="Clustering Analysis", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <p class="page-eyebrow">Module 03 &nbsp;·&nbsp; Unsupervised Learning</p>
    <h1 class="page-title">Clustering Analysis</h1>
    <p class="page-subtitle">
        K-Means segmentation of 6,607 students into five behavioral profiles — revealing academic archetypes that exam scores alone cannot capture.
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Row ──────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("Algorithm",        "K-Means",  "Partitional clustering",    "0s"),
    ("Optimal K",        "5",        "Cluster count",             "0.1s"),
    ("Silhouette Score", "0.09",     "Cluster separation quality","0.2s"),
    ("Largest Segment",  "2,208",    "Students in Cluster 2",     "0.3s"),
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

# ── Elbow + Silhouette ───────────────────────────────────────────
col_e, col_s = st.columns(2)

with col_e:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Elbow Method — Optimal K Selection</div>', unsafe_allow_html=True)
    st.image("app/assets/images/clustering_elbow_method.png",    width=550)
    st.markdown("""
    <div class="insight-box" style="margin-top:12px;">
        <strong>How to Read This</strong>
        The curve plots inertia (within-cluster sum of squares) against K. The elbow at K=5
        marks the point of diminishing return — adding more clusters beyond 5 yields negligible
        compactness improvement while increasing model complexity.
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_s:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Silhouette Score — Cluster Quality</div>', unsafe_allow_html=True)
    st.image("app/assets/images/clustering_silhouette_score.png",    width=550)
    st.markdown("""
    <div class="insight-box" style="margin-top:12px;">
        <strong>Interpreting the Score</strong>
        A silhouette score of 0.09 reflects the inherent continuous nature of academic data —
        students do not belong to sharply distinct groups. The clusters are statistically valid
        but represent a spectrum rather than discrete categories.
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)
# ── Heatmap ──────────────────────────────────────────────────────
col_h, col_h_txt = st.columns([3, 2])

with col_h:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Cluster Characteristics Heatmap</div>',
        unsafe_allow_html=True
    )

    st.image(
        "app/assets/images/clustering_cluster_heatmap.png",
        width=550
    )

    st.markdown('</div>', unsafe_allow_html=True)
with col_h_txt:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Cluster Profiles</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    The heatmap shows mean feature values per cluster, normalized for comparability.
    Darker cells indicate higher relative values, allowing side-by-side profiling
    of each student segment.
    """)

    st.markdown("""
    <div class="insight-highlight">
        <strong>Distinguishing Signals</strong><br>
        Clusters separate primarily along study-time intensity and parental involvement dimensions.
        High-performing clusters show elevated hours studied paired with active family support,
        while lower-performing clusters combine irregular attendance with limited resource access.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <strong>Practical Application</strong><br>
        School administrators can use cluster membership to assign targeted support programs
        before exam-score data becomes available.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── PCA Visualization ────────────────────────────────────────────
col_p, col_p_txt = st.columns([3, 2])

with col_p:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">PCA 2D Cluster Visualization</div>',
        unsafe_allow_html=True
    )

    st.image(
        "app/assets/images/clustering_pca_visualization.png",
        width=550
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_p_txt:

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Reading the PCA Plot</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    Principal Component Analysis projects the 20-dimensional feature space
    onto two orthogonal axes that maximize explained variance.

    Each point represents one student, while colors indicate cluster membership.
    """)

    st.markdown("""
    <div class="insight-highlight">
        <strong>Geometric Insight</strong><br>
        Partially overlapping regions in PCA space confirm that cluster boundaries
        are real but soft, consistent with the relatively low silhouette score and
        the continuous nature of academic performance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box insight-warn">
        <strong>Limitation</strong><br>
        PCA compresses 20 dimensions into 2 dimensions. Some cluster structure
        and separation information is inevitably lost during this projection process.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)