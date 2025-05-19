
import streamlit as st
from modules import estimate_all_with_semantics_multilang, generate_full_report

st.set_page_config(page_title="사유 정식 해석기", layout="wide")

st.title("한계 철학 기반 사유 정식 해석기")
st.markdown("문장을 입력하면 다국어 사유 정식 분석 리포트를 생성합니다.")

text_input = st.text_area("분석할 문장을 입력하세요", height=200)

if st.button("분석 실행"):
    if text_input.strip() == "":
        st.warning("문장을 입력하세요.")
    else:
        with st.spinner("분석 중..."):
            result = estimate_all_with_semantics_multilang(text_input)
            report = generate_full_report(text_input, result)
            st.success(f"분석 완료! (언어 감지: {result['언어']})")
            st.markdown("### 자동 해석 리포트")
            st.text_area("리포트 결과", value=report, height=600)
