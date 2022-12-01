from django.contrib.auth import views
from django.urls import path

from account.views import connection, register, deconnection

urlpatterns = [

    path('login/',connection,name="login"),
    path('register/',register,name="register"),
    path('logout/',deconnection,name="logout"),

    path('reset_password', views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_send',views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>",views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete")
]