from django.urls import path 

from cafe.views import *

from cafe.models import *

from cafe.views import inicio
from cafe.views import acerca

urlpatterns = [
    
    
    # URLS de cafes (basadas den Class Based Views, vistas basadas en clases)
    path('cafe/',CafeListView.as_view(),name="listar_cafe"),
    path('buscar-cafe/', buscar_cafe, name="buscar_cafe"),
    path('cafes/<int:pk>/', CafeDetailView.as_view(), name="ver_cafe"),
    path('crear-cafe/', CafeCreateView.as_view(), name="crear_cafe"),
    path('editar-cafe/<int:pk>/', CafeUpdateView.as_view(), name="editar_cafe"),
    path('eliminar-cafe/<int:pk>/', CafeDeleteView.as_view(), name="eliminar_cafe"),
    
    path('capsulas/',CapsulasListView.as_view(), name="listar_capsulas"),
    path('buscar-capsulas/', buscar_capsulas, name="buscar_capsulas"),
    path('capsulas/<int:pk>/', CapsulasDetailView.as_view(), name="ver_capsulas"),
    path('crear-capsulas/', CapsulasCreateView.as_view(), name="crear_capsulas"),
    path('editar-capsulas/<int:pk>/', CapsulasUpdateView.as_view(), name="editar_capsulas"),
    path('eliminar-capsulas/<int:pk>/', CapsulasDeleteView.as_view(), name="eliminar_capsulas"),
    
    path('Te/', TeListView.as_view(), name="listar_Te"),
    path('buscar-Te/', buscar_te, name="buscar_Te"),
    path('Te/<int:pk>/', TeDetailView.as_view(), name="ver_Te"),
    path('crear-Te/', TeCreateView.as_view(), name="crear_Te"),
    path('editar-Te/<int:pk>/', TeUpdateView.as_view(), name="editar_Te"),
    path('eliminar-Te/<int:pk>/', TeDeleteView.as_view(), name="eliminar_Te"),
    
    path('Vendedor/', VendedorListView.as_view(), name="listar_vendedor"),
    path('buscar-Vendedor/', buscar_Vendedor, name="buscar_Vendedor"),
    path('Vendedor/<int:pk>/', VendedorDetailView.as_view(), name="ver_Vendedor"),
    path('crear-Vendedor/', VendedorCreateView.as_view(), name="crear_Vendedor"),
    path('editar-Vendedor/<int:pk>/', VendedorUpdateView.as_view(), name="editar_Vendedor"),
    path('eliminar-Vendedor/<int:pk>/', VendedorDeleteView.as_view(), name="eliminar_Vendedor"),
    
    path('cliente/', ClienteListView.as_view(), name="listar_cliente"),
    path('buscar-cliente/', buscar_cliente, name="buscar_cliente"),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name="ver_cliente"),
    path('crear-cliente/', ClienteCreateView.as_view(), name="crear_cliente"),
    path('editar-cliente/<int:pk>/', ClienteUpdateView.as_view(), name="editar_cliente"),
    path('eliminar-cliente/<int:pk>/', ClienteDeleteView.as_view(), name="eliminar_cliente"),
    # URLS Usuario y sesion
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    # URLS de Perfil
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    # url acerca de mi url/view/variable
    path('acerca/', acerca, name="acerca"),
]