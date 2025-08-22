import streamlit as st
import pandas as pd

# ----------------------------
# 1) 데이터베이스 예시
# ----------------------------
content_db = [
    {"키워드": "패션", "타겟": "10대", "유형": "SNS", "아이디어": "여름 한정 패션 아이템 리뷰", "전략": "AIDA, FOMO"},
    {"키워드": "패션", "타겟": "20대", "유형": "블로그", "아이디어": "출근룩 스타일 가이드", "전략": "참여 유도, 해시태그 활용"},
    {"키워드": "IT", "타겟": "20대", "유형": "영상", "아이디어": "신제품 언박싱 영상", "전략": "호기심 자극, 스토리텔링"},
    {"키워드": "여행", "타겟": "직장인", "유형": "블로그", "아이디어": "주말 근교 여행 추천", "전략": "문제 해결, 정보 제공"},
    {"키워드": "음식", "타겟": "모든 연령", "유형": "SNS", "아이디어": "레시피 영상 시리즈", "전략": "참여 유도, 교육적 콘텐츠"},
    {"키워드": "경제", "타겟": "대학생", "유형": "뉴스레터", "아이디어": "재테크 기초 가이드", "전략": "교육적 콘텐츠, 스토리텔링"}
]

df_content = pd.DataFrame(content_db)

# ----------------------------
# 2) Streamlit UI
# ----------------------------
st.set_page_config(page_title="콘텐츠 아이디어 추천기", page_icon="💡", layout="wide")
st.title("💡 콘텐츠 아이디어 추천기")
st.markdown("관심 키워드, 타겟층, 콘텐츠 유형, 학습 포인트를 선택하면 관련 아이디어와 전략을 추천해드립니다!")

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    keyword_input = st.text_input("키워드 입력 (예: 패션, IT, 여행, 음식, 경제)")
with col2:
    target_input = st.selectbox("타겟층 선택", ["10대", "20대", "대학생", "직장인", "모든 연령"])

content_type_input = st.multiselect("콘텐츠 유형 선택", ["블로그", "SNS", "영상", "뉴스레터"], default=["블로그", "SNS"])

# 검색 버튼
if st.button("추천받기"):
    if keyword_input.strip() == "":
        st.warning("⚠️ 키워드를 입력해주세요.")
    else:
        # 필터링
        filtered = df_content[
            (df_content["키워드"].str.contains(keyword_input, case=False)) &
            (df_content["타겟"] == target_input) &
            (df_content["유형"].isin(content_type_input))
        ]

        if filtered.empty:
            st.info("관련 아이디어가 없습니다. 다른 키워드/타겟/유형을 선택해보세요!")
        else:
            st.subheader("추천 콘텐츠 아이디어")
            for idx, row in filtered.iterrows():
                st.markdown(f"**아이디어:** {row['아이디어']}")
                st.markdown(f"- 콘텐츠 유형: {row['유형']}")
                st.markdown(f"- 전략/학습 포인트: {row['전략']}")
                st.markdown("---")

            # CSV 다운로드
            csv = filtered.to_csv(index=False).encode('utf-8-sig')
            st.download_button(label="추천 아이디어 CSV 다운로드", data=csv, file_name="추천_콘텐츠_아이디어.csv", mime="text/csv")

   
