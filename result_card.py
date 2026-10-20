"""사용자 사진과 질문 응답 결과를 로컬 PNG로 만듭니다."""
import warnings
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from mbti_core import calculate_mbti, DESCRIPTIONS

Image.MAX_IMAGE_PIXELS = 24_000_000
BG, INK = '#f5f3eb', '#214e43'


def load_profile(path):
    if Path(path).stat().st_size > 20 * 1024 * 1024:
        raise ValueError('20MB 이하의 사진을 선택해 주세요.')
    with warnings.catch_warnings():
        warnings.simplefilter('error', Image.DecompressionBombWarning)
        with Image.open(path) as source:
            if source.format not in ('JPEG', 'PNG', 'WEBP'):
                raise ValueError('JPG, PNG, WEBP 사진을 선택해 주세요.')
            source.load()
            image = ImageOps.exif_transpose(source).convert('RGBA')
            image.thumbnail((1200, 1200))
            flat = Image.new('RGB', image.size, BG)
            flat.paste(image, mask=image.getchannel('A'))
            return flat


def font(size, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf' if bold else 'C:/Windows/Fonts/malgun.ttf', size)


def wrap(draw, text, face, width):
    lines, line = [], ''
    for char in text:
        if draw.textlength(line + char, font=face) > width:
            lines.append(line)
            line = char
        else:
            line += char
    if line:
        lines.append(line)
    return lines


def make_card(answers, photo=None):
    result, scores = calculate_mbti(answers)
    card = Image.new('RGB', (900, 1100), BG)
    draw = ImageDraw.Draw(card)
    draw.text((54, 35), '나의 성향 체험 카드', fill=INK, font=font(40, True))
    if photo is not None:
        portrait = ImageOps.contain(photo, (792, 320))
        card.paste(portrait, ((900 - portrait.width) // 2, 105 + (320 - portrait.height) // 2))
    else:
        draw.rounded_rectangle((54, 105, 846, 425), radius=20, fill='#e0e9e3')
        draw.text((300, 235), '사진 없이 만든 카드', fill=INK, font=font(28))
    draw.text((54, 448), result, fill=INK, font=font(90, True))
    draw.text((370, 490), '12문항 응답 기반 결과', fill=INK, font=font(28))
    for i, (a, b) in enumerate(['EI', 'SN', 'TF', 'JP']):
        y = 575 + i * 55
        draw.text((54, y), f'{a} {scores[a]}점   /   {b} {scores[b]}점', fill=INK, font=font(28))
        draw.rounded_rectangle((400, y + 8, 846, y + 30), radius=10, fill='#dce5de')
        width = round(446 * scores[a] / 3)
        if width:
            draw.rounded_rectangle((400, y + 8, 400 + width, y + 30), radius=10, fill='#478c75')
    for i, line in enumerate(wrap(draw, DESCRIPTIONS[result], font(27), 792)):
        draw.text((54, 810 + i * 40), line, fill=INK, font=font(27))
    draw.line((54, 1005, 846, 1005), fill='#c5d2ca', width=2)
    draw.text((54, 1020), '사진은 꾸미기용 · 결과는 질문 응답으로만 계산', fill=INK, font=font(24))
    draw.text((54, 1056), '학습용 성향 체험이며 공식 MBTI 검사가 아닙니다.', fill=INK, font=font(23))
    return card


def save_card(card, path):
    card.save(path, format='PNG')  # 새 이미지에는 원본 사진의 EXIF가 포함되지 않음
