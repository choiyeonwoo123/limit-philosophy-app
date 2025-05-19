
from langdetect import detect

# 해석 함수들
def interpret_d(d):
    if d == 0:
        return "해체 계수 d가 0입니다. 자아의 동일성이 유지되고 있습니다."
    elif d == 1:
        return "자아에 약간의 균열이 생기며, 질문의 가능성이 열리고 있습니다."
    elif d == 2:
        return "자아의 균열이 구조적으로 드러나며, 자기 해체가 시작됩니다."
    else:
        return "심화된 해체 상태입니다. 자아의 경계가 붕괴되고 있습니다."

def interpret_sigma(sigma):
    if sigma == 0:
        return "동일성 계수 σ가 0입니다. 자아 동일성이 완전히 붕괴된 상태입니다."
    elif sigma == 1:
        return "자아 동일성이 약하게 존재합니다."
    elif sigma == 2:
        return "자아는 일정한 동일성을 유지하려는 구조를 보입니다."
    else:
        return "동일성의 강한 강조입니다. 구조적 고착 가능성이 있습니다."

def interpret_r(r):
    return f"반영 구조 r = {r}. 자기 반영은 {r}단계의 층위를 가지고 있습니다."

def interpret_x(x):
    if x == 0:
        return "타자 인식이 없습니다."
    elif x == 1:
        return "타자가 존재하지만 자아에 깊게 개입되진 않습니다."
    elif x == 2:
        return "타자와의 경계 인식이 구조적으로 존재합니다."
    else:
        return "타자의 개입이 자아에 주요한 영향을 주는 수준입니다."

def interpret_lambda(Lambda):
    if Lambda == 0:
        return "규범의 내면화가 없습니다."
    elif Lambda == 1:
        return "철학적 혹은 윤리적 요청이 암시적으로 포함되어 있습니다."
    elif Lambda == 2:
        return "구조화된 내면 명령이 존재합니다."
    else:
        return "강한 내면화된 규범이 자아를 지배하고 있습니다."

def interpret_g(g):
    return f"감응 강도 g = {g}. 자아에 영향을 미친 감응 요소들의 총합입니다."

def interpret_S(S):
    return f"사유량 S = {S}. 해체와 감응을 통한 총 사유량입니다."

def interpret_tau(tau):
    return f"확장 사유량 τ = {tau}. 반영, 타자성, 규범까지 포함된 전체 사유 범위입니다."

def interpret_theta(theta):
    return f"사유 방향성 θ = {theta}. 동일성 대비 해체의 각도입니다."

def interpret_delta(delta):
    return f"자아 안정성 δ = {delta}. 자아 구조에서 동일성이 차지하는 비율입니다."

def interpret_phi(phi):
    return f"감응률 φ = {phi}. 전체 사유 중 감응이 차지하는 비율입니다."

def interpret_mu(mu):
    return f"언어 농도 μ = {mu}. 단어 수 대비 사유의 밀도입니다."

def classify_thinking_style(d, sigma, r, x, Lambda, g, theta, delta, phi, mu):
    styles = []
    if d > sigma and g > 4: styles.append("해체적 사유")
    if sigma > d and delta > 0.8: styles.append("동일성 고정 사유")
    if r >= 4: styles.append("반영적 사유")
    if phi > 0.6: styles.append("감응 중심 사유")
    if x >= 3: styles.append("타자 지향 사유")
    if Lambda >= 3: styles.append("규범 수용 사유")
    if mu > 0.8: styles.append("압축적 사유")
    if 0.45 <= delta <= 0.55 and 0.9 <= theta <= 1.1: styles.append("정체성 혼성 사유")
    if not styles:
        styles.append("구조적 중립 사유")
    return styles

def generate_full_report(text, result):
    c = result["계수"]
    f = result["정식 계산 결과"]
    styles = classify_thinking_style(c["d"], c["σ"], c["r"], c["x"], c["Λ"], c["g"], f["θ"], f["δ"], f["φ"], f["μ"])
    return f"""[자동 해석 리포트]

◆ 입력 문장:
{text}

◆ 계수 해석:
- {interpret_d(c['d'])}
- {interpret_sigma(c['σ'])}
- {interpret_r(c['r'])}
- {interpret_x(c['x'])}
- {interpret_lambda(c['Λ'])}
- {interpret_g(c['g'])}

◆ 정식 계산 해석:
- {interpret_S(f['S'])}
- {interpret_tau(f['τ'])}
- {interpret_theta(f['θ'])}
- {interpret_delta(f['δ'])}
- {interpret_phi(f['φ'])}
- {interpret_mu(f['μ'])}

◆ 사유 스타일 분류:
- {' / '.join(styles)}
"""

# 감응 패턴
epsilon_weights = {"ε₁": 1.0, "ε₂": 1.2, "ε₃": 1.3, "ε₄": 1.5, "ε₅": 1.1, "ε₆": 1.4, "ε₇": 1.3, "ε₈": 1.5, "ε₉": 1.0}
epsilon_patterns_multilang = {
    'en': {"ε₁": ["sadness"], "ε₉": ["wind", "waves"]},
    'ko': {"ε₁": ["슬픔"], "ε₉": ["바람", "파도"]},
    'zh': {"ε₁": ["悲伤"], "ε₉": ["风", "浪"]}
}
def estimate_epsilon_and_g_multilang(text, lang):
    from collections import defaultdict
    epsilon_counts = defaultdict(int)
    g = 0.0
    patterns = epsilon_patterns_multilang.get(lang, {})
    for eps, words in patterns.items():
        for word in words:
            count = text.count(word)
            epsilon_counts[eps] += count
            g += count * epsilon_weights.get(eps, 1.0)
    return dict(epsilon_counts), round(g, 2)

# 계수 추정 함수들 (예시적)
def estimate_d_with_semantics(text): return 2
def estimate_sigma_with_semantics(text): return 3
def estimate_r_with_semantics(text): return 2
def estimate_x_with_semantics(text): return 3
def estimate_lambda_with_semantics(text): return 1

def estimate_all_with_semantics_multilang(text):
    lang = detect(text)
    d = estimate_d_with_semantics(text)
    sigma = estimate_sigma_with_semantics(text)
    r = estimate_r_with_semantics(text)
    x = estimate_x_with_semantics(text)
    Lambda = estimate_lambda_with_semantics(text)
    epsilon_counts, g = estimate_epsilon_and_g_multilang(text, lang)
    S = abs(d - sigma) + g
    tau = S + r + x + Lambda
    theta = round((sigma / d), 3) if d != 0 else 0
    delta = round(sigma / (sigma + d), 3) if (sigma + d) != 0 else 0
    phi = round(g / S, 3) if S != 0 else 0
    mu = round(S / len(text.split()), 3) if len(text.split()) > 0 else 0
    return {
        "문장": text,
        "언어": lang,
        "계수": {"d": d, "σ": sigma, "g": g, "ε": epsilon_counts, "r": r, "x": x, "Λ": Lambda},
        "정식 계산 결과": {"S": S, "τ": tau, "θ": theta, "δ": delta, "φ": phi, "μ": mu}
    }
