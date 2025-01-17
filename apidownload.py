import streamlit as st
import google.generativeai as genai

# API 키 입력
api_key = st.text_input("API 키를 입력하세요:", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # PDF 파일 업로드
    uploaded_file = st.file_uploader("PDF 파일을 업로드하세요:", type="pdf")

    if uploaded_file is not None:
        # 파일 내용 읽기
        file_content = uploaded_file.read()

        # Gemini API 호출 (예시)
        response = genai.generate_content([
            {'mime_type': 'application/pdf', 'data': file_content},
            "이 PDF 파일을 요약해주세요."
        ])

        # 결과 출력
        st.write(response.text)

    else:
        st.write("PDF 파일을 업로드해주세요.")

else:
    st.write("API 키를 입력해주세요.")

"""streamlit==1.28.1
google-generativeai==0.2.0
"""
