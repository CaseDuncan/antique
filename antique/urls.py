from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view
from users import views
from django.contrib.auth import views as auth
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', login_request, name='login'),
    # path('verify/', verification_view, name='verify'),
    # # path('register/', register, name='register'),
    # path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    # path('evaluation/' , evaluation , name='evaluation'),
    # path('create_evaluation/' , create_evaluation , name='create_evaluation'),
   

    path('', views.index, name ='index'),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('evaluation/' , user_view.evaluation , name='evaluation'),
    path('create_evaluation/' , user_view.create_evaluation , name='create_evaluation'),
    path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    path('verify/', user_view.verification_view, name='verify'),
    path('listings/' , user_view.evaluation_listings , name='listings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)