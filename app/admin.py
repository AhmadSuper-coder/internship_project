from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from app.models import Data
# Register your models here.

# @admin.register(Data)
# class DataAdminModel(ImportExportModelAdmin):
#     list_display=['id','image_name','objects_detected','timestamp']

@admin.register(Data)
class ModelDAtaAdmin(admin.ModelAdmin):
    list_display=['id','image_name','objects_detected','timestamp']
