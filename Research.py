import streamlit as st

def render_Research():
    # Compact CSS targeted specifically for research cards and videos
    st.markdown("""
        <style>
            /* Reduce line spacing and margin inside expander content */
            div[data-testid="stExpander"] div[role="region"] p {
                margin-bottom: 0.3rem !important;
                line-height: 1.35 !important;
                font-size: 0.88rem !important;
            }
            div[data-testid="stExpander"] div[role="region"] ul {
                padding-left: 1.1rem !important;
                margin-top: 0.2rem !important;
                margin-bottom: 0.4rem !important;
            }
            div[data-testid="stExpander"] div[role="region"] li {
                margin-bottom: 0.25rem !important;
                line-height: 1.3 !important;
                font-size: 0.85rem !important;
            }
            /* Limit maximum width of YouTube videos to keep them compact */
            div[data-testid="stExpander"] iframe {
                max-height: 160px !important;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header("💼 Research & Engineering Projects")
    st.write("**Overview of key research projects spanning biomedical engineering, scientific machine learning, multiphase flows, and renewable energy.**")

    # Project Data
    projects = [
        {
            "title": "🫀 CFD Simulation of AAA",
            "subtitle": "Patient Specific Insights",
            "bullets": [
                "**Objective:** Investigate AAA hemodynamics.",
                "**Impact:** Clinical insights via flow analysis & visualization.",
                "**Methods:** Patient-specific CFD simulations."
            ],
            "video": "https://www.youtube.com/watch?v=Kf8XltJbZOM&t=9s"
        },
        {
            "title": "🩺 Microcatheter Design",
            "subtitle": "Dual-Lumen Microcatheter (Patent)",
            "bullets": [
                "**Objective:** Targeted embolization catheter minimizing reflux.",
                "**Impact:** Delivery efficiency up **10–20%** vs SEHC.",
                "**Methods:** Multiphase CFD and DEM principles."
            ],
            "video": "https://www.youtube.com/watch?v=8DsSZnUeTzI"
        },
        {
            "title": "🫀 Splenic Artery Embolization",
            "subtitle": "Patient-Specific SAE",
            "bullets": [
                "**Objective:** Hemodynamic effects during proximal/distal SAE.",
                "**Impact:** Guide coil placement while saving blood supply.",
                "**Methods:** Patient specific CFD and particle tracking."
            ],
            "video": "https://www.youtube.com/watch?v=G5tYQsT5WHo&t=1s"
        },
        {
            "title": "🧠 Adam-SINDy Framework",
            "subtitle": "Data-Driven Optimization",
            "bullets": [
                "**Objective:** Discover equations & find unknown params.",
                "**Impact:** Extends SINDy with automated parameter tuning.",
                "**Methods:** ADAM differentiable optimization."
            ],
            "video": "https://www.youtube.com/watch?v=4vTV2xLCOGQ"
        },
        {
            "title": "🌋 Geothermal Particle Flow",
            "subtitle": "CFD-DEM & Machine Learning",
            "bullets": [
                "**Objective:** Microcapsule transport in geothermal fractures.",
                "**Impact:** Interpretable ML predicting fracture sealing.",
                "**Methods:** OpenFOAM + LIGGGHTS & Tree based classification."
            ],
            "video": "https://www.youtube.com/watch?v=NdHD69IpL2c"
        },
        {
            "title": "🚜 Combine Cleaning ROM",
            "subtitle": "Surrogate Model (CNH Industrial)",
            "bullets": [
                "**Objective:** Data-Driven surrogate model for cleaning system.",
                "**Impact:** Fast prediction app for mass flow analysis.",
                "**Methods:** POD dimensionality reduction & GPR."
            ],
            "video": "https://www.youtube.com/watch?v=AAVcsnTX_Ec"
        },
        {
            "title": "👁️ Facial Keypoint Detection",
            "subtitle": "Deep Learning / CNNs",
            "bullets": [
                "**Objective:** Facial landmark estimation.",
                "**Impact:** Real-time feature extraction.",
                "**Methods:** Convolutional Neural Networks in TensorFlow."
            ],
            "video": "https://www.youtube.com/watch?v=eyu26V3eu4o&list=PLpAOa3a0LXExGaZd-R2IvwLSz6I6Eanw7"
        },
        {
            "title": "🔴 Particle Bifurcation Flow",
            "subtitle": "Four-Way CFD-DEM",
            "bullets": [
                "**Objective:** Four-Way coupled CFD-DEM.",
                "**Impact:** Optimize targeted particle delivery.",
                "**Methods:** OpenFOAM coupled with LIGGGHTS."
            ],
            "video": "https://www.youtube.com/watch?v=p9OgJCp4FUQ"
        },
        {
            "title": "⚡ Corona Discharge",
            "subtitle": "OpenFOAM FVM Solver",
            "bullets": [
                "**Objective:** Corona discharge & fluid cavitation.",
                "**Impact:** Calculated generated electric pulse.",
                "**Methods:** Custom FVM implementation in OpenFOAM."
            ],
            "video": None
        }
    ]

    # Render 3-column grid
    for i in range(0, len(projects), 3):
        cols = st.columns(3, gap="small")
        for j in range(3):
            if i + j < len(projects):
                proj = projects[i + j]
                with cols[j]:
                    with st.expander(proj["title"], expanded=True):
                        st.markdown(f"**{proj['subtitle']}**")
                        for bullet in proj["bullets"]:
                            st.markdown(f"* {bullet}")
                        if proj["video"]:
                            st.video(proj["video"])