import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="발로란트 서버별 사용자 수 시각화", layout="wide")

st.title("발로란트 서버별 사용자 수 분석 (한국 제외)")

# 엑셀 파일 경로
FILE_PATH = "발로란트_서버별_사용자_수_한국제외_정리.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(FILE_PATH)
    return df

df = load_data()

st.subheader("원본 데이터")
st.dataframe(df)

# '추정 사용자 수' 컬럼에서 숫자만 추출 (백만 단위)
def extract_number(s):
    numbers = re.findall(r"[\d\.]+", s)
    if numbers:
        return float(numbers[0])
    return None

df["사용자수_백만"] = df["추정 사용자 수"].apply(extract_number)

st.subheader("전처리된 데이터")
st.dataframe(df[["서버 지역", "추정 사용자 수", "사용자수_백만"]])

# 서버 지역을 인덱스로 하고 숫자 컬럼으로 선 그래프 생성
chart_data = df.set_index("서버 지역")[["사용자수_백만"]]

st.subheader("서버별 사용자 수 선 그래프")
st.line_chart(chart_data)

st.write("""
* 사용자 수는 '추정 사용자 수'에서 숫자만 추출한 값이며, 단위는 백만 명입니다.
* 한국 서버는 제외된 상태입니다.
""")
