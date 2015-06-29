from django.contrib import admin
from models import Page

class PageAdmin(admin.ModelAdmin):
    fields = ['url_string','image','link']

admin.site.register(Page, PageAdmin)