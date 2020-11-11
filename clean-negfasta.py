import pandas as pd

path = input("type your path:")
name = input("type your file name:")


rst = name + 'negf.fasta'
aim= path+ '/' + name + "neg.csv"
resu=path+ '/' + rst
df1 = pd.read_csv(aim)

with open(resu,'a') as file_handle:
    n2=0
    for row in df1.itertuples():
        aimid = row[2]
        aimseq = row[4]
        if len(aimseq)==51 and aimseq[25]=='C':
            n2 = n2+1
            seq= f">seq_{name}neg_{n2}_{aimid}"+ "\n" + aimseq
            file_handle.write("{}\n".format(seq))
