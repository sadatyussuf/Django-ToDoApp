from django.urls import path
from . import views
urlpatterns = [
    path('',views.todoApp,name='todoapp'),
    path('addTodoItem/',views.addTodoItem,name='addTodoItem'),
    path('deleteTodoItem/<int:pk>/',views.deleteTodoItem,name='deleteTodoItem'),
]

