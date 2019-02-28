# from django.urls import path, include
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ListReservation.as_view()),
    path('<int:pk>/', views.DetailReservation.as_view()),
    path('rest-auth/', include('rest_auth.urls'))
]