import streamlit as st
import pandas as pd

# ----------------------------
# 데이터베이스 (간단 매핑)
# ----------------------------
career_db = {
    "심리": {
        "학과": ["심리학과", "상담학과", "아동가족학과"],
        "직업": ["임상심리사", "상담교사", "HR 전문가"]
    },
    "컴퓨터": {
        "학과": ["컴퓨터공학과", "소프트웨어학과", "데이터사이언스학과"],
        "직업": ["프로그래머", "데이터분석가", "AI 연구원"]
    },
    "예술": {
        "학과": ["미술학과", "음악학과", "공연예술학과"],
        "직업": ["화가", "음악가", "연극배우"]
    },
    "경제": {
        "학과": ["경제학과", "경영학과", "국제통상학과"],
        "직업": ["금융애널리스트", "기업컨설턴트", "무역전문가"]
    },
    "생명": {
        "학과": ["생명과학과", "생명공학과", "의학과"],
        "직업": ["연구원", "의사", "제약개발자"]
    },
    "교육": {
        "학과": ["교육학과", "유아교육과", "특수교육과"],
        "직업": ["교사", "교육컨설턴트", "교재개발자"]
    },
    "법": {
        "학과": ["법학과", "경찰행정학과", "국제법학과"],
        "직업": ["변호사", "판사", "경찰"]
    }
}

# ----------------------------
# Streamlit 앱 UI
# ----------------------------
st.set_page_config(page_title="진로 탐색기", page_icon="🎯", layout="wide")
st.title("🎯 진로 탐색기")
st.markdown("평소 관심 있는 키워드를 입력하면 관련 학과와 직업을 추천해드려요!")

# 사용자 입력
user_input = st.text_input("관심 분야를 입력하세요 (예: 심리, 컴퓨터, 예술, 경제, 생명, 교육, 법)")

if st.button("추천받기"):
    if user_input.strip() == "":
        st.warning("⚠️ 관심 키워드를 입력해주세요.")
    else:
        keyword = None
        for k in career_db.keys():
            if k in user_input:
                keyword = k
                break

        if keyword:
            data = career_db[keyword]
            st.subheader(f"🔎 '{keyword}' 분야 추천 결과")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 📚 추천 학과")
                for major in data["학과"]:
                    st.write("- ", major)
            with col2:
                st.markdown("### 💼 추천 직업")
                for job in data["직업"]:
                    st.write("- ", job)

            st.success("추천된 학과와 직업을 더 조사해보면서 진로를 탐색해 보세요!")
        else:
            st.info("관련 데이터가 없어요. 더 많은 키워드를 입력해보세요!")

