from django.urls import path
from .views import *

urlpatterns = [
    path("",get_all,name="get_all"),
    path("get_by_id/<int:pk>",get_by_id,name="Get_by_id"),
    path("add",add,name="add"),
    path("update/<int:pk>",update,name="update"),
    path("delete/<int:pk>",delete,name="delete")
    
]
