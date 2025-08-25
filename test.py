import streamlit as st
import pandas as pd

# -------------------------------
# 🎨 Custom CSS (디자인 꾸미기)
# -------------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #89f7fe, #66a6ff);
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #34495e;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #ff7675;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #d63031;
    }
    .download-btn {
        background-color: #6c5ce7;
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🎯 제목
# -------------------------------
st.markdown('<div class="title">📚 스마트 학습 계획표 생성기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">나에게 맞는 맞춤형 학습 계획을 세워보세요!</div>', unsafe_allow_html=True)

# -------------------------------
# 📝 입력값 설정
# -------------------------------
st.sidebar.header("📌 입력 옵션")

subjects = st.sidebar.multiselect(
    "과목을 선택하세요:",
    ["국어", "영어", "수학", "과학", "사회", "제2외국어", "예체능", "자율학습", "독서", "코딩", "기타"]
)

days = st.sidebar.multiselect(
    "학습 요일 선택:",
    ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
)

hours_per_day = st.sidebar.slider("하루 공부 시간 (시간)", 1, 10, 3)

study_style = st.sidebar.radio(
    "학습 스타일을 선택하세요:",
    ["집중형 (한 과목에 몰입)", "분산형 (여러 과목 조금씩)", "복습중심형 (짧은 복습 반복)"]
)

output_format = st.sidebar.radio(
    "결과 화면 형식:",
    ["표 (Table)", "리스트 (List)", "캘린더형 (Calendar)"]
)

# -------------------------------
# 📊 계획표 생성 함수
# -------------------------------
def generate_plan(subjects, days, hours, style):
    plan = []
    if not subjects or not days:
        return pd.DataFrame(columns=["요일", "시간", "과목", "학습 내용"])

    for d in days:
        if style == "집중형 (한 과목에 몰입)":
            for h in range(1, hours+1):
                plan.append([d, f"{h}시간차", subjects[h % len(subjects)], "집중 학습"])
        elif style == "분산형 (여러 과목 조금씩)":
            for h in range(1, hours+1):
                plan.append([d, f"{h}시간차", subjects[(h-1) % len(subjects)], "분산 학습"])
        elif style == "복습중심형 (짧은 복습 반복)":
            for h in range(1, hours+1):
                plan.append([d, f"{h}시간차", subjects[(h-1) % len(subjects)], "복습 및 점검"])

    return pd.DataFrame(plan, columns=["요일", "시간", "과목", "학습 내용"])

# -------------------------------
# 🚀 실행 버튼
# -------------------------------
if st.sidebar.button("✅ 학습 계획표 생성하기"):
    df = generate_plan(subjects, days, hours_per_day, study_style)

    if df.empty:
        st.warning("⚠️ 과목과 요일을 선택해주세요!")
    else:
        st.success("✨ 학습 계획표가 생성되었습니다!")

        # -------------------------------
        # 🖼️ 출력 형식 선택
        # -------------------------------
        if output_format == "표 (Table)":
            st.dataframe(df, use_container_width=True)
        elif output_format == "리스트 (List)":
            for i, row in df.iterrows():
                st.write(f"📌 {row['요일']} | {row['시간']} → {row['과목']} ({row['학습 내용']})")
        elif output_format == "캘린더형 (Calendar)":
            st.markdown("### 🗓️ 주간 학습 캘린더")
            pivot = df.pivot(index="시간", columns="요일", values="과목").fillna("")
            st.table(pivot)

        # -------------------------------
        # 💾 다운로드 버튼
        # -------------------------------
        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "📥 CSV로 다운로드",
            csv,
            "학습계획표.csv",
            "text/csv",
            key="download-csv"
        )


 
