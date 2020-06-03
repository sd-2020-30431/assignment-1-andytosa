from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import FoodItem
from .business import FoodItemBusinessLogic

objects = [
    {
        'title': 'Red Cross',
        'content': 'The International Red Cross and Red Crescent Movement is an international humanitarian movement with approximately 97 million volunteers, members and staff worldwide[2] which was founded to protect human life and health, to ensure respect for all human beings, and to prevent and alleviate human suffering. ',
        'open_hours': 'Monday to Friday, 8AM - 6PM',
        'imgurl': 'media/food_banks/redcross.jpg'
    },
    {
        'title': 'Salvation Army',
        'content': 'The Army was founded in 1865 in London by one-time Methodist circuit-preacher William Booth and his wife Catherine as the East London Christian Mission, and can trace its origins to the Blind Beggar tavern. ',
        'open_hours': 'Monday to Saturday, 10AM - 6PM',
        'imgurl': 'media/food_banks/salvarmy.png'
    },
    {
        'title': 'Food Bank',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'open_hours': 'Lorem ipsum dolor, sit - amet',
        'imgurl': 'media/food_banks/rename.png'
    }
]

def home(request):
    context = {
        'objects': objects
    }
    return render(request, 'core/home.html', context)


def myfood(request):
    context = {
        'food_items': FoodItemBusinessLogic.GetAllFoodForUser(request.user)
    }
    return render(request, 'core/myfood.html', context)


class FoodListView(ListView):
    model = FoodItem
    template_name = 'core/myfood.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 5

    def get_queryset(self):
        _user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FoodItemBusinessLogic.GetAllFoodForUser(_user)

class ExpiredListView(ListView):
    model = FoodItem
    template_name = 'core/myfood.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 5

    def get_queryset(self):
        _user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FoodItemBusinessLogic.GetExpiredFoodForUser(_user)


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = FoodItem
    fields = ['name', 'quantity', 'calories', 'buy_date', 'exp_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)