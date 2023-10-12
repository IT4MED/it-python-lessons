import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a CSV file 'medical_data.csv' with columns
data = pd.read_csv('medical_data.csv')

# Print information about the DataFrame
print(data.info())

# Гистограмма возраста
plt.hist(data['Age'], bins=10)
plt.title('Гистограмма возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

# Диаграмма рассеяния возраста и состояния
plt.scatter(data['Age'], data['Condition'])
plt.title('Диаграмма рассеяния возраста и состояния')
plt.xlabel('Возраст')
plt.ylabel('Состояние')
plt.show()
