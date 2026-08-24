import base64
import os
import streamlit as st

def render_cv():
    st.header("📄 Curriculum Vitae")

    # ---------------------- SECTION 1: CV PREVIEW & DOWNLOAD ----------------------
    #st.subheader("📄 Curriculum Vitae")

    cv_file_path = "Younes_Tatari__CV.pdf"

    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        # Download button
        st.download_button(
            label="📥 Download Full CV (PDF)",
            data=pdf_bytes,
            file_name="Younes_Tatari_CV.pdf",
            mime="application/pdf"
        )

        st.write("")  # Spacing

        # Encode PDF to base64 for browser preview
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        
        # Embedded PDF preview container
        pdf_display = f'''
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="900px" 
                type="application/pdf"
                style="border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);"
            >
            </iframe>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.info("💡 Place `Younes_Tatari__CV.pdf` inside your project root folder to enable direct PDF download and inline viewing.")

    st.markdown("---")

    