from django.urls import path
from . import views
from .views import NewsDeleteView,NewsUpdateView

urlpatterns = [
    path('',views.newsList,name='newslist'),
    path('addNews',views.addNews,name='addNews'),
    path('apiNews',views.apiNews ,name='apiNews'),
    path('editNews',views.editNews,name='editNews'),
    path('<pk>/delete',NewsDeleteView.as_view(),name='delete'),
     path('<pk>/update',NewsUpdateView.as_view(),name='update')

]
