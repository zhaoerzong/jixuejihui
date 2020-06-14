import xadmin
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from users.views import logout_view,LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView
from organization.views import OrgView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('logout/',logout_view,name='logout'),
    path('login/',LoginView.as_view(),name='login'),
    path('captcha/',include('captcha.urls')),
    path('register/',RegisterView.as_view(),name='register'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/',ResetPwdView.as_view(),name='reset_pwd'),
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),
    # 机构页面路由
    path('org_list/',OrgView.as_view(),name='org_list')
]
