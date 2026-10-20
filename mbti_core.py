# -*- coding: utf-8 -*-
from __future__ import annotations

# 학습용 안내 문구 (과학적/공식 진단이 아님을 명시)
DISCLAIMER = (
    "⚠️ 안내: 본 프로그램은 교육 및 실습용으로 제작된 간이 체험 프로그램이며, "
    "과학적 타당성이 검증된 공식 MBTI 진단 도구가 아닙니다."
)

# 12문항 데이터 (지표별 각 3문항)
QUESTIONS = [
    # --- E / I 지표 (문항 1 ~ 3) ---
    {
        "id": 1,
        "dimension": "EI",
        "text": "주말이나 휴일에 에너지를 충전하는 방식은?",
        "option_a": {"text": "친구들과 모임이나 파티에 참석해 활력을 얻는다.", "type": "E"},
        "option_b": {"text": "집에서 혼자 책을 읽거나 영화를 보며 조용히 쉰다.", "type": "I"}
    },
    {
        "id": 2,
        "dimension": "EI",
        "text": "새로운 사람들과 어울리는 자리에 갔을 때 나의 모습은?",
        "option_a": {"text": "먼저 말을 걸며 적극적으로 대화를 주도하는 편이다.", "type": "E"},
        "option_b": {"text": "주로 다른 사람들의 이야기를 경청하며 조용히 있는 편이다.", "type": "I"}
    },
    {
        "id": 3,
        "dimension": "EI",
        "text": "아이디어나 생각을 정리할 때 선호하는 방식은?",
        "option_a": {"text": "다른 사람들과 대화하며 말로 표현하면서 정리한다.", "type": "E"},
        "option_b": {"text": "혼자 골똘히 생각하며 머릿속으로 충분히 정리한다.", "type": "I"}
    },
    
    # --- S / N 지표 (문항 4 ~ 6) ---
    {
        "id": 4,
        "dimension": "SN",
        "text": "새로운 프로젝트나 과제를 시작할 때 나는?",
        "option_a": {"text": "구체적인 사실, 데이터, 현실적인 실행 방안부터 챙긴다.", "type": "S"},
        "option_b": {"text": "전체적인 가능성, 미래의 비전, 독창적인 아이디어부터 떠올린다.", "type": "N"}
    },
    {
        "id": 5,
        "dimension": "SN",
        "text": "길을 찾거나 설명을 들을 때 선호하는 방식은?",
        "option_a": {"text": "‘우체국을 지나 좌회전 후 100m’ 같은 구체적인 지표가 좋다.", "type": "S"},
        "option_b": {"text": "‘대략 저쪽 방향으로 큰 사거리 근처야’ 같은 전체적 감이 좋다.", "type": "N"}
    },
    {
        "id": 6,
        "dimension": "SN",
        "text": "영화를 보거나 책을 읽을 때 더 주목하는 부분은?",
        "option_a": {"text": "실제 일어날 법한 현실적인 이야기와 세부 묘사", "type": "S"},
        "option_b": {"text": "숨겨진 의미, 상징, 앞으로 전개될 독특한 상상력", "type": "N"}
    },

    # --- T / F 지표 (문항 7 ~ 9) ---
    {
        "id": 7,
        "dimension": "TF",
        "text": "친구가 고민을 털어놓으며 조언을 구할 때 나의 반응은?",
        "option_a": {"text": "객관적인 원인을 분석하고 해결책을 제시해 준다.", "type": "T"},
        "option_b": {"text": "먼저 친구의 감정에 공감하고 위로와 지지를 건넨다.", "type": "F"}
    },
    {
        "id": 8,
        "dimension": "TF",
        "text": "중요한 결정을 내려야 할 때 가장 중요하게 생각하는 것은?",
        "option_a": {"text": "논리적 타당성, 효율성, 그리고 객관적인 원칙", "type": "T"},
        "option_b": {"text": "주위 사람들에 미치는 영향, 조화, 그리고 인간관계", "type": "F"}
    },
    {
        "id": 9,
        "dimension": "TF",
        "text": "평가나 피드백을 주고받을 때 선호하는 태도는?",
        "option_a": {"text": "감정을 배제하고 사실 위주로 정확하게 짚어주는 것", "type": "T"},
        "option_b": {"text": "상대방의 기분이 상하지 않게 부드럽고 배려 있게 전달하는 것", "type": "F"}
    },

    # --- J / P 지표 (문항 10 ~ 12) ---
    {
        "id": 10,
        "dimension": "JP",
        "text": "여행을 떠날 때 나의 계획 스타일은?",
        "option_a": {"text": "시간대별로 철저하게 일정을 짜고 계획대로 움직인다.", "type": "J"},
        "option_b": {"text": "대략적인 목적지만 정하고 현지 상황에 따라 유연하게 움직인다.", "type": "P"}
    },
    {
        "id": 11,
        "dimension": "JP",
        "text": "마감이나 과제가 주어졌을 때 일하는 방식은?",
        "option_a": {"text": "미리미리 여유 있게 계획을 세워 끝마치는 편이다.", "type": "J"},
        "option_b": {"text": "마감 직전에 집중력을 발휘해 몰아치는 편이다.", "type": "P"}
    },
    {
        "id": 12,
        "dimension": "JP",
        "text": "내 방이나 책상의 정리 정돈 상태는?",
        "option_a": {"text": "물건마다 제자리가 있고 깔끔하게 정돈되어 있다.", "type": "J"},
        "option_b": {"text": "필요할 때 찾을 수만 있다면 약간 어지러워도 괜찮다.", "type": "P"}
    },
]

