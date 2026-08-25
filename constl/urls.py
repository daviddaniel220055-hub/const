from django.urls import path

from .views import ContactEnquiryAPIView


urlpatterns = [
    path(
        "contact/",
        ContactEnquiryAPIView.as_view(),
        name="contact-api",
    ),
]