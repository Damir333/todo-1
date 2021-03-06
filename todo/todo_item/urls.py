from django.urls import path
from todo_item.views import item_view

app_name = 'item'

urlpatterns = [
    path('', item_view),
    path('create/', item_view),
    path('delete/', item_view),
    path('edit/', item_view),
]
