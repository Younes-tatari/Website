import os
import streamlit as st


def render_cv():
    st.header("📄 Curriculum Vitae")

    # ---------------------- SECTION 1: CV PREVIEW & DOWNLOAD ----------------------
    cv_file_path = "assets/Younes_Tatari__CV.pdf"

    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        # Download button
        st.download_button(
            label="📥 Download Full CV (PDF)",
            data=pdf_bytes,
            file_name="Younes_Tatari_CV.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

        st.write("")  # Spacing

        # Native Streamlit PDF preview
        st.pdf(
            pdf_bytes,
            height=900,
            key="cv_pdf_preview",
        )

    else:
        st.info(
            "💡 Place `Younes_Tatari__CV.pdf` inside your project root "
            "folder to enable direct PDF download and inline viewing."
        )

    st.markdown("---")