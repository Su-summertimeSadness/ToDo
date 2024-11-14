from django.shortcuts import render
from django.views.generic import View

from .forms import TagForm, ActionForm
from .models import *
from .utils import DataMixin, DataCreateMixin, UpdateMixin, DeleteMixin


# Create your views here.
class ActionDetail(DataMixin, View):
    model = Action
    template = 'todo/action_detail.html'


def actions_list(request):
    actions = Action.objects.all()
    return render(request, 'todo/index.html', context={'actions': actions})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tags_list.html', context={'tags': tags})


class TagDetail(DataMixin, View):
    model = Tag
    template = 'todo/tag_detail.html'


class ActionCreate(DataCreateMixin, View):
    form = ActionForm
    template = 'todo/action_create.html'


class TagCreate(DataCreateMixin, View):
    form = TagForm
    template = 'todo/tag_create.html'


class TagUpdate(UpdateMixin, View):
    model = Tag
    form = TagForm
    template = 'todo/tag_update.html'


class ActionUpdate(UpdateMixin, View):
    model = Action
    form = ActionForm
    template = 'todo/action_update.html'


class ActionDelete(DeleteMixin, View):
    model = Action
    template = 'todo/action_delete.html'
    redir = 'actions_list'


class TagDelete(DeleteMixin, View):
    model = Tag
    template = 'todo/tag_delete.html'
    redir = 'tags_list'
