import pandas as pd
import matplotlib.pyplot as plt

# Путь к CSV-файлу с данными
input_file_path = 'input/medical_data_input.csv'

# Чтение CSV-файла в DataFrame
medical_data = pd.read_csv(input_file_path)

# Вывод первых нескольких строк DataFrame
print("Первые несколько строк данных:")
print(medical_data.head())

# Базовая предобработка данных (можно добавить дополнительные шаги предобработки при необходимости)
# Преобразование 'Age' в числовой формат
medical_data['Age'] = pd.to_numeric(medical_data['Age'], errors='coerce')

# Визуализация данных
# Гистограмма возраста
medical_data['Age'].plot(kind='hist', bins=20,
                         edgecolor='black', figsize=(10, 6))
plt.title('Гистограмма возраста')
# !
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

# Столбчатая диаграмма диагнозов!
condition_counts = medical_data['Condition'].value_counts()
condition_counts.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Распределение медицинских состояний')
plt.xlabel('Состояние')
plt.ylabel('Количество')
plt.show()
