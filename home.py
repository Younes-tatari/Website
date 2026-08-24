import streamlit as st

def render_home(display_image_safe):
    col_text, col_img = st.columns([8, 2], gap="large")
    
    with col_text:
        st.markdown("""
        <div class="hero-card">
            <h1 style="font-size: 52px; margin-bottom: 0px; color: white;">Younes Tatari</h1>
            <h3 style="color: #63b3ed; font-weight: 400; margin-top: 5px; margin-bottom: 20px;">PhD Researcher in Mechanical Engineering</h3>
            <p style="font-size: 25px; line-height: 1.6; color: #e2e8f0; margin-bottom: 25px;">
                Computational modeling researcher working at the intersection of fluid mechanics, 
                particle transport, multiphysics simulation, and data-driven scientific machine 
                learning. My work combines CFD, CFD–DEM, reduced-order modeling, and 
                interpretable ML to solve challenging problems in biomedical and energy systems.
            </p>
            <div>
                <span class="badge">🌀 CFD</span>
                <span class="badge">⚙️ CFD–DEM</span>
                <span class="badge">🧠 Scientific ML</span>
                <span class="badge">∇ OpenFOAM</span><br>
                <span class="badge">🔥 PyTorch</span>
                <span class="badge">🎈 Streamlit</span>
                <span class="badge">🫀 Cardiovascular CFD</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_img:
        display_image_safe("assets/profile.jpg", width=300, use_container=True)

    # Bottom 4 Feature Cards
    f1, f2, f3, f4 = st.columns(4)
    
    with f1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px; margin-bottom: 8px;">🧪</div>
            <div class="feature-title">Research Driven</div>
            <div class="feature-desc">Solving real-world problems with scientific rigor</div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px; margin-bottom: 8px;">📊</div>
            <div class="feature-title">Data & Physics</div>
            <div class="feature-desc">Bridging physics-based models with data-driven insights</div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px; margin-bottom: 8px;">⚡</div>
            <div class="feature-title">Innovation</div>
            <div class="feature-desc">Developing efficient and interpretable solutions</div>
        </div>
        """, unsafe_allow_html=True)

    with f4:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 24px; margin-bottom: 8px;">🎯</div>
            <div class="feature-title">Impact</div>
            <div class="feature-desc">Advancing science for a sustainable future</div>
        </div>
        """, unsafe_allow_html=True)