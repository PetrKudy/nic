from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Domain, DomainFlag


class IndexListView(ListView):
    template_name = 'index.html'
    model = Domain

    def get_context_data(self, **kwargs):
        data = {'data': Domain.objects.filter(erdate=None)}
        return data


class DetailView(DetailView):
    template_name = 'detail.html'
    model = Domain

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain_flags'] = DomainFlag.objects.filter(domain=context['object'].id).exclude(flag='EXPIRED')
        return context
