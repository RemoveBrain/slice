import pandas as pd
data = pd.read_csv("./slice.csv",header=None)  #index 따로 없을시 숫자 순서대로 배치

data=data.fillna(" ") #data 내 nan 값 " "처리  nan 인채로 연산시 에러남 방지.

df = pd.DataFrame(data ={"이메일":[],"아이디":[],"이패스":[]}) #기존의 data에서 필요한 데이터만 따로 저장할 df 생성.
i = len(df)  # df의 i번째 위치에 새로운 행 추가.추가할때마다 i 증가.
j = 0        # data의 인덱스 추적. 
for email in data[5]:
    try:
        endex = email.index("@")                        #try 사용하게된 주범. @가 없을시 except로 가게됨.
        df.loc[i]=[email,email[0:endex],data[8][j]]     #email이 @가 포함된 이메일 형식일시 이메일 / 아이디 / 이패스 로 각각 데이터 저장.
        j+=1                                            
        i+=1                                            
    except:
        j+=1                                              

print(df)

df.to_csv("epass.csv")