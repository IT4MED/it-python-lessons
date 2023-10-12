from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs from the graphics app
    path('graphics/', include('graphics.urls')),
    # Add a direct route to the interactive_graphic view
    path('graphics/interactive_graph/', include('graphics.urls')),
]
