import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="발로란트 요원 픽률", layout="centered")

# 타이틀
st.title("🔥 발로란트 프로 요원별 픽률 시각화 (2025)")

# 엑셀 파일 경로 (같은 디렉토리에 있어야 함)
excel_path = "요원별_픽률_분석_2025.xlsx"

try:
    # 엑셀 파일 불러오기
    df = pd.read_excel(excel_path)

    # 데이터 표시
    st.subheader("📋 요원별 픽률 데이터")
    st.dataframe(df)

    # 그래프 출력
    st.subheader("📊 요원별 픽률 그래프")
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df["요원"], df["픽률 (%)"], color="orange")
    ax.set_ylabel("픽률 (%)")
    ax.set_xlabel("요원")
    ax.set_title("2025 시즌 기준 요원별 픽률")
    plt.xticks(rotation=45)

    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❗ 엑셀 파일을 찾을 수 없습니다: `{excel_path}` 를 같은 폴더에 넣어주세요.")
except Exception as e:
    st.error(f"❗ 오류 발생: {e}")
