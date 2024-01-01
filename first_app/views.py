from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    dic = {'name':'Uhai','age':24,'pet':['cat','dog','rabbit'],'courses':[
        {
        'title':'Basic c',
        'duration':4,
        'mark':'95%'
    },
        {
        'title':'OOP',
        'duration':2,
        'mark':'91%'
    },
        {
        'title':'Python Programming',
        'duration':3,
        'mark':'90%'
    },
    ],
    'date':datetime.datetime.now(),
    'default':"something",
    'default2':"",
    'val1':10,
    'arr1':[1,2,3,4],
    'arr2':[5,6,7,8,9],
    'capfirst':"bangladesh",
    'cut':"Python is the best programming language.",
    'lower':"this line will convert to",
    'upper':'This Line Will Convert To.',
    }
    return render(request,'home.html',dic)
