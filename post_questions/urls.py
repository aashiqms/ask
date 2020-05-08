from django.urls import path
from post_questions import views
urlpatterns = [
    path('posts_list/', views.PostListView.as_view(), name='post_list'),
    path('post_detail_view/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.PostDraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comments/<int:pk>/approve', views.comment_approved, name='comment_approved'),
    path('comments/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),

]
