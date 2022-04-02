from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('login', views.Login,name="Login"),
    path('logout', views.user_logout,name="Logout"),
    path('register', views.register,name="register"),


    path('add-app', views.add_app,name="add_app"),
    path('home', views.home,name="home"),
    # path('view-app/<int:id>', views.view_app,name="view_app"),

    path('app/<int:id>', views.app,name="app"),
    path('point', views.point,name="point"),
    path('task', views.task,name="task"),
    path('add-point',views.add_point,name="add_point"),
    path('edit-profile',views.edit_profile,name="edit_profile")
]