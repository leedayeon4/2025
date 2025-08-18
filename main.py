import streamlit as st

# 🌟 페이지 설정
st.set_page_config(
    page_title="🌈✨MBTI 직업 추천기✨🌈",
    page_icon="💡",
    layout="centered"
)

# 🎨 CSS 스타일링 (배경, 글씨 색, 글꼴 등)
st.markdown(
    """
    <style>
        body {
            background-color: #fffafc;
        }
        .title {
            font-size: 50px;
            text-align: center;
            color: #ff69b4;
            font-weight: bold;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #ff1493;
        }
        .result {
            font-size: 30px;
            color: #8a2be2;
            background-color: #fff0f5;
            padding: 20px;
            border-radius: 15px;
        }
        .job {
            font-size: 22px;
            color: #ff4500;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 타이틀
st.markdown('<div class="title">🌟 MBTI로 알아보는 ✨인생 직업✨ 추천기 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🎯 당신의 MBTI를 선택하면, 찰떡같은 직업을 추천해드려요! 💖</div>', unsafe_allow_html=True)
st.markdown("## ")

# 📊 MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": {"desc": "🛡️ 책임감 넘치는 관리자", "jobs": ["👮‍♂️ 경찰", "🧾 회계사", "🏛️ 공무원", "🪖 군인"]},
    "ISFJ": {"desc": "💗 따뜻한 헌신형 도우미", "jobs": ["🧑‍⚕️ 간호사", "👩‍🏫 교사", "📋 사회복지사", "📞 고객센터"]},
    "INFJ": {"desc": "🔮 통찰력 있는 이상주의자", "jobs": ["🧘‍♂️ 상담사", "✍️ 작가", "🔬 연구원", "🎓 교육자"]},
    "INTJ": {"desc": "🧠 전략적인 계획가", "jobs": ["📊 데이터 사이언티스트", "👨‍⚕️ 의사", "🧑‍💼 컨설턴트", "🧑‍🔬 연구개발자"]},
    "ISTP": {"desc": "🛠️ 현실주의적 탐험가", "jobs": ["🧑‍🔧 정비사", "✈️ 파일럿", "🚨 소방관", "🕵️‍♂️ 보안전문가"]},
    "ISFP": {"desc": "🎨 감성적 아티스트", "jobs": ["👩‍🍳 요리사", "📸 사진작가", "🌸 플로리스트", "🧵 디자이너"]},
    "INFP": {"desc": "🌌 이상적인 철학가", "jobs": ["📖 시인", "🎼 작곡가", "🧘 상담사", "🎨 일러스트레이터"]},
    "INTP": {"desc": "🧩 아이디어 뱅크", "jobs": ["🤖 AI 개발자", "👨‍🏫 교수", "👨‍💻 개발자", "🔍 데이터 분석가"]},
    "ESTP": {"desc": "⚡ 에너지 넘치는 해결사", "jobs": ["🚘 자동차 딜러", "💼 세일즈", "🏍️ 레이서", "🧗‍♂️ 익스트림 스포츠 선수"]},
    "ESFP": {"desc": "🎉 무대 위 스타", "jobs": ["🎤 연예인", "📹 유튜버", "💄 뷰티 크리에이터", "🎈 이벤트 플래너"]},
    "ENFP": {"desc": "🔥 열정적인 창의가", "jobs": ["🎬 영화감독", "📣 마케터", "📚 콘텐츠 제작자", "🎤 방송작가"]},
    "ENTP": {"desc": "🌀 토론을 즐기는 혁신가", "jobs": ["🚀 스타트업 창업자", "💬 전략기획자", "⚖️ 변호사", "🎯 브랜드 디렉터"]},
    "ESTJ": {"desc": "📋 철저한 관리자", "jobs": ["🏗️ 현장감독", "📑 회계사", "🪖 군 간부", "🏢 CEO"]},
    "ESFJ": {"desc": "💞 사교적인 헬퍼", "jobs": ["🧑‍🏫 초등교사", "🧑‍🍳 영양사", "📞 고객 상담사", "🏥 병원 코디네이터"]},
    "ENFJ": {"desc": "🌟 리더십의 화신", "jobs": ["🎓 교육자", "🧠 상담가", "🎤 강연가", "🌍 NGO 활동가"]},
    "ENTJ": {"desc": "👑 카리스마 넘치는 리더", "jobs": ["📈 CEO", "🧑‍💼 경영전략가", "💹 투자전문가", "⚖️ 변호사"]}
}

# 🎯 MBTI 선택
st.markdown("### 🔍 아래에서 당신의 MBTI를 선택해보세요! 👇")
selected_mbti = st.selectbox("✨ MBTI 유형 선택", list(mbti_jobs.keys()))

# 💡 추천 결과
if selected_mbti:
    result = mbti_jobs[selected_mbti]
    st.markdown("## ")
    st.markdown(f'<div class="result">💖 당신의 MBTI는 <strong>{selected_mbti}</strong><br><br>✨ 성격 요약: <em>{result["desc"]}</em></div>', unsafe_allow_html=True)
    st.markdown("## ")
    st.markdown("### 🌟 어울리는 직업 리스트 👑")
    for job in result["jobs"]:
        st.markdown(f'<div class="job">• {job}</div>', unsafe_allow_html=True)

# 🥳 푸터
st.markdown("---")
st.markdown("📬 문의: [dream@careerland.com](mailto:dream@careerland.com) | 💻 Made with ❤️ by AI")
st.markdown("🎨 이모지 & 스타일로 더욱 예쁜 진로 추천 사이트 🌈")
st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #fce4ec, #f8bbd0, #f48fb1, #ec407a);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
""", unsafe_allow_html=True)
st.balloons()


