import matplotlib.pyplot as plt

# Данные для оси x (значения от -5 до 5 с шагом 0.1)
x = [i / 10 for i in range(-50, 51)]

# Данные для оси y (значения функции y = x^2)
y = [i ** 2 for i in x]

# Построение графика
plt.plot(x, y)

# Добавление подписей осей и заголовка
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = x^2')

# Отображение графика
plt.show()
