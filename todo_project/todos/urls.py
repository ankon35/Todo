# from django.urls import include, path
# from .views import Todoviewset
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'todos', Todoviewset, basename='todo')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import TodoListCreateAPIView, TodoDetailAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
]
