from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name="index"),
    path ('About/', views.About, name="About"),
    path ('Gallery/', views.Gallery, name="Gallery"),
    path ('Login/', views.Login, name="Login"),
    path ('registration/', views.registration, name="registration"),
    path ('sign_out/', views.sign_out, name='sign_out'),
    path ('Dashboard/', views.Dashboard, name="Dashboard"),
    path ('Childrenlist/', views.Childrenlist, name="Childrenlist"),
    path ('Viewchildren/<int:pk>/', views.Viewchildren, name="Viewchildren"),
]
