from django.db import models


# Mood question(기분에 대해 질문함)
class Mood(models.Model):
    MOOD_VERY_BAD = 1
    MOOD_BAD = 2
    MOOD_GOOD = 3
    MOOD_VERY_GOOD = 4

    MOOD_CHOICE = (
        (MOOD_VERY_BAD, 'VeryBad'),
        (MOOD_BAD, 'Bad'),
        (MOOD_GOOD, 'Good'),
        (MOOD_VERY_GOOD, 'VeryGood'),
    )

    created_date = models.DateTimeField(auto_now_add=True)
    mood_chk = models.IntegerField(choices=MOOD_CHOICE)
    mood_comment = models.CharField(max_length=400)

    class Meta:
        ordering = (
            'created_date',
        )
