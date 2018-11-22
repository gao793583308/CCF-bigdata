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

### 代码运行方式
### 使用三次指数模型做出预测
          python Three_exp.py
### 使用均值模型做出预测
          python average_model.py
          
