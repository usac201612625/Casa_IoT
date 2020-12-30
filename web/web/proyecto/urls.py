from django.urls import path
from proyecto import views


app_name = 'proyecto'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('json_response/',views.json_response, name = 'json_response'),
    path('general/',views.vista1,name='vista_general'),

]