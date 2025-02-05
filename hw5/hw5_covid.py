import requests 
import json
from collections import defaultdict
from datetime import datetime

increase = "positiveIncrease"
date = "date"
statename = "state"
state = ["al", "ar", "as", "az", "ca", "co", "ct", "dc", "de", "fl", "ga", "gu", "hi", "ia", "id", "il", "in", "ks", "ky", "la",
 "ma", "md", "me", "mi", "mn", "mo", "mp", "ms", "mt", "nc", "nd", "ne", "nh", "nj", "nm", "nv", "ny", "oh", "ok", "or", "pa", "pr", "ri", "sc", "sd", "tn", "tx", "ut",
 "va", "vi", "vt", "wa", "wi", "wv", "wy"]

example_url = " https://api.covidtracking.com/v1/states/"

#Make a list for each states url
state_url = []
for abr in state:
  url = example_url + abr + "/daily.json"
  state_url.append(url)

#Use urls to get the info for each state into python
for urrl in state_url:
  request = requests.get(urrl)
  data = request.json()
  st_name = data[0][statename]
  print("State name: " + st_name)
  
  #find the average increase, and round percentage to look better
  total = []
  for avg in data:
    total.append(avg[increase])
  average_in = round(sum(total) / len(total), 2)
  avg_day = print("Average number of new daily confirmed cases for the entire state dataset:", average_in)

  #Find date with the highest new covid cases,  had help from chatgpt on this, learned about lambda
  max_case = max(data, key=lambda x: x[increase])
  highest_date = max_case[date]
  print("Month with the highest new cases:", highest_date)

  #Most recent date with no new covid cases, again worked with chatgpt to understand this code and implement it
  no_cases = [entry for entry in data if entry[increase] == 0]
  most_recent = max(no_cases, key=lambda x: x[date])
  most_recent_date = most_recent[date]
  print("Most recent date with no new covid cases:", most_recent_date)

  #Month with highest new number of covid cases, worked with chatgpt quite a bit to understand this code, imported datetime and defaultdict as well
  monthly_cases = defaultdict(int)
  for dt in data:
    dayt_str = str(dt[date])
    dayt = datetime.strptime(dayt_str, "%Y%m%d")
    month = dayt.strftime("%Y-%m")
    monthly_cases[month] += dt[increase]
  max_month = max(monthly_cases, key=monthly_cases.get)
  month_max = print("Month with the highest new cases:", max_month)

  #Month with the lowest number of covid cases, very similar to max, and I learned more about datetime functions from chatgpt
  monthly_case = defaultdict(int)
  for dt in data:
    dayt_str = str(dt[date])
    dayt = datetime.strptime(dayt_str, "%Y%m%d")
    month = dayt.strftime("%Y-%m")
    monthly_case[month] += dt[increase]
  min_month = min(monthly_case, key=monthly_case.get)
  print("Month with the lowest new cases:", min_month)

  #Make the dictionary used to dump into a json file, and dump
  result = {
    "State name": st_name,
    "Average number of new daily confirmed cases for entire state dataset": average_in,
    "Date with the highest new number of covid cases": highest_date,
    "Most recent date with no new covid cases": most_recent_date,
    "Month with the highest new cases": max_month,
    "Month with the lowest new cases": min_month
  }
  with open("data5500_mycode/hw5/" + st_name + ".json", "w") as json_file:
    json.dump(result, json_file, indent=4)










