from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group


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

# when view.login is called will send to loginPage.html
def loginRequest(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #stores the users in the variable user, including all their groups attributes
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #if it could find a user that made a match, log them in (essentially store them
            login(request, user)
            #if the user belongs to the group Reviewer, send them to the reviewer dashboard
            if user.groups.filter(name='Reviewer').exists():
                return redirect('reviewerDash/')
            # if the user belongs to the group Editor, send them to the editor dashboard
            elif user.groups.filter(name='Editor').exists():
                return redirect('editorDash/')
            # since author is the default, in all other cases send them to the author dashboard
            else:
                return redirect('authorDash/')

        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'loginPage.html', {'form': form})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'loginPage.html', {'form': form})

