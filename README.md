# CCF-大数据竞赛-基金间的相关性预测-复赛19名
### <a href = "https://www.datafountain.cn/competitions/312/details/data-evaluation">赛题介绍</a>
### 队伍名称：萌仔仔zm    
### 队员:drxkm0、张萌20172014、gyq、DFUser1537867702929
### 运行代码前，需要将数据放在data目录下，目录树如下：
     |--data
         |--correlation.csv
         |--test_fund_return.csv
     |--Three_exp.py
     |--average_model.py
#### correlation.csv 是手动把训练集和测试集的相关性数据拼合起来，一共是539天的数据
#### test_fund_retuen.csv 直接取比赛提供的测试集数据，未作处理

#### 代码运行方式(需要安装pandas，numpy)
#### 使用三次指数模型做出预测（生成预测结果result_file_exp.csv）
          python Three_exp.py
#### 使用均值模型做出预测(生成预测结果mean_1026.csv)
          python average_model.py

### 整体思路
### 思路1:
          基金间的相关性数据基于从对应日期开始向后61个交易日的市场数据和运营权重综合统计得出,因此要想得到最后一天的相关系数只需要向后预测61天的基金复权净值收益率，然后计算相关系数即可，实际实验发现预测时间太长精度比较低，于是缩短预测的时间长度，最终采用了往后预测5天，然后加上已知的56天的数据来计算相关系数，作为预测的结果，预测方法采用三次指数平滑
### 思路2:
          基金的相关性数据短时间内变化很大，但变化趋势往往在一个范围内，首先对已知的539天的相关性数据去除最大的和最小的10个值，然后直接计算均值作为预测结果

