from Bio import SeqIO
import pandas as pd



dictseq = {}
n = 0
for seq_record in SeqIO.parse("TIR.fasta", "fasta"):
    n = n + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
    print('运行至第',n,'次，蛋白质ID为',yid)
