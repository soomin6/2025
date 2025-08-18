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

# 함수: 다음 단계로 이동
def next_step(choice_score):
    st.session_state.score += choice_score
    st.session_state.step += 1
    st.experimental_rerun()  # 화면 새로고침

# 1️⃣ 멤버 이름 입력 단계
if st.session_state.step == 0:
    st.session_state.member_name = st.text_input("오늘 하루를 함께할 멤버 이름을 입력하세요:")
    if st.session_state.member_name:
        if st.button("시작하기"):
            st.session_state.step = 1
            st.experimental_rerun()

# 2️⃣ 아침 선택
elif st.session_state.step == 1:
    st.subheader("아침: 무엇을 할까요?")
    choice = st.radio(
        "선택지를 골라주세요:",
        ("카페에서 조용히 대화하기", "콘서트 준비 도와주기", "산책하며 함께 사진 찍기", "멤버와 함께 게임하기")
    )
    if st.button("선택"):
        score = 1 if choice in ["카페에서 조용히 대화하기", "멤버와 함께 게임하기"] else 2
        next_step(score)

# 3️⃣ 점심 선택
elif st.session_state.step == 2:
    st.subheader("점심: 멤버가 선물해준다면?")
    choice = st.radio(
        "선택지를 골라주세요:",
        ("간단한 소품 받기", "직접 만든 간식 받기", "좋아하는 음식을 같이 먹기", "멤버가 추천하는 음식 시도하기")
    )
    if st.button("선택"):
        score = 1 if choice in ["간단한 소품 받기", "멤버가 추천하는 음식 시도하기"] else 2
        next_step(score)

# 4️⃣ 오후 선택
elif st.session_state.step == 3:
    st.subheader("오후: 무엇을 할까요?")
    choice = st.radio(
        "선택지를 골라주세요:",
        ("연습실에서 같이 춤 연습하기", "쇼핑몰 구경하며 잡담하기", "노래방에서 듀엣 부르기", "카페에서 서로의 취향 공유하기")
    )
    if st.button("선택"):
        score = 2 if choice in ["연습실에서 같이 춤 연습하기", "노래방에서 듀엣 부르기"] else 1
        next_step(score)

# 5️⃣ 저녁 선택
elif st.session_state.step == 4:
    st.subheader("저녁: 하루 마무리는?")
    choice = st.radio(
        "선택지를 골라주세요:",
        ("같이 영화 보기", "별 보기 산책", "팬과 멤버 서로 편지 주고받기", "오늘 하루 돌아보며 사진 찍기")
    )
    if st.button("선택"):
        score = 2 if choice in ["별 보기 산책", "팬과 멤버 서로 편지 주고받기"] else 1
        next_step(score)

# 6️⃣ 결과 화면
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
        st.experimental_rerun()
