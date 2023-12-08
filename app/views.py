from django.shortcuts import render

# Create your views here.
def data_render(request):
        data='This data is our assumption '
        d={'assumption':data}
        return render(request,'data_render.html',context=d)

def login (request):
        d={'username':'swetha','age':21}
        return render (request,'login.html',context=d)

def logout(request):
        d={'username':'ranga','age':22}
        return render(request,'logout.html',d)