# study_planner.py

import streamlit as st
import pandas as pd
from datetime import date, timedelta

# 앱 제목
st.title("📚 나만의 학습 계획표 만들기")

# 사이드바에서 설정
st.sidebar.header("📌 계획 설정")

# 학습 기간 입력
start_date = st.sidebar.date_input("시작 날짜", date.today())
end_date = st.sidebar.date_input("종료 날짜", date.today() + timedelta(days=7))

# 과목 입력
subjects = st.sidebar.text_area("과목 입력 (줄바꿈으로 구분)", "국어\n수학\n영어\n과학\n사회")
subject_list = [s.strip() for s in subjects.split("\n") if s.strip()]

# 하루 공부 시간
study_hours = st.sidebar.slider("하루 공부 시간 (시간)", 1, 12, 5)

# 결과 출력 형식 선택
output_type = st.sidebar.radio("결과 화면 형식 선택", ["표로 보기", "리스트로 보기"])

# 버튼
if st.sidebar.button("계획표 생성하기"):
    # 날짜 생성
    days = pd.date_range(start_date, end_date)

    # 과목 분배 (단순 반복 분배)
    plan = []
    idx = 0
    for d in days:
        daily_subjects = []
        for h in range(study_hours):
            daily_subjects.append(subject_list[idx % len(subject_list)])
            idx += 1
        plan.append([d.date()] + daily_subjects)

    # DataFrame 생성
    columns = ["날짜"] + [f"{i+1}교시" for i in range(study_hours)]
    df = pd.DataFrame(plan, columns=columns)

    st.success("✅ 학습 계획표가 생성되었습니다!")

    # 결과 화면 선택
    if output_type == "표로 보기":
        st.dataframe(df)
    else:
        for i, row in df.iterrows():
            st.markdown(f"### 📅 {row['날짜']}")
            for j in range(1, study_hours + 1):
                st.write(f"{j}교시: {row[j]}")
            st.markdown("---")

    # CSV 저장 버튼
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "📥 계획표 다운로드 (CSV)",
        data=csv,
        file_name="학습계획표.csv",
        mime="text/csv",
    )


 
