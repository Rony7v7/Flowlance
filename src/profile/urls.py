from django.urls import path

from .views import profile_views, data_views, calification_views, register_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # TODO: No se tiene url my_profile en donde se pueda ver el perfil del usuario cliente o freelancer
    # path('my_profile/', views.my_profile, name='my_profile'),  # URL for viewing the own profile
    # No se tiene en cuenta la url por defecto profile/ en donde se pueda ver el perfil del usuario cliente o freelancer o NAN
    path('', profile_views.my_profile, name='my_profile'), # TODO: URL for viewing the own profile - name debería ser 'my_profile' y por lo tanto ser actualizado en donde se llame
    path('freelancer_profile/<str:username>/', profile_views.freelancer_profile_view, name='freelancer_profile_view'),  # URL for viewing another freelancer profile
    path("customize_profile/", data_views.customize_profile, name="customize_profile"),
    path('update/', profile_views.update_company_profile, name='update_company_profile'),
    path("add_experience/", data_views.add_experience, name="add_experience"),
    path('upload_curriculum/', data_views.upload_curriculum, name='upload_curriculum'),
    path('add_project/', data_views.add_project, name='add_project'),
    path('add_course/', data_views.add_course, name='add_course'),   
    path('notifications/', profile_views.notifications, name='notifications'),
    path('add_rating/<str:freelancer_username>/', calification_views.add_rating, name='add_rating'),
    path('add_rating_response/<int:rating_id>/', calification_views.add_rating_response, name='add_rating_response'),
    path('edit_rating_response/<int:response_id>/', calification_views.edit_rating_response, name='edit_rating_response'),
    path('delete_rating/<int:rating_id>/', calification_views.delete_rating, name='delete_rating'),
    path('delete_rating_response/<int:response_id>/', calification_views.delete_rating_response, name='delete_rating_response'),
    path('freelancer_profile/<str:username>/', profile_views.freelancer_profile_view, name='freelancer_profile'),  # URL for finshing edit the RatingResponse
    path('register/freelancer/', register_views.register_freelancer, name='register_freelancer'),
    path('register/company/', register_views.register_company, name='register_company'),
    path('notification-preferences/', profile_views.notification_preferences, name='notification_preferences'),
    path('reset-notification-preferences/', profile_views.reset_notification_preferences, name='reset_notification_preferences'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)