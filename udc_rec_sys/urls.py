from django.urls import path

from udc_rec_sys.views import index, article_upload

app_name = 'udc_rec_sys'

urlpatterns = [
    path('', index, name='index'),
    path('article_upload/', article_upload, name='article_upload'),
]
