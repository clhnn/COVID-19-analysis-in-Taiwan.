import matplotlib.pyplot as plt
import pandas as pd

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
            
class Month_Chart:
    def __init__(self):
        self.Month_diagnosed_people=Diagnosed_data()
        self.Month_dead_people=Dead_data()
        
    def Month_diagnosed_people_chart(self,month):
        for day,diagnosed__people in self.Month_diagnosed_people.Diagnosed_people.items():
            if day.startswith(month):
                print(f"{day}確診的有{diagnosed__people}人")
        month_diagnosed_people_day=[] 
        month_diagnosed_people_num=[]
        for date,diagnosed_people in self.Month_diagnosed_people.Diagnosed_people.items():
            if date.startswith(month):
                month_diagnosed_people_day.append(date)
                month_diagnosed_people_num.append(diagnosed_people)
        plt.plot(month_diagnosed_people_day,month_diagnosed_people_num)
        plt.title(f"Diagnosed people in {month}")
        plt.xlabel("Day")
        plt.ylabel("Number of diagnosed people")
        plt.show()
        print(f"{month}月確診的人總共有:{sum(month_diagnosed_people_num)}人") 
            
    def Month_dead_people_chart(self,month):
        for day,dead__people in self.Month_dead_people.Dead_people.items():
            if day.startswith(month):
                print(f"{day}死亡的有{dead__people}人")
        month_dead_people_day=[] 
        month_dead_people_num=[]
        for date,dead_people in self.Month_dead_people.Dead_people.items():
            if date.startswith(month):
                month_dead_people_day.append(date)
                month_dead_people_num.append(dead_people)
        plt.plot(month_dead_people_day,month_dead_people_num)
        plt.title(f"Dead people in {month}")
        plt.xlabel("Day")
        plt.ylabel("Number of dead people")
        plt.show()
        print(f"{month}月死亡的人總共有:{sum(month_dead_people_num)}人")  

class Year_Chart:
    def __init__(self):
        self.Year_diagnosed_people=Diagnosed_data()
        self.Year_dead_people=Dead_data()
        
    def Year_diagnosed_people_chart(self, year):
        year_diagnosed_people_day=[] 
        year_diagnosed_people_num=[]
        for date,diagnosed_people in self.Year_diagnosed_people.Diagnosed_people.items():
            if date.startswith(year):
                year_diagnosed_people_day.append(date)
                year_diagnosed_people_num.append(diagnosed_people)
        plt.plot(year_diagnosed_people_day,year_diagnosed_people_num)
        plt.title(f"Diagnosed people in {year}")
        plt.xlabel("Day")
        plt.ylabel("Number of diagnosed people")
        plt.show()
        print(f"{year}年確診的人總共有:{sum(year_diagnosed_people_num)}人") 
        
    def Year_dead_people_chart(self, year):
        year_dead_people_day=[] 
        year_dead_people_num=[]
        for date,dead_people in self.Year_dead_people.Dead_people.items():
            if date.startswith(year):
               year_dead_people_day.append(date)
               year_dead_people_num.append(dead_people)
        plt.plot(year_dead_people_day,year_dead_people_num)
        plt.title(f"Dead people in {year}")
        plt.xlabel("Day")
        plt.ylabel("Number of dead people")
        plt.show()
        print(f"{year}年死亡的人總共有:{sum(year_dead_people_num)}人")     
        
class Data:
    def __init__(self):
        self.Event_data=Event_data()
        
    def Event(self, month):
        for date,major_event in self.Event_data.Major_event.items():
            if date.startswith(month):
                print(f"{date}:{major_event}")

