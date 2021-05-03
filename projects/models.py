from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
   title = models.CharField(max_length=200) 
   slug = models.SlugField(blank=True)
   description = HTMLField()
   featured_image = models.ImageField(blank=True)
   url = models.URLField()
   rank = models.IntegerField(default=0)
   is_visible = models.BooleanField(default=True)

   def __str__(self):
      return self.title

   def viewable_credits(self):
      return self.credit_set.all()

   def viewable_assets(self):
      return self.asset_set.all()  

   class Meta:
      ordering = ("rank", "title", "pk")

class Credit(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   role = models.CharField(max_length=200)
   name = models.CharField(max_length=200)
   rank = models.IntegerField(default=0)
   url = models.URLField(blank=True)

   class Meta:
      ordering = ('rank', 'role', 'pk')

class Asset(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   role = models.CharField(max_length=200)
   image = models.ImageField()
   caption = models.TextField(blank=True)
   rank = models.IntegerField(default=0)

   class Meta:
      ordering = ('rank', 'role', 'pk')

