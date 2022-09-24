# Datawrangling_project

1. 데이터에 대한 설명
 
-1. 데이터의 tag와 attrib에 관한 설명
 사용한 데이터는 2011년에 파산법 11장에 따라 제출된 공기업의 파산사건 목록이다. tag 값은 district, state, company name, assets와 liabilities가 있다. 각각의 tag에 관한 정보는 다음과 같다.
-district : ND, SD, D 등 관할 구역에 관한 정보이다.
-state : 국가명을 국가 코드로 나타냈다. DE(독일), CA(캐나다), GA(가봉)등이 있다.
-company_name : 공기업 이름이다.
-assets: 기업의 자산이다. 
-liabilities: 부채, 채무에 관한 정보다.
두 가지 속성 값이 있었는데, 그것은 assets와 liabilities의 단위였다. 각 단위는 millions(100만)으로 통일된 상태다.

-2. 데이터 출처
https://catalog.data.gov/dataset/public-company-bankruptcy-cases-opened-and-monitored
사이트에서 구했고, 데이터는 Securities and Exchange Commission 이라는 미국 증권 거래 위원회 기관에서 비롯되었다. 

2. 누락데이터 평가

-1. 데이터 프레임 생성
 district, state, company_name, assets와 liabilities 총 5개의 태그 값과, assets와 liabilities의 속성 값 2개를 파싱하였다. 이때 assets와 liabilities는 수치형 데이터였기 때문에 float형태로 저장하기 위해 try ~ except 문을 사용하였다. try 문에는 float로 데이터의 태그값을 변경하도록 하였고, 만약 누락된 값일 경우 except 문으로 넘어가 None값이 저장되도록 하였다. 최종적으로 pandas 라이브러리를 이용해 out_df 라는 데이터프레임을 생성하였다. 

-2. 누락 데이터 평가
 각 열마다 누락 데이터가 있는지 평가하기 위해 3가지 방법을 이용하였다. 첫 번째, out_df.info()를 통해 각 열마다 누락 데이터가 아닌 데이터 개수를 출력하였다. 두 번째, 범주형 데이터 state와 district 열에서 범주형 값들의 개수와 Nan 값이 있는지 확인하기 위해 .value_counts(dropna=False) 메소드를 이용했다. 세 번째, 누락데이터의 개수를 직관적으로 파악하기 위해 .isnull().sum(axis=0) 메소드를 이용해 각 열마다 누락 데이터 개수를 확인하였다.

 그 결과, assets 열에 4개의 누락 데이터, liabilities 열에는 1개의 누락 데이터가 있었다.

-3. 누락 데이터 처리

 누락 데이터를 처리하는 방법에는 크게 제거와 대체라는 방법이 있다. assets 열은 liabilities 에 비해 누락 데이터가 4배 많기 때문에 제거를 하면 데이터 양이 손실될 것으로 판단하였다. 따라서 assets 열의 누락 데이터는 평균값으로 대체, liabilities 열은 행을 제거하는 방향으로 선택하였다. 그 이유는 liabilties 는 분석에 꼭 필요한 속성이기 때문에 열을 제거할 수는 없기 때문이다.

 우선 행을 제거하기 위해 .dropna(subset=['liabilities'],how='any'] 메소드를 사용하고 결과를 새로운 데이터 프레임 df_lia 에 저장하였다. 해당 메소드는 liabilities 열에 있는 값이 Nan이면 해당 행을 삭제한다는 의미이다. assets열 누락 데이터 처리를 위해 우선 .mean()으로 평균값을 구하고 .fillna(평균값, inplace=True)를 적용하였다. inplace=True 속성은 데이터 프레임을 직접 수정하여 새로운 데이터 프레임을 생성할 필요가 없다는 뜻이다. 

-4. 검토

 누락 데이터를 처리하고 난후, .value_counts(dropna=False)메소드와 .info()로 처리가 완료되었는지 확인하였다. 행을 하나 제거하였기 때문에 모든 열을 61개의 non-null 값을 갖고 있고, liabilties열과 assets 열에 Nan값이 없음을 확인하였다. 
