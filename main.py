import streamlit as st

st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

st.title("💖 MBTI 궁합 테스트")
st.write("당신의 MBTI를 선택하면 잘 맞는 유형과 이유를 알려드릴게요!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

best_match = {
    "INTJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "계획적인 당신에게 자유롭고 창의적인 파트너가 활력을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "INTP": {
        "matches": ["ENTJ", "ESTJ"],
        "desc": "아이디어 많은 당신에게 실행력 강한 파트너가 방향을 잡아줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ENTJ": {
        "matches": ["INFP", "INTP"],
        "desc": "리더십 있는 당신에게 감성적 파트너가 균형을 제공합니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ENTP": {
        "matches": ["INFJ", "INTJ"],
        "desc": "즉흥적인 당신에게 깊이 있는 대화를 나눌 상대가 필요합니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "INFJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "이상주의적인 당신에게 유쾌하고 열정적인 사람이 어울립니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "INFP": {
        "matches": ["ENFJ", "ENTJ"],
        "desc": "감성이 풍부한 당신에게 현실적인 방향을 제시해줄 파트너가 필요합니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ENFJ": {
        "matches": ["INFP", "ISFP"],
        "desc": "사람을 이끄는 당신에게 따뜻한 내향형 파트너가 조화를 이룹니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ENFP": {
        "matches": ["INTJ", "INFJ"],
        "desc": "활발한 당신에게 차분하고 통찰력 있는 파트너가 안정감을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ISTJ": {
        "matches": ["ESFP", "ESTP"],
        "desc": "원칙적인 당신에게 자유로운 성향이 새로운 경험을 선사합니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ISFJ": {
        "matches": ["ESFP", "ESTP"],
        "desc": "배려심 깊은 당신에게 에너지 넘치는 파트너가 즐거움을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ESTJ": {
        "matches": ["INFP", "ISFP"],
        "desc": "현실적인 당신에게 감성적인 사람이 색다른 시각을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ESFJ": {
        "matches": ["ISFP", "ISTP"],
        "desc": "사교적인 당신에게 조용하고 단단한 내향형이 잘 어울립니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ISTP": {
        "matches": ["ESFJ", "ENFJ"],
        "desc": "실용적인 당신에게 따뜻한 감성을 가진 사람이 균형을 잡아줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ISFP": {
        "matches": ["ENFJ", "ESFJ"],
        "desc": "온화한 당신에게 활기찬 리더형이 좋은 자극을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ESTP": {
        "matches": ["ISFJ", "ISTJ"],
        "desc": "모험심 있는 당신에게 안정적인 사람이 든든함을 줍니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    "ESFP": {
        "matches": ["ISTJ", "ISFJ"],
        "desc": "에너지 넘치는 당신에게 차분한 내향형이 좋은 균형을 제공합니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    }
}

user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if st.button("궁합 보기"):
    data = best_match.get(user_mbti)
    if data:
        st.subheader(f"💘 잘 맞는 MBTI: {', '.join(data['matches'])}")
        st.write(f"**이유:** {data['desc']}")
        st.image(data['img'], caption=f"{user_mbti} 궁합 이미지", use_column_width=True)
    else:
        st.warning("아직 데이터가 없어요 😅")
