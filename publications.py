import base64
import os
import streamlit as st

def render_publications():
    st.header("📄 Publications & Presentations")

    # ---------------------- SECTION 1: PUBLICATIONS ----------------------
    st.subheader("📚 Peer-Reviewed Publications")
    
    publications = [
        {
            "title": "A Dual-Lumen Microcatheter for Minimizing Particle Reflux During Embolization: Proof-of-concept with multiphysics simulations",
            "journal": "Computers in Biology and Medicine",
            "year": "2026",
            "badge": "Journal Article",
            "link": "https://www.sciencedirect.com/science/article/pii/S0010482526002489" 
        },
        {
            "title": "Investigation of particle transport in geothermal systems using integrated CFD-DEM and data-driven approaches",
            "journal": "Journal of Geothermics",
            "year": "2026",
            "badge": "Journal Article",
            "link": "https://www.sciencedirect.com/science/article/pii/S0375650525002846"  
        },
        {
            "title": "Adam-sindy: An efficient optimization framework for parameterized nonlinear dynamical system identification",
            "journal": "Journal of Physical Review Research",
            "year": "2026",
            "badge": "Journal Article",
            "link": "https://journals.aps.org/prresearch/abstract/10.1103/dwkk-5g2h"  
        },
        {
            "title": "Optimizing distal and proximal splenic artery embolization with patient-specific computational fluid dynamics",
            "journal": "Journal of Biomechanics",
            "year": "2024",
            "badge": "Journal Article",
            "link": "https://www.sciencedirect.com/science/article/pii/S0021929024003981"  
        }
    ]

    for pub in publications:
        # Wrap title in an anchor tag if link exists
        if pub.get("link"):
            title_display = f'<a href="{pub["link"]}" target="_blank" style="text-decoration: none; color: #1a202c;">{pub["title"]}</a>'
        else:
            title_display = pub["title"]

        st.markdown(f"""
        <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 5px solid #2a5298; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
            <span style="background-color: #ebf8ff; color: #2b6cb0; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 4px;">{pub['badge']}</span>
            <h4 style="margin-top: 8px; margin-bottom: 4px; font-size: 16px;">{title_display}</h4>
            <p style="color: #4a5568; margin-bottom: 0px; font-size: 14px;"><em>{pub['journal']}</em> ({pub['year']})</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------------- SECTION 2: CONFERENCES ----------------------
    st.subheader("🎤 Conference Presentations & Abstracts")

    conferences = [
        {
            "title": "Coupled CFD-Particle Approaches to Predict Particle Transport and Reflux in Embolization",
            "authors": "Y Tatari, O Amili, J Hu, A Arzani",
            "event": "78th Annual Meeting of the Division of Fluid Dynamics",
            "year": "2025",
            "badge": "Conference Presentation",
            "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kH2LO3MAAAAJ&citation_for_view=kH2LO3MAAAAJ:Tyk-4Ss8FVUC"
        },
        {
            "title": "Enhancing Splenic Artery Embolization Outcomes with Patient-Specific Computational Fluid Dynamics",
            "authors": "Y Tatari, T Smith, J Hu, A Arzani",
            "event": "APS Division of Fluid Dynamics Meeting Abstracts, X05. 005",
            "year": "2024",
            "badge": "Conference Abstract",
            "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kH2LO3MAAAAJ&citation_for_view=kH2LO3MAAAAJ:qjMakFHDy7sC"
        },
        {
            "title": "SGD-SINDy: Stochastic Gradient-Descent based Framework for Flexible System Identification",
            "authors": "A Arzani, S Viknesh, Y Tatari",
            "event": "APS Division of Fluid Dynamics Meeting Abstracts, A15. 003",
            "year": "2024",
            "badge": "Conference Abstract",
            "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kH2LO3MAAAAJ&citation_for_view=kH2LO3MAAAAJ:2osOgNQ5qMEC"
        },
        {
            "title": "Patient Specific Modeling of Hemodynamics During Splenic Artery Embolization",
            "authors": "Y Tatari, TA Smith, J Hu, A Arzani",
            "event": "Summer Biomechanics, Bioengineering, & Biotransport Conference",
            "year": "2024",
            "badge": "Conference Presentation",
            "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kH2LO3MAAAAJ&citation_for_view=kH2LO3MAAAAJ:IjCSPb-OGe4C"
        }
    ]

    for conf in conferences:
        if conf.get("link"):
            title_display = f'<a href="{conf["link"]}" target="_blank" style="text-decoration: none; color: #1a202c;">{conf["title"]}</a>'
        else:
            title_display = conf["title"]

        st.markdown(f"""
        <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 5px solid #319795; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
            <span style="background-color: #e6fffa; color: #234e52; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 4px;">{conf['badge']}</span>
            <h4 style="margin-top: 8px; margin-bottom: 4px; font-size: 16px;">{title_display}</h4>
            <p style="color: #718096; margin-bottom: 2px; font-size: 13px;">{conf['authors']}</p>
            <p style="color: #4a5568; margin-bottom: 0px; font-size: 14px;"><em>{conf['event']}</em> ({conf['year']})</p>
        </div>
        """, unsafe_allow_html=True)