import streamlit as st

st.title("MBTI 궁합 테스트")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

best_match = {
    "INTJ": ["ENFP", "ENTP"],
    "ENFP": ["INTJ", "INFJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ESFP": ["ISTJ", "ISFJ"],
    # 나머지도 채워 넣으면 됨
}

user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if st.button("궁합 보기"):
    matches = best_match.get(user_mbti, [])
    if matches:
        st.success(f"당신과 잘 맞는 MBTI: {', '.join(matches)}")
    else:
        st.warning("아직 데이터가 없어요 😅")

