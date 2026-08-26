import streamlit as st

def render_genealogy(display_image_safe):
    st.header("🧬 Academic Genealogy")
    st.write(
        "**My academic lineage goes through scientists like Gauss, Poisson, Dirichlet, Ohm, Fourier, Lagrange, Euler, and Bernoulli.**"
    )

    st.write("")

    # Display your original genealogy image
    col_left, col_center, col_right = st.columns([0.1, 0.8, 0.1])
    
    with col_center:
        display_image_safe("assets/genology.jpg", width = 40 , use_container=True)