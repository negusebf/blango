from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ("title",)}
  list_display = ["title", "author", "created_at"]
  # exclude = ["author"]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


