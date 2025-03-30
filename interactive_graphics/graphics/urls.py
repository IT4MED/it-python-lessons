# fmt: off

from django.urls import path
from . import views

urlpatterns = [
    path('interactive_graph/', views.interactive_graphic, name='interactive_graphic'),
]