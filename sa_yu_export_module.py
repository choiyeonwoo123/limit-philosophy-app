
# -*- coding: utf-8 -*-
import streamlit as st
import json
import base64

def generate_shareable_link(text, analysis):
    payload = json.dumps({
        "text": text,
        "analysis": analysis
    }, ensure_ascii=False).encode("utf-8")
    encoded = base64.urlsafe_b64encode(payload).decode("utf-8")
    link = f"https://limit-philosophy.app/share#{encoded}"
    st.markdown(f"[공유 가능한 링크 생성]({link})")
    return link
