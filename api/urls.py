from django.conf.urls import url

import api.views as views

urlpatterns=[
    url(r'^$',views.Employee.as_view()),
    url(r'^create$',views.EmployeeCreateAPIView.as_view(),name='create'),
    url(r'^list$',views.EmplyeeWithListAPIView.as_view(),name='list'),
    url(r'^list/(?P<pk>[\d]+)/$', views.EmplyeeDetailAPIView.as_view(), name='detail'),
    url(r'^list/(?P<pk>[\d]+)/edit/$', views.EmployeeUpdateAPIView.as_view(), name='edit'),
    url(r'^list/(?P<pk>[\d]+)/delete$', views.EmployeeDeleteAPIView.as_view(), name='delete')
]