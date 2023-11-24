import generics as generics
from django.shortcuts import render

# Create your views here.
from django.template import context
from django.views import generic

from credit.models import Client, Credit


class ClientListView(generic.ListView):
    context_object_name = 'client'
    template_name = 'client_list.html'

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()

        accounts = client.account_set.all()

        credits = Credit.objects.filter(account__in=accounts)


        context['accounts'] = accounts
        context['credits'] = credits
        return context
