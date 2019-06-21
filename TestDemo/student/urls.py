from django.urls import path
from .views import index, IndexView

app_name = 'student'
urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
]
