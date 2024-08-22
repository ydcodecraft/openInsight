from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from ..models.club_models import Club

class ClubBaseView(View):
    model = Club
    fields = '__all__'

class ClubListView(ClubBaseView, ListView):
    template_name = "../templates/club/club_directory/club_directory.html"
    context_object_name = 'clubs'
    
class ClubCreateView(ClubBaseView, CreateView):
    template_name = "../templates/club/add_a_club/add_a_club.html"
    context_object_name = 'club'
    success_url = reverse_lazy('list_club')