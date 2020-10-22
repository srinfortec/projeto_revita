from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar , name='listar' )
]