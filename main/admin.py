from django.contrib import admin
from .models import Post, PostImages



class PostImageItem(admin.StackedInline):
    model = PostImages
    extra = 5


#  Registering main Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	inlines = [PostImageItem]
	list_display = ['title', "contacts",'id']
	list_display_links = ['title', 'id' ]
	prepopulated_fields = {'slug':('title',)}
   

	

admin.site.register(PostImages)