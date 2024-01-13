from django.urls import path
from . import views
app_name = "food"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), 
    path("add/",views.CreateItem.as_view(),name="create_item"),
    path('edit/<int:item_id>/',views.edit_item,name="edit_item"),
    path("delete/<int:item_id>",views.delete_item,name="delete_item")
]