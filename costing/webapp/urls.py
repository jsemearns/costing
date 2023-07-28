from django.urls import path
from webapp.views import CustomLoginView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login')
]