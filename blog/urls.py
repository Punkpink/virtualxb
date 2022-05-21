from django.urls import path
from .views import BlogListView, BlogCreateView,BlogDetailView

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name ="home"),
    path('crear/', BlogCreateView.as_view(), name ="crear"),
    path('<int:pk>/', BlogDetailView.as_view(), name = "detail")
]