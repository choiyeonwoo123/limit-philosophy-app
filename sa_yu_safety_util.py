
import streamlit as st

def safe_run(func, fallback=None):
    try:
        return func()
    except Exception as e:
        st.error(f"오류 발생: {str(e)}")
        return fallback

def ensure_session_keys(keys_with_defaults):
    for key, default in keys_with_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default
