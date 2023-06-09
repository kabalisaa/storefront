from django.db import models
#when you wannna create generic relationship you must import bellow lines
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField( max_length= 255)
    def __str__(self) -> str:
        return self.label
    
class TagggedItem(models.Model):
    tagnameitem = models.CharField(max_length=255, null=True, blank=True)
    #WHAT TAG TO APPLIE TO WHICH OBJECT
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #TYPE(PRODUCT, VIDEO...)
    #ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    def __str__(self) -> str:
        return self.tagnameitem