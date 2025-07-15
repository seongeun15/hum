import streamlit as st
st.title('나의 첫 웹 서비스 만들기!!')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 듀얼리스트선수를 선택해주세요:', ['텍스쳐','버즈,','우드','현민','담비'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 선수는 '+menu+'이군요?! 저도 좋아요!!')
