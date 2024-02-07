import streamlit as st
import pypdfium2 as pdfium

st.title('------PDF TO JPG ------')

uploaded_file = st.file_uploader("Upload your file here...", type=['pdf'])
if uploaded_file is not None:
    pdf = pdfium.PdfDocument(uploaded_file)
    fn = uploaded_file.name
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=1.45).to_pil()
        st.image(image)
        image.save(f"{fn}.jpg")
        with open(f"{fn}.jpg", "rb") as file:
                        btn = st.download_button(
                        label="Download image",
                        data=file,
                        file_name=f"*{fn}.jpg",
                        mime="image/jpg"
                        )
st.text('$/$ Made with ❤ By Cyper24 $/$')
