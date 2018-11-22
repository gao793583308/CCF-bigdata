import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#bench_mark =  pd.read_csv("./train_data/train_fund_return.csv", index_col=0)
#cor = pd.read_csv("./train_data/train_correlation.csv", index_col=0)
bench_mark =  pd.read_csv("./data/test_fund_return.csv", index_col=0)
predict_len = 5
alpha = 0.2
move = 0

fun_series = []
cor_true=[]
cor_ini =[]
#for i in range(len(cor)):
   # cor_true.append(cor.iloc[i][-1-move])
   # cor_ini.append(cor.iloc[i][-62-move])
fund_sumnum = 723
for Fund_number1 in range(fund_sumnum):
    series1 = []
    for i in bench_mark.iloc[Fund_number1]:
        series1.append(float(i))
    #print(np.mean(series1))
    mean = np.mean(series1)
    std = np.std(series1)



    exp1 = []
    exp2 = []
    exp3 = []
    exp1.append(series1[0])
    exp2.append(series1[0])
    exp3.append(series1[0])
    predict = []
    for i in range(1,len(series1)):
        exp1.append(alpha*series1[i]+(1-alpha)*exp1[i-1])
        exp2.append(alpha*exp1[i]+(1-alpha)*exp2[i-1])
        exp3.append(alpha*exp2[i]+(1-alpha)*exp3[i-1])
        at = 3 * exp1[-1] - 3 * exp2[-1] + exp3[-1]
        bt = alpha / (2 * (1 - alpha) * (1 - alpha)) * (
                (6 - 5 * alpha) * exp1[-1] - 2 * (5 - 4 * alpha) * exp2[-1] + (4 - 3 * alpha) * exp3[-1])
        ct = alpha * alpha / (2 * (1 - alpha) * (1 - alpha)) * (exp1[-1] - 2 * exp2[-1] + exp3[-1])
        predict.append(series1[i])
    #plt.plot(series1[1:])
    for i in range(predict_len):
        at = 3 * exp1[-1] - 3 * exp2[-1] + exp3[-1]
        bt = alpha / (2 * (1 - alpha) * (1 - alpha)) * (
                (6 - 5 * alpha) * exp1[-1] - 2 * (5 - 4 * alpha) * exp2[-1] + (4 - 3 * alpha) * exp3[-1])
        ct = alpha * alpha / (2 * (1 - alpha) * (1 - alpha)) * (exp1[-1] - 2 * exp2[-1] + exp3[-1])
        predict.append(at + bt + ct)
        exp1.append(alpha * predict[-1] + (1 - alpha) * exp1[-1])
        exp2.append(alpha * exp1[-1] + (1 - alpha) * exp2[- 1])
        exp3.append(alpha * exp2[-1] + (1 - alpha) * exp3[-1])
    temp=np.array(series1[-61+predict_len:]).tolist()
    for i in predict[-predict_len:]:
        temp.append(i)
    fun_series.append(temp)
pre_cor = []
for f1 in range(fund_sumnum):
    for f2 in range(f1 + 1, fund_sumnum):
        x1 = pd.Series(fun_series[f1])
        x2 = pd.Series(fun_series[f2])
        pre_cor.append(round(x1.corr(x2),8))

#print dif
#plt.plot(dif[0:300])
#plt.plot(cor_true[0:300])
# pre_cor = [pre_cor[i]*0.4+cor_ini[i]*0.6 for i in range(len(pre_cor))]
#print pre_cor
'''

score1 = 0
score2 = 0
for i in range(len(pre_cor)):
    score1 = score1 + abs(pre_cor[i]-cor_true[i])
    #4952 17524
    score2 = score2 + abs((pre_cor[i]-cor_true[i])/(1.5-cor_true[i]))
score1 = score1/len(pre_cor)
score2 = score2/len(pre_cor)
score = pow((2/(2+score2+score1)),2)
print ("predict_len:%lf score:%lf "%(predict_len,score))
#plt.plot(predict)
#plt.show()
'''
result_file = open("result_file_exp.csv","w")
result_file.write("ID,value\n")
for f1 in range(fund_sumnum):
    for f2 in range(f1+1,fund_sumnum):
        x1 = pd.Series(fun_series[f1])
        x2 = pd.Series(fun_series[f2])
        cor = x1.corr(x2)
        result_file.write("Fund "+str(f1+1)+"-Fund "+ str(f2+1))
        result_file.write(",")
        result_file.write(str(cor))
        result_file.write("\n")
        print("fund%d-fund%d:%lf" % (f1 + 1, f2 + 1, cor))
