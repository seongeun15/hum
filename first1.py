import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="발로란트 요원 픽률", layout="centered")

# 데이터 직접 삽입 (엑셀 없이 동작)
data = {
    '요원': [
        '제트', '스카이', '소바', '브림스톤', '페이드',
        '요루', '카이오', '바이퍼', '킬조이', '아스트라',
        '레이즈', '세이지', '브리치', '피닉스', '하버'
    ],
    '픽률 (%)': [
        74.5, 63.1, 55.0, 32.8, 30.3,
        25.7, 22.1, 18.4, 16.0, 14.2,
        13.0, 10.9, 8.3, 5.7, 3.4
    ]
}

df = pd.DataFrame(data)

# 제목
st.title("🔥 발로란트 프로 요원별 픽률 분석 (2025)")
st.markdown("**2025 시즌 기준** 주요 요원의 픽률을 시각화한 결과입니다.")

# 데이터 테이블 출력
st.subheader("📋 데이터 테이블")
st.dataframe(df)

# 그래프 출력
st.subheader("📊 요원별 픽률 그래프")
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["요원"], df["픽률 (%)"], color="cornflowerblue")
ax.set_ylabel("픽률 (%)")
ax.set_xlabel("요원")
ax.set_title("2025 시즌 기준 요원별 픽률")
plt.xticks(rotation=45)
st.pyplot(fig)
