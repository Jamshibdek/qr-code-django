from django.shortcuts import render, redirect
from .models import QRCode
# Create your views here.

def qr_home(request):
    if request.method == "POST":
        name = request.POST["name"]
        QRCode.objects.create(name=name)
        return redirect("/")
    qrs = QRCode.objects.all()
    
    return render(request, "qrhome.html", {"qrs":qrs})