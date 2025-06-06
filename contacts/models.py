from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    pass



class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contacts')
    name=models.CharField(max_length=100)
    document=models.FileField(upload_to='contact_doc/',
             validators=[FileExtensionValidator(['pdf','docs','docx','txt'])],blank=True,null=True)
    email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('email','user')
    
    def __str__(self):
        return f'{self.name} <{self.email}>'
