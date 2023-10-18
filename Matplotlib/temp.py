import matplotlib.pyplot as plt

# Данные для оси x (дни)
days = ['День 1', 'День 2', 'День 3', 'День 4', 'День 5']

# Данные для оси y (температура)
temperatures = [36.6, 37.2, 36.9, 37.5, 36.8]

# Построение графика
plt.plot(days, temperatures, marker='o', color='b')

# Добавление подписей осей и заголовка
plt.xlabel('Дни')
plt.ylabel('Температура, °C')
plt.title('Температурные показатели пациента')

# Отображение графика
plt.show()