from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from rest_framework import routers
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'workouts', WorkoutViewSet, base_name='user-workouts')
router.register(r'exercise', ExerciseViewSet, base_name='user-exercise')
router.register(r'exercises', ExercisesViewSet, base_name='exercises-list')

urlpatterns = [
    url(r'^signup/$', views.create_account, name='create_account'),
    # url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/signout.html'}, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),

    url(r'^signin/$', views.signin, name='signin'),



    url(r'^dashboard/edit/$', views.complete_profile, name='complete_profile'),
    url(r'^dashboard/create-workout/$', views.create_workout, name='create_workout'),
    url(r'^dashboard/profile/$', views.profile, name='profile'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),



    url(r'^v1/', include(router.urls)),
    url(r'^v1/user/login/$', views.UserLogin.as_view()),
    url(r'^api/exercises/$', views.ExercisesList.as_view()),
    url(r'^api/workouts/$', views.WorkoutList.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),


    url(r'^$', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)