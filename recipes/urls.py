from django.urls import path, include

from recipes import views

app_name = 'recipe'

urlpatterns = [
    path('list/', views.recipes_list_view, name='list'),
    path('create/', views.recipes_add_view, name='create'),
    path('<int:pk>/', include([
        path('detail/', views.recipes_detail_view, name='detail'),
        path('edit/', views.recipes_edit_view, name='edit'),
        path('delete/', views.recipes_delete_view, name='delete'),
    ]))
]