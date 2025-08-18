import streamlit as st

# 📚 MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": {
        "desc": "조용하지만 책임감 강한 관리자 💼",
        "jobs": ["공무원 🏛️", "회계사 📊", "군인 🪖", "경찰관 🚓"]
    },
    "ISFJ": {
        "desc": "따뜻하고 헌신적인 조력자 🌸",
        "jobs": ["간호사 🏥", "사회복지사 🤝", "초등교사 📚", "비서 📝"]
    },
    "INFJ": {
        "desc": "통찰력 있는 조언자 🔮",
        "jobs": ["심리상담사 🧠", "작가 ✍️", "교육 컨설턴트 🎓", "연구원 🔬"]
    },
    "INTJ": {
        "desc": "전략적인 사색가 🧠",
        "jobs": ["데이터 과학자 📈", "엔지니어 ⚙️", "경영 컨설턴트 💼", "의사 🩺"]
    },
    "ISTP": {
        "desc": "유연하고 현실적인 문제 해결자 🛠️",
        "jobs": ["정비사 🔧", "파일럿 ✈️", "소방관 🚒", "보안전문가 🛡️"]
    },
    "ISFP": {
        "desc": "예술적이고 감성적인 실용주의자 🎨",
        "jobs": ["디자이너 🖌️", "플로리스트 🌷", "사진작가 📸", "요리사 👨‍🍳"]
    },
    "INFP": {
        "desc": "이상적인 세상을 꿈꾸는 철학가 🌌",
        "jobs": ["시인 ✒️", "작곡가 🎼", "상담사 🧘", "작가 📖"]
    },
    "INTP": {
        "desc": "지적인 탐험가 🔍",
        "jobs": ["AI 개발자 🤖", "교수 👨‍🏫", "연구원 🔬", "프로그래머 👨‍💻"]
    },
    "ESTP": {
        "desc": "모험을 즐기는 현실주의자 🏍️",
        "jobs": ["기업가 💼", "스턴트맨 🎬", "스포츠 트레이너 🏋️", "세일즈맨 💬"]
    },
    "ESFP": {
        "desc": "삶을 즐기는 사교적인 연예인 🌟",
        "jobs": ["연예인 🎤", "방송인 📺", "이벤트 플래너 🎉", "뷰티 유튜버 💄"]
    },
    "ENFP": {
        "desc": "창의적이고 열정적인 활동가 🔥",
        "jobs": ["광고기획자 📢", "작가 📝", "영화감독 🎥", "사회운동가 ✊"]
    },
    "ENTP": {
        "desc": "논쟁을 즐기는 혁신가 ⚡",
        "jobs": ["스타트업 창업자 🚀", "기획자 📈", "변호사 ⚖️", "마케터 📊"]
    },
    "ESTJ": {
        "desc": "철저하고 조직적인 관리자 📋",
        "jobs": ["경영자 🏢", "군인 🪖", "회계사 📚", "현장감독 🏗️"]
    },
    "ESFJ": {
        "desc": "따뜻하고 친근한 헌신가 💕",
        "jobs": ["간호사 🏥", "초등교사 🧑‍🏫", "비서 📠", "식품영양사 🥗"]
    },
    "ENFJ": {
        "desc": "타인을 이끄는 카리스마 리더 🌟",
        "jobs": ["교육자 🎓", "강연가 🎤", "상담사 🧠", "사회운동가 ✊"]
    },
    "ENTJ": {
        "desc": "대담한 리더형 전략가 👑",
        "jobs": ["CEO 💼", "투자 전문가 💹", "경영 컨설턴트 🧑‍💼", "변호사 ⚖️"]
    },
}

# 🎨 Streamlit 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 💡",
    page_icon="🧠",
    layout="centered",
)

# 🎉 헤더
st.markdown("""
# 🌟 나의 MBTI로 알아보는 미래 직업! 💼
> MBTI 유형을 선택하면, 당신에게 어울리는 직업을 추천해드려요! 😊  
""")

# 🌈 사용자 입력 받기
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("🧬 당신의 MBTI를 선택해주세요!", mbti_list)

# 📤 결과 출력
if selected_mbti:
    st.markdown(f"## 🎯 {selected_mbti} - {mbti_jobs[selected_mbti]['desc']}")
    st.markdown("### 🔍 추천 직업 리스트:")
    for job in mbti_jobs[selected_mbti]["jobs"]:
        st.markdown(f"- {job}")

# 🧠 푸터
st.markdown("""
---
🧠 만든이: **AI 진로 추천 엔진**  
💌 문의: [contact@example.com](mailto:contact@example.com)
""")

