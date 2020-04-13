from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def newAccount_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/newAccount.html', {'form': form})


# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from home import views
#
# # Create your views here.
# def newAccount_view(request):
#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #log the user in
#             return redirect('home:views.index')
#         # add redirect 'module:list'
#         # in articles urls
#         # urlpatterns=[
#         #   url('', views.article_list, name="list")
#
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/newAccount.html', {'form': form})
