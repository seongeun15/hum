import streamlit as st
import pandas as pd

st.set_page_config(page_title="발로란트 서버별 사용자 수 시각화", layout="wide")

st.title("발로란트 서버별 사용자 수 분석 (한국 제외)")

# 엑셀 파일 경로
FILE_PATH = "발로란트_서버별_사용자_수_한국제외_정리.xlsx"

@st.cache_data
def load_data():
    # 엑셀 파일 읽기 (EUC-KR 인코딩은 Excel에선 자동처리)
    df = pd.read_excel(FILE_PATH)
    return df

df = load_data()

st.subheader("원본 데이터")
st.dataframe(df)

# '서버 지역'은 그대로 두고, '추정 사용자 수' 열 전처리
# "약 2.75백만 명" 형태에서 숫자만 추출
def extract_number(s):
    import re
    # 숫자와 소수점만 추출
    numbers = re.findall(r"[\d\.]+", s)
    if numbers:
        return float(numbers[0])
    else:
        return None

df["사용자수_숫자"] = df["추정 사용자 수"].apply(extract_number)

# '총사용자수'라는 컬럼은 따로 유지하고 싶다 했는데, 원본에는 없으니 여기서는
# '추정 사용자 수' 열을 '총사용자수'로 해석해서 숫자값으로 사용

st.subheader("전처리된 데이터")
st.dataframe(df[["서버 지역", "추정 사용자 수", "사용자수_숫자"]])

# 그래프용 데이터프레임 준비: 서버 지역을 인덱스로, 사용자수_숫자 컬럼으로 선 그래프
chart_df = df.set_index("서버 지역")[["사용자수_숫자"]]

st.subheader("서버별 사용자 수 선 그래프")
st.line_chart(chart_df)

st.write("""
* 그래프는 '추정 사용자 수'에서 숫자만 추출한 값으로 그렸으며, 단위는 백만 명입니다.
* ‘한국 서버’는 제외된 상태의 데이터입니다.
""")
