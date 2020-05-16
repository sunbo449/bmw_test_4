from django.urls import path
from mycar import views

app_name = "mycar"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("date_input", views.date_input, name="date_input"),
    path("capacity", views.capacity, name="capacity"),
    path("bj_capacity", views.bj_capacity, name="bj_capacity"),
    path("qcl_capacity", views.qcl_capacity, name="qcl_capacity"),
    path("pt_pg_capacity", views.pt_pg_capacity, name="pt_pg_capacity"),
    path("car_message", views.car_message, name="car_message"),
    path("qcl_daka", views.qcl_daka, name="qcl_daka"),
    path("pt_daka", views.pt_daka, name="pt_daka"),
    path("pg_daka", views.pg_daka, name="pg_daka"),
]


