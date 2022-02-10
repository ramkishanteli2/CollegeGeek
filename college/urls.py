from django.contrib import admin
from django.urls import path,include
from college import views as college_views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .forms import SetNewPassword,ResetPasswordForm,SetNewPasswordForm
urlpatterns = [
    # path('college/',include('college.urls')),
    path('',college_views.index,name='home'),
    path('login/',college_views.login,name='login'),
    path('register/',college_views.register,name='register'),
    path('create_student/<str:email_>/<slug:college>/<slug:course>/<str:name>',college_views.create_student,name='create_student'),
    path('get_branches/',college_views.get_branches,name='get_branches'),
    path('get_courses/',college_views.get_courses,name='get_courses'),
    path('resetpassword/',auth_views.PasswordResetView.as_view(template_name='college/resetpassword.html',form_class=ResetPasswordForm),name='password_reset'),
     path('resetpassword/done',auth_views.PasswordResetDoneView.as_view(template_name='college/passwordresetdone.html'),name='password_reset_done'),
    path('resetpasswordconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='college/passwordresetconfirm.html',form_class=SetNewPasswordForm),name='password_reset_confirm'),
    path('resetpasswordcomplete',auth_views.PasswordResetCompleteView.as_view(template_name='college/passwordresetcomplete.html'),name='password_reset_complete'),
    path('profile/',college_views.profile,name="profile"),
    path('edit_profile/',college_views.edit_profile,name="edit_profile"),
    path('logout/',college_views.logout,name="logout"),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='college/changepassword.html',form_class=SetNewPassword,success_url='/changepassworddone/'),name='changepassword'),
    path('changepassworddone/',college_views.changepassworddone,name='changepassworddone'),
    path('academic/',college_views.academic,name="academic"),
    path('subjects/',college_views.subjects,name="subjects"),
    path('subjects/<int:sem_no>',college_views.subjects,name="subjects"),
    path('classtimetable/',college_views.classtimetable,name="classtimetable"),
    path('classtimetable/<int:sem_no>',college_views.classtimetable,name="classtimetable"),
    path('academiccalendar/<int:sem_no>',college_views.academiccalendar,name="academiccalendar"),
    path('notifications/',college_views.notifications,name="notifications"),
    path('material/<int:id>',college_views.material,name="material"),
    path('batchmates/',college_views.batchmates,name="batchmates"),
    path('seniors/',college_views.seniors,name="seniors"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)