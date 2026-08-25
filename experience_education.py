import streamlit as st

def render_experience_education():
    st.header("🎓 Experience & Education")

    col_exp, col_edu = st.columns([1, 1], gap="large")

    with col_exp:
        st.subheader("💼 Professional & Research Experience")

        st.markdown("""
        #### **Soil and Crop Modeling Intern**  
        *CNH Industrial | New Holland, PA, USA*  
        🗓️ **May 2026 – Aug 2026**  
        * Developed a data-driven reduced-order surrogate model (ROM) from CFD simulations.
        * Applied Proper Orthogonal Decomposition (POD) and Gaussian Process Regression (GPR) for rapid predictions.

        ---

        #### **Graduate Research Assistant**  
        *Scientific Computing and Imaging Institute, University of Utah | Salt Lake City, UT, USA*  
        🗓️ **Aug 2023 – Present** 
        * Novel microcatheter design for embolization (*Provisional Patent*).
        * CFD-DEM four-way fluid-particle coupling in patient-specific vascular networks.
        * Patient Specific Modeling of Hemodynamics During Splenic Artery Embolization.
        * Developed data-driven and ML to generate interpretable predictive models for fracture sealing based on CFD-DEM
          simulation data in geothermal systems
        * Machine learning framework design (Adam-SINDy, GPR, PINNs) for system dynamics and fracture sealing.

        ---

        #### **Graduate Research Assistant**  
        *Harbin Institute of Technology | Harbin, China*  
        🗓️ **Aug 2018 – Jun 2020**  
        * FVM OpenFOAM solver implementations for high-voltage plasma/corona discharges.
        * High electric pulse fluid cavitation simulations.
        * Facial Keypoints Detection using CNN architectures.

        ---

        #### **R&D / Thermal Design Engineer**  
        *Hengam Company*  
        🗓️ **2016 – 2018 & 2020 – 2022**  
        * Designed and manufactured solar-powered fruit dryers using CFD thermal performance optimization.
        * Engineered and manufactured small-scale wind turbines to optimize localized power generation.
        """)

    with col_edu:
        st.subheader("🎓 Education")

        st.markdown("""
        #### **PhD in Mechanical Engineering**  
        *University of Utah, USA*  
        🗓️ **2023 – Present** 
        * **Thesis:** *Computational Modeling of Fluid-Particle Interactions: Multiphysics and Data-driven Approaches*

        ---

        #### **MS in Energy Science and Engineering**  
        *Harbin Institute of Technology, China*  
        🗓️ **2018 – 2020**  
        * **Thesis:** *Numerical modeling of corona discharge using Finite Volume Method (FVM) in OpenFOAM*
        """)

        st.markdown("---")
        
        # Enhanced Technical Skills Section
        st.subheader("🛠️ Technical Skills & Tools")

        # Custom CSS for skill badges and tool cards
        st.markdown("""
        <style>
            .skill-card {
                background-color: var(--background-color, #ffffff);
                border: 1px solid rgba(128, 128, 128, 0.2);
                border-radius: 10px;
                padding: 12px 15px;
                margin-bottom: 12px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.03);
            }
            .skill-title {
                font-weight: 700;
                font-size: 0.92rem;
                margin-bottom: 8px;
                color: var(--text-color, #1a202c);
            }
            .tool-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                background-color: rgba(128, 128, 128, 0.08);
                border: 1px solid rgba(128, 128, 128, 0.2);
                border-radius: 6px;
                padding: 4px 10px;
                margin: 3px;
                font-size: 0.82rem;
                font-weight: 500;
            }
            .tool-badge img {
                width: 16px;
                height: 16px;
                object-fit: contain;
            }
            @media (prefers-color-scheme: dark) {
                .skill-card {
                    background-color: #1e293b !important;
                    border-color: #334155 !important;
                }
            }
        </style>
        """, unsafe_allow_html=True)

        # Skill Categories Data with Icons
        skill_groups = [
            {
                "category": "🌀 CFD & Particle Methods",
                "tools": [
                    {"name": "OpenFOAM", "icon": "∇"},
                    {"name": "Ansys Fluent", "icon": "https://cdn.simpleicons.org/ansys"},
                    {"name": "SimVascular", "icon": "🫀"},
                    {"name": "STAR-CCM+", "icon": "⚙️"},
                    {"name": "LIGGGHTS", "icon": "🔴"},
                    {"name": "DPM / MPPIC", "icon": "⚛️"}
                ]
            },
            {
                "category": "🧠 Machine Learning & Data",
                "tools": [
                    {"name": "PyTorch", "icon": "https://cdn.simpleicons.org/pytorch"},
                    {"name": "TensorFlow", "icon": "https://cdn.simpleicons.org/tensorflow"},
                    {"name": "scikit-learn", "icon": "https://cdn.simpleicons.org/scikitlearn"},
                    {"name": "Streamlit", "icon": "https://cdn.simpleicons.org/streamlit"},
                    {"name": "NumPy", "icon": "https://cdn.simpleicons.org/numpy"},
                    {"name": "SciPy", "icon": "https://cdn.simpleicons.org/scipy"}
                ]
            },
            {
                "category": "💻 Languages & CAD",
                "tools": [
                    {"name": "Python", "icon": "https://cdn.simpleicons.org/python"},
                    {"name": "C++", "icon": "https://cdn.simpleicons.org/cplusplus"},
                    {"name": "MATLAB", "icon": "📐"},
                    {"name": "SolidWorks", "icon": "🛠️"},
                    {"name": "Inventor", "icon": "🔧"}
                ]
            },
            {
                "category": "📊 Visualization & HPC",
                "tools": [
                    {"name": "ParaView", "icon": "👁️"},
                    {"name": "3D Slicer", "icon": "🩺"},
                    {"name": "Linux", "icon": "https://cdn.simpleicons.org/linux"},
                    {"name": "SLURM", "icon": "🖥️"}
                ]
            }
        ]

        # Render Grouped Cards
        for group in skill_groups:
            badges_html = ""
            for t in group["tools"]:
                if t["icon"].startswith("http"):
                    icon_html = f'<img src="{t["icon"]}"/>'
                else:
                    icon_html = f'<span>{t["icon"]}</span>'
                badges_html += f'<div class="tool-badge">{icon_html} <span>{t["name"]}</span></div>'

            st.markdown(f"""
            <div class="skill-card">
                <div class="skill-title">{group['category']}</div>
                <div>{badges_html}</div>
            </div>
            """, unsafe_allow_html=True)