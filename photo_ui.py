"""기존 MBTI 질문 화면에 사진 선택과 결과 카드 기능을 연결합니다."""
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from result_card import load_profile, make_card, save_card


class PhotoCardMixin:
    def add_photo_controls(self):
        toolbar = tk.Frame(self.top_frame, bg='#f8d7da')
        toolbar.pack(pady=5)
        tk.Button(toolbar, text='프로필 사진 선택', command=self.choose_photo).pack(side='left', padx=5)
        tk.Button(toolbar, text='사진 지우기', command=self.clear_photo).pack(side='left', padx=5)
        self.photo_status = tk.Label(self.top_frame, bg='#f8d7da', font=('맑은 고딕', 9))
        self.photo_status.pack()
        self.update_photo_status()
        self.photo_label = tk.Label(self.content_frame)
        self.photo_label.pack(before=self.lbl_progress, pady=4)
        self.update_photo_preview()

    def update_photo_status(self):
        self.photo_status.config(text='사진 선택됨 · 이 컴퓨터에서만 처리합니다.' if self.photo is not None
                                else '사진은 선택 사항입니다. JPG·PNG·WEBP / 20MB 이하')

    def update_photo_preview(self):
        if not self.photo_label.winfo_exists():
            return
        if self.photo is None:
            self.photo_preview = None
            self.photo_label.config(image='', text='사진은 꾸미기용이며 결과 계산에 사용하지 않습니다.')
        else:
            image = self.photo.copy()
            image.thumbnail((140, 100))
            self.photo_preview = ImageTk.PhotoImage(image, master=self.root)
            self.photo_label.config(image=self.photo_preview, text='')

    def choose_photo(self):
        path = filedialog.askopenfilename(parent=self.root, title='프로필 사진 선택',
                                         filetypes=[('사진', '*.jpg *.jpeg *.png *.webp')])
        if not path:
            return
        try:
            photo = load_profile(path)
        except Exception as error:
            messagebox.showerror('사진을 열 수 없습니다', str(error), parent=self.root)
            return
        self.photo = photo
        self.update_photo_status()
        if self.card_image is not None:
            self.render_result_card()
        else:
            self.update_photo_preview()

    def clear_photo(self):
        self.photo = None
        self.update_photo_status()
        if self.card_image is not None:
            self.render_result_card()
        else:
            self.update_photo_preview()

    def show_result(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.nav_frame.destroy()
        self.card_label = tk.Label(self.content_frame)
        self.card_label.pack(expand=True)
        self.render_result_card()
        self.nav_frame = tk.Frame(self.root, padx=20, pady=12)
        self.nav_frame.pack(side='bottom', fill='x')
        tk.Button(self.nav_frame, text='카드 PNG 저장', command=self.export_card,
                  bg='#286c55', fg='white', padx=16).pack(side='left')
        tk.Button(self.nav_frame, text='다시 시작 (사진 유지)', command=self.restart).pack(side='right')

    def render_result_card(self):
        self.card_image = make_card(self.answers, self.photo)
        preview = self.card_image.copy()
        preview.thumbnail((410, 500))
        self.result_preview = ImageTk.PhotoImage(preview, master=self.root)
        self.card_label.config(image=self.result_preview)

    def export_card(self):
        path = filedialog.asksaveasfilename(parent=self.root, title='결과 카드 저장',
                    defaultextension='.png', initialfile='나의_MBTI_결과카드.png',
                    filetypes=[('PNG 이미지', '*.png')])
        if not path:
            return
        try:
            save_card(self.card_image, path)
        except OSError as error:
            return messagebox.showerror('저장 실패', str(error), parent=self.root)
        messagebox.showinfo('저장 완료', '사진과 결과가 담긴 카드를 저장했습니다.', parent=self.root)
