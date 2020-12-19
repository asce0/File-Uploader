from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import UploadForm

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Cv Uploaded Successfully!")
    else: 
        form = UploadForm()

    context = {
        'form':form,
    }
    return render(request, 'uploader/main.html', context)