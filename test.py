import streamlit as st
import pandas as pd
import datetime
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="학습 계획 자동 생성기", layout="wide")

st.title("📚 학습 계획 자동 생성기")

# -------------------------------
# 사용자 입력 (사이드바)
# -------------------------------
st.sidebar.header("📌 기본 설정")

exam_date = st.sidebar.date_input("시험 날짜를 선택하세요", datetime.date.today() + datetime.timedelta(days=10))
days_left = (exam_date - datetime.date.today()).days
study_hours = st.sidebar.number_input("하루 공부 가능 시간(시간)", min_value=1, max_value=24, value=4)
max_subjects = st.sidebar.number_input("하루 최대 공부 과목 수", min_value=1, max_value=10, value=3)

st.sidebar.write(f"시험일까지 {days_left}일 남음")

# -------------------------------
# 과목 입력
# -------------------------------
st.sidebar.header("📘 과목 추가")
subject_data = []

with st.sidebar.form("subject_form", clear_on_submit=True):
    subject = st.text_input("과목명 (예: 수학)")
    total_range = st.number_input("학습 범위 (예: 문제 수/쪽수)", min_value=1, value=50)
    importance = st.slider("중요도 (1=낮음, 5=높음)", 1, 5, 3)
    difficulty = st.selectbox("난이도", ["쉬움", "보통", "어려움"])
    repeat = st.number_input("반복 횟수", min_value=1, value=1)

    submitted = st.form_submit_button("추가하기")
    if submitted and subject:
        subject_data.append({
            "과목": subject,
            "범위": total_range,
            "중요도": importance,
            "난이도": difficulty,
            "반복": repeat
        })

# 세션에 저장 (리셋 방지)
if "subjects" not in st.session_state:
    st.session_state.subjects = []
if subject_data:
    st.session_state.subjects.extend(subject_data)

# -------------------------------
# 계획 생성
# -------------------------------
if st.session_state.subjects:
    st.header("📅 생성된 학습 계획")

    df = pd.DataFrame(st.session_state.subjects)

    # 난이도 가중치 설정
    difficulty_weights = {"쉬움": 0.8, "보통": 1.0, "어려움": 1.2}

    # 각 과목의 총 가중치 계산
    df["가중치"] = df["중요도"] * df["범위"] * df["반복"] * df["난이도"].map(difficulty_weights)

    # 전체 가중치 대비 각 과목 비율
    df["비율"] = df["가중치"] / df["가중치"].sum()

    # 하루 전체 학습량 = 하루 공부 가능 시간 × 60 (분 단위)
    total_minutes_per_day = study_hours * 60

    # 각 과목 분배 (분 단위)
    df["일일 학습 시간(분)"] = df["비율"] * total_minutes_per_day

    # 일자별 계획표 생성
    schedule = []
    for day in range(1, days_left + 1):
        today_date = datetime.date.today() + datetime.timedelta(days=day)
        today_plan = {"날짜": today_date}
        subjects_today = df.sample(min(len(df), max_subjects))  # 랜덤으로 최대 과목 수만큼 배정
        for _, row in subjects_today.iterrows():
            amount = math.ceil(row["범위"] / days_left)  # 균등 분배
            today_plan[row["과목"]] = f"{amount} 단위 ({int(row['일일 학습 시간(분)'])}분)"
        schedule.append(today_plan)

    schedule_df = pd.DataFrame(schedule)

    # -------------------------------
    # 결과 화면 형식 선택
    # -------------------------------
    st.header("📌 결과 화면 형식 선택")
    view_mode = st.radio(
        "결과 표시 방식을 선택하세요",
        ("표 형식", "시간표 형식", "그래프 중심")
    )

    # -------------------------------
    # 출력 분기
    # -------------------------------
    if view_mode == "표 형식":
        st.subheader("✅ 오늘의 공부 계획")
        st.write(schedule_df.iloc[0])

        st.subheader("📊 전체 학습 일정표")
        st.dataframe(schedule_df, use_container_width=True)

    elif view_mode == "시간표 형식":
        st.subheader("🗓️ 시간표 스타일")
        timetable = []
        for day in range(1, days_left + 1):
            today_date = datetime.date.today() + datetime.timedelta(days=day)
            subjects_today = df.sample(min(len(df), max_subjects))
            slots = ["오전", "오후", "저녁"]
            day_plan = {"날짜": today_date}
            for i, (_, row) in enumerate(subjects_today.iterrows()):
                day_plan[slots[i % len(slots)]] = f"{row['과목']} - {math.ceil(row['범위']/days_left)} 단위"
            timetable.append(day_plan)
        st.dataframe(pd.DataFrame(timetable), use_container_width=True)

    elif view_mode == "그래프 중심":
        st.subheader("📈 과목별 학습 비율")
        fig, ax = plt.subplots()
        ax.pie(df["비율"], labels=df["과목"], autopct="%1.1f%%")
        st.pyplot(fig)

        st.subheader("📉 과목별 일일 학습 시간 (분)")
        st.bar_chart(df.set_index("과목")["일일 학습 시간(분)"])

    # -------------------------------
    # 다운로드 버튼
    # -------------------------------
    st.download_button(
        label="📥 학습 계획표 다운로드 (CSV)",
        data=schedule_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="study_schedule.csv",
        mime="text/csv"
    )
else:
    st.info("왼쪽 사이드바에서 과목을 추가해주세요!")


 
