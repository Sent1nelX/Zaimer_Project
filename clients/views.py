from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from .models import Client, Passport
from django.views.generic import ListView, TemplateView

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    paginate_by = 50  # Количество записей на странице

    def get_queryset(self):
        # Получаем базовый queryset
        queryset = super().get_queryset()
        # Получаем поисковый запрос из параметров URL
        search_query = self.request.GET.get('search', '')
        
        # Фильтруем по полям, если есть поисковый запрос
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(middle_name__icontains=search_query)
            )
        return queryset

class PassportListView(ListView):
    model = Passport
    template_name = 'passport_list.html'
    context_object_name = 'passports'
    paginate_by = 50  # Количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        
        # Фильтруем по номеру паспорта, если есть поисковый запрос
        if search_query:
            queryset = queryset.filter(passport_number__icontains=search_query)
        return queryset

class ClientPassportListView(ListView):
    model = Passport
    template_name = 'client_passport_list.html'
    context_object_name = 'client_passports'
    paginate_by = 50  # Количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset().select_related('client')
        filter_type = self.request.GET.get('filter', 'all')

        # Фильтруем паспорта по связанным клиентам, если фильтр установлен
        if filter_type == 'linked':
            queryset = queryset.filter(client__isnull=False)
        return queryset


class HomePageView(TemplateView):
    template_name = 'home.html'  # Указываем, что шаблон будет называться 'home.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Перенаправление после успешной регистрации
    template_name = 'signup.html'
