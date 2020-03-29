from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class FoodItem(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    buy_date = models.DateField()
    exp_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def get_absolute_url(self):
        return reverse('add-food')
        #return reverse('myfood', kwargs={'username': self.user.username})