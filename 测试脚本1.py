from Bio import SeqIO
import pandas as pd




'''
print("start?")
start = input('That is :')
print("end?")
end = input('That is :')
'''

aimseq = []
site = []
prid = []

n = 0
for seq_record in SeqIO.parse("D:/BaiduYunDownload/YZ Meng/python爬虫/测试用氨基酸/TIR.fasta", "fasta"):
    n = n + 1

    for index,AA in enumerate(seq_record):
         if AA == 'C':
             print(n,index)

             if index < 25:
                 c1 = (25-index)*'*' + str(seq_record.seq[0:(index+25)])
                 aimseq.append(c1)
                 print(c1)
             if (index + 25) > len(seq_record.seq):
                 c2 = str(seq_record.seq[(index-25):]) + (25-(len(seq_record.seq)-index)+1)*'*'
                 aimseq.append(c2)
                 print(c2)
             else:
                 c3 = str(seq_record.seq[(index-25):(index+25)])
                 aimseq.append(c3)
                 print(c3)

             site.append(index)
             prid.append(seq_record.id[3:9])
    print('\t')

while aimseq.count('')>0:
	aimseq.remove('')

data = {"uniprotID":prid,"site":site,"sequence":aimseq}
dfend = pd.DataFrame(data)
dfend.to_excel('D:\BaiduYunDownload\YZ Meng\python爬虫\测试用氨基酸\TIRseqC.xlsx')
