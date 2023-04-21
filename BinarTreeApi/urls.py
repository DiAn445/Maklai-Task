from BinarTreeApi.views import ParaphraseAPIView
from django.urls import path


urlpatterns = [
    path('paraphrase/', ParaphraseAPIView.as_view(), name='paraphrase'),
]
