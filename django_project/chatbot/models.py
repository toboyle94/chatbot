from django.db import models
from django.contrib.auth.models import AbstractUser

SEX_CHOICES = ("Male", "Female", "Other")


class User(AbstractUser):
    age = models.IntegerField(null=True)
    sex = models.CharField(null=True, max_length=10, choices=[(n, n) for n in SEX_CHOICES])


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Question(TimestampedModel):
    title = models.CharField(max_length=30, null=True)

    @property
    def current_text(self):
        return self.text_variations.order_by('-created').first().text

    @property
    def previous_text_versions(self):
        return (n.text for n in self.text_variations.order_by('-created')[1:])


class QuestionText(TimestampedModel):
    question = models.ForeignKey(Question, related_name='text_variations', on_delete=models.CASCADE)
    text = models.TextField(null=True)


class Response(TimestampedModel):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    question_text = models.ForeignKey(QuestionText, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
