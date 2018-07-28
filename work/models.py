from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class AbstractLevel(models.Model):
  class Meta:
        abstract = True
  
  title = models.CharField(unique = True,max_length=255)
  description = models.CharField(null=True,blank=True,max_length=255)
  
  def __str__(self):
        return self.title

class Level1(AbstractLevel):
  pass
class Level2(AbstractLevel):
  level1 = models.ForeignKey(Level1,null=True,on_delete=models.CASCADE)
class Level3(AbstractLevel):
  level2 = models.ForeignKey(Level2,null=True,on_delete=models.CASCADE)


class Task(models.Model):
  CHOICE = ((None,'選択'),(30,'00:30'),(60,'01:00'),(90,'01:30'),(120,'02:00'),(150,'02:30'),(180,'03:00'),
            (210,'03:30'),(240,'04:00'),(270,'04:30'),(300,'05:00'),(330,'05:30'),(360,'06:00'),
            (390,'06:30'),(420,'07:00'),(450,'07:30'),(480,'08:00'),
          )
  time = models.PositiveIntegerField(choices=CHOICE)
  day = models.DateField(default=datetime.date.today())
  create_at = models.DateTimeField(auto_now_add = True,null=True)
  update_at = models.DateTimeField(auto_now = True,null=True)
  level1 = models.ForeignKey(Level1,on_delete=models.CASCADE)
  level2 = models.ForeignKey(Level2,on_delete=models.CASCADE)
  level3 = models.ForeignKey(Level3,on_delete=models.CASCADE)
  user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)