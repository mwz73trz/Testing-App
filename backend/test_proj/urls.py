from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('test_auth.urls')),
    path('api/', include('test_app.urls')),
]
