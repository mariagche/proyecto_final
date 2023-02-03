
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from cafe.models import Cafe, Capsulas, Te, Cliente, Vendedor, Avatar
from cafe.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario

from cafe.views import *




# Create your views here.

@login_required # si pongo aca requiero logueo
def inicio(request):
    return render(
        request=request,
        template_name='cafe/inicio.html',
    )



class CafeListView(LoginRequiredMixin,ListView):
    model = Cafe
    template_name = "cafe/lista_cafe.html"


class CafeCreateView(CreateView):
    model = Cafe
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('crear_cafe')
    template_name = "cafe/formulario_cafe.html"


class CafeDetailView(LoginRequiredMixin, DetailView):
    model = Cafe
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/detalle_cafe.html"


class CafeUpdateView(LoginRequiredMixin, UpdateView):
    model = Cafe
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/formulario_cafe.html"


class CafeDeleteView(LoginRequiredMixin, DeleteView):
    model = Cafe
    success_url = reverse_lazy('listar_cafe')
    template_name = "cafe/confirmar_eliminacion_cafe.html"
     

def buscar_cafe(request):
    if request.method == "POST":
        data = request.POST
        cafe = Cafe.objects.filter(
            Q(tipo__contains=data['busqueda'])
        )
        contexto = {
            'cafe': cafe
        }
        return render(
            request=request,
            template_name='cafe/lista_cafe.html',
            context=contexto,
        )   

    
    


class CapsulasListView(LoginRequiredMixin, ListView):
    model = Capsulas
    template_name = "cafe/lista_capsulas.html"


class CapsulasCreateView(LoginRequiredMixin, CreateView):
    model = Capsulas
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/formulario_capsulas.html"


class CapsulasDetailView(LoginRequiredMixin, DetailView):
    model = Capsulas
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/detalle_capsulas.html"


class CapsulasUpdateView(LoginRequiredMixin, UpdateView):
    model = Capsulas
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_capsulas')
    template_name = "cafe/formulario_capsulas.html"


class CapsulasDeleteView(LoginRequiredMixin, DeleteView):
    model = Capsulas
    success_url = reverse_lazy('listar_Capsulas')
    template_name = "cafe/confirmar_eliminacion_capsulas.html"
    
def buscar_capsulas(request):
    if request.method == "POST":
        data = request.POST
        capsulas = Capsulas.objects.filter(
            Q(tipo__contains=data['busqueda'])
        )
        contexto = {
            'capsulas': Capsulas
        }
        return render(
            request=request,
            template_name='cafe/lista_capsulas.html',
            context=contexto,
        )


    
class TeListView(LoginRequiredMixin, ListView):
    model = Te
    template_name = "cafe/lista_te.html"


class TeCreateView(LoginRequiredMixin, CreateView):
    model = Te
    fields = ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/formulario_te.html"


class TeDetailView(LoginRequiredMixin, DetailView):
    model = Te
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/detalle_Te.html"


class TeUpdateView(LoginRequiredMixin, UpdateView):
    model = Te
    fields =  ['tipo', 'cantidad', 'descripcion', 'precio', 'fecha_entrega']
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/formulario_te.html"


class TeDeleteView(LoginRequiredMixin, DeleteView):
    model = Te
    success_url = reverse_lazy('listar_Te')
    template_name = "cafe/confirmar_eliminacion_te.html" 
    #cliente = models.ForeignKey(to="Cliente", on_delete=models.SET NULL)
    

def buscar_te(request):
    if request.method == "POST":
        data = request.POST
        te = Te.objects.filter(
            Q(tipo__contains=data['busqueda'])
        )
        contexto = {
            'te': te
        }
        return render(
            request=request,
            template_name='cafe/lista_te.html',
            context=contexto,
        )

 
#para los clientes

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cafe/lista_cliente.html"


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/formulario_cliente.html"


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/detalle_cliente.html"


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('listar_cliente')
    template_name = "cafe/formulario_cliente.html"


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')
    template_name = "cafe/confirmar_eliminacion_cliente.html"

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        cliente = Cliente.objects.filter(
            Q(apellido__contains=data['busqueda']) | Q(DNI__contains=data['busqueda'])
        )
        contexto = {
            'cliente': cliente
        }
        return render(
            request=request,
            template_name='cafe/lista_cliente.html',
            context=contexto,
        )   

# para los vendedores (ver como queda sino sacar)

class VendedorListView(LoginRequiredMixin, ListView):
    model = Vendedor
    template_name = "cafe/lista_vendedor.html"


class VendedorCreateView(LoginRequiredMixin, CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('crear_Vendedor')              #cambie por listar_vendedor
    template_name = "cafe/formulario_vendedor.html"


class VendedorDetailView(LoginRequiredMixin, DetailView):
    model = Vendedor
    success_url = reverse_lazy('lista_vendedor')
    template_name = "cafe/detalle_vendedor.html"


class VendedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'DNI', 'email']
    success_url = reverse_lazy('lista_vendedor')
    template_name = "cafe/formulario_vendedor.html"


class VendedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('lista_vendedor')
    template_name = "cafe/confirmar_eliminacion_vendedor.html"

#@login_required #para ponerle logueo a funcion 

def buscar_Vendedor(request):
    if request.method == "POST":
        data = request.POST
        vendedor = Vendedor.objects.filter(
            Q(apellido__contains=data['busqueda']) | Q(DNI__exact=data['busqueda'])
        )
        contexto = {
            'vendedor': vendedor
        }
        return render(
            request=request,
            template_name='cafe/lista_vendedor.html',
            context=contexto,
        )
    
 # configuro el registro
    
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='cafe/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='cafe/login.html',
        context={'form': form},
    )
    
class CustomLogoutView(LogoutView):
    template_name = 'cafe/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'cafe/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user
    
#agregado del avatar

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='cafe/formulario_avatar.html',
        context={'form': formulario},
    )
    

def acerca(request):
    return render(
        request=request,
        template_name='cafe/acerca.html',
    )

