from django.contrib import admin
from .models import Articles
from .models import Books
# Register your models here.

admin.site.register(Articles)
admin.site.register(Books)