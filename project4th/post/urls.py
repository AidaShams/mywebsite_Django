from django.urls import path
from .views import post_listview, post_detailview, post_createview, post_updateview
urlpatterns=[
    path('post/',post_listview.as_view(),name = 'post_listview'),
    path('post/<int:pk>', post_detailview.as_view(), name = "post_detailview"),
    path('post/create', post_createview.as_view(), name = "post_createview"),
    path('post/update/<int:pk>', post_updateview.as_view(), name = "post_updateview")
]