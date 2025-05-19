
import streamlit as st

def example_sentence_selector():
    st.markdown("### 예시 문장 선택")
    examples = {
        "데카르트 – 코기토": "나는 생각한다. 고로 존재한다.",
        "장자 – 제물론": "그 변을 알지 못하는 것은 사물도 또한 그러하다.",
        "부처 – 초기 경전": "모든 것은 덧없다. 모든 것은 괴롭다. 모든 것은 무아다.",
        "카프카 – 단편": "나는 그 문을 지나갈 수 없으며, 그것은 나만을 위해 열려 있었다.",
        "피트 타운센드 – Time is Passing": "It's only by the music I'll be free.",
        "사용자 정의 문장": ""
    }

    selected = st.selectbox("아래에서 예시 문장을 선택하거나 직접 입력하세요", list(examples.keys()))
    default_text = examples[selected]
    input_text = st.text_area("분석할 문장", value=default_text, key="main_input")
    return input_text
