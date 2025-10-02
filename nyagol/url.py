from django.urls import path
from . import views

# urlpatterns = [
#     path('hello/', views.hello, name='nyagol-home'),
# ]

urlpatterns = [
    path('main/', views.main, name='main'),
    path('members/', views.members, name='all-members'),
    path('members/details/<int:id>', views.details, name='details'),
]