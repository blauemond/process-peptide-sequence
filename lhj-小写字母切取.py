import pandas as pd


df=pd.read_excel('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/LDEs/pres5.xlsx')
seq=[]
ID=[]

n = 0
for info in df['Replicate']:
    n = n + 1
    x = info.split("-")
    y = x[0]
    seq.append(y)
    z = x[1]
    ID.append(z)
    print('运行至第',n,'次，蛋白质ID为',x[1])

df['ID']=ID
df['seq']=seq
df.to_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/LDEs/pres5_5.csv')
print('运行完毕')

for row in df.itertuples():
    aimid = row[1]
    aimseq = row[3]
    if aimseq.find('h')>-1:
        seq51="error"
        aimsite="error"
        site.append(aimsite)
        stseq.append(seq51)
    else:
        a=aimseq.find('c')
        b=len(aimseq)-a
        c=aimseq.upper()
        try:
            sseq = dictseq[aimid]
            n=0
            for n,AA in enumerate(sseq):
                if ((AA=='C') and (c==sseq[n-a:n+b])):
                    aimsite=n+1
                    if aimsite < 26:
                        seq51 = (26-aimsite)*'*' + sseq[0:aimsite+25]
                    elif (aimsite+24) > len(sseq):
                        seq51 = sseq[aimsite-26:] + (25-(len(sseq)-aimsite))*'*'
                    else:
                        seq51 = sseq[aimsite-26:aimsite+25]
                    site.append(aimsite)
                    stseq.append(seq51)
        except:
            seq51="error"
            aimsite="error"
            site.append(aimsite)
            stseq.append(seq51)
        nn=nn+1
        print('蛋白质序列匹配中,目前已经运行至第',nn,'个',aimid,'数字为',len(site),len(stseq),seq51)


    #while stseq.count('')>0:
    #stseq.remove('')

df['site']=site
df['standard_sequence']=stseq
df.to_csv('ldes/rs4.csv')
print("运行完毕！")
