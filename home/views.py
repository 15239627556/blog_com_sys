from django.http import HttpResponse
from django.shortcuts import render
def main(request):
    return render(request,'main.html')
def login(request):
    return render(request,'login.html')
def login_logic(request):
    phone = request.POST.get('phone')
    code = request.POST.get('code')
    return HttpResponse('ok')
# Create your views here.
