import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 예시 행정구역별 위도/경도 좌표 (실제 데이터에 맞게 수정 필요)
coordinates = {
    '서울특별시 종로구': (37.572950, 126.979357),
    '서울특별시 중구': (37.563757, 126.997257),
    '서울특별시 용산구': (37.531530, 126.981230),
    '서울특별시 성동구': (37.563215, 127.036411),
    '서울특별시 광진구': (37.545837, 127.082992),
}

st.title("2025년 5월 기준 연령별 인구 현황 - 지도 시각화")

# CSV 파일 불러오기 (경로 및 인코딩 조정)
df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding='euc-kr')

# 총인구수 컬럼 정리
df['총인구수'] = df['2025년05월_계_총인구수'].str.replace(',', '').astype(int)

# 상위 5개 행정구역 추출
top5_df = df.sort_values(by='총인구수', ascending=False).head(5)

# Folium 지도 생성 (서울 중심 좌표)
m = folium.Map(location=[37.55, 126.98], zoom_start=11)

# 각 행정구역별로 원형 마크 추가
for _, row in top5_df.iterrows():
    gu_name = row['행정구역']
    population = row['총인구수']
    
    # 좌표가 있으면 원 추가
    if gu_name in coordinates:
        lat, lon = coordinates[gu_name]
        folium.Circle(
            location=(lat, lon),
            radius=population / 10,  # 반지름 (인구수에 비례, 조정 가능)
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.4,  # 반투명
            popup=f"{gu_name}: {population}명"
        ).add_to(m)
    else:
        st.warning(f"{gu_name} 좌표가 없습니다.")

# Streamlit에 folium 지도 표시
st_folium(m, width=700, height=500)
