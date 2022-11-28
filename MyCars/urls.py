import statistics
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'MyCars'

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('login/', views.loginView.as_view(), name='login'),
    path('deslogar/', views.loginView.sair),
    path('cadastro/', views.cadastro.as_view(), name='cadastro'),
    path('editar/<int:pk>/', views.editCar.as_view(), name='editar'),
    path('apagar/<int:pk>/', views.apagar_carro.as_view(), name='deletar')
]