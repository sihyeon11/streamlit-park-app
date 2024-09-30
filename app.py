import pandas as pd 
import numpy as np
import streamlit as st
from PIL import Image

df = pd.read_csv('./공원_클러스터링.csv', encoding='cp949')
place =pd.read_csv('./공원_위도_경도.csv', encoding='cp949')
#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')

title_img = Image.open('세종공모전_v1-002.png')

#불러온 사진 표시하기
st.image(title_img)

##사이드바
st.sidebar.title('🌤️ 공원 테마 🌿')

## 탭 생성 
tab1, tab2= st.tabs(['테마별 공원' , '공원 분포'])

with tab1:
  #tab1를 누르면 표시될 내용
  # select_species 변수에 사용자가 선택한 값이 지정됩니다
    park_type = st.sidebar.selectbox('어떤 공원을 찾으시나요?',
                                     ['이도저도아닌형', '가족어린이형','자연풍경형','레저스포츠형','역사유적형','문화/도시형'])
    # 원래 dataframe으로 부터 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
    result_df = df[df['type']==park_type][['type','Park']]
    result_df.reset_index(drop=True, inplace=True)
    tab1.table(result_df)
    
with tab2:
  #tab2를 누르면 표시될 내용 
  #지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
        # 사이드바에서 선택한 유형에 맞는 데이터만 필터링
    park_type = st.sidebar.selectbox('분포를 확인 할 공원 테마를 선택하세요!', 
                                     ['이도저도아닌형', '가족어린이형', '자연풍경형', '레저스포츠형', '역사유적형', '문화/도시형'])
    
    # 선택한 유형의 공원만 필터링하여 지도에 표시
    filtered_place = place[place['type'] == park_type][['위도', '경도']].rename(columns={'위도': 'lat', '경도': 'lon'})
    
    # 지도 시각화
    st.subheader(f'{park_type} 공원의 분포 지도')
    st.map(filtered_place)


