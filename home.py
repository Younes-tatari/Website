import streamlit as st

def render_home(display_image_safe):
    # Adjust column proportions: [3, 1] keeps image at ~25% relative layout
    col_text, col_img = st.columns([3, 1], gap="medium")
    
    with col_text:
        st.markdown("""
        <div class="hero-card">
            <h1 style="font-size: clamp(2rem, 4vw, 3.2rem); margin-bottom: 0px; color: white;">Younes Tatari</h1>
            <h3 style="color: #63b3ed; font-size: clamp(1.1rem, 2vw, 1.5rem); font-weight: 400; margin-top: 5px; margin-bottom: 20px;">
                PhD Researcher in Mechanical Engineering
            </h3>
            <p style="font-size: clamp(1rem, 1.3vw, 1.25rem); line-height: 1.6; color: #e2e8f0; margin-bottom: 25px;">
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
        # Wrap image in profile container class and remove static width argument
        st.markdown('<div class="profile-pic-container">', unsafe_allow_html=True)
        display_image_safe("assets/profile.jpg", use_container=True)
        st.markdown('</div>', unsafe_allow_html=True)

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