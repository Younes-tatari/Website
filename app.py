import os
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Younes Tatari - Academic Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

import home
import Research
import experience_education
import cv
import publications

# ==============================================================================
# ---------------------- CUSTOM CSS --------------------------------------------
# ==============================================================================
st.markdown(
    """
<style>
/* Style radio group container */
    div[role="radiogroup"] {
        display: flex;
        gap: 8px;
    }
    
    /* Hide the radio circles */
    div[role="radiogroup"] label div:first-child {
        display: none !important;
    }

    /* Style the option labels like tab buttons */
    div[role="radiogroup"] label {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 8px 16px !important;
        border-radius: 20px !important;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    /* Hover effect */
    div[role="radiogroup"] label:hover {
        background-color: rgba(255, 255, 255, 0.15);
    }
    
    /* Dark sidebar styling - explicit text contrast */
    [data-testid="stSidebar"] {
        background-color: #0b132b !important;
    }
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] a {
        color: #ffffff !important;
    }

    /* HERO CONTAINER STYLING */
    .hero-card {
        background: linear-gradient(135deg, #0a192f 0%, #1e3c72 50%, #2a5298 100%);
        border-radius: 16px;
        padding: 30px;
        color: #ffffff !important;
        margin-bottom: 25px;
    }
    .hero-card * {
        color: #ffffff !important;
    }

    /* Target ONLY profile images for circular styling */
    .profile-pic-container img {
        border-radius: 50% !important;
        border: 4px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3) !important;
        object-fit: cover !important;
    }

    /* Custom badge styling */
    .badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 20px;
        padding: 6px 16px;
        margin-right: 8px;
        margin-bottom: 10px;
        font-size: 14px;
        font-weight: 500;
        backdrop-filter: blur(5px);
        color: inherit;
    }

    /* Dynamic Feature Cards (Adapts to Light & Dark Mode) */
    .feature-card {
        background-color: var(--background-color, #ffffff);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid rgba(128, 128, 128, 0.2);
        height: 100%;
    }

    .feature-title {
        font-weight: 700;
        color: var(--text-color, #1a202c);
        font-size: 16px;
        margin-bottom: 4px;
    }

    .feature-desc {
        color: var(--text-color, #718096);
        opacity: 0.8;
        font-size: 13px;
        line-height: 1.4;
    }
    
    /* Dark Mode Specific Overrides */
    @media (prefers-color-scheme: dark) {
        .feature-card {
            background-color: #1e293b !important;
            border-color: #334155 !important;
        }
        .feature-title {
            color: #f8fafc !important;
        }
        .feature-desc {
            color: #cbd5e1 !important;
        }
    }

    div.row-widget.stRadio > div {
        flex-direction: row;
        justify-content: space-around;
        background-color: var(--background-color, #ffffff);
        padding: 8px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""",
    unsafe_allow_html=True,
)

def display_image_safe(image_path, width=None, use_container=False):
    if os.path.exists(image_path):
        if use_container:
            st.image(image_path, use_container_width=True)
        elif width:
            st.image(image_path, width=width)
        else:
            st.image(image_path, use_container_width=True)
    else:
        st.write("🖼️")

# ---------------------- SIDEBAR ----------------------
with st.sidebar:
    st.title("Younes Tatari")
    st.caption("Mechanical Engineering · CFD · Multiphysics · Scientific Machine Learning")
    
    st.markdown("---")
    st.markdown("### ACADEMIC & PROFESSIONAL")
    
    affiliations = [
        {"name": "Scientific Computing and Imaging Institute", "location": "USA", "logo": "assets/logos/sci.png"},
        {"name": "University of Utah", "location": "USA", "logo": "assets/logos/utah.png"},
        {"name": "CNH Industrial", "location": "Global", "logo": "assets/logos/CNH.png"},
        {"name": "Harbin Institute of Technology", "location": "China", "logo": "assets/logos/HIT.png"},
        {"name": "Isfahan University of Technology", "location": "Iran", "logo": "assets/logos/IUT.png"}
    ]
    
    for aff in affiliations:
        col1, col2 = st.columns([1, 2.8])
        with col1:
            display_image_safe(aff["logo"], width=85)
        with col2:
            st.markdown(f"**{aff['name']}** \n<small style='color: #a0aec0;'>{aff['location']}</small>", unsafe_allow_html=True)
        st.write("")

    st.markdown("---")
    st.markdown("### CONNECT")
    
    linkedin_svg = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
    scholar_svg = "https://cdn.simpleicons.org/googlescholar"
    Google_svg = "https://cdn-icons-png.flaticon.com/512/2991/2991148.png"
    youtube_svg = "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"

    st.markdown(f"""
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <a href="https://www.linkedin.com/in/younes-tatari-b1baa0110/" target="_blank" style="text-decoration: none; color: white; display: flex; align-items: center; gap: 10px;">
            <img src="{linkedin_svg}" width="22"/> LinkedIn
        </a>
        <a href="https://scholar.google.com/citations?user=kH2LO3MAAAAJ&hl=en" target="_blank" style="text-decoration: none; color: white; display: flex; align-items: center; gap: 10px;">
            <img src="{Google_svg}" width="22"/> <span> Google Scholar 
        </a>
        <a href="https://www.youtube.com/@younestatari4645" target="_blank" style="text-decoration: none; color: white; display: flex; align-items: center; gap: 10px;">
            <img src="{youtube_svg}" width="22"/> YouTube Channel
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------------- MAIN CONTENT ----------------------
# Banner Image remains strictly rectangular
display_image_safe("assets/logos/banner.jpg", use_container=True)
st.write("")


#selected_tab = st.radio(label="Navigation",options=["Home", "Research", "Experience & Education", "CV", "Publications"],horizontal=True,label_visibility="collapsed")

selected_tab = st.segmented_control(label="Navigation",options=["Home", "Research", "Experience & Education", "CV", "Publications"],default="Home",label_visibility="collapsed")

st.write("")

if selected_tab == "Home":
    home.render_home(display_image_safe)
elif selected_tab == "Research":
    Research.render_Research()
elif selected_tab == "Experience & Education":
    experience_education.render_experience_education()
elif selected_tab == "CV":
    cv.render_cv()
elif selected_tab == "Publications":
    publications.render_publications()