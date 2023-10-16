# **Introduction**
此示範程式皆為Python

# **2021年5月~2023年2月台灣疫情分析.py**
1.可以快速查詢到2021年5月~2023年2月每日的確診人數及死亡人數。
2.可以結合數據及圖表進行比對了解到疫情的增長速度。
3.快速了解到每月政府發佈的重要事件。

`注意!在執行程式前請確保已安裝所需的Python庫:'pandas'和'matplotlib'`

## 資料庫準備
請下載 'diagnosed_dead_data.csv' 以及 'major_event_data.csv'

檔案內的資料來源由<https://www.aweb.tpin.idv.tw/COVID-19/>取得

###### 導入所需的模組
- `pandas`：用於處理 csv 數據庫。
- `matplotlib`：用於繪製數據圖。
```js
import matplotlib.pyplot as plt
import pandas as pd
```

###### 創建三個class分別記錄疫情資料
第一個Diagnosed_data class 使用pandas讀取diagnosed_dead_data csv檔，紀錄每天的確診人數，並存至dictionary

第二個 Dead_data class 使用pandas讀取diagnosed_dead_data csv檔，記錄每天的死亡人數，並存至dictionary

第三個 Event_data class 使用pandas讀取major_event_data csv檔，記錄疫情重大事件，並存至dictionary
```js
class Diagnosed_data:
    def __init__(self):
        self.Diagnosed_people={}
        diagnosed_people_data=pd.read_csv("diagnosed_dead_data.csv")
        for index,row in diagnosed_people_data.iterrows():
            day=row["Time"]
            diagnosed_people=row["Diagnosed_people"]
            self.Diagnosed_people[day]=diagnosed_people 
            
class Dead_data:
    def __init__(self):
        self.Dead_people={}
        dead_people_data=pd.read_csv("diagnosed_dead_data.csv")
        for index,row in dead_people_data.iterrows():
            day=row["Time"]
            dead_people=row["Dead_people"]
            self.Dead_people[day]=dead_people    
            
class Event_data:
    def __init__(self):
        self.Major_event={}
        major_event_data=pd.read_csv("major_event_data.csv",encoding=("Big5"))
        for index,row in major_event_data.iterrows():
            day=row["Time"]
            event = row['Major_event']
            self.Major_event[day]=event    
```





