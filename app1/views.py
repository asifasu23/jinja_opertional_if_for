from django.shortcuts import render

# Create your views here.
d = {'a':122,'b':15,'c':20,'d':23}
def a1_if_if_else(request):
    return render(request,'a1_if_if_else.html',d)

def a1_if_elif_if(request):
    return render(request,'a1_if_elif_if.html',d)