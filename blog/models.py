from django.db import models
from django.utils import timezone
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.six.moves.urllib.parse import urlparse


class Board(models.Model):
    name = models.CharField(_('board name'),max_length=50)
    #slug = models.CharField(_('board slug'), unique=True, max_length=100, default="")

    # class Meta():
    #     verbose_name = _('board')
    #     verbose_name_plural = _('boards')

    def __str__(self):
        return self.name
'''
    def get_absolute_url(self):
        return reverse('blog:board', args=[self.slug])
'''


class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    board = models.ForeignKey(Board, default="")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #slug = models.CharField(_('post slug'), unique=True, max_length=100, default="")
   
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    '''   
    def get_absolute_url(self):
        # this expression also used in Comment.get_absolute_url()
        return reverse('blog:post', args=[self.slug])
    '''    


class Comment(models.Model):
    #author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post, default="")
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.text

    def publish(self):
        self.published_date = timezone.now()
        self.save()

'''
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
'''    
        