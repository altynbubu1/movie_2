from django.contrib import admin
from movie.models import Movie



class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "date")
    list_filter = ("name", "year", "date")
    search_fields = ("name", "year")



admin.site.register(Movie, MovieAdmin)

