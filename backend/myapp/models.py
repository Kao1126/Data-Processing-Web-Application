from django.db import models

# Create your models here.

class CSVData(models.Model):
    file = models.FileField(upload_to='csv_files/')