# 응답에 대한 간단한 설명. 사람의 능력이나 성격을 단정하지 않습니다.
from itertools import product
_HINTS = {"E":"사람들과 이야기하며 에너지를 얻는 선택", "I":"혼자 조용히 쉬는 선택",
          "S":"구체적인 사실을 살피는 선택", "N":"가능성과 의미를 생각하는 선택",
          "T":"논리와 기준을 먼저 살피는 선택", "F":"감정과 관계를 먼저 살피는 선택",
          "J":"미리 계획하는 선택", "P":"상황에 유연하게 대응하는 선택"}
DESCRIPTIONS = {"".join(t): "이번 응답에서는 " + ", ".join(_HINTS[x] for x in t) + "이 상대적으로 많았습니다. 상황에 따라 응답은 달라질 수 있습니다."
                for t in product("EI", "SN", "TF", "JP")}

def calculate_mbti(answers: dict[int, str]) -> tuple[str, dict[str, int]]:
    """
    사용자의 응답(answers)을 바탕으로 지표별 점수를 집계하고 MBTI 유형을 반환합니다.
    answers: {문항ID: 'A' 또는 'B'}
    """
    if set(answers) != {q["id"] for q in QUESTIONS} or any(v not in ("A", "B") for v in answers.values()):
        raise ValueError("12개 문항에 A 또는 B로 모두 응답해야 합니다.")
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    for q in QUESTIONS:
        qid = q["id"]
        if qid in answers:
            choice = answers[qid]
            if choice == "A":
                chosen_type = q["option_a"]["type"]
            elif choice == "B":
                chosen_type = q["option_b"]["type"]
            else:
                continue
            
            if chosen_type in scores:
                scores[chosen_type] += 1

    # 지표별 우세 성향 판정 (동점일 경우 앞선 알파벳 우선 등 기본 처리)
    e_i = "E" if scores["E"] >= scores["I"] else "I"
    s_n = "S" if scores["S"] >= scores["N"] else "N"
    t_f = "T" if scores["T"] >= scores["F"] else "F"
    j_p = "J" if scores["J"] >= scores["P"] else "P"

    mbti_type = f"{e_i}{s_n}{t_f}{j_p}"
    return mbti_type, scores
