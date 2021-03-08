from django.urls import path, include
from rest_framework_nested import routers


from .views import (
    DecksViewSet,
    DeckCardsViewSet,
)

router = routers.SimpleRouter()
router.register(r'', DecksViewSet)

cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register(r'cards', DeckCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
]