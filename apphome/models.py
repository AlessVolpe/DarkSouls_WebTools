from django.db import models


# Create your models here.
class Tools(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=256, default='')
    tool_description = models.CharField(max_length=256, default='')
    tool_icon = models.ImageField(upload_to=None)
