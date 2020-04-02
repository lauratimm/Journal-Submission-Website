from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.template import RequestContext


# when view.home is called will send to HomePage.html
def home(request):
    function1 = "Contact Us"
    function2 = "Journals"
    function3 = "About Us"
    function4 = "Login"
    dashVariable = "/contact"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'HomePage.html', args)
g

# when view.login is called will send to loginPage.html
def loginRequest(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')

        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'loginPage.html', {'form': form})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'loginPage.html', {'form': form})
