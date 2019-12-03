from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name='index.html'),
        name='calendar_index'
    ),

    # path("auth_info/", AuthInfoView.as_view()),
    # path("signin/", SigninAPI.as_view(), name="signin_api"),
    # path("signup/", SignupAPI.as_view(), name="signup_api"),
]
