from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class QuestionChoice(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.TextField()
    Choice_A = models.CharField(max_length=200)
    Choice_B = models.CharField(max_length=200)
    Choice_C = models.CharField(max_length=200)
    Choice_D = models.CharField(max_length=200)
    Answer = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
