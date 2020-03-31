from django.shortcuts import render

#each of these are view requests that link the url pattern to the html webpage
def review_view(request):
    return render(request, 'reviewHome.html')

def reviewLogout_view(request):
    return render(request, 'HomePage.html')