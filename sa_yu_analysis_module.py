
# -*- coding: utf-8 -*-
import math

def estimate_all_with_semantics_multilang(text):
    # 예시용 간단한 계수 추정
    length = len(text)
    d = 1 if "질문" in text or "왜" in text else 0
    sigma = 1 if "나는" in text else 0
    r = 1 if "생각" in text else 0
    x = 1 if "너" in text or "타자" in text else 0
    Lambda = 1 if "해야" in text or "마땅하다" in text else 0
    g = 1 if "느낌" in text or "직관" in text or "환상" in text else 0

    S = d + sigma + r + x + Lambda + g
    theta = math.atan2(sigma, d) if d > 0 else math.pi / 2
    delta = sigma / (sigma + d) if (sigma + d) != 0 else 0
    phi = g / S if S != 0 else 0
    mu = S / length if length > 0 else 0

    return {
        "계수": {
            "d": d,
            "σ": sigma,
            "r": r,
            "x": x,
            "Λ": Lambda,
            "g": g
        },
        "정식 계산 결과": {
            "S": S,
            "θ": theta,
            "δ": delta,
            "φ": phi,
            "μ": mu
        }
    }

def generate_full_report(text, result):
    r = result["계수"]
    f = result["정식 계산 결과"]
    return f"""[분석 보고서]

문장: {text}

- 해체 계수 (d): {r['d']}
- 동일성 계수 (σ): {r['σ']}
- 반영 계수 (r): {r['r']}
- 타자성 계수 (x): {r['x']}
- 내면화된 규범 계수 (Λ): {r['Λ']}
- 감응 계수 (g): {r['g']}

- 총 사유량 (S): {f['S']}
- 사유 방향성 (θ): {round(f['θ'], 2)} 라디안
- 자아 안정성 (δ): {round(f['δ'], 2)}
- 감응률 (φ): {round(f['φ'], 2)}
- 언어 농도 (μ): {round(f['μ'], 4)}
"""

def classify_thinking_style(result):
    S = result["정식 계산 결과"]["S"]
    if S >= 6:
        return "매우 복합적 사유"
    elif S >= 4:
        return "심층적 사유"
    elif S >= 2:
        return "일반적 사유"
    else:
        return "단편적 사유"
