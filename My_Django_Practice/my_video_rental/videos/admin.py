from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    fields = ["release_year", "title", "length"]

    search_fields = ["title", "length"]

    list_filter = ["release_year", "length"]

    list_display =["title", "length", "release_year"]

    list_editable = ["length", "release_year"]

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
