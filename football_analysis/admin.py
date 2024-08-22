from django.contrib import admin

from .models.club_models import Club
from .models.match_models import Match
from .models.player_models import Player
from .models.stadium_models import Stadium

# Register your models here.

admin.site.register(Stadium)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Match)


