from django.conf import settings
from django.core.mail import EmailMessage

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactEnquirySerializer


class ContactEnquiryAPIView(APIView):

    def post(self, request):

        # ============================================
        # VALIDATE SUBMITTED DATA
        # ============================================

        serializer = ContactEnquirySerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": "Please correct the errors below.",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ============================================
        # SAVE ENQUIRY
        # ============================================

        enquiry = serializer.save()

        # ============================================
        # SEND EMAIL NOTIFICATION
        # ============================================

        try:

            email = EmailMessage(
                subject=f"New Contact Enquiry from {enquiry.name}",

                body=f"""
You have received a new contact enquiry.

========================================
CONTACT ENQUIRY
========================================

Name:
{enquiry.name}

Organisation:
{enquiry.organisation}

Email:
{enquiry.email}

Phone:
{enquiry.phone}

Service:
{enquiry.service}

Message:
{enquiry.message}

========================================
Enquiry ID:
{enquiry.id}
========================================
""",

                # IMPORTANT:
                # Your authenticated Gmail account is the sender.
                from_email=settings.DEFAULT_FROM_EMAIL,

                # Your receiving email address.
                to=[
                    settings.CONTACT_RECEIVER_EMAIL
                ],

                # IMPORTANT:
                # The visitor's email goes here instead of
                # being used as the sender.
                reply_to=[
                    enquiry.email
                ],
            )

            email.send(
                fail_silently=False
            )

            email_sent = True

        except Exception as e:

            print(
                f"Email sending failed: {e}"
            )

            email_sent = False

        # ============================================
        # RETURN RESPONSE
        # ============================================

        if email_sent:

            return Response(
                {
                    "success": True,
                    "message": (
                        "Thank you! Your message has "
                        "been sent successfully."
                    ),
                    "enquiry_id": enquiry.id,
                },
                status=status.HTTP_201_CREATED,
            )

        # The enquiry was saved successfully even if
        # the email could not be delivered.

        return Response(
            {
                "success": True,
                "message": (
                    "Your message was saved, but the "
                    "email notification could not be sent."
                ),
                "enquiry_id": enquiry.id,
            },
            status=status.HTTP_201_CREATED,
        )