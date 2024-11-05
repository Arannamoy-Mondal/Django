from django.shortcuts import render

def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1']
    }
    return render(request,'index.html',data)
