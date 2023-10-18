import plotly.graph_objects as go

# Данные для оси x (значения от -5 до 25 с шагом 2)
x = list(range(-5, 25, 2))

# Данные для оси y (значения функции y = 2x)
y = [2 * val for val in x]

# Создание интерактивного линейного графика
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# Добавление подписей осей и заголовка
fig.update_layout(title='Интерактивный график функции y = 2x', xaxis_title='x', yaxis_title='y')

# Отображение графика
fig.show()