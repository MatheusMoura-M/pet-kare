from django.urls import path
from .views import TraitView

urlpatterns = [path("traits/", TraitView.as_view())]
