from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings


# when view.home is called will send to HomePage.html
def home(request):
    # the labels for all of the buttons, variables because this is a template and is inherited through-out
    # the pages, including the dashboards
    function1 = "Contact Us"
    function2 = "Journals"
    function3 = "About Us"
    function4 = "Login"

    #variables for the path of one of the buttons
    dashVariable = "/contact"

    #the dictionary that contains all the labels and pairs them as the value of their function within the
    #tempalte
    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    #render that page with all of the customized arguments
    return render(request, 'HomePage.html', args)

# when view.login is called will send to loginPage.html
def loginRequest(request):
    # the method will be a post if the log in button was pushed, thus data must be grabbed from the form

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

        # the user did not exist in the database, thus redirect them to the same sign in page
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'loginPage.html', {'form': form})

    # the method was not a post, thus the user is navigating or reloaded the page, thus no data
    # should be grabbed and the page should just be loaded

    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'loginPage.html', {'form': form})

def index(request):
    # the labels for all of the buttons, variables because this is a template and is inherited through-out
    # the pages, including the dashboards
    function1 = "Contact Us"
    function2 = "Journals"
    function3 = "About Us"
    function4 = "Login"

    # variables for the path of one of the buttons
    dashVariable = "/contact"
    dashVariable2 = "/login"
    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable, 'dashVariable2': dashVariable2}
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['alexandratenney@hotmail.ca'],
                  fail_silently=False)
        return render(request, 'contactUs.html', args)
    else:
        return render(request, 'contactUs.html', args)