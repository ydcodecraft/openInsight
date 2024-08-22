from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from football_analysis.models.stadium_models import Stadium


class StadiumBaseView(View):
    model = Stadium
    fields = "__all__"


class StadiumListView(StadiumBaseView, ListView):
    template_name = "../templates/stadium/stadium_directory/stadium_directory.html"
    context_object_name = "stadiums"


class StadiumCreateView(StadiumBaseView, CreateView):
    template_name = "../templates/stadium/add_a_stadium/add_a_stadium.html"
    context_object_name = "stadium"
    success_url = reverse_lazy('list_stadium')
    