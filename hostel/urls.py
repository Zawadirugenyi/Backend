from django.urls import path
from django.conf import settings
from django.urls import path
from .views import mpesa_payment
from .views import RoomDescriptionDetailView
from .views import MpesaPaymentView, MpesaCallbackView
from .views import AvailableRoomsList
from .views import RoomAvailabilityCheckView
from django.conf.urls.static import static
from . import views
from .views import book_room
from rest_framework.authtoken.views import obtain_auth_token
from .views import RoomListCreateView, RoomDescriptionListCreateView, RoomDetailView, RoomDescriptionDetailView
from .views import (
    HostelListCreateView, HostelDetailView,
    RoomListCreateView, RoomDetailView,
    TenantListCreateView, TenantDetailView,
    StaffListCreateView, StaffDetailView,
    BookingListCreateView, BookingDetailView,
    MaintenanceListCreateView, MaintenanceDetailView,
    FacilityListCreateView, FacilityDetailView,
    PaymentListCreateView, PaymentDetailView,
    NotificationListCreateView, NotificationDetailView,
    admin_send_notification, user_request_requisition,
    RoomDescriptionDetailView, RoomDescriptionListCreateView,  # Add RoomDescriptionListCreateView
)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/send_notification/', admin_send_notification, name='admin_send_notification'),
    path('user/request_requisition/', user_request_requisition, name='user_request_requisition'),

    path('hostels/', HostelListCreateView.as_view(), name='hostel-list-create'),
    path('hostels/<int:pk>/', HostelDetailView.as_view(), name='hostel-detail'),

    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
     path('api/room-descriptions/<int:room_number>/description/', views.room_description, name='room-description'),
    path('room-descriptions/', RoomDescriptionListCreateView.as_view(), name='room-description-list-create'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('book-room/<str:room_number>/', book_room, name='book_room'),

    path('tenants/', TenantListCreateView.as_view(), name='tenant-list-create'),
    path('tenants/<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),

    path('staffs/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staffs/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('api/rooms/check-availability/<int:hostel_id>/<str:room_number>/', RoomAvailabilityCheckView.as_view(), name='check-room-availability'),
    path('available-rooms/', AvailableRoomsList.as_view(), name='available-rooms'),

    path('maintenance/', MaintenanceListCreateView.as_view(), name='maintenance-list-create'),
    path('maintenance/<int:pk>/', MaintenanceDetailView.as_view(), name='maintenance-detail'),
   

    path('facilities/', FacilityListCreateView.as_view(), name='facility-list-create'),
    path('facilities/<int:pk>/', FacilityDetailView.as_view(), name='facility-detail'),

    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/mpesa/', mpesa_payment, name='mpesa_payment'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),

    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

    path('api/room-descriptions/', RoomDescriptionListCreateView.as_view(), name='room-description-list'),
    path('api/room-descriptions/<str:hostel_name>/<str:room_number>/', RoomDescriptionDetailView.as_view(), name='room-description-detail'),

    path('api/payments/mpesa/', MpesaPaymentView.as_view(), name='mpesa_payment'),
    path('payments/mpesa/', MpesaPaymentView.as_view(), name='mpesa_payment'),
    path('payments/mpesa/callback/', MpesaCallbackView.as_view(), name='mpesa_callback'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





