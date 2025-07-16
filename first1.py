import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="발로란트 요원 픽률 시각화", layout="centered")

# 제목
st.title("🎯 발로란트 프로 요원별 픽률 시각화")
st.write("엑셀 파일을 업로드하면 요원별 픽률을 시각화해줍니다.")

# 파일 업로드
uploaded_file = st.file_uploader("📁 엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        # 데이터 확인
        st.subheader("📋 데이터 미리보기")
        st.dataframe(df)

        # 그래프 그리기
        st.subheader("📊 요원별 픽률 그래프")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df["요원"], df["픽률 (%)"], color="mediumseagreen")
        ax.set_xlabel("요원")
        ax.set_ylabel("픽률 (%)")
        ax.set_title("요원별 픽률")
        ax.set_ylim(0, max(df["픽률 (%)"]) + 10)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ 오류 발생: {e}")
else:
    st.info("먼저 엑셀 파일을 업로드해주세요. (예: 요원, 픽률(%) 열 포함)")
