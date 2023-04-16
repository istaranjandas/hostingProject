from django.urls import path
from .views import test,home

urlpatterns = [
    path('',home,name='contest-page'),
    path('test/',test, name='test-celery')
]