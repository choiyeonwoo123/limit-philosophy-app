
import streamlit as st
import json
import os

HISTORY_PATH = "sa_yu_history.json"

def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def filter_history_by_session(history, nickname=None, session_id=None):
    if nickname:
        return [entry for entry in history if entry.get("nickname") == nickname]
    if session_id:
        return [entry for entry in history if entry.get("session_id") == session_id]
    return history

def session_filter_ui():
    history = load_history()
    all_users = sorted(set(entry.get("nickname", "익명") for entry in history))
    selected_user = st.selectbox("특정 사용자 닉네임 기록 보기", ["모두 보기"] + all_users)
    if selected_user != "모두 보기":
        return filter_history_by_session(history, nickname=selected_user)
    return history
