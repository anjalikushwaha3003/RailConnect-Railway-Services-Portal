from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.index),
    path('trainbwst/',views.trainbwst, name="trainbwst"),
    path('pnr/',views.pnr),
    path('ticketbooking/',views.ticketbooking),
    path('aboutus/',views.aboutus),
    path('seatavailability/',views.seatavailability),
    path('login/',views.login),
    path('privacy/',views.privacy),
    path('login_acc/',views.login_acc),
    path('myprofile/',views.myprofile),
    path('signup/',views.signup),
    path('viewprofile/',views.viewprofile),
    path('signout/',views.signout),
    path('feedback/',views.feedback_user),
    path('booking_success/',views.booking_success),
    path('book/',views.book_ticket ,name="book_ticket"),
    path('contact/',views.contact),
    path('tickets/',views.tickets),
    path('ticket/<str:pnr>/delete/', views.delete_ticket, name='delete_ticket'),
    path('livestatus/',views.livestatus,name="livestatus"),
    
    path('payment/', views.payment_view, name='payment'),
    path('successreg/',views.successreg),
    path('registered/',views.already),
    path('terms/',views.terms),
     path('stationcodes/', views.stationcodes, name='stationcodes'),
     path('confirm/',views.confirm),
]