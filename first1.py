import streamlit as st
import pandas as pd

# 제목
st.title("💡 발로란트 요원별 픽률 분석")

# 설명
st.markdown("""
이 페이지는 업로드된 엑셀 파일을 기반으로 **요원별 픽률**을 분석하고,  
픽률 데이터를 선 그래프로 시각화합니다.
""")

# 파일 업로드
uploaded_file = st.file_uploader("📂 요원별_픽률_분석_2025.xlsx (EUC-KR 인코딩)", type=["xlsx"])

if uploaded_file:
    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(uploaded_file)

        # 데이터 출력
        st.subheader("📋 원본 데이터")
        st.dataframe(df)

        # 데이터 전처리 (요원별 픽률 정렬)
        df_sorted = df.sort_values(by="픽률 (%)", ascending=False).reset_index(drop=True)

        # 시각화
        st.subheader("📈 요원별 픽률 선 그래프")
        st.line_chart(data=df_sorted, x="요원", y="픽률 (%)")

    except Exception as e:
        st.error(f"❗ 오류가 발생했습니다: {e}")
else:
    st.info("엑셀 파일을 먼저 업로드해주세요.")
