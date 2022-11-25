from django.shortcuts import render

# Create your views here.
d = {'a':122,'b':15,'c':20,'d':23}
def a2_nested_if(request):
    return render(request,'a2_nested_if.html',d)
def a2_forloop_(request):
    d = {'name':'asif'}
    return render(request,'a2_forloop_.html',d)
