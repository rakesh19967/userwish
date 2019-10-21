from django.db import models

# Create your models here.

class User(models.Model):
    Wish_List = models.CharField(max_length=30)
    Date = models.DateTimeField(null= True, blank=False)

def Datetime():
    app_data = User.objects.all()
    for item in app_data:
        the_date = str(item.Date.strftime("%b-%d-%y")) + "," + the_date


