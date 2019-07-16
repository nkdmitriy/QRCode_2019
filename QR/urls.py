from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.qrcode, name='qrcode'),
    url(r'^studentslist/$', views.StudentListView.as_view(), name='get_studentslist'),
	#url(r'^lection/(?P<lection_id>[0-9]+)/studentslist$', views.StudentsView.as_view(), name='lection_studentslist'),
	url(r'^lection/(?P<lection_id>[0-9]+)/studentslist$', views.lection_studentslist, name='lection_studentslist'),
	url(r'^lection/(?P<lection_id>[0-9]+)/$', views.create_lection, name='create_lection'),
	#url(r'^validation/$', views.validphone, name='validphone'),
	url(r'^validation/(?P<lection_id>[0-9]+)/(?P<student_id>[0-9]+)/$', views.validphone, name='validphone'),
]