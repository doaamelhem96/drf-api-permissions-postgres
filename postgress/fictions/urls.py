from django.urls import path
from .views import FictionListView, FictionDetailView

urlpatterns = [
   
    path('', FictionListView.as_view(), name= 'fiction_list'),
    path('<int:pk>/',FictionDetailView.as_view(), name= 'fiction_detail'),

]