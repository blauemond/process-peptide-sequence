f=open("D:\BaiduYunDownload\YZ Meng\work\你的综述\cysteine-modification\孟彦铮cys修饰结果汇总\Oxidation\cs2.txt")
with open('D:\BaiduYunDownload\YZ Meng\work\你的综述\cysteine-modification\孟彦铮cys修饰结果汇总\Oxidation\css2.txt','a') as file_handle:
        i=0
        for line in f.readlines():
                i=i+1
                line = line.strip('\n')
                if len(line)==51:
                    seq= f">seq{i}"+ "\n" + line
                    file_handle.write("{}\n".format(seq))
