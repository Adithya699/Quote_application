from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_quote, name='add_quote'),
]
