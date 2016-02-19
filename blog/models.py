from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):  #post es el nombre de nuestro modelo
                            # models.Model significa que el Post es un modelo de django y debe guardarse en la BD.
    author=models.ForeignKey('auth.User')  #es un vínculo con otro modelo
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
        
    def __str__(self):
        return self.title