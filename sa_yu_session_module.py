
import streamlit as st
import uuid

def init_user_session():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())
    nickname = st.text_input("세션 구분을 위한 이름을 입력하세요 (선택)", key="nickname_input")
    if nickname.strip():
        st.session_state["nickname"] = nickname.strip()
    else:
        st.session_state["nickname"] = "익명"

    st.markdown(f"**세션 ID**: `{st.session_state['session_id']}`")
    st.markdown(f"**닉네임**: `{st.session_state['nickname']}`")

def get_user_info():
    return {
        "session_id": st.session_state.get("session_id", "unknown"),
        "nickname": st.session_state.get("nickname", "익명")
    }
