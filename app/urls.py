from django.urls import path
from app.views import index_page, candidate_delete, form_page, candidateCreate

urlpatterns = [
    path('candidates', index_page, name='index_page'),
    path('candidates/cretae', candidateCreate, name='candidateCreate'),
    path('candidates/<int:pk>', form_page, name='form_page'),
    path('candidates/del/<int:pk>', candidate_delete, name='candidate_delete'),

]
