from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
#agregaddo a git