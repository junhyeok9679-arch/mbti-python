# -*- coding: utf-8 -*-
from mbti_core import QUESTIONS, DISCLAIMER, DESCRIPTIONS, calculate_mbti

def main():
    print("=" * 65)
    print("           MBTI 성향 체험 프로그램 (콘솔 버전)           ")
    print("=" * 65)
    print(DISCLAIMER)
    print("=" * 65)
    print("각 문항을 읽고 자신에게 더 가까운 보기를 선택해 주세요 (A 또는 B).\n")

    answers = {}
    for q in QUESTIONS:
        print(f"[문항 {q['id']} / 12] (지표: {q['dimension']})")
        print(f"Q. {q['text']}")
        print(f"  [A] {q['option_a']['text']}")
        print(f"  [B] {q['option_b']['text']}")
        
        while True:
            ans = input("선택 (A/B): ").strip().upper()
            if ans in ["A", "B"]:
                answers[q["id"]] = ans
                break
            print("⚠️ 잘못된 입력입니다. 'A' 또는 'B'를 입력해주세요.")
        print("-" * 55)

    # 결과 계산
    mbti_type, scores = calculate_mbti(answers)
    
    print("\n" + "=" * 65)
    print(" 📊 진단 결과 요약 ")
    print("=" * 65)
    print(DISCLAIMER)
    print(f"\n당신의 체험용 MBTI 유형은: 【 {mbti_type} 】 입니다!\n")
    
    print("지표별 점수 현황:")
    print(f" • 외향(E): {scores['E']} 점  vs  내향(I): {scores['I']} 점")
    print(f" • 감각(S): {scores['S']} 점  vs  직관(N): {scores['N']} 점")
    print(f" • 사고(T): {scores['T']} 점  vs  감정(F): {scores['F']} 점")
    print(f" • 판단(J): {scores['J']} 점  vs  인식(P): {scores['P']} 점")
    
    desc = DESCRIPTIONS.get(mbti_type, "설명이 없는 유형입니다.")
    print(f"\n[유형 해설]")
    print(f" {desc}")
    print("=" * 65)

if __name__ == "__main__":
    main()
