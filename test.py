import streamlit as st

st.set_page_config(page_title="!!!", layout="centered")
st.title("!!!")

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "step" not in st.session_state:
    st.session_state.step = 0
if "member_name" not in st.session_state:
    st.session_state.member_name = ""

# 선택 처리 함수
def process_choice(choice, scoring):
    st.session_state.score += scoring[choice]
    st.session_state.step += 1

# 1️⃣ 멤버 이름 입력
if st.session_state.step == 0:
    st.session_state.member_name = st.text_input("오늘 하루를 함께할 멤버 이름을 입력하세요:")
    if st.session_state.member_name and st.button("시작하기"):
        st.session_state.step = 1

# 2️⃣ 아침
elif st.session_state.step == 1:
    st.subheader("아침: 무엇을 할까요?")
    options = ["카페에서 조용히 대화하기", "콘서트 준비 도와주기", "산책하며 함께 사진 찍기", "멤버와 함께 게임하기"]
    scoring = {"카페에서 조용히 대화하기":1,"콘서트 준비 도와주기":2,"산책하며 함께 사진 찍기":2,"멤버와 함께 게임하기":1}

    with st.form(key="morning_form"):
        choice = st.radio("선택지를 골라주세요:", options)
        submitted = st.form_submit_button("다음")
        if submitted:
            process_choice(choice, scoring)

# 3️⃣ 점심
elif st.session_state.step == 2:
    st.subheader("점심: 멤버가 선물해준다면?")
    options = ["간단한 소품 받기", "직접 만든 간식 받기", "좋아하는 음식을 같이 먹기", "멤버가 추천하는 음식 시도하기"]
    scoring = {"간단한 소품 받기":1,"직접 만든 간식 받기":2,"좋아하는 음식을 같이 먹기":2,"멤버가 추천하는 음식 시도하기":1}

    with st.form(key="lunch_form"):
        choice = st.radio("선택지를 골라주세요:", options)
        submitted = st.form_submit_button("다음")
        if submitted:
            process_choice(choice, scoring)

# 4️⃣ 오후
elif st.session_state.step == 3:
    st.subheader("오후: 무엇을 할까요?")
    options = ["연습실에서 같이 춤 연습하기","쇼핑몰 구경하며 잡담하기","노래방에서 듀엣 부르기","카페에서 서로의 취향 공유하기"]
    scoring = {"연습실에서 같이 춤 연습하기":2,"쇼핑몰 구경하며 잡담하기":1,"노래방에서 듀엣 부르기":2,"카페에서 서로의 취향 공유하기":1}

    with st.form(key="afternoon_form"):
        choice = st.radio("선택지를 골라주세요:", options)
        submitted = st.form_submit_button("다음")
        if submitted:
            process_choice(choice, scoring)

# 5️⃣ 저녁
elif st.session_state.step == 4:
    st.subheader(f"{st.session_state.member_name}과 저녁에 할 일은?")
    options = ["같이 영화 보기", "별 보기 산책", "팬과 멤버 서로 편지 주고받기", "오늘 하루 돌아보며 사진 찍기"]
    scoring = {"같이 영화 보기":1,"별 보기 산책":2,"팬과 멤버 서로 편지 주고받기":2,"오늘 하루 돌아보며 사진 찍기":1}

    with st.form(key="evening_form"):
        choice = st.radio("선택지를 골라주세요:", options)
        submitted = st.form_submit_button("다음")
        if submitted:
            process_choice(choice, scoring)

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
