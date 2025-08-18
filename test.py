import streamlit as st

st.set_page_config(page_title="!!!", layout="centered")
st.title("!!!")

# 점수와 진행 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "step" not in st.session_state:
    st.session_state.step = 0
if "member_name" not in st.session_state:
    st.session_state.member_name = ""

# 단계별 선택지 함수
def step_choice(question, options, scoring):
    st.subheader(question)
    choice = st.radio("선택지를 골라주세요:", options)
    if st.button("선택"):
        st.session_state.score += scoring[choice]
        st.session_state.step += 1

# 1️⃣ 멤버 이름 입력
if st.session_state.step == 0:
    st.session_state.member_name = st.text_input("오늘 하루를 함께할 멤버 이름을 입력하세요:")
    if st.session_state.member_name and st.button("시작하기"):
        st.session_state.step = 1

# 2️⃣ 아침
elif st.session_state.step == 1:
    step_choice(
        "아침: 무엇을 할까요?",
        ("카페에서 조용히 대화하기", "콘서트 준비 도와주기", "산책하며 함께 사진 찍기", "멤버와 함께 게임하기"),
        {
            "카페에서 조용히 대화하기":1,
            "콘서트 준비 도와주기":2,
            "산책하며 함께 사진 찍기":2,
            "멤버와 함께 게임하기":1
        }
    )

# 3️⃣ 점심
elif st.session_state.step == 2:
    step_choice(
        "점심: 멤버가 선물해준다면?",
        ("간단한 소품 받기", "직접 만든 간식 받기", "좋아하는 음식을 같이 먹기", "멤버가 추천하는 음식 시도하기"),
        {
            "간단한 소품 받기":1,
            "직접 만든 간식 받기":2,
            "좋아하는 음식을 같이 먹기":2,
            "멤버가 추천하는 음식 시도하기":1
        }
    )

# 4️⃣ 오후
elif st.session_state.step == 3:
    step_choice(
        "오후: 무엇을 할까요?",
        ("연습실에서 같이 춤 연습하기", "쇼핑몰 구경하며 잡담하기", "노래방에서 듀엣 부르기", "카페에서 서로의 취향 공유하기"),
        {
            "연습실에서 같이 춤 연습하기":2,
            "쇼핑몰 구경하며 잡담하기":1,
            "노래방에서 듀엣 부르기":2,
            "카페에서 서로의 취향 공유하기":1
        }
    )

# 5️⃣ 저녁 (문구 변경)
elif st.session_state.step == 4:
    step_choice(
        f"{st.session_state.member_name}과 저녁에 할 일은?",
        ("같이 영화 보기", "별 보기 산책", "팬과 멤버 서로 편지 주고받기", "오늘 하루 돌아보며 사진 찍기"),
        {
            "같이 영화 보기":1,
            "별 보기 산책":2,
            "팬과 멤버 서로 편지 주고받기":2,
            "오늘 하루 돌아보며 사진 찍기":1
        }
    )

# 6️⃣ 결과
elif st.session_state.step == 5:
    st.subheader(f"오늘 **{st.session_state.member_name}**와 보내는 하루")
    if st.session_state.score <= 5:
        st.write("★★★☆☆ - 함께 보내는 소소한 하루")
    elif st.session_state.score <= 7:
        st.write("★★★★☆ - 즐거운 하루가 될 것 같아요!")
    else:
        st.write("★★★★★ - 완벽한 하루! 최고의 하루!")
    st.balloons()

    if st.button("다시 시작"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.member_name = ""
