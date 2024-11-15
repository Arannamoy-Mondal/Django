from django.shortcuts import render
import datetime
def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1'],
        "list":["Hello","Hi","Bye"],"time":datetime.datetime.now(),"empty":"","truncate":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa corporis quae, fugiat, ex inventore tenetur"
        +"delectus culpa placeat quibusdam incidunt rerum. Natus facilis ipsam velit aspernatur, temporibus error"
        +"provident ipsum!"
    }
    return render(request,'index.html',data)
