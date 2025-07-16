import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="발로란트 요원별 픽률", layout="centered")

st.title("🧠 발로란트 프로 요원별 픽률 분석 (2025)")
st.markdown("2025 시즌 기준 프로 경기에서의 요원별 픽률 데이터를 시각화한 결과입니다.")

# 엑셀 파일 불러오기
# uploaded_file = st.file_uploader("엑셀 파일 업로드", type=["xlsx"])

if True:
    df = pd.read_excel("요원별_픽률_분석_2025.xlsx", encoding='euc-kr')

    st.subheader("📋 데이터 테이블")
    st.dataframe(df)

    st.subheader("📊 요원별 픽률 그래프")

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df["요원"], df["픽률 (%)"], color="skyblue")
    ax.set_ylabel("픽률 (%)")
    ax.set_xlabel("요원")
    ax.set_title("요원별 픽률 (2025)")
    ax.set_ylim(0, max(df["픽률 (%)"]) + 10)
    plt.xticks(rotation=45)

    # 그래프 표시
    st.pyplot(fig)
else:
    st.info("왼쪽 사이드바 또는 위에서 엑셀 파일을 업로드하세요.")
