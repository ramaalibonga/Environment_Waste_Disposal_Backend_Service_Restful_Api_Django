from django.contrib import admin 
from .models import Address, Landchange, Comment, Admin

admin.site.register(Address)
admin.site.register(Landchange)
admin.site.register(Comment)
admin.site.register(Admin)

