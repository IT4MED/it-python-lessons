import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Шаг 1: Загрузка и предобработка данных
# Предположим, что данные находятся в файле "medical_data.csv" с указанной структурой.
data = pd.read_csv('medical_data.csv')

# Шаг 2: Создание красивых графиков с помощью Seaborn
# Гистограмма распределения возраста
sns.histplot(data['age'], kde=True)
plt.title('Распределение возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

# Диаграмма рассеяния между возрастом и артериальным давлением верхнего уровня (ap_hi)
sns.scatterplot(x='age', y='ap_hi', data=data)
plt.title(
    'Диаграмма рассеяния между возрастом и артериальным давлением верхнего уровня')
plt.xlabel('Возраст')
plt.ylabel('Артериальное давление верхнего уровня')
plt.show()

# Ящик с усами для распределения артериального давления нижнего уровня (ap_lo) по полу (gender)
sns.boxplot(x='gender', y='ap_lo', data=data)
plt.title('Распределение артериального давления нижнего уровня по полу')
plt.xlabel('Пол')
plt.ylabel('Артериальное давление нижнего уровня')
plt.show()

# Шаг 3: Настройка стиля Seaborn
sns.set_style('whitegrid')
sns.set(font_scale=1.2)

# Создание тепловой карты (heatmap) корреляции между различными признаками
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Тепловая карта корреляции')
plt.show()
