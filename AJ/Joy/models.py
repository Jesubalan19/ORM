from django.db import models
from django.contrib import admin
class Text_Book(models.Model):
    Barcode=models.IntegerField(primary_key="Barcode");
    Book_Title=models.CharField(max_length=25);
    Author_Name=models.CharField(max_length=25);
    Author_email=models.EmailField();
    DoP=models.DateField();
    Pages=models.IntegerField();
class Text_BookAdmin(admin.ModelAdmin):
    list_display=("Barcode","Book_Title","Author_Name","Author_email","DoP","Pages");