from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    function1 = "Contact Us"
    function2 = "Journals"
    function3 = "About Us"
    function4 = "Login"
    dashVariable = "/contact"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'home/home.html', args)