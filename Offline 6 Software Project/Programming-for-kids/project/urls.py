from django.urls import path
from . import views

urlpatterns = [
    path('allreadingmaterials/', views.members, name='members'),
    path('allreadingmaterials/details/<int:ID>', views.details, name='details'),
    path('mcq/<int:c_id>/<int:q_id>',views.mcq, name='mcq'),
    path('prog/<int:rmid>',views.progprob, name='progprob'),
    path('week/<int:c_id>',views.weekmod, name='weekmod'),
    path('',views.home, name='home'),
    #path('courselist')
    #path('courselist/<int:c_id')
    #path('student/<int:s_id>')
    
]
