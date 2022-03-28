# Name : Shubham Sapkal
# Roll No. : 2012118
# subject: ML DL
# practical no. : 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 
# collect data
data = {'Temp': [10,30,44,28,36,19,50,37,42,31,43,18,30,55,24,15,29,40,36,51,45,41,39,24,18,47,28,40,30,36,29],
        'Celsius': [20,40,34,28,36,19,50,37,42,31,30,55,24,15,29,40,36,51,45,41,39,24,18,47,28,40,36,19,50,37,42]
}
# form dataframe
dataframe = pd.DataFrame(data, columns=['Temp', 'Celsius'])
print("Dataframe is : ")
print(dataframe)
plt.scatter(dataframe['Temp'], dataframe['Celsius'])
plt.plot(np.unique(dataframe['Temp']), np.poly1d(np.polyfit(dataframe['Temp'], dataframe['Celsius'], 1))(np.unique(dataframe['Temp'])), color='red')
plt.xlabel('Temp')
plt.ylabel('Celsius')
plt.show()
 
# form correlation matrix
matrix = dataframe.corr()
print("Correlation matrix is : ")
print(matrix)