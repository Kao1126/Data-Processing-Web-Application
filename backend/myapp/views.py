from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CSVUploadForm
import csv
from .infer import InferCSV
import pandas as pd
import json


@csrf_exempt
def uploadCSV(request):

    if request.method == 'POST' and request.FILES['csv_file']:

        uploaded_file = request.FILES['csv_file']
        file_type = request.FILES['csv_file'].name.split('.').pop()
   
        infer = InferCSV(csv_file=uploaded_file, file_type=file_type)
        types = infer.get_infer_types()
        return HttpResponse(json.dumps(types) )
    
    else:
        form = CSVUploadForm()
    return JsonResponse({'error': 'No file found in the request'}, status=400)