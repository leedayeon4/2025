import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="💘 이상형 연예인 추천기 💘",
    page_icon="🎬",
    layout="centered"
)

# 🌈 배경 스타일 추가 (움직이는 그라디언트)
st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #ffdde1, #fceabb, #c2e9fb, #d4fc79);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .title {
        font-size: 48px;
        color: hotpink;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
    }
    .sub {
        font-size: 20px;
        text-align: center;
        color: #ff69b4;
        margin-bottom: 30px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 20px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 🎀 UI 헤더
st.markdown("<div class='title'>💘 이상형을 말해봐!<br>어울리는 연예인을 추천해줄게 🎬</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>예: 귀엽고 웃긴 사람, 차갑고 시크한 스타일, 순수한 남자 등등</div>", unsafe_allow_html=True)

# 🎯 연예인 추천 데이터
celebs = [
    {
        "name": "정해인",
        "keywords": ["순수", "부드러운", "미소", "따뜻한", "착한"],
        "desc": "💫 부드러운 미소의 국민 연하남",
        "image": "https://i.namu.wiki/i/R9Te44qLtoMYTKG6H3uZxGPc6-6mc9Fh49dl-AZybdJf8g0X38G4WBkFv4sk-m_nN_dQw9qTwPduZk5MXG3x-Q.webp"
    },
    {
        "name": "장원영",
        "keywords": ["귀여운", "러블리", "키 큰", "아이돌", "화사한"],
        "desc": "🌟 만화에서 튀어나온 요정 비주얼",
        "image": "https://i.namu.wiki/i/ZfyGNo7CZXkpOM_2cf6WkKz7f4Mbe6ZKDWreUu_rXoRvSSuLs0hL7tPfNbfdGgOGHyX-nWg9MWFRHP_oYMJcNQ.webp"
    },
    {
        "name": "유재석",
        "keywords": ["웃긴", "유쾌한", "예능", "센스있는", "재밌는"],
        "desc": "😂 국민 예능인, 유쾌함 그 자체",
        "image": "https://i.namu.wiki/i/Hzu-2QWyv2oScEIlLPdI-Tv_l9g95m7cJ3WDjPb06M4bwUG6UjuScXB4Hoo1pBz9o7DZnU6gFAzvmpsRSff-OA.webp"
    },
    {
        "name": "수지",
        "keywords": ["청순한", "단아한", "여신", "배우", "감성"],
        "desc": "🌸 모두가 사랑하는 국민 첫사랑",
        "image": "https://i.namu.wiki/i/Wz_vR5s3eOfVnG7hZhWqmtmsZu0h_TYke4Upxn0dzkwzWbF3nL9l2vZp7wOK5-Y1SmuGc-Ca6lgfTbafzUnMRg.webp"
    },
    {
        "name": "뷔 (BTS)",
        "keywords": ["섹시한", "시크한", "차가운", "미남", "강렬한"],
        "desc": "🔥 시크한 눈빛, 아우라 폭발하는 미남",
        "image": "https://i.namu.wiki/i/I7N94cMJ4FzYZ0aDKmlPEnTAiX7LPaKCTbyXYyhlbyzTI3aCJSdrjFvP3W1w5QVRBPdZ4hBl1OamEdw0_R4MCA.webp"
    },
]

# 🎤 사용자 입력
user_input = st.text_input("📝 이상형을 자유롭게 입력해 주세요!", placeholder="예: 웃기고 귀여운 사람", max_chars=50)

# 🔍 추천 로직
def match_celeb(text):
    results = []
    for celeb in celebs:
        score = sum(1 for kw in celeb["keywords"] if kw in text)
        if score > 0:
            results.append((score, celeb))
    results.sort(key=lambda x: x[0], reverse=True)
    return [celeb for score, celeb in results[:2]]

# 🎈 결과 출력
if user_input:
    st.balloons()
    matched = match_celeb(user_input)
    if matched:
        st.markdown("## 💘 당신의 이상형과 어울리는 연예인 💘")
        for celeb in matched:
            st.markdown(f"""
                <div class="card">
                    <h3>🌟 {celeb['name']}</h3>
                    <p>{celeb['desc']}</p>
                    <img src="{celeb['image']}" width="300">
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("😢 오잉? 해당 스타일과 딱 맞는 연예인을 찾지 못했어요. 다시 입력해볼래요?")

# 👣 푸터
st.markdown("""
---
<p style='text-align: center; font-size: 14px; color: gray;'>
Made with 💖 by <strong>AI 이상형 매칭기</strong> | Contact: dream@idolmatch.com
</p>
""", unsafe_allow_html=True)
