import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import re

# 행정구역 → 좌표 수동 매핑 (직접 지정)
coordinates = {
    '서울특별시 종로구': (37.572950, 126.979357),
    '서울특별시 중구': (37.563757, 126.997257),
    '서울특별시 용산구': (37.531530, 126.981230),
    '서울특별시 성동구': (37.563215, 127.036411),
    '서울특별시 광진구': (37.545837, 127.082992),
    # 필요시 여기에 더 추가
}

st.title("2025년 5월 행정구역별 인구 - 지도 시각화")

# CSV 파일 불러오기 (파일명과 경로는 실제 환경에 맞게 수정)
df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding='euc-kr')

# 괄호 안 숫자 제거: "서울특별시 종로구(11110)" → "서울특별시 종로구"
df['행정구역'] = df['행정구역'].apply(lambda x: re.sub(r'\([^)]*\)', '', x).strip())

# 총인구수 쉼표 제거 및 정수 변환
df['총인구수'] = df['2025년05월_계_총인구수'].str.replace(',', '').astype(int)

# 상위 5개 행정구역 선택
top5_df = df.sort_values(by='총인구수', ascending=False).head(5)

# folium 지도 생성 (서울 중심)
m = folium.Map(location=[37.55, 126.98], zoom_start=11)

# 원형 마커 추가
for _, row in top5_df.iterrows():
    name = row['행정구역']
    pop = row['총인구수']
    
    if name in coordinates:
        lat, lon = coordinates[name]
        folium.Circle(
            location=(lat, lon),
            radius=pop / 10,  # 인구수에 비례 (값 조정 가능)
            color='pink',
            fill=True,
            fill_color='pink',
            fill_opacity=0.4,
            popup=f"{name} - 인구수: {pop:,}명"
        ).add_to(m)
    else:
        st.warning(f"좌표가 없는 행정구역: {name}")

# 지도 출력
st.subheader("📍 지도 시각화")
st_folium(m, width=700, height=500)
