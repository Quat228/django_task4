from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic

from . import models


class IndexView(generic.ListView):
    model = models.Client
    template_name = "client.html"
    context_object_name = "clients"

    def get_queryset(self):
        return self.model.objects.all()

    def post(self, request):
        return redirect(reverse("detail", kwargs={"pk": request.POST.get("client")}))


class DetailView(generic.DetailView):
    model = models.Client
    # template_name = "detail.html"
