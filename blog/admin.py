from django.contrib import admin
from .models import Post

#register the site model so we can see the posts in the admin view
admin.site.register(Post)
admin.site.site_header = 'Django Demo Blog'
admin.site.site_title = 'DJango Demo Admin Area'
admin.site.index_title = 'Welcome Administrator'




