import streamlit as st

def render_Research():
    st.header("💼 Research & Engineering Projects")
    st.write("**Overview of key research projects spanning biomedical engineering, scientific machine learning, multiphase flows, and renewable energy.**")

    # Project 1: Patient Specific Modeling
    with st.expander("🫀 CFD Simulation of Abdominal Aortic Aneurysm", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Patient Specific Insights")
            st.markdown("""
            * **Objective:** Investigate the effects of an abdominal aortic aneurysm (AAA) on patient-specific hemodynamics.
            * **Impact:**  Provide clinically relevant insights into the patient’s vascular condition through detailed analysis and visualization of blood-flow patterns.
            * **Methods:** Patient-specific computational fluid dynamics (CFD) simulations combined with advanced hemodynamic visualization techniques.
            """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=Kf8XltJbZOM&t=9s")

    # Project 2: Dual-Lumen Microcatheter
    with st.expander("🩺 Dual-Lumen Microcatheter Design for Targeted Embolization", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Dual-Lumen Microcatheter Design (Provisional Patent)")
            st.markdown("""
            * **Objective:** Designed a novel microcatheter for targeted embolization to minimize particle reflux.
            * **Impact:** Improved delivery efficiency by **10–20%** compared to standard End-Hole Catheters (SEHC) and commercial alternatives.
            * **Methods:** Integrated multiphysics CFD simulations and fluid-structure interaction principles.
            """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=8DsSZnUeTzI")

    # Project 3: Patient Specific Modeling SAE
    with st.expander("🫀 Patient-Specific Hemodynamics During Splenic Artery Embolization", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Patient-Specific Splenic Artery Embolization")
            st.markdown("""
            * **Objective:** To investigate how patient-specific hemodynamics influence proximal and distal splenic artery embolization (SAE) and identify factors that can improve embolization outcomes.
            * **Impact:** The study demonstrates the potential of patient-specific computational modeling to guide embolization strategies, including coil placement and particle delivery, toward more effective treatment while preserving splenic blood supply.
            * **Methods:** Patient-specific CFD simulations were combined with collateral-flow analysis, particle residence-time calculations, and Lagrangian particle tracking to evaluate proximal coil placement and the effects of particle size, release location, and timing during distal embolization.
            """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=G5tYQsT5WHo&t=1s")

    # Project 4: Adam-SINDy
    with st.expander("🧠 Adam-SINDy: Data-Driven Optimization for Dynamical Systems", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Adam-SINDy Framework")
            st.markdown("""
            * **Objective:** Develop an improved SINDy framework that can identify governing equations while simultaneously estimating unknown nonlinear parameters.
            * **Impact:** Extends SINDy to more complex dynamical systems while reducing reliance on prior knowledge of nonlinear parameters and manual hyperparameter tuning.
            * **Methods:** Introduces ADAM-SINDy, a differentiable framework using ADAM optimization to jointly optimize model coefficients, nonlinear parameters, and sparsity parameters.
            """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=4vTV2xLCOGQ")

    # Project 5: Geothermal Systems & CFD-DEM
    with st.expander("🌋 Fracture Sealing & Particle Transport in Geothermal Systems", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("CFD-DEM & Machine Learning for Geothermal Systems")
            st.markdown("""
            * **Objective:** To investigate the transport and accumulation of microcapsules in geothermal fracture networks and identify the key factors governing particle movement and sealing behavior.
            * **Impact:** The study provides an interpretable data-driven approach for predicting particle transport and identifying critical design parameters, helping improve microcapsule-based permeability control in geothermal systems.
            * **Methods:** CFD–DEM simulations were performed using OpenFOAM and LIGGGHTS to generate particle-transport data under varying conditions, followed by random forest and decision-tree models to classify blockage and determine the most influential parameters.
            """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=NdHD69IpL2c")

    # Project 6: Soil and Crop ROM Model (CNH Industrial)
    with st.expander("🚜 Data-Driven Reduced-Order Model for Combine Cleaning System (CNH Industrial)", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Surrogate Modeling via POD and GPR")
            st.markdown("""
            * Developed a data-driven reduced-order surrogate model (ROM) from CFD simulations during industrial internship at **CNH Industrial**.
            * Leveraged **Proper Orthogonal Decomposition (POD)** for spatial dimensionality reduction and **Gaussian Process Regression (GPR)** for fast predictive evaluation.
            * Build a user friendly app to use the model for fast prediction and mass flow analysis. 
        """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=AAVcsnTX_Ec")

    # Project 7: Facial Keypoint Detection
    with st.expander("👁️ Facial Keypoint Detection", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Deep Learning and Convolutional NN")
            st.markdown("""
            * Facial Keypoints Detection using convolutional neural network and machine learning technics. 
        """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=eyu26V3eu4o&list=PLpAOa3a0LXExGaZd-R2IvwLSz6I6Eanw7")

    # Project 8: Particle transport in idealized bifrucations
    with st.expander("🔴 Particle transport in successively bifurcating vessels", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Four-way coupled CFD-DEM")
            st.markdown("""
            * Developed a four-way coupled CFD–DEM framework for particle tracking in successively bifurcating vessels using an Eulerian–Lagrangian approach.
            * Coupled OpenFOAM and LIGGGHTS to capture fluid–particle and particle–particle interactions with flexible particle properties and behavior.
            * Demonstrated the potential of CFD–DEM simulations to optimize targeted particle injection and delivery in complex flow networks. 
        """)
        with col2:
            st.markdown("##### Project Video")
            # Replace URL with your YouTube video link
            st.video("https://www.youtube.com/watch?v=p9OgJCp4FUQ")

    # Project 9: OpenFOAM FVM & Corona Discharge
    with st.expander("⚡ Corona Discharge & High Electric Pulse Cavitation", expanded=True):
        st.subheader("Numerical Modeling in OpenFOAM")
        st.markdown("""
        * Modeled corona discharge dynamics using the **Finite Volume Method (FVM)** implemented in **OpenFOAM**.
        * Investigated compressible fluid cavitation behavior under high electric pulses and calculated electrical forces acting on fluid domain boundaries.
        """)