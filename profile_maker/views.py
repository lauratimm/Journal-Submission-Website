from django.http import FileResponse
from django.shortcuts import render
from .forms import Profile_Form
import io
from reportlab.pdfgen import canvas

from .models import User_Profile
# Source: https://data-flair.training/blogs/django-file-upload/
# Author: Laura Timm
# Date Created: March 29, 2020
# Date Updated:
# This checks if the file uploaded is a pdf or not if it is it goes to the create html page and the file is
# uploaded to the data base. If it is not a pdf it shows an error message.

FILE_TYPES = ['pdf']
def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='user_pr.display_picture.url')
