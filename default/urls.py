from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('upload/', views.uploadfile, name='upload'),
    path('result/<str:folder>/<uuid:id>/', views.retrieve_result, name='retrieve_result'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('upgrade/go/', views.perform_upgrade, name='perform_upgrade'),
    path('package-releases/', views.package_releases, name='package_releases'),
    path('package-releases/go/', views.perform_package_releases, name='perform_package_releases'),
    path('merge/', views.merge, name='merge'),
    path('merge/go/', views.perform_merge, name='perform_merge'),
    path('mapping-sheet/', views.mapping_sheet, name='mapping_sheet')
]
