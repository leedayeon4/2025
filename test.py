import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="🎀 귀여운 학습 계획표", layout="wide")
st.markdown("<h1 style='text-align: center; color: #ff6f91;'>🎀 맞춤형 학습 계획표 생성기 🎀</h1>", unsafe_allow_html=True)

# -----------------------------
# 1️⃣ 학습 기간, 기관, 목표 선택
# -----------------------------
기간 = st.selectbox(
    "🗓 학습 기간 선택",
    ["1주", "2주", "3주", "4주", "5주", "6주", "7주", "8주"]
)

학습기관 = st.selectbox(
    "🏫 학습 기관 선택",
    ["학교", "학원", "온라인 강의", "자율 학습", "독서실", "스터디 그룹", "개인 과외", "e-learning 플랫폼"]
)

목표 = st.selectbox(
    "🎯 학습 목표 선택",
    ["개념 완성", "문제풀이 집중", "복습", "시험 대비", "자기계발", "포트폴리오 준비", "어휘/암기", "프로젝트 학습"]
)

계획 = st.text_area("✏️ 구체적인 학습 계획 작성 (예: 매일 2시간 학습)", "")

과목 = st.multiselect(
    "📚 학습 과목 선택",
    ["국어", "수학", "영어", "과학", "사회", "역사", "예체능", "자율학습", "코딩", "독서", "기타"]
)

# -----------------------------
# 2️⃣ 결과 이미지 업로드
# -----------------------------
photo = st.file_uploader("📸 결과에 넣을 이미지 선택 (선택)", type=["jpg", "jpeg", "png"])

# -----------------------------
# 3️⃣ 학습 계획표 생성 (귀여운 스타일)
# -----------------------------
if st.button("✅ 학습 계획표 생성하기"):
    st.subheader("📌 나만의 귀여운 학습 계획표")

    # 기본 정보 출력
    st.markdown(f"💖 **기간:** {기간}  |  🏫 **학습 기관:** {학습기관}  |  🎯 **목표:** {목표}")
    st.markdown(f"📝 **계획:** {계획}")
    st.markdown(f"📚 **과목:** {', '.join(과목)}")

    # 결과 이미지 표시
    if photo:
        st.image(photo, caption="열공 모드 ON! ✨", use_column_width=True)
    else:
        st.info("이미지를 업로드하면 계획표 아래에 표시됩니다.")

    # 귀여운 테이블 생성
    plan_data = []
    today = datetime.date.today()
    for i, sub in enumerate(과목):
        plan_data.append({
            "📅 날짜": today + datetime.timedelta(days=i),
            "📖 과목": sub,
            "⏰ 공부 시간": "2시간",
            "💡 메모": "집중 집중!"
        })
    df = pd.DataFrame(plan_data)

    # 테이블 스타일링
    def style_table(df):
        return df.style.set_properties(**{
            'background-color': '#ffe6f0',
            'color': '#d6336c',
            'border-color': '#ffb3c1',
            'font-size': '16px',
            'text-align': 'center'
        }).set_table_styles([{
            'selector': 'th',
            'props': [('background-color', '#ffb3c1'), ('color', 'white'), ('font-size', '16px')]
        }])

    st.table(style_table(df))

# -----------------------------
# 4️⃣ 공부 타이머 (Streamlit-friendly)
# -----------------------------
st.subheader("⏱️ 공부 타이머")
minutes = st.number_input("타이머 설정 (분 단위)", min_value=1, max_value=180, value=25, step=1)
start_timer = st.button("▶️ 타이머 시작")

timer_placeholder = st.empty()

if start_timer:
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    while True:
        remaining = end_time - datetime.datetime.now()
        if remaining.total_seconds() <= 0:
            timer_placeholder.markdown("### ✅ 타이머 종료! 수고하셨습니다 🎉")
            break
        else:
            mins, secs = divmod(int(remaining.total_seconds()), 60)
            timer_placeholder.markdown(f"### ⏳ 남은 시간: {mins:02d}:{secs:02d}")



 
