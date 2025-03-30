
from django.shortcuts import render
import plotly.offline as opy
import plotly.graph_objs as go


def interactive_graphic(request):
    x = list(range(-10, 15))
    y = [2 * val for val in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))
    fig.update_layout(title='Интерактивный график функции y = 2x',
                      xaxis_title='x', yaxis_title='y')

    graph_html = opy.plot(fig, auto_open=False, output_type='div')
    return render(request, 'graphics/interactive_graphic.html', {'graph_html': graph_html})
