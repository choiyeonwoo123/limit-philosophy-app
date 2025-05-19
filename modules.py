
from langdetect import detect

def interpret_d(d):
    if d == 0: return "해체 계수 d = 0 → 자아의 동일성이 유지됨"
    elif d == 1: return "해체 계수 d = 1 → 자아에 균열이 시작됨"
    elif d == 2: return "해체 계수 d = 2 → 구조적 균열로 해체가 전개됨"
    else: return f"해체 계수 d = {d} → 고도 해체 상태"

def interpret_sigma(sigma):
    if sigma == 0: return "동일성 계수 σ = 0 → 자아 동일성 붕괴"
    elif sigma == 1: return "동일성 계수 σ = 1 → 약한 동일성"
    elif sigma == 2: return "동일성 계수 σ = 2 → 구조적 동일성 유지"
    else: return f"동일성 계수 σ = {sigma} → 강한 동일성 강조"

def interpret_r(r): return f"반영 구조 r = {r} → {r}단계 자기 반영"
def interpret_x(x): return f"타자성 x = {x} → 타자의 개입 수준"
def interpret_lambda(L): return f"내면화된 규범 Λ = {L} → 철학적/도덕적 명령 강도"
def interpret_g(g): return f"감응 강도 g = {g} → 감정/직관 흔적의 총합"
def interpret_S(S): return f"사유량 S = {S} → 해체와 감응의 총합"
def interpret_tau(t): return f"확장 사유량 τ = {t} → 반영, 타자성, 규범 포함 총량"
def interpret_theta(th): return f"사유 방향성 θ = {th} → 동일성 대비 해체의 각도"
def interpret_delta(dlt): return f"자아 안정성 δ = {dlt} → 동일성이 차지하는 비율"
def interpret_phi(phi): return f"감응률 φ = {phi} → 감응의 비율"
def interpret_mu(mu): return f"언어 농도 μ = {mu} → 단어 수 대비 사유 밀도"

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

epsilon_weights = {"ε₁": 1.0, "ε₂": 1.2, "ε₃": 1.3, "ε₄": 1.5, "ε₅": 1.1, "ε₆": 1.4, "ε₇": 1.3, "ε₈": 1.5, "ε₉": 1.0}
epsilon_patterns_multilang = {
    'ko': {"ε₁": ["슬픔"], "ε₉": ["바람", "파도"]},
    'en': {"ε₁": ["sadness"], "ε₉": ["wind", "waves"]},
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
