
import streamlit as st

LANGUAGES = {
    "한국어": "ko",
    "English": "en",
    "中文": "zh"
}

TERMS = {
    "ko": {
        "자아(Self)": "내적 반영 구조를 가진 불완전한 존재. 스스로에 대한 질문이 가능한 주체.",
        "해체(d)": "자아의 동일성이 파열되는 정도. 사유의 시작점이자 균열의 진폭.",
        "동일성(σ)": "자아가 자기 자신을 유지하려는 경향. 구조 고착성의 지표.",
        "감응(g)": "감정, 직관, 파열 등 자아에 흔적을 남기는 요소의 총합.",
        "반영(r)": "자기 인식을 거듭하는 층위의 깊이. 자각 구조의 반복성.",
        "타자성(x)": "자아 외부의 존재 인식 정도. 경계의 외부에 대한 감도.",
        "규범(Λ)": "자아 내부에 내면화된 요청이나 명령. 윤리적 구조의 형식화.",
        "사유량(S)": "해체와 감응이 생성한 총 사유의 크기.",
        "사유 방향성(θ)": "동일성 대비 해체의 비율을 나타내는 구조 각도.",
        "자아 안정성(δ)": "자아에서 동일성이 차지하는 비율.",
        "감응률(φ)": "전체 사유 중 감응이 차지하는 비율.",
        "언어 농도(μ)": "문장에서 단어 수 대비 사유량이 차지하는 밀도."
    },
    "en": {
        "Self": "An incomplete being with internal reflective structure; capable of asking questions about itself.",
        "Deconstruction (d)": "Degree to which self-identity is fractured.",
        "Identity (σ)": "Tendency of the self to maintain its structure.",
        "Affect (g)": "Sum of emotional, intuitive, or fractured traces affecting the self.",
        "Reflection (r)": "Depth of recursive self-awareness layers.",
        "Otherness (x)": "Degree to which the self recognizes entities beyond itself.",
        "Normativity (Λ)": "Internalized philosophical or moral rules.",
        "Thought Quantity (S)": "Total conceptual output from deconstruction and affect.",
        "Thought Direction (θ)": "Ratio of identity vs. deconstruction (as angular orientation).",
        "Self Stability (δ)": "Ratio of identity in overall self structure.",
        "Affect Ratio (φ)": "Proportion of affect in total thought.",
        "Language Density (μ)": "Density of thought relative to number of words."
    },
    "zh": {
        "自我（Self）": "具有内在反思结构的不完整存在，能够对自身提问。",
        "解构（d）": "自我同一性的破裂程度。",
        "同一性（σ）": "自我保持自身结构的倾向。",
        "感应（g）": "影响自我的情感、直觉或断裂痕迹的总和。",
        "反思（r）": "递归自我意识的层级深度。",
        "他性（x）": "自我对外部存在的认知程度。",
        "规范（Λ）": "内化的哲学或道德规则。",
        "思维量（S）": "由解构与感应生成的整体思维。",
        "思维方向（θ）": "同一性与解构的比例（角度）。",
        "自我稳定性（δ）": "自我结构中同一性所占比例。",
        "感应率（φ）": "感应在整体思维中所占的比例。",
        "语言密度（μ）": "单位词汇中所包含的思维密度。"
    }
}

def tutorial_interface():
    st.subheader("한계 철학 용어 튜토리얼 / Limit Philosophy Glossary")

    lang = st.selectbox("언어를 선택하세요 / Choose Language / 选择语言", list(LANGUAGES.keys()))
    lang_code = LANGUAGES[lang]

    for term, definition in TERMS[lang_code].items():
        st.markdown(f"**{term}**: {definition}")
