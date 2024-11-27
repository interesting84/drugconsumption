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
#all category tables
#index 0 is education level index 1 is the sum of the drug score all indivduals in that education level index 2 is number individuals in that education level index 3 is average score for that education level

Education_Drug = [['Doctorate degree',0,0,0],
                  ['Masters degree',0,0,0],
                  ['University degree',0,0,0],
                  ['Professional certificate/ diploma',0,0,0],
                  ['Some college or university, no certificate or degree',0,0,0],
                  ['Left school at 18 years',0,0,0],
                  ['Left school at 17 years',0,0,0],
                  ['Left school at 16 years',0,0,0],
                  ['Left school before 16 years',0,0,0]]

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
def RunDrugCalc (Category,List_Drug, Drug1, Drug2, Drug3):
  #Calculates the weight
  #Category is the column name; List_Drug is the category table, Drug 1-3 are the Drugs that you want to test for correlation entry empty string to leave blank
  print(List_Drug)
  for i in range(len(List_Drug)):
    Category_Value = List_Drug[i][0]
    for j in range(len(Modified_Data)):
      if Modified_Data.loc[j,Category] == Category_Value:
        List_Drug[i][1] += Modified_Data.loc[j,Drug1]
        if not Drug2 == '':
          List_Drug[i][1] += Modified_Data.loc[j,Drug2]
        if not Drug3 == '':
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
  plt.show()
  for i in range(len(List_Drug)):
    j=1
    while j < 3:
      List_Drug[i][j] = 0
      j +=1

RunDrugCalc('Age',Age_Drug,'Ecstasy','Ketamine','')