from django.shortcuts import render

# when view.home is called will send to HomePage.html
def home(request):
    return render(request, 'HomePage.html')

# when view.login is called will send to loginPage.html
def login(request):
    return render(request, 'loginPage.html')


