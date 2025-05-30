from django.urls import path
from .views import article_list, article_detail, article_update, article_delete, article_create
urlpatterns = [
    path("", article_list.as_view(), name='list'),
    path("<int:pk>", article_detail.as_view(), name='detail'),
    path("update/<int:pk>", article_update.as_view(), name='update'),
    path("delete/<int:pk>", article_delete.as_view(), name='delete'),
    path("create/", article_create.as_view(), name='create'),
]