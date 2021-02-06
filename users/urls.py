from django.urls import path
from django.contrib.auth import views as auth_views
from users.email import VerificationView
from . import views

urlpatterns = [
    # Регистрация, вход, уход с аккаунта, профиль
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('account/', views.EditProfile.as_view(), name='edit_profile'),

    # Сменить пароль в профиле
    path('account/password_change/', auth_views.PasswordChangeView.as_view(
                                                            template_name="users/password/password_change_form.html"),
                                                            name='password_change'),
    path('account/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
                                                            template_name="users/password/password_change_done.html"),
                                                            name="password_change_done"),
    # Восстановить пароль при входе в аккаунт
    path('password_reset/', auth_views.PasswordResetView.as_view(
                                                            template_name="users/password/password_reset.html"),
                                                            name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                                                            template_name="users/password/password_reset_confirm.html"),
                                                            name="password_reset_confirm"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
                                                            template_name="users/password/password_reset_done.html"),
                                                            name="password_reset_done"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
                                                            template_name="users/password/password_reset_complete.html"),
                                                            name="password_reset_complete"),
    # Подтвердить аккаунт через почту
    path('activate/<uid64>/<token>/', VerificationView.as_view(), name='activate')
]