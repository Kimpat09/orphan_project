from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name="index"),
    path ('About/', views.About, name="About"),
    path ('Gallery/', views.Gallery, name="Gallery"),
    path ('Login/', views.Login, name="Login"),
    path ('Dashboard/', views.Dashboard, name="Dashboard"),
    path ('Childrenlist/', views.Childrenlist, name="Childrenlist"),
    path ('Viewchildren/', views.Viewchildren, name="Viewchildren"),
]
