from fileinput import filename
from sqlite3 import Timestamp
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from app.models import Data
import pandas as pd


# Create your views here.
def Home(request):
    if request.method == 'POST':
        new_data=request.FILES['myfile']
        print(new_data)
        df=pd.read_csv(new_data)
        for index, row in df.iterrows():
            value=Data(image_name=row['image_name'],objects_detected=row['objects_detected'],timestamp=row['timestamp'])
            value.save()
    else:
        pass
    return render(request,'app/index.html')



def Search(request):
    if request.method=='POST':
        sdate= request.POST.get('startdate')
        print(sdate)
        ldate= request.POST.get('lastdate')
        print(ldate)
        data=Data.objects.filter(timestamp__lte=ldate,timestamp__gte=sdate)
        print(data)
    else:
        pass
    return render(request,'app/index.html',{'datas':data})



