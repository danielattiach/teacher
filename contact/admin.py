from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'subject', 'name', 'email', 'contact_date', 'author', 'author_name', 'target', 'target_name')
  list_display_links = ('id', 'subject')
  search_fields = ('name', 'email', 'subject')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)