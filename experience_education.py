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
        st.subheader("🛠️ Technical Skills & Tools")

        st.markdown("""
        * **CFD Software:** OpenFOAM, SimVascular, Ansys-Fluent, Star-CCM+
        * **Particle Methods:** LIGGGHTS (CFDEM), FlowVC, DPM, MPPIC
        * **Fluid Physics:** Biotransport, Multiphase, Lagrangian Particle Tracking, Heat Transfer, Blood Flow Simulation
        * **Machine Learning:** PyTorch, scikit-learn, TensorFlow, CNNs, PINNs, NumPy, Pandas, SciPy, Streamlit
        * **Languages & CAD:** Python, Matlab, C++, Autodesk Inventor, SolidWorks
        * **Visualization & HPC:** ParaView, 3D Slicer, Linux, SLURM HPC clusters
        """)