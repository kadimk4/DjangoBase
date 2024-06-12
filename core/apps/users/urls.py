from django.urls import path

from core.apps.users.api.views import SelfListView, SelfUpdareDeleteView, SelfCreateView

urlpatterns = [
    path('users/', SelfListView.as_view()),
    path('user_change/', SelfUpdareDeleteView.as_view()),
    path('user_create/', SelfCreateView.as_view())

]