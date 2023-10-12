from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphics/', include('graphics.urls')),
    path('graphics/interactive_graph/', include('graphics.urls')),
]
