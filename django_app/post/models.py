from django.db import models

# Create your models here.
MOOD_CHOICE = (
    ('Bad', '1'),
    ('SoSo', '2'),
    ('Good', '3'),
    ('VaryGood', '4'),
)


# Mood question(기분에 대해 질문함)
class Mood(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    mood_chk = models.CharField(choices=MOOD_CHOICE, max_length=100)
    mood_comment = models.CharField(max_length=400)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = (
            'created_date',
        )
