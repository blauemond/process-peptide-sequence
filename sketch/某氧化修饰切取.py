import pandas as pd


df=pd.read_excel('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/O-PTM/sample4.xlsx')
ID=[]

n = 0
for info in df['ProteinDescription']:
    n = n + 1
    x = info.split("|")
    y = x[3]
    if (y.find(';'))==-1:
        ID.append(y)
    else:
        z=y.split(';')
        zz=z[0]
        ID.append(zz)
    print('运行至第',n,'次，蛋白质ID为',x[3])

df['ID']=ID
df.to_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/O-PTM/pres4.csv')
print('运行完毕')
