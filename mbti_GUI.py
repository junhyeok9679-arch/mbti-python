# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from mbti_core import QUESTIONS, DISCLAIMER, DESCRIPTIONS, calculate_mbti

from photo_ui import PhotoCardMixin

class MBTIApp(PhotoCardMixin):
    def __init__(self, root):
        self.root = root
        self.root.title("MBTI 성향 체험 프로그램 (실습용)")
        self.root.geometry("760x820")
        self.root.resizable(True, True)
        self.root.minsize(680, 780)

        self.current_index = 0
        self.photo = None
        self.card_image = None
        self.photo_preview = None
        self.result_preview = None
        self.answers = {} # {question_id: 'A' 또는 'B'} 저장 딕셔너리

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        # 상단 안내 레이블 (디스클레이머)
        self.top_frame = tk.Frame(self.root, bg="#f8d7da", padx=10, pady=8)
        self.top_frame.pack(fill=tk.X)
        
        self.lbl_disclaimer = tk.Label(
            self.top_frame, 
            text=DISCLAIMER, 
            font=("맑은 고딕", 9, "bold"), 
            fg="#721c24", 
            bg="#f8d7da", 
            wraplength=580,
            justify="center"
        )
        self.lbl_disclaimer.pack()

        # 메인 콘텐츠 프레임
        self.content_frame = tk.Frame(self.root, padx=25, pady=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        self.lbl_progress = tk.Label(self.content_frame, text="", font=("맑은 고딕", 10, "bold"), fg="#555")
        self.lbl_progress.pack(anchor="w", pady=(0, 10))

        self.lbl_question = tk.Label(self.content_frame, text="", font=("맑은 고딕", 12, "bold"), wraplength=560, justify="left")
        self.lbl_question.pack(anchor="w", pady=(0, 20))

        self.selected_option = tk.StringVar(value="")

        self.rb_a = tk.Radiobutton(
            self.content_frame, 
            text="", 
            variable=self.selected_option, 
            value="A", 
            font=("맑은 고딕", 11),
            wraplength=540,
            justify="left",
            pady=8
        )
        self.rb_a.pack(anchor="w", fill=tk.X, pady=5)

        self.rb_b = tk.Radiobutton(
            self.content_frame, 
            text="", 
            variable=self.selected_option, 
            value="B", 
            font=("맑은 고딕", 11),
            wraplength=540,
            justify="left",
            pady=8
        )
        self.rb_b.pack(anchor="w", fill=tk.X, pady=5)

        # 하단 네비게이션 버튼 프레임
        self.nav_frame = tk.Frame(self.root, padx=25, pady=15, bg="#e9ecef")
        self.nav_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.btn_prev = tk.Button(self.nav_frame, text="◀ 이전", font=("맑은 고딕", 10), width=10, command=self.prev_question, state=tk.DISABLED)
        self.btn_prev.pack(side=tk.LEFT)

        self.btn_next = tk.Button(self.nav_frame, text="다음 ▶", font=("맑은 고딕", 10, "bold"), width=12, command=self.next_question, bg="#007bff", fg="white")
        self.btn_next.pack(side=tk.RIGHT)
        self.add_photo_controls()

    def load_question(self):
        if self.current_index < len(QUESTIONS):
            q = QUESTIONS[self.current_index]
            self.lbl_progress.config(text=f"문항 {self.current_index + 1} / {len(QUESTIONS)}  (지표: {q['dimension']})")
            self.lbl_question.config(text=q["text"])
            self.rb_a.config(text=f"A. {q['option_a']['text']}")
            self.rb_b.config(text=f"B. {q['option_b']['text']}")

            # 기존에 응답한 기록이 있다면 라디오버튼에 복원, 없으면 빈 값으로 초기화
            qid = q["id"]
            if qid in self.answers:
                self.selected_option.set(self.answers[qid])
            else:
                self.selected_option.set("")

            # 이전 버튼 활성화/비활성화 처리
            if self.current_index == 0:
                self.btn_prev.config(state=tk.DISABLED)
            else:
                self.btn_prev.config(state=tk.NORMAL)

            # 마지막 문항일 때 버튼 문구 변경
            if self.current_index == len(QUESTIONS) - 1:
                self.btn_next.config(text="결과 보기 ✨", bg="#28a745")
            else:
                self.btn_next.config(text="다음 ▶", bg="#007bff")
        else:
            self.show_result()

    def save_current_answer(self):
        val = self.selected_option.get()
        if val:
            q = QUESTIONS[self.current_index]
            self.answers[q["id"]] = val
            return True
        return False

    def next_question(self):
        if not self.save_current_answer():
            messagebox.showwarning("선택 필요", "보기를 선택해 주세요!")
            return
        
        self.current_index += 1
        self.load_question()

    def prev_question(self):
        # 현재 화면의 응답이 선택되어 있다면 임시 저장
        val = self.selected_option.get()
        if val:
            q = QUESTIONS[self.current_index]
            self.answers[q["id"]] = val

        if self.current_index > 0:
            self.current_index -= 1
            self.load_question()

    def restart(self):
        self.current_index = 0
        self.answers.clear()
        self.card_image = None
        self.result_preview = None
        
        # 화면 초기화 후 재구성
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.create_widgets()
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MBTIApp(root)
    root.mainloop()
