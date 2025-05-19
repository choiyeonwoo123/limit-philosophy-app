
import streamlit as st
from typing import Dict
from 분석모듈 import estimate_all_with_semantics_updated, generate_full_report

st.set_page_config(page_title="사유 정식 해석기", layout="wide")

st.title("한계 철학 기반 사유 정식 해석기")
st.markdown("입력한 문장을 기반으로 사유 구조를 분석하고 해석 리포트를 생성합니다.")

text_input = st.text_area("분석할 문장을 입력하세요", height=200)

if st.button("분석 실행"):
    if text_input.strip() == "":
        st.warning("문장을 입력하세요.")
    else:
        with st.spinner("분석 중..."):
            result = estimate_all_with_semantics_updated(text_input)
            report = generate_full_report(text_input, result)
            st.success("분석 완료!")
            st.markdown("### 자동 해석 리포트")
            st.text_area("리포트 결과", value=report, height=600)
