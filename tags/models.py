from django.db import models
#when you wannna create generic relationship you must import bellow lines
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField( max_length= 255)
    
class TagggedItem(models.Model):
    #WHAT TAG TO APPLIE TO WHICH OBJECT
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #TYPE(PRODUCT, VIDEO...)
    #ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()