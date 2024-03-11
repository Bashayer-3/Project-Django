from django.db import models

# Create your models here.
class items(models.Model):
  name=models.CharField(max_length=50)
  def __str__(self):
    return self.name

class itemDetails(models.Model):
  color=models.CharField(max_length=50)
  price=models.FloatField()
  qty=models.IntegerField()
  tax=models.FloatField()
  image=models.CharField(max_length=150)
  total=models.FloatField()
  date=models.DateTimeField(auto_now_add=True)
  itemsid = models.ForeignKey(items, on_delete=models.CASCADE)
def __str__(self):
  return self.price

class cart(models.Model):
  id_product=models.IntegerField(null=True) 
  id_user=models.IntegerField()
  price=models.FloatField()
  qty=models.IntegerField()
  tax=models.FloatField()
  total=models.FloatField()
  discount=models.FloatField()
  net=models.FloatField()
  state=models.BooleanField()
  cteated_at=models.DateTimeField(auto_now_add=True)
  

