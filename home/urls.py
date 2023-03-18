from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_time_entry, name='create_time_entry'),
    # path('<int:time_entry_id>/', views.view_time_entry, name='view_time_entry'),
    # path('<int:time_entry_id>/update/', views.update_time_entry, name='update_time_entry'),
    # path('<int:time_entry_id>/delete/', views.delete_time_entry, name='delete_time_entry'),
]
