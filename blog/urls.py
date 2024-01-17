from django.urls import path
from .views import post_list, post_detail, add_comment, to_get_comment, start_parser


app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path("page/<int:page_number>/", post_list, name="paginator"),
    path('start_parser/', start_parser, name='start_parser'),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"
    ),
    path("comment/<int:post_id>/", add_comment, name="add_comment"),
    path("<int:comment_id>/", to_get_comment, name="get_comment"),
    path("<slug:tag_slug>/", post_list, name="post_list_by_tag"),
]
