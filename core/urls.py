from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('ajax-pesquisar-endereco/', views.ajax_pesquisar_endereco, name='ajax_pesquisar_endereco'),
]