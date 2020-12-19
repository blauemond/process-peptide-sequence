import pandas as pd
from Bio import SeqIO


print("Please load your proteome information.")
prot = input("That is:")
print("Please type your input file name.")
inp = input("That is :")
print("Please type your output file name.")
outp = input("That is :")



#下面是读取全部蛋白质组进入一个大字典的脚本部分
dictseq = {}
n1 = 0
for seq_record in SeqIO.parse(prot, "fasta"):
    n1 = n1 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
print("加载完毕！")


#下面是逐个匹配的过程
df = pd.read_csv(inp)
stseq = []
n2 = 0
for row in df.itertuples():
    aimid = row[1]
    aimsite = row[2]
    sseq = dictseq[aimid]
    
    try:
        if (aimsite<25):
            nonn=(26-aimsite)*'-'
            seq51 = nonn+sseq[0:aimsite+25]
        elif (aimsite+24)>len(sseq):
            nonn=(25-(len(sseq)-aimsite))*'-'
            seq51 = sseq[aimsite-26:]+nonn
        else:
            seq51 = sseq[aimsite-26:aimsite+25]
    except:
        seq51 = "error"

    stseq.append(seq51)
    n2 = n2 + 1
print("匹配完毕！")

df['standard_sequence']=stseq
df.to_csv(outp)
print("over!")
