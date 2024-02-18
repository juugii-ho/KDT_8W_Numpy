import numpy as np
import pandas as pd

data = pd.read_csv('CARD_SUBWAY_MONTH_202312.csv')
data = pd.DataFrame(data)
# data = data.dropna()


print(data)


# print(data.dtypes)


'''
1. 각 지하철 역별 평균 이용객 수
2. 가 지하철 역별 이용객 수의 표준 편차
3. 가장 많은 이용객이 있는 역의 이용객 수
4. 가장 적은 이용객이 있는 역의 이용객 수
5. 이용객 수가 가장 많은 역의 이름
6. 이용객 수가 가장 적은 역의 이름
6. 이용객 수의 분포를 히스토그램으로 시각화하세요.

'''

# print(data['노선명'])