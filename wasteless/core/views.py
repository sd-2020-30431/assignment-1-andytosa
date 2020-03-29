from django.shortcuts import render, get_object_or_404
from django.utils import datetime_safe as datetime
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

def home(request):
    return render(request, 'core/home.html')


def myfood(request):
    context = {
        'food_items': FoodItem.objects.filter(user = request.user)
    }
    return render(request, 'core/myfood.html', context)


class FoodListView(ListView):
    model = FoodItem
    template_name = 'core/myfood.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 5

    def get_queryset(self):
        _user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FoodItem.objects.filter(user=_user).order_by('exp_date')

class ExpiredListView(ListView):
    model = FoodItem
    template_name = 'core/myfood.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'foods'
    paginate_by = 5

    def get_queryset(self):
        _user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FoodItem.objects.filter(user=_user).filter(exp_date__lte=datetime.date.today()).order_by('exp_date')


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = FoodItem
    fields = ['name', 'quantity', 'calories', 'buy_date', 'exp_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)