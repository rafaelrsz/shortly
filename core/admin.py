from django.contrib import admin
from .entities.shorturl import *
from .entities.click import *
from .entities.urltag import *

admin.site.register(ShortURL)
admin.site.register(URLTag)
admin.site.register(Click)