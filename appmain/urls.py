from django.urls import path, re_path

from appmain.views.reckoning import NewReckoningView
from appmain.views.views import index, ReckoningView

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^user/(?P<username>[-\w\.]+)/reckoning/$', ReckoningView.as_view(), name="reckoning_view"),
    re_path(r'^reckoning/new/$', NewReckoningView.as_view(), name="new_reckoning_url"),     # создать новое КП
]
