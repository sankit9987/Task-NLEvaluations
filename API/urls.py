from django.urls import path,include
from .views import *

urlpatterns = [
    path('all-app/', AppSerializer.as_view(),name="view_app"),
    path('view-app/<int:id>', View_appSerializer.as_view(),name="view_app"),
    path('add', AddAppSerializer.as_view(),name="add"),
]