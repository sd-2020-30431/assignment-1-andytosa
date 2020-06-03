from .models import FoodItem
from django.utils import datetime_safe as datetime

class FoodItemBusinessLogic:

    def GetAllFoodForUser(_user):
        food = FoodItem.objects.filter(user=_user)

        return food.order_by('exp_date')

    def GetExpiredFoodForUser(_user):
        food = FoodItem.objects.filter(user=_user)
        exp_food = food.filter(exp_date__lte=datetime.date.today())

        return exp_food.order_by('exp_date')