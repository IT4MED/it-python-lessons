import matplotlib.pyplot as plt

# Задаем данные
categories = ['A', 'B', 'C', 'D']
values = [15, 24, 30, 12]

# Создаем столбчатую диаграмму
plt.bar(categories, values)

# Настройка осей и заголовка
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.title('Столбчатая диаграмма')

# Отображаем диаграмму
plt.show()
