import streamlit as st

def render_news(display_image_safe):
    st.header("📢 News & Updates")
    st.write("Recent highlights, research updates, and professional milestones.")
    st.write("")

    # Modern card styling with dark/light theme support
    st.markdown("""
        <style>
            .news-card-wrapper {
                background-color: var(--background-color, #ffffff);
                border: 1px solid rgba(128, 128, 128, 0.2);
                border-radius: 14px;
                padding: 22px;
                margin-bottom: 24px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .news-card-wrapper:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            }
            .news-badge {
                display: inline-block;
                background-color: rgba(49, 130, 206, 0.12);
                color: #3182ce;
                font-weight: 600;
                font-size: 0.8rem;
                padding: 3px 10px;
                border-radius: 12px;
                margin-bottom: 10px;
            }
            .news-title-text {
                font-size: 1.25rem;
                font-weight: 700;
                color: var(--text-color, #1a202c);
                margin-bottom: 8px;
            }
            .news-body-text {
                font-size: 0.95rem;
                line-height: 1.6;
                color: var(--text-color, #4a5568);
                opacity: 0.9;
                margin-bottom: 12px;
            }
            .news-link-btn {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                color: #3182ce !important;
                font-weight: 600;
                font-size: 0.9rem;
                text-decoration: none !important;
            }
            .news-link-btn:hover {
                text-decoration: underline !important;
            }
            @media (prefers-color-scheme: dark) {
                .news-card-wrapper {
                    background-color: #1e293b !important;
                    border-color: #334155 !important;
                }
                .news-badge {
                    background-color: rgba(99, 179, 237, 0.2);
                    color: #63b3ed;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # News items dataset
    news_items = [
        {
            "date": "August 2026",
            "tag": "Industry Experience",
            "title": "Concluded Internship at CNH Industrial ☑️",
            "body": "Completed my internship at CNH Industrial in New Holland, PA as a Soil and Crop Modeling Intern, developing data-driven reduced-order models (ROM) from complex multiphase flow simulations.",
            "image": "assets/news/CNH.jpg",
            "link": ""
        },
        {
            "date": "April 2026",
            "tag": "Publication",
            "title": "New Paper Published 📖",
            "body": "Our research paper on novel Dual-Lumen microcatheter design is now published in *Computers in Biology and Medicine*. Demonstration videos are available on my YouTube channel.",
            "image": "assets/news/cath.jpg",
            "link": "https://doi.org/10.1016/j.compbiomed.2026.111684"
        },
        {
            "date": "December 2025",
            "tag": "Publication",
            "title": "New Paper Published 📖",
            "body": "My research paper on microcapsule transport in Geothermal fractures is published. This project was in collabration with Prof. Pania Newll and it was funded by U.S. Deparment of Energy's office of Energy Efficiency and Renewable Energy.",
            "image": "assets/news/geo.jpg",
            "link": "https://www.sciencedirect.com/science/article/pii/S0375650525002846"
        },
        {
            "date": "November 2025",
            "tag": "Conference",
            "title": "APS-DFD Conference Presentation 🎤",
            "body": "Presented our latest computational findings on particle dynamics and hemodynamics at the 78th Annual Meeting of the APS Division of Fluid Dynamics in Houston, TX.",
            "image": "assets/news/APS_2025.jpg",
            "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kH2LO3MAAAAJ&citation_for_view=kH2LO3MAAAAJ:Tyk-4Ss8FVUC"
        },
        {
            "date": "November 2025",
            "tag": "PhD Journey",
            "title": "Proposal Defense 📝🎓🎤",
            "body": "I successfully defended my PhD proposal titled: “Computational Modeling of Fluid–Particle Interactions: Multiphysics and Data-Driven Approaches”.",
            "image": "assets/news/proposal.jpg",
            "link": "https://www.linkedin.com/posts/younes-tatari-b1baa0110_cfd-machinelearning-phdresearch-activity-7392346191298088960-6d4X?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAABvs6EcBG58nNDJAeQTbC0Nd4k_M8bRgUUk"
        },
        {
            "date": "November 2024",
            "tag": "Publication",
            "title": "First Paper Published 📖",
            "body": "My First Academic Paper!!!. In this study I did a patient specific modeling for splenic artery embolization.",
            "image": "assets/news/spleen_paper.jpg",
            "link": "https://www.sciencedirect.com/science/article/pii/S0021929024003981"
        },
        {
            "date": "June 2024",
            "tag": "Conference",
            "title": "SB3C: Summer Biomechanics, Bioengineering, and Biotransport 🎤",
            "body": "I Presented my research on patinet specific modeling of splenic artery embolization at SB3C in Lake Geneva, Wisconsin.",
            "image": "assets/news/sb3c_2024.jpg",
            "link": "https://www.linkedin.com/posts/younes-tatari-b1baa0110_sb3c-conferencepresentation-hemodynamics-activity-7206876019075522560-s4RM?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAABvs6EcBG58nNDJAeQTbC0Nd4k_M8bRgUUk"
        }
    ]

    # Clean multi-column layout per card
    for item in news_items:
        with st.container():
            col_text, col_img = st.columns([2.4, 1.2], gap="large")
            
            with col_text:
                st.markdown(f'<span class="news-badge">🗓️ {item["date"]} • {item["tag"]}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="news-title-text">{item["title"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="news-body-text">{item["body"]}</div>', unsafe_allow_html=True)
                if item.get("link"):
                    st.markdown(f'<a href="{item["link"]}" target="_blank" class="news-link-btn">🔗 Read Publication / Link</a>', unsafe_allow_html=True)
            
            with col_img:
                if item.get("image"):
                    display_image_safe(item["image"], use_container=True)
            
            st.markdown("---")