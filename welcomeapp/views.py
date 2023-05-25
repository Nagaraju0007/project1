from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=yellow><h1><center>welcome to lokeshit</center></h1><body></html>""")
    return res
