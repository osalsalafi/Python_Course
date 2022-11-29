from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_world),
    path('main-page/',views.main_page),
    path('article/<int:id>/<slug:slug>',views.articles)
]

# but we will still have 404 error
# 1) we should go to the url.py in the main project
# 2) add include class

# <int:id>/<slug:slug> : Regular expressions
# for more about URLs patterns : https://academy.hsoub.com/programming/python/django/%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%B1%D8%A7%D8%AA-%D9%81%D9%8A-django-r426/
