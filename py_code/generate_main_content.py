import pandas as pd
df=pd.read_csv("./shared_data.csv")
data_type=df["类别"].unique()
print(data_type)

total_str=""
for item in data_type:
    type_str=f"## {item}  \n"
    type_str+="|名称|时间范围|空间范围|时间分辨率|空间分辨率|简介|特征码| \n"
    type_str+="|-|-|-|-|-|-|-| \n"
    temp=df[df['类别']==item]
    for idx,row in temp.iterrows():
        type_str+=f"|{row['名称']}|{row['时间范围']}|{row['空间范围']}|{row['时间分辨率']}|{row['空间分辨率']}|{row['简介']}|{row['特征码']}| \n"
    total_str+=type_str
print(total_str)

init_md="""# 磁力分享科研数据  
`在实际的数据分享中，存在两个问题`  
1、数据分享过期  
2、数据存于网盘，下载速度慢  
`该项目尝试解决这两个问题`  
"""

f=open("README.md",mode='w',encoding='utf-8')
f.write(init_md+total_str)
f.close()