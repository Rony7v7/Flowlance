from django.urls import path
from . import views

urlpatterns = [
    path("mark-as-read/<int:notification_id>",views.mark_notification_as_read, name="mark-as-read"),
    path("mark-all-as-read",views.mark_all_notifications_as_read, name="mark-all-as-read"),
    path("delete-notification/<int:notification_id>",views.delete_notification,name="delete-notification"),
    path("report-notification/create",views.create_report_notifications,name='create-report-notification'),
    path("search-notifications",views.search_notifications,name='search-notifications'),
    path("unread-notifications",views.mark_notification_as_unread,name='unread-notifications'),
]
