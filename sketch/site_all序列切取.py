import pandas as pd


df=pd.read_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/O-PTM/2/site_all-2.csv.')
position=[]

n = 0
for info in df['site']:
    n = n + 1
    xid = info.split("|")
    yid = xid[2]
    zid = yid.split("_")
    m = zid[2]
    position.append(m)
    print('运行至第',n,'次，蛋白质ID为',xid[1])

df['position']=position
df.to_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/O-PTM/2/site2')
print('运行完毕')
