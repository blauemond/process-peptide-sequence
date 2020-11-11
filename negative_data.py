import pandas as pd
from Bio import SeqIO


'''
print("start?")
start = input('That is :')
print("end?")
end = input('That is :')
'''


#下面是读取全部蛋白质组进入一个大字典的脚本部分
dictseq = {}
n1 = 0
for seq_record in SeqIO.parse("D:\BaiduYunDownload\YZ Meng\python爬虫\测试用氨基酸\[人]uniprot-proteome UP000005640.fasta", "fasta"):
    n1 = n1 + 1
    xid = seq_record.id.split("|")
    yid = xid[1]
    z = str(seq_record.seq)
    m = {yid:z}
    dictseq.update(m)
print('over!')

#下面是逐个匹配的过程
df1 = pd.read_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/孟彦铮cys修饰结果汇总/Oxidation/rs5.csv')
uid=[]
negseq=[]
ssit=[]
n2 = 0
for row in df1.itertuples():
    try:
        n2 = n2 + 1
        aimid = row[2]
        aimsite = row[3]
        sseq = dictseq[aimid]
        n3 = 0

        for index,AA in enumerate(sseq):
            n3 = n3 + 1
            if (AA == 'C') and ((index + 1) != aimsite):
                index=index+1
                try:
                    if (index<26):
                        nonn=(26-index)*'-'
                        seq51 = nonn+sseq[0:index+25]
                    elif (index+24)>len(sseq):
                        nonn=(25-(len(sseq)-index))*'-'
                        seq51 = sseq[index-26:]+nonn
                    else:
                        seq51 = sseq[index-26:index+25]
                except:
                        seq51=''

                uid.append(aimid)
                ssit.append(n3)
                negseq.append(seq51)
    except:
        print('error in this')


alldict={'ID':uid,'site':ssit,'Seq':negseq}
df2=pd.DataFrame(alldict)
df2.to_csv('D:/BaiduYunDownload/YZ Meng/work/你的综述/cysteine-modification/孟彦铮cys修饰结果汇总/Oxidation/rs5neg.csv')
print("over!!")
