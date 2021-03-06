from datetime import datetime

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Service(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to="clients/")
    client_url = models.URLField(null=True, blank=True)
    disp_priority = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.client_url}"

    class Meta:
        ordering = ["disp_priority"]


class Chat(models.Model):
    CHAT_CHOICES = (
        ("PHN", "via Phone/WhatsApp"),
        ("EML", "via Email"),
        ("WEB", "via Website Chat"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    contact_platform = models.CharField(max_length=3, choices=CHAT_CHOICES)
    mobile_num_chat = models.CharField(max_length=15, default="N/A")
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: {self.subject}"

    class Meta:
        ordering = ["-created_at"]


class Message(models.Model):
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
    offset = models.BigIntegerField(editable=False)
    by_admin = models.BooleanField(default=False)
    message_text = models.TextField()

    def save(self, *args, **kwargs):
        d = datetime.now()
        self.offset = d.strftime("%Y%m%d%H%M%S")
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        if self.by_admin:
            return f"ADMIN: {self.message_text}"
        return f"{self.chat}: {self.message_text}"

    class Meta:
        unique_together = (("chat", "offset", "by_admin"),)


class Advisor(models.Model):
    name = models.CharField(max_length=50)
    disp_priority = models.IntegerField(unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, editable=False)
    picture = models.ImageField(upload_to="advisors/")
    position = models.CharField(max_length=50)
    linkedin = models.URLField()
    bio = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["disp_priority"]


class Subscriber(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
