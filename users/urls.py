from django.urls import  path 
from users.views import post,  add_post, change_post

urlpatterns = [
    path("<slug:slug>", post, name = 'post'),

    path(("addpost/<slug:slug>"), add_post, name = 'addpost'),

    path(("change/<slug:slug>/<int:user_id>/"), change_post, name = 'changepost' )
]
