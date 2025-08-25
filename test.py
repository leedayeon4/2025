import streamlit as st
import time

st.title("📚 맞춤형 학습 계획표 생성기")

# 입력값 받기
기간 = st.text_input("학습 기간을 입력하세요 (예: 2주)")
목표 = st.text_input("학습 목표를 입력하세요 (예: 수학 개념 완성)")
계획 = st.text_area("학습 계획을 구체적으로 작성하세요 (예: 매일 2시간 학습)")
과목 = st.multiselect(
    "학습 과목을 선택하세요", 
    ["국어", "수학", "영어", "과학", "사회", "기타"]
)

# 타이머 설정
타이머_분 = st.number_input("타이머 설정 (분 단위)", min_value=1, max_value=120, value=10)
타이머_초 = 타이머_분 * 60

# 학습 계획표 생성 버튼
if st.button("학습 계획표 생성하기"):
    st.subheader("📌 나만의 학습 계획표")
    st.write("📅 선택한 기간:", 기간)
    st.write("🎯 목표:", 목표)
    st.write("📝 계획:", 계획)
    st.write("📚 학습 과목:", 과목)

    # 결과 이미지 출력
    st.image("study.jpg", caption="열공 모드 ON!", use_column_width=True)

# 타이머 실행 버튼
if st.button("⏱️ 타이머 시작"):
    st.write(f"타이머 시작: {타이머_분}분 동안 집중하세요!")
    timer_placeholder = st.empty()

    for remaining in range(타이머_초, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"### ⏳ 남은 시간: {mins:02d}:{secs:02d}")
        time.sleep(1)

    timer_placeholder.markdown("### ✅ 타이머 종료! 수고하셨습니다 🎉")



 
