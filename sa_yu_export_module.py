
import streamlit as st
import json
import base64
import io
from fpdf import FPDF

def generate_shareable_link(text, analysis):
    payload = json.dumps({
        "text": text,
        "analysis": analysis
    }, ensure_ascii=False).encode("utf-8")
    encoded = base64.urlsafe_b64encode(payload).decode("utf-8")
    link = f"https://limit-philosophy.app/share#{encoded}"
    st.markdown(f"[공유 가능한 링크 생성]({link})")
    return link

def decode_shared_link(encoded_str):
    try:
        decoded = base64.urlsafe_b64decode(encoded_str.encode("utf-8"))
        return json.loads(decoded)
    except Exception:
        return None

def export_analysis_to_pdf(text, analysis):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Arial", "", fname=None, uni=True)
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"[분석 문장]: {text}", align="L")
    pdf.multi_cell(0, 10, "\n[계수]:", align="L")
    for k, v in analysis.get("계수", {}).items():
        pdf.multi_cell(0, 10, f"{k}: {v}", align="L")
    pdf.multi_cell(0, 10, "\n[정식 계산 결과]:", align="L")
    for k, v in analysis.get("정식 계산 결과", {}).items():
        pdf.multi_cell(0, 10, f"{k}: {v}", align="L")

    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)

    b64 = base64.b64encode(output.read()).decode("utf-8")
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="사유_분석_결과.pdf">PDF 다운로드</a>'
    st.markdown(href, unsafe_allow_html=True)
