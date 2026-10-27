"""수업 5번: 본인 GitHub 저장소를 복제해 실행하는 로컬 웹앱."""
import io
import warnings
import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError
from mbti_core import QUESTIONS, DESCRIPTIONS, calculate_mbti
from result_card import make_card

st.set_page_config(page_title='나의 MBTI 성향 카드', page_icon='🌿', layout='centered')
st.title('나의 MBTI 성향 카드')
st.write('12개의 질문에 답하고, 내 사진을 넣은 결과 카드를 만들어 보세요.')
st.info('사진은 카드 꾸미기용입니다. 결과는 질문 응답으로만 계산하며 공식 MBTI 검사가 아닙니다.')
st.caption('사진과 응답은 이 컴퓨터의 로컬 서버에서만 처리하며 외부 서비스로 전송하지 않습니다.')


def decode_photo(data):
    if len(data) > 20 * 1024 * 1024:
        raise ValueError('20MB 이하의 사진을 선택해 주세요.')
    with warnings.catch_warnings():
        warnings.simplefilter('error', Image.DecompressionBombWarning)
        with Image.open(io.BytesIO(data)) as source:
            if source.format not in ('JPEG', 'PNG', 'WEBP'):
                raise ValueError('JPG, PNG, WEBP 사진을 선택해 주세요.')
            source.load()
            image = ImageOps.exif_transpose(source).convert('RGBA')
            image.thumbnail((1200, 1200))
            flat = Image.new('RGB', image.size, '#f5f3eb')
            flat.paste(image, mask=image.getchannel('A'))
            return flat


upload = st.file_uploader('프로필 사진 선택 (선택 사항)', type=['jpg', 'jpeg', 'png', 'webp'])
photo = None
if upload is not None:
    try:
        photo = decode_photo(upload.getvalue())
        st.image(photo, caption='카드에 들어갈 사진', width=180)
    except (OSError, ValueError, UnidentifiedImageError, Image.DecompressionBombError,
            Image.DecompressionBombWarning) as error:
        st.error(f'사진을 열 수 없습니다: {error}')
        st.stop()


def reset_answers():
    st.session_state.pop('submitted_answers', None)
    for q in QUESTIONS:
        st.session_state.pop(f'q{q["id"]}', None)


st.button('응답 다시 시작 (사진 유지)', on_click=reset_answers)
with st.form('questions'):
    answers = {}
    for q in QUESTIONS:
        answers[q['id']] = st.radio(
            f'{q["id"]}. {q["text"]}', ['A', 'B'], index=None,
            format_func=lambda value, question=q: question['option_a' if value == 'A' else 'option_b']['text'],
            key=f'q{q["id"]}')
    submitted = st.form_submit_button('결과 카드 만들기', type='primary')

if submitted:
    if any(v is None for v in answers.values()):
        st.session_state.pop('submitted_answers', None)
        st.warning('12문항에 모두 답해 주세요. 아직 답하지 않은 문항이 있습니다.')
    else:
        st.session_state['submitted_answers'] = answers.copy()

if 'submitted_answers' in st.session_state:
    result_answers = st.session_state['submitted_answers']
    result, scores = calculate_mbti(result_answers)
    st.divider()
    st.subheader(f'나의 응답 결과: {result}')
    st.caption('마지막으로 제출한 응답의 결과입니다. 답을 바꿨다면 결과 카드 만들기를 다시 눌러 주세요.')
    st.write(DESCRIPTIONS[result])
    for a, b in ['EI', 'SN', 'TF', 'JP']:
        st.write(f'{a}: {scores[a]}점 / {b}: {scores[b]}점')
    card = make_card(result_answers, photo)
    st.image(card, caption='사진과 질문 응답을 합친 결과 카드', width=450)
    output = io.BytesIO()
    card.save(output, format='PNG')
    st.download_button('결과 카드 PNG 저장', output.getvalue(),
                       file_name=f'MBTI_{result}_결과카드.png', mime='image/png')
