print('beginning')
import pandas as pd
import matplotlib.pyplot as plt
print('imports success')
Orignial_Data=pd.read_csv('Drug_Consumption.csv')
 #drug varaibles
ID = 0
Age = 1
Gender = 2
Education = 3
Country = 4
Ethnicity = 5
Alcohol = 13
Amphet = 14
Amyl = 15
Benzos = 17
Caffeine = 18
Cannabis = 19
Chocolate = 20
Coke = 21
Crack = 22
Ecstasy = 23
Heroin = 24
Ketamine = 25
Legalh = 26
LSD = 27
Meth = 28
Mushroom = 29
Nicotine = 30
VSA = 32

Drugs = ['Alcohol','Amphet','Amyl','Benzos','Caff','Cannabis','Choc','Coke','Crack','Ecstasy','Heroin','Ketamine','Legalh','LSD','Meth','Mushrooms','Nicotine','Semer','VSA']
plt.show()
Modified_Data = Orignial_Data

for i in range(len(Modified_Data)):
  j = 14
  while j < 31:

    if Modified_Data.iloc[i,j] == 'CL0' or Modified_Data.iloc[i,j] == 'CL1' or Modified_Data.iloc[i,j] == 'CL2':
      Modified_Data.iloc[i,j] = 0
    elif Modified_Data.iloc[i,j] == 'CL3':
      Modified_Data.iloc[i,j] = 1
    elif Modified_Data.iloc[i,j] == 'CL4':
      Modified_Data.iloc[i,j] = 12
    elif Modified_Data.iloc[i,j] == 'CL5':
      Modified_Data.iloc[i,j] = 52
    elif Modified_Data.iloc[i,j] == 'CL6':
      Modified_Data.iloc[i,j] = 100
    j += 1
print('line 49')
Education_Drug = [['Doctorate degree',0,0,0],
                  ['Masters degree',0,0,0],
                  ['University degree',0,0,0],
                  ['Professional certificate/diploma',0,0,0],
                  ['Some college or university, no certificate or degree',0,0,0],
                  ['Left school at 18 years',0,0,0],
                  ['Left school at 17 years',0,0,0],
                  ['Left school at 16 years',0,0,0],
                  ['Left school before 16 years',0,0,0]]
#index 0 is education level index 1 is the sum of the drug score all indivduals in that education level index 2 is number individuals in that education level index 3 is average score for that education level
print('line 60')
for i in range(len(Education_Drug)):
  education_level = Education_Drug[i][0]
  Drug = 'Heroin'
  for j in range(len(Modified_Data)):
    if Modified_Data.loc[j,'Education'] == education_level:
      Education_Drug.loc[i,1] += Modified_Data.loc[j,Drug]
      Education_Drug.loc[i,2] += 1
  Education_Drug[i][3] = Education_Drug[i][1]/Education_Drug[i][2]

plt.bar(Education_Drug[0], Education_Drug[3])
plt.show()
input()


#for index, row in Modified_Data.iterrows()


