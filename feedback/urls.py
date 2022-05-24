from django.contrib import admin
from django.urls import path
from .views import index, update_feedback, FeedBackView, DoneView, FeedBackUpdateView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate

urlpatterns = [
    path('', FeedBackView.as_view()),
    path('done', DoneView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('detail/<int:pk>', FeedBackViewUpdate.as_view()),
    path('update/<int:pk>', FeedBackViewUpdate.as_view()),
]
