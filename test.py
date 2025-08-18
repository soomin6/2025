import streamlit as st

st.set_page_config(page_title="!!!", layout="centered")

st.title("!!!")

# 1️⃣ 멤버 이름 입력
member_name = st.text_input("오늘 하루를 함께할 멤버 이름을 입력하세요:")

if member_name:
    st.write(f"오늘의 상대: **{member_name}**")

    # 2️⃣ 선택지 1
    st.subheader("아침에 무엇을 할까요?")
    choice1 = st.radio(
        "선택지를 골라주세요:",
        ("카페에서 조용히 대화하기", "콘서트 준비 도와주기")
    )

    # 점수 계산
    score = 0
    if choice1 == "카페에서 조용히 대화하기":
        score += 1
    else:
        score += 2

    # 3️⃣ 선택지 2
    st.subheader("점심에 멤버가 선물해준다면?")
    choice2 = st.radio(
        "선택지를 골라주세요:",
        ("간단한 소품", "직접 만든 간식")
    )
    if choice2 == "간단한 소품":
        score += 1
    else:
        score += 2

    # 4️⃣ 결과
    if st.button("결과 확인하기"):
        st.subheader(f"오늘 **{member_name}**와 보내는 하루")
        if score <= 2:
            st.write("★★★☆☆ - 함께 보내는 소소한 하루")
        elif score <= 3:
            st.write("★★★★☆ - 즐거운 하루가 될 것 같아요!")
        else:
            st.write("★★★★★ - 완벽한 하루! 최고의 궁합!")

        st.balloons()

