import pandas as pd
from Bio import SeqIO

'''
dictseq = {}
n9 = 0
for seq_record in SeqIO.parse("ipi.HUMAN.v3.87.fasta", "fasta"):
    n9 = n9 + 1
    prexid = seq_record.id.split("|")
    xid=prexid[0].split(':')
    yid = xid[1]
    zid = yid.split('.')
    z = str(seq_record.seq)
    mm = zid[0]
    m = {mm:z}
    dictseq.update(m)
    print('蛋白质组数据读取运行中，目前已至第',n9,'次，蛋白质ID为',mm)
'''


df = pd.read_excel('ldes/sample1.xlsx')
stseq = []
site=[]
nn = 0
for row in df.itertuples():
    preaimid = row[1]
    if preaimid.isalnum():
        aimid = preaimid
    else:
        paimid = preaimid.split('.')
        aimid = paimid[0]
    aimseq = row[3]
    try:
        sseq = dictseq[aimid]
        for n,AA in enumerate(sseq):
            a=aimseq.index('C')
            b=len(aimseq)-a
            if ((AA=='C') and (sseq[n-a:n+b]==aimseq)):
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
        seq51='error'
        aimsite='error'
        site.append(aimsite)
        stseq.append(seq51)
    nn=nn+1
    if (nn-1)==len(site) and (nn-1)==len(stseq):
        site.append('error')
        stseq.append('error')
    print('蛋白质序列匹配中,目前已经运行至第',nn,'个',aimid,'数字为',len(site),len(stseq),seq51)

#while stseq.count('')>0:
#    stseq.remove('')

df['site']=site
df['standard_sequence']=stseq
df.to_csv('ldes/rs1.csv')
print("运行完毕！")
