from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CSVUploadForm
import csv
from .infer import InferCSV
import pandas as pd
import json

def uploadCSV(request):

    if request.method == 'POST' and request.FILES['file']:

        uploaded_file = request.FILES['file']
   
        infer = InferCSV(csv_file=uploaded_file)
        types = infer.get_infer_types()

        return HttpResponse(json.dumps(types) )

        return render(request, 'success.html')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})


def sayHello(request):
    return HttpResponse('Hello World')

@csrf_exempt
def upload_file(request):
    
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        # uploaded_file = request.FILES['file']
        # Handle the uploaded file, save it, process it, etc.
        return JsonResponse({'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'error': 'No file found in the request'}, status=400)
