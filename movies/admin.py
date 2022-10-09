from django.contrib import admin
from .models import *
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'isim', 'onetoone']
    list_display_links = ['id',]
    list_filter = ['kategori',]
    search_fields = ['isim', 'kategori__name']
    list_per_page = 2
    list_editable = ['isim',]
# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Kategori)
admin.site.register(Kategori2)
admin.site.register(Sub_category)
admin.site.register(Izlenenler)