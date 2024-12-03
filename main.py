import pandas as pd
import matplotlib.pyplot as plt
Orignial_Data=pd.read_csv('Drug_Consumption.csv')
Drugs = ['Alcohol','Amphet','Amyl','Benzos','Caff','Cannabis','Choc','Coke','Crack','Ecstasy','Heroin','Ketamine','Legalh','LSD','Meth','Mushrooms','Nicotine','Semer','VSA']
Modified_Data = Orignial_Data

for i in range(len(Modified_Data)):
  j = 13
  while j < 31:

    if Modified_Data.iloc[i,j] == 'CL0' or Modified_Data.iloc[i,j] == 'CL1' or Modified_Data.iloc[i,j] == 'CL2':
      Modified_Data.iloc[i,j] = 0 #weighs CL0, CL1, CL2 as 0 because if have not used within a decade must not longer be regular user
    elif Modified_Data.iloc[i,j] == 'CL3':
      Modified_Data.iloc[i,j] = 1 #yearly is weighed as 1
    elif Modified_Data.iloc[i,j] == 'CL4':
      Modified_Data.iloc[i,j] = 12 #monthly is weighed as 12
    elif Modified_Data.iloc[i,j] == 'CL5':
      Modified_Data.iloc[i,j] = 52 #weekly is weighed as 52
    elif Modified_Data.iloc[i,j] == 'CL6':
      Modified_Data.iloc[i,j] = 100 #daily is weighed as 100 because not all CL6 are daily users
    j += 1
    
print('Data Reformatted successfully')
#reformat Education Row for legibility
for i in range(len(Modified_Data)):
  if Modified_Data.loc[i, 'Education'] == 'Doctorate degree':
    Modified_Data.loc[i, 'Education'] = 'PDH'
  if Modified_Data.loc[i, 'Education'] == 'Masters degree':
    Modified_Data.loc[i, 'Education'] = 'Masters'
  if Modified_Data.loc[i, 'Education'] == 'University degree':
    Modified_Data.loc[i, 'Education'] = 'Degree'
  if Modified_Data.loc[i, 'Education'] == 'Professional certificate/ diploma':
    Modified_Data.loc[i, 'Education'] = 'Certificate'
  if Modified_Data.loc[i, 'Education'] == 'Some college or university, no certificate or degree':
    Modified_Data.loc[i, 'Education'] = 'Some College'
  if Modified_Data.loc[i, 'Education'] == 'Left school at 18 years':
    Modified_Data.loc[i, 'Education'] = 'Left at 18'
  if Modified_Data.loc[i, 'Education'] == 'Left school at 17 years':
    Modified_Data.loc[i, 'Education'] = 'Left at 17'
  if Modified_Data.loc[i, 'Education'] == 'Left school at 16 years':
    Modified_Data.loc[i, 'Education'] = 'Left at 16'
  if Modified_Data.loc[i, 'Education'] == 'Left school before 16 years':
    Modified_Data.loc[i, 'Education'] = 'Left before 16'
  
Reformat_Data = Modified_Data
#all category tables
#index 0 is education level index 1 is the sum of the drug score all indivduals in that education level index 2 is number individuals in that education level index 3 is average score for that education level

Education_Drug = [['PDH',0,0,0],
                  ['Masters',0,0,0],
                  ['Degree',0,0,0],
                  ['Certificate',0,0,0],
                  ['Some College',0,0,0],
                  ['Left at 18',0,0,0],
                  ['Left at 17',0,0,0],
                  ['Left at 16',0,0,0],
                  ['Left before 16',0,0,0]]

Age_Drug = [['18-24',0,0,0],
            ['25-34',0,0,0],
            ['35-44',0,0,0],
            ['45-54',0,0,0],
            ['55-64',0,0,0],
            ['65+',0,0,0]]

Country_Drug = [['UK',0,0,0],
                ['USA',0,0,0],
                ['Australia',0,0,0],
                ['Republic of Ireland',0,0,0],
                ['New Zealand',0,0,0],
                ['Other',0,0,0]]

Gender_Drug = [['M',0,0,0],['F',0,0,0]]

Ethnicity_Drug = [['White',0,0,0],
                  ['Asian',0,0,0],
                  ['Black',0,0,0],
                  ['Mixed-White/Black',0,0,0],
                  ['Mixed-White/Asian',0,0,0],
                  ['Mixed-Black/Asian',0,0,0]]
print('line 59')
def RunDrugCalc (Category,List_Drug, Drug1, Drug2, Drug3, Drug4, Drug5, Drug6,Title):
  #Category is the column name; List_Drug is the category table, Drug 1-3 are the Drugs that you want to test for correlation entry empty string to leave blank, UK only is a boolean to filter for only UK or not
  for i in range(len(List_Drug)):
    Category_Value = List_Drug[i][0]
    for j in range(len(Modified_Data)):
      if Modified_Data.loc[j,Category] == Category_Value:
        List_Drug[i][1] += Modified_Data.loc[j,Drug1]
        if not Drug2 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug2]
        if not Drug3 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug3]
        if not Drug4 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug3]
        if not Drug5 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug3]
        if not Drug6 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug3]
        List_Drug[i][2] += 1
    List_Drug[i][3] = List_Drug[i][1]/List_Drug[i][2]
  print(List_Drug)
  #plotting of the values
  x_value = []
  y_value =[]
  for i in range(len(List_Drug)):
    x_value.append(List_Drug[i][0])
    y_value.append(List_Drug[i][3])
  plt.bar(x_value, y_value)
  plt.title(Title)
  plt.xlabel(Category)
  plt.show()
  for i in range(len(List_Drug)):
    j=1
    while j < 3:
      List_Drug[i][j] = 0
      j +=1

RunDrugCalc('Education',Education_Drug,'Coke','Crack','Heroin','','','','Hard Drugs')
#RunDrugCalc('Age',Age_Drug,'Ecstasy','Ketamine','','','','','Title')