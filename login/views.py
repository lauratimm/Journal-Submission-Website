from django.shortcuts import render
from login.customizedAuthenticationForm import customizedAuthenticationForm


def loginauth(request):
    print(1)
    print(request.method)
    if request.method == 'POST':  # if the user has filled out the form we want to take the information and redirect?
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        form = customizedAuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request, 'authorHome.html', {})
        else:
            print("not a valid user")
    else:  # if the user is trying to navigate to the page we want to give them the from
        form = customizedAuthenticationForm()
    return render(request, 'loginPage.html', {'form': form})
