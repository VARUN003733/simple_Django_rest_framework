from  django.urls import path
from .import views


urlpatterns=[
    path("blogpost/",views.BlogpostListCreate.as_view(),name="Blogpost-view-create"),
    path("blogpost/<int:pk>/",views.BlogPostRetrieveUpdateDestory.as_view(),name="update",)
]