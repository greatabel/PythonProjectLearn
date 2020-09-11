from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import DocumentForm
from .file_processor import handle_uploaded_file
# Create your views here.


def home(request):
    return render(request, 'vimss_app/home.html')


def simple_ms1(request):
    if request.method == 'POST':
        # print(request.FILES.getlist("document"),'#'*10)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            processed_files = handle_uploaded_file(request.FILES['document'], 'simple_ms1')
            form.save()
            # return redirect('home')
            return render(request, 'vimss_app/simple_ms1.html', {
                        'form': form, 'processed_files': processed_files
                    })
    else:
        form = DocumentForm()
    return render(request, 'vimss_app/simple_ms1.html', {
        'form': form
    })



def dia(request):
    return render(request, 'vimss_app/dia.html')


def multiple_sample(request):
    return render(request, 'vimss_app/multiple_sample.html')


def top_n(request):
    return render(request, 'vimss_app/top_n.html')
