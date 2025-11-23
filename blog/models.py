from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
    image=models.ImageField(upload_to='media/images/blog',null=True,blank=True)
    title=models.CharField(max_length=200)
    content=CKEditor5Field("Content",config_name="default")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    