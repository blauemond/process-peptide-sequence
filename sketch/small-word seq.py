#专门做小写字母
import pandas as pd
from Bio import SeqIO
​
​
df=pd.read_excel('ldes/sample4.xlsx')
stseq=[]
site=[]
nn = 0
​
for row in df.itertuples():
    aimid = row[1]
    aimseq = row[3]
    if (aimseq.find('c')>-1) and (aimseq.find('h')==-1):
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
        except:
            seq51="error"
            aimsite="error"
        
    else:
        seq51='error'
        aimsite='error'
            
    site.append(aimsite)
    stseq.append(seq51)
    nn=nn+1
    print('蛋白质序列匹配中,目前已经运行至第',nn,'个',aimid,'数字为',len(site),len(stseq),seq51)
   
​
    #while stseq.count('')>0:
    #stseq.remove('')
    
df['site']=site
df['standard_sequence']=stseq
df.to_csv('ldes/rs4.csv')
print("运行完毕！")
