import pandas as pd
from Bio import SeqIO


'''
print("start?")
start = input('That is :')
print("end?")
end = input('That is :')
'''


#下面是读取全部人类蛋白质组进入一个大字典的脚本部分
dictseq = {}
n1 = 0
for seq_record in SeqIO.parse("[人]uniprot-proteome UP000005640.fasta", "fasta"):
    n1 = n1 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
    print('蛋白质组数据读取运行中，目前已至第',n1,'次，蛋白质ID为',yid)

#下面是逐个匹配的过程
df = pd.read_excel('测试样本.xlsx')
stseq = []
n2 = 0
for row in df.itertuples():
    aimid = row[1]
    aimsite = row[2]
    sseq = dictseq[aimid]

    if (aimsite<25):
        nonn=(26-aimsite)*'*'
        seq51 = nonn+sseq[0:aimsite+25]
    if (aimsite+24)>len(sseq):
        nonn=(25-(len(sseq)-aimsite))*'*'
        seq51 = sseq[aimsite-26:]+nonn
    else:
        seq51 = sseq[aimsite-26:aimsite+25]

    stseq.append(seq51)
    n2 = n2 + 1
    print('蛋白质序列匹配中,目前已经运行至第',n2,'个')


df['standard_sequence']=stseq
df.to_csv('human seqC.csv')
