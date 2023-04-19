from django.contrib import admin
from django.urls import path
from application.views import first

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first)
]
