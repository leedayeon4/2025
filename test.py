import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="학습 계획표 웹앱", layout="wide")
st.title("📚 맞춤형 학습 계획표 생성기")

# -----------------------------
# 1️⃣ 학습 기간, 기관, 목표 선택 (다양화)
# -----------------------------
기간 = st.selectbox(
    "학습 기간 선택",
    ["1주", "2주", "3주", "4주", "5주", "6주", "7주", "8주"]
)

학습기관 = st.selectbox(
    "학습 기관 선택",
    ["학교", "학원", "온라인 강의", "자율 학습", "독서실", "스터디 그룹", "개인 과외", "e-learning 플랫폼"]
)

목표 = st.selectbox(
    "학습 목표 선택",
    ["개념 완성", "문제풀이 집중", "복습", "시험 대비", "자기계발", "포트폴리오 준비", "어휘/암기", "프로젝트 학습"]
)

계획 = st.text_area("구체적인 학습 계획 작성 (예: 매일 2시간 학습)", "")

과목 = st.multiselect(
    "학습 과목 선택",
    ["국어", "수학", "영어", "과학", "사회", "역사", "예체능", "자율학습", "코딩", "독서", "기타"]
)

# -----------------------------
# 2️⃣ 결과 이미지 업로드
# -----------------------------
photo = st.file_uploader("📸 결과에 넣을 이미지 선택 (선택)", type=["jpg", "jpeg", "png"])

# -----------------------------
# 3️⃣ 학습 계획표 생성
# -----------------------------
if st.button("✅ 학습 계획표 생성하기"):
    st.subheader("📌 나만의 학습 계획표")
    st.write("📅 선택한 기간:", 기간)
    st.write("🏫 학습 기관:", 학습기관)
    st.write("🎯 학습 목표:", 목표)
    st.write("📝 계획:", 계획)
    st.write("📚 학습 과목:", 과목)

    # 결과 이미지 표시
    if photo:
        st.image(photo, caption="열공 모드 ON!", use_column_width=True)
    else:
        st.info("이미지를 업로드하면 계획표 아래에 표시됩니다.")

# -----------------------------
# 4️⃣ 공부 타이머 (Streamlit-friendly)
# -----------------------------
st.subheader("⏱️ 공부 타이머")
minutes = st.number_input("타이머 설정 (분 단위)", min_value=1, max_value=180, value=25, step=1)
start_timer = st.button("▶️ 타이머 시작")

# 타이머 표시용 placeholder
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


 
