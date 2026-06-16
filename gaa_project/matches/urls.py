from django.urls import path
from . import views
from . import views
from .views import logged_in_screen
urlpatterns = [
    path('', views.home, name='home'),
    path("logged_in_screen/",views.logged_in_screen, name="logged_in_screen"),
    path('signup/', views.signup, name='signup'),
]
#path("some_baseball/", views.some_baseball, name="some_baseball"),