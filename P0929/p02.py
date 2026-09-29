import pandas as pd

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}


# DataFrame으로 변경후 영화,평점을 출력하시오.
# 영화 index로 지정하시오.
# 영화이름으로 역순정렬하시오.

df = pd.DataFrame(data)
print(df)
print(df['평점'])
df.set_index('영화',inplace=True)
print(df)

df.sort_index(inplace=True,ascending=False)
print(df)


import pandas as pd
df = pd.read_excel('file/score.xlsx',index_col='지원번호')

# 컬럼선택 : df[컬럼] , 2개이상 []리스트로 추가
df[['이름','키','학교']]
df.columns # 컬럼전체출력
df.columns[0]
df.columns[1]
df.columns[-1]     # 마지막 컬럼명 출력
df['SW특기']       # 마지막 컬럼 출력
df[df.columns[-1]] # 마지막 컬럼 출력
df[['이름','학교']]

df['이름']  #df[컬럼명만 들어갈수 있음]

# 컬럼 슬라이싱
df[ df.columns[[0,3,-1]] ] # 컬럼 슬라이싱
df[df.columns[1:4]]        # 컬럼 슬라이싱
df.columns[1:4]   # 컬럼명