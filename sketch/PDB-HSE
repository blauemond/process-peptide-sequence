import pandas as pd
from Bio import PDB
from Bio.PDB.PDBParser import PDBParser
import time
#import eventlet


df7 = pd.read_csv("pr62.csv")
unid2 = []
pdbid2 = []
site = []
HSE_BU = []
HSE_BD = []


upid_temp = ()
i=0
for row in df7.itertuples():
    ss=time.time()
    pdbid = 'pdb' + row[2] + '.ent'
    unipid = row[1]
    position = row[3]
    p = PDBParser(PERMISSIVE=1)
    if unipid!= upid_temp:
        try:
            s = p.get_structure(unipid,pdbid)
            m=s[0]
            print("建模成")
            RADIUS=12.0
            hse=PDB.HSExposureCB(m, RADIUS)
            residue_list=PDB.Selection.unfold_entities(m,'R')
            upid_temp = unipid
            print("运算成")
        except:
            pdbid = ('error!')
            residue_list=("s")
            print("跳过了:",unipid)
    try:
        for r in residue_list:
            if (r.get_resname()==CYS) and (r.get_id()[1]==position):
                BU = r.xtra['EXP_HSE_B_U']
                BD = r.xtra['EXP_HSE_B_D']
                print("匹配上了")
    except:
        BU = ("error!")
        BD = ("error!")
                
    unid2.append(unipid)
    pdbid2.append(pdbid)
    site.append(position)
    HSE_BU.append(BU)
    HSE_BD.append(BD)
    i=i+1
    ee=time.time()
    print("运行至第",i,"用时",ee-ss)

print("运行完毕，开始写入")
df4 = pd.DataFrame({'uniprotID':unid2, 'pdbID':pdbid2, 'sites':site, 'HSEBU':HSE_BU, 'HSEBD':HSE_BD})

df4.to_csv('pr42.csv',encoding='utf-8', index=False)