class CovidQA:
    def __init__(self):
        self.covidqa_data=pd.read_csv("diagnosed_dead_data.csv")
        
    def max_month_diagnosed_people_question(self):
        data={}
        for index,row in self.covidqa_data.iterrows():
            year_month=row['Time'][:7]
            diagnosed=row['Diagnosed_people']          
            if year_month in data:
                data[year_month][row['Time']]=diagnosed
            else:
                data[year_month]={row['Time']:diagnosed}
        max_month=''
        max_diagnosed=0
        for key,value in data.items():
            if sum(value.values())>max_diagnosed:
                max_month=key
                max_diagnosed=sum(value.values())  
        print(max_month,"月有最多人確診")
        
    def min_month_diagnosed_people_question(self):
        data={}
        for index,row in self.covidqa_data.iterrows():
            year_month=row['Time'][:7]
            diagnosed=row['Diagnosed_people']          
            if year_month in data:
                data[year_month][row['Time']]=diagnosed
            else:
                data[year_month]={row['Time']:diagnosed}
        min_month=''
        min_diagnosed=float("inf")
        for key,value in data.items():
            if sum(value.values())<min_diagnosed:
                min_month=key
                min_diagnosed=sum(value.values())  
        print(min_month,"月有最少人確診")              

    def max_month_dead_people_question(self):
        data={}
        for index,row in self.covidqa_data.iterrows():
            year_month=row['Time'][:7]
            dead=row['Dead_people']          
            if year_month in data:
                data[year_month][row['Time']]=dead
            else:
                data[year_month]={row['Time']:dead}
        max_month=''
        max_dead=0
        for key,value in data.items():
            if sum(value.values())>max_dead:
                max_month=key
                max_dead=sum(value.values())  
        print(max_month,"月有最多人死亡")

    def min_month_dead_people_question(self):
        data={}
        for index,row in self.covidqa_data.iterrows():
            year_month=row['Time'][:7]
            dead=row['Dead_people']          
            if year_month in data:
                data[year_month][row['Time']]=dead
            else:
                data[year_month]={row['Time']:dead}
        min_month=''
        min_dead=float("inf")
        for key,value in data.items():
            if sum(value.values())<min_dead:
                min_month=key
                min_dead=sum(value.values())  
        print(min_month,"月有最少人死亡")

if __name__=="__main__":
    while True:
        print("2021年5月~2023年2月台灣疫情分析")
        print("1.查看每月確診人數折線圖")
        print("2.查看每月死亡人數折線圖")
        print("3.查看每年確診人數折線圖")
        print("4.查看每年死亡人數折線圖")
        print("5.查看每月疫情重大事項")
        print("6.疫情相關QA")
        print("7.離開系統")
        choice=input("請選擇要執行的操作(輸入1~7):")
        if choice=="1":
            diagnosed_people_month=input("請輸入月份(YYYY\MM):")
            diagnosed_people_chart=Month_Chart()
            diagnosed_people_chart.Month_diagnosed_people_chart(diagnosed_people_month)
        elif choice=="2":
            dead_people_month=input("請輸入月份(YYYY\MM):")
            dead_people_chart=Month_Chart()
            dead_people_chart.Month_dead_people_chart(dead_people_month)
        elif choice=="3":
            diagnosed_people_year=input("請輸入年份(YYYY):")
            diagnosed_people_chart=Year_Chart()
            diagnosed_people_chart.Year_diagnosed_people_chart(diagnosed_people_year)
        elif choice=="4":
            dead_people_year=input("請輸入月份(YYYY):")
            dead_people_chart=Year_Chart()
            dead_people_chart.Year_dead_people_chart(dead_people_year)
        elif choice=="5":
            event_data_month=input("請輸入月份(YYYY\MM):")
            event_data=Data()
            event_data.Event(event_data_month)
        elif choice=="6":
            print("QA1:哪個月的確診人數最多?")
            print("QA2:哪個月的確診人數最少?")
            print("QA3:哪個月的死亡人數最多?")
            print("QA4:哪個月的死亡人數最少?")
            month_covidqa=input("請輸入想詢問的問題(ex:QA1):")
            covidqa=CovidQA()
            if month_covidqa=="QA1":
               covidqa.max_month_diagnosed_people_question()
            elif month_covidqa=="QA2":
               covidqa.min_month_diagnosed_people_question()
            elif month_covidqa=="QA3": 
               covidqa.max_month_dead_people_question()
            elif month_covidqa=="QA4":
               covidqa.min_month_dead_people_question() 
            else:
                print("請輸入正確的編號 !")
        elif choice=="7":
            print("離開")
            break
        else:
            print("請輸入正確的選項 !")
        print("\n")    
            

        