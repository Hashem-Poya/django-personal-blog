from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = ''
    description = 'New posts of my blog.'
    
    def items(self):
        return Post.objects.filter(status=1)
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)    