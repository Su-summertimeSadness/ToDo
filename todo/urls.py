from django.urls import path

from .views import *

urlpatterns = [
    path('', actions_list, name='actions_list'),
    path('action/create/', ActionCreate.as_view(), name='action_create'),
    path('action/<str:slug>/', ActionDetail.as_view(), name='action_detail'),
    path('action/<str:slug>/update/', ActionUpdate.as_view(), name='action_update'),
    path('action/<str:slug>/delete/', ActionDelete.as_view(), name='action_delete'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete'),
]
