from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function_view_test(request):
    return HttpResponse("<h1>Hello World! Class-based View Test</h1>")



example of class 
class ClassName(ParentClassName):
    template_name = 'HTML template file name'
    model = ModelName
    # other logic in requred