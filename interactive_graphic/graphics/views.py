# views.py

from django.shortcuts import render
import plotly.offline as opy
import plotly.graph_objs as go


def interactive_graphic(request):
    # Данные для оси x (значения от -10 до 10 с шагом 1)
    x = list(range(-10, 11))

    # Данные для оси y (значения функции y = 2x)
    y = [2 * val for val in x]

    # Создание интерактивного линейного графика
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

    # Добавление подписей осей и заголовка
    fig.update_layout(title='Интерактивный график функции y = 2x',
                      xaxis_title='x', yaxis_title='y')

    # Save the Plotly graph as a standalone HTML file
    graph_html = opy.plot(fig, auto_open=False, output_type='div')

    return render(request, 'graphics/interactive_graphic.html', {'graph_html': graph_html})
