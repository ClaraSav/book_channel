from django.contrib import admin

from .forms import *
from .models import *


class LinkAdminInLine(admin.TabularInline):
    model = Link
    fields = ('url', 'platform_id')
    extra = 0


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    inlines = (LinkAdminInLine,)

admin.site.register(Languaje)
admin.site.register(Book, BookAdmin)
admin.site.register(Link)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Platform)
