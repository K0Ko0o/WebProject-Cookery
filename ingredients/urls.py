from django.urls import path, include

from ingredients import views

app_name = 'ingredient'

urlpatterns = [
    path('list/', views.ingredients_list_view, name='list'),
    path('create/', views.ingredients_add_view, name='create'),
    path('<int:pk>/', include([
        path('detail/', views.ingredients_detail_view, name='detail'),
        path('edit/', views.ingredients_edit_view, name='edit'),
        path('delete/', views.ingredients_delete_view, name='delete'),
    ]))
]