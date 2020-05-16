from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def date_input(request):
    return render(request, "date_input.html")


def capacity(request):
    return render(request, "capacity.html")


def login(request):
    return render(request, "login.html")


def bj_capacity(request):
    return render(request, "bj_capacity.html")


def qcl_capacity(request):
    return render(request, "qcl_capacity.html")

def pt_pg_capacity(request):
    return render(request, "pt_pg_capacity.html")

def car_message(request):
    return render(request, "car_message.html")

def qcl_daka(request):
    return render(request, "qcl_daka.html")

def pt_daka(request):
    return render(request, "pt_daka.html")

def pg_daka(request):
    return render(request, "pg_daka.html")


