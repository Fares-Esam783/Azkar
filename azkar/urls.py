from django.urls import path
from .views import all_dhikr, category_list, dhikr_by_category, dhikr_detail, add_dhikr, edit_dhikr, delete_dhikr

urlpatterns = [
  path('', category_list, name='category_list'),
  path('all_dhikr/', all_dhikr, name='all_dhikr'),
  path('category/<int:cat_id>/', dhikr_by_category, name='dhikr_by_category'),
  path('detail/<int:dhikr_id>/', dhikr_detail, name='dhikr_detail'),
  path('add/', add_dhikr, name='add_dhikr'),
  path('edit/<int:dhikr_id>/', edit_dhikr, name='edit_dhikr'),
  path('delete/<int:dhikr_id>/', delete_dhikr, name='delete_dhikr'),
]
