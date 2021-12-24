import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from bs4 import BeautifulSoup

def merge(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12, list13):
      
    merged_list = [(list1[i], list2[i], list3[i], list4[i], list5[i], list6[i], list7[i], list8[i], list9[i], list10[i], list11[i], list12[i], list13[i]) for i in range(0, len(list1))]
    return merged_list

seasonContract = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/qbSeasonContracts.csv')

name = seasonContract['Name'].tolist()
year = seasonContract['Year'].tolist()
team = seasonContract['Team'].tolist()
baseSalary = seasonContract['Base Salary'].tolist()
proratedBonus = seasonContract['Prorated Bonus'].tolist()
rosterBonus = seasonContract['Roster Bonus'].tolist()
capNumber = seasonContract['Cap Number'].tolist()
capPercentage = seasonContract['Cap%'].tolist()
cashPaid = seasonContract['Cash Paid'].tolist()
guaranteedSalary = seasonContract['Guaranteed Salary'].tolist()
otherBonus = seasonContract['Other Bonus'].tolist()
workoutBonus = seasonContract['Workout Bonus'].tolist()
perGameRosterBonus = seasonContract['Per Game Roster Bonus'].tolist()

combinedTuple = merge(name, team, year, baseSalary, proratedBonus, rosterBonus, capNumber, capPercentage, cashPaid, guaranteedSalary, otherBonus, workoutBonus, perGameRosterBonus)

finalList = []
newNames = []
noList = []
for element in combinedTuple:
    name, team, year, baseSalary, proratedBonus, rosterBonus, capNumber, capPercentage, cashPaid, guaranteedSalary, otherBonus, workoutBonus, perGameRosterBonus = element
    if name not in noList and name not in newNames and year < 1994:
        noList.append(name)
    elif name not in newNames and (year >= 1994) and name not in noList:
        finalList.append(element)
        newNames.append(name)
    elif name in newNames:
        finalList.append(element)
print(finalList)