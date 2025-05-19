
import streamlit as st
from datetime import datetime
from modules import estimate_all_with_semantics_multilang, generate_full_report, classify_thinking_style

from sa_yu_session_module import init_user_session, get_user_info
from sa_yu_session_filter import session_filter_ui, load_history
from sa_yu_example_selector import example_sentence_selector
from sa_yu_export_module import generate_shareable_link, export_analysis_to_pdf
from sa_yu_tutorial_module import tutorial_interface
from sa_yu_safety_util import safe_run, ensure_session_keys

import matplotlib.pyplot as plt
import numpy as np
import json
import os

HISTORY_PATH = "sa_yu_history.json"

# 레이더 차트 함수
def draw_radar_chart(analysis_result, label):
    c = analysis_result["계수"]
    f = analysis_result["정식 계산 결과"]
    labels = ['d', 'σ', 'r', 'x', 'Λ', 'g', 'θ°', 'δ', 'φ', 'μ']
    values = [
        c["d"], c["σ"], c["r"], c["x"], c["Λ"], c["g"],
        round(np.degrees(np.arctan(f["θ"])) / 90, 3),
        f["δ"], f["φ"], f["μ"]
    ]
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.plot(angles, values, label=label)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 3)
    st.pyplot(fig)

# 분석 결과 저장
def save_to_history(user, text, result):
    history = load_history()
    history.append({
        "session_id": user["session_id"],
        "nickname": user["nickname"],
        "timestamp": str(datetime.now()),
        "text": text,
        "analysis": result
    })
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# 사이드바 초기 설정
st.sidebar.title("한계 철학 분석기 설정")
init_user_session()
mode = st.sidebar.radio("분석 모드", ["간단 분석", "기록 기반 확장"])
show_tutorial = st.sidebar.checkbox("튜토리얼 보기")

# 본문
st.title("『한계 철학 사유 분석기』")
st.markdown("자신의 사유 구조를 정식화하고 해석하는 도구입니다.")

if show_tutorial:
    tutorial_interface()

input_text = example_sentence_selector()
user = get_user_info()

if st.button("분석 실행"):
    result = safe_run(lambda: estimate_all_with_semantics_multilang(input_text))
    if result:
        st.text(generate_full_report(input_text, result))
        draw_radar_chart(result, "현재 분석 결과")
        generate_shareable_link(input_text, result)
        export_analysis_to_pdf(input_text, result)
        if mode == "기록 기반 확장":
            save_to_history(user, input_text, result)

# 기록 기반 UI
if mode == "기록 기반 확장":
    st.subheader("내/전체 기록 보기 및 비교")
    history = session_filter_ui()
    for entry in history:
        st.markdown(f"**{entry['text']}**  _(닉네임: {entry['nickname']})_")
        draw_radar_chart(entry["analysis"], entry["text"])
