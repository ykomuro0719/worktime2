from django.db import models
import datetime
# Create your models here.

class AbstractLevel(models.Model):
  class Meta:
        abstract = True
  
  title = models.CharField(unique = True,max_length=255)
  description = models.CharField(null=True,blank=True,max_length=255)

class Level1(AbstractLevel):
  pass
class Level2(AbstractLevel):
  pass
class Level3(AbstractLevel):
  pass


class Task(models.Model):
  time = models.PositiveIntegerField()
  day = models.DateField(default=datetime.date.today())
  create_at = models.DateTimeField(auto_now_add = True,null=True)
  update_at = models.DateTimeField(auto_now = True,null=True)
  level1 = models.ForeignKey(Level1,on_delete=models.CASCADE)
  level2 = models.ForeignKey(Level2,on_delete=models.CASCADE)
  level3 = models.ForeignKey(Level3,on_delete=models.CASCADE)