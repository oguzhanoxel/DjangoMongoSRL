from django.contrib import admin

from .models import Deck

class DeckAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deck, DeckAdmin)
