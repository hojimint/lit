#라이브러리 import
import requests
import pprint
import json
import pandas as pd
import streamlit as st
import numpy as np
file_path = "C:\\Users\hojin\Desktop\gwajea\python\gimal\simple.txt"
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=파주&dataTerm=DAILY&pageNo=1&numOfRows=20&returnType=json&serviceKey=KQRR%2BJLPRITcRv6CvRB1QUxmDQ%2BKmcKWMjK1A19g%2BiHLEbXTpqjWmut5pwHfKkH6O7KfqLSXxEmrLt6Ctooliw%3D%3D"

response = requests.get(url)

contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))

## json을 DataFrame으로 변환하기 ##

#문자열을 json으로 변경
json_ob = json.loads(contents)
# print(type(json_ob)) #json타입 확인

# 필요한 내용만 꺼내기
body = json_ob['response']['body']['items']
# print(body)

# # Dataframe으로 만들기
dataframe = pd.json_normalize(body)
# dataframe.index = ['khaiValue', 'pm10Value', 'no2Value', '03Value']
# print(dataframe['khaiValue'])
time = dataframe['dataTime']
total = dataframe['khaiValue']
dust = dataframe['pm10Value']
p1 = pd.concat([time,total],axis=1)
# ,dust
# st.dataframe(p1)
# p1.head()
chart = alt.Chart(p1).mark_bar().encode( x = 'time', y='dust' ) 
st.altair_chart(chart, use_container_width=True)     #use_container_width=True  가로로 화면에 꽉 채워줌.  

# with open(file_path, 'w') as f:
#     json.dump(dataframe, f)
