#!/usr/bin/env python
# coding: utf-8

# In[50]:


import xml.etree.ElementTree as ET


# In[51]:


import pandas as pd


# In[52]:


tree=ET.parse('bankrupt_cases.xml')


# In[53]:


root=tree.getroot() # 최상위태그 파싱


# In[54]:


# 단위를 입력받아서 무슨 단위가 있는지 확인

a_units=[] # asset 단위
l_units=[] # liabilities 단위
for x in root:
    a_units.append(x.find('assets').attrib['unit'])
    l_units.append(x.find('liabilities').attrib['unit'])

a_unitset=set(a_units)
l_unitset=set(l_units)
print(a_unitset)
print(l_unitset)
# 결과 : assets과 liaibilites 단위는 million밖에 없음


# In[55]:


df_cols=["district","state","company_name","assets","assets unit","liabilities","liabilities unit"]

rows=[]

for node in root:
    try:
        s_assets=float(node.find('assets').text)
    except:
        s_assets=None
        
    try:
        s_liabilities=float(node.find('liabilities').text)
    except:
        s_liabilities=None
    
    s_district=node.find('district').text
    s_state=node.find('state').text
    s_company_name=node.find('company_name').text
    u_assets=node.find('assets').attrib['unit']
    u_liabilities=node.find('liabilities').attrib['unit']
    rows.append({'district':s_district,'state':s_state,'company_name':s_company_name,'assets':s_assets,'assets unit':u_assets,
                 'liabilities':s_liabilities,'liabilities unit':u_liabilities})
    
out_df=pd.DataFrame(rows,columns=df_cols)
out_df


# In[56]:


# 요약정보 출력
out_df.info()


# In[57]:


# 범주형 데이터 개수 확인

for col in ['state','district']:
    print('*'*3,col,'*'*3)
    print(out_df[col].value_counts(dropna=False))
    print('\n')


# In[58]:


# 각 열마다 누락데이터 개수
out_df.isnull().sum(axis=0)


# In[61]:


# 누락데이터 처리
# asset 열은 누락데이터 개수 4개이므로 데이터 손실이 우려되 평균값으로 대체한다.
# liabilities 열은 누락데이터 개수 1개이므로 삭제한다.(행 삭제)

df_lia=out_df.dropna(subset=['liabilities'],how='any').copy()
len(df_lia)


# In[62]:


# asset 열 누락 데이터 처리
mean_asset=df_lia['assets'].mean()
df_lia['assets'].fillna(mean_asset,inplace=True)


# In[63]:


# 누락데이터 처리가 잘됐는지 검토
df_lia['liabilities'].value_counts(dropna=False)


# In[64]:


df_lia.info()


# In[65]:


df_lia['assets'].value_counts(dropna=False)


# In[ ]:




