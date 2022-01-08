from django.contrib import admin
from App4.models import AccessRecord,Topic,Webpage 
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
