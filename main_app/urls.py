from django.urls import path

from .views import LoginView, MemoriesView, MemoryCreateView

urlpatterns = [
    path('memories/', MemoriesView.as_view(), name='memories'),
    path('sign-in/', LoginView.as_view(), name='sign_in'),
    path('add-memory/', MemoryCreateView.as_view(), name='memory_create'),
]