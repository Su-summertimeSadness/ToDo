from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .models import *


class DataMixin:
    model = None
    template = None

    def get(self, request, slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})


class DataCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST)
        if bound_form.is_valid():
            new_data = bound_form.save()
            return redirect(new_data)
        return render(request, self.template, context={'form': bound_form})


class UpdateMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj_form = self.form(instance=obj)
        return render(request, self.template, context={'form': obj_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class DeleteMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redir))


