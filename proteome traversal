import pandas as pd
from Bio import SeqIO

#全部蛋白质组
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
    print('人类蛋白质组数据读取运行中，目前已至第',n1,'次，蛋白质ID为',yid)

#大鼠
n2 = 0
for seq_record in SeqIO.parse("[大鼠]uniprot-proteome UP000002494.fasta", "fasta"):
    n2 = n2 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
    print('大鼠蛋白质组数据读取运行中，目前已至第',n2,'次，蛋白质ID为',yid)
    
#小鼠
n3 = 0
for seq_record in SeqIO.parse("[小鼠]uniprot-proteome UP000000589.fasta", "fasta"):
    n3 = n3 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
    print('小鼠蛋白质组数据读取运行中，目前已至第',n3,'次，蛋白质ID为',yid)
    
print('运行完毕')

#酵母
n4 = 0
for seq_record in SeqIO.parse("[酵母]uniprot-proteome UP000002311.fasta", "fasta"):
    n4 = n4 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
    print('酵母蛋白质组数据读取运行中，目前已至第',n4,'次，蛋白质ID为',yid)
    
print('运行完毕')


