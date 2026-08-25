from django.db import models


class ContactEnquiry(models.Model):
    SERVICE_CHOICES = [
        ("consultancy", "Consultancy Services"),
        ("training", "Training & Capacity Building"),
        ("research", "Research & Knowledge"),
        ("organisational-development", "Organisational Development"),
        ("strategic-advisory", "Strategic Advisory"),
        ("policy-governance", "Policy & Governance"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=150)
    organisation = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES,
        blank=True
    )
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):
        return f"{self.name} - {self.email}"