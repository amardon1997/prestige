from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login1, name='login1'),
    path('logout/', views.logout_view, name='logout'),
    path('login1', views.login1, name='login1'),
    path('register/', views.register, name='register'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('newbase/', views.newbase, name='newbase'),
    path('newemployee_insights/', views.employee, name='employee'),
    path('newdata_visualization/', views.newdata_visualization, name='newdata_visualization'),
    path('newattrition_probability/', views.newattrition_probability, name='newattrition_probability'),
    # path('resume_library_search/', views.resume_library_search, name='resume_library_search'),
    path('newhire_prediction_time/', views.hire_prediction_time, name='newhire_prediction_time'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
