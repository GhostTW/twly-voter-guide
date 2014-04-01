from django.conf.urls import patterns, url
from legislator import views

urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.index, {"index": 'biller'}),
    # ex: /legislator/
    url(r'^(?P<index>biller|conscience_vote|committee|district|notvote)?/$', views.index, name='index'),
    url(r'^district/(?P<index>.+)$', views.index_district, name='index_district'),
    url(r'^committee/(?P<index>.+)$', views.index_committee, name='index_committee'),
    url(r'^proposer/(?P<legislator_id>\d+)/(?P<keyword_url>.+)?$', views.proposer_detail, name='proposer_detail'),
    url(r'^voter/(?P<legislator_id>\d+)/(?P<ad>\d+)?/?(?P<index>conscience)?/?(?P<keyword_url>.+)?$', views.voter_detail, name='voter_detail'),
    url(r'^biller/(?P<legislator_id>\d+)/?(?P<keyword_url>.+)?$', views.biller_detail, name='biller_detail'),
    url(r'^platform/(?P<legislator_id>\d+)/$', views.platformer_detail, name='platformer_detail'),
    url(r'^report/(?P<index>biller|conscience_vote|vote|proposal|ly|committee|attend_committee)/(?P<ad>\d+)?/?$', views.chart_report, name='chart_report'),
    url(r'^report/political_contributions/(?P<index>\S+)/(?P<compare>\S+)/(?P<party>\S+)/$', views.political_contributions_report, name='political_contributions_report'),
    # ex: /legislator/personal_report/
    #url(r'^personal_report/(?P<legislator_id>\d+)/(?P<index>proposal|ly|vote)?/?$', views.chart_personal_report, name='chart_personal_report'),
)
