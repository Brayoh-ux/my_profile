from django.contrib import admin
from .models import Pictures, Profile

@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfilAdmin(admin.ModelAdmin):
    pass