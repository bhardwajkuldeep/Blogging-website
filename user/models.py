from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class UMessage(models.Model):
    Name = models.CharField(max_length = 50,verbose_name = "Name")
    Email = models.CharField(max_length = 20,verbose_name = "Email")
    Message = models.TextField(max_length = 500,verbose_name = "Message")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    class Meta:
        ordering = ["-created_date"]

