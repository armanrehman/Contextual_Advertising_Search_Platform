from django.contrib import admin

#importing models
from .models import Tag,Advert

# Register your models here.
admin.site.register(Tag)
admin.site.register(Advert)  

