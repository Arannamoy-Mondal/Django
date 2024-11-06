from django.shortcuts import render
import datetime
def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1'],
        "list":["Hello","Hi","Bye"],"time":datetime.datetime.now()
    }
    return render(request,'index.html',data)
