from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [

    path('people/', views.people, name='people'),
    path('people/<int:id>/', views.peoplebyid, name='peoplebyid')
]