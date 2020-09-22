from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/create/
    path('create/', views.create, name='create'),

    # ex: /polls/5/results/
    path('<int:session_id>/results/', views.results, name='results'),

    # ex: /polls/5/results/ajax/
    path('<int:session_id>/results/ajax/', views.results_ajax, name='results_ajax'),

    # ex: /polls/5/join/
    path('<int:session_id>/join/', views.join, name='join'),

    # ex: /polls/5/vote/
    path('<int:session_id>/vote/', views.vote, name='vote'),

    # ex: /polls/5/vote/save/
    path('<int:session_id>/vote/save/', views.save_vote, name='save_vote'),

    # ex: /polls/vote/5/update/
    path('vote/<int:vote_id>/update/', views.update_vote, name='update_vote'),
]
