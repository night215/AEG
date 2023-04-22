from django.db import models

class Question(models.Model):
    """ A model of the 8 questions. """
    question_title = models.CharField(max_length=255)
    set = models.IntegerField(unique=True)
    min_score = models.PositiveIntegerField()
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return f"Question {self.set}: {self.question_title}"

    def essays(self):
        """ Return a queryset of all essays associated with this question. """
        return self.essay_set.all()

class Essay(models.Model):
    """ Essay to be submitted. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=100000)
    score = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Essay {self.pk} ({self.question})"

    def save(self, *args, **kwargs):
        """ Ensure that the score is within the range defined by the associated question. """
        if self.score is not None and (self.score < self.question.min_score or self.score > self.question.max_score):
            raise ValueError(f"Score must be between {self.question.min_score} and {self.question.max_score}.")
        super().save(*args, **kwargs)


# from django.db import models

# # Create your models here.
# class Question(models.Model):
#     """ A model of the 8 questions. """
#     question_title = models.TextField(max_length=100000)
#     set = models.IntegerField(unique=True)
#     min_score = models.IntegerField()
#     max_score = models.IntegerField()

#     def __str__(self):
#         return str(self.set)

# class Essay(models.Model):
#     """ Essay to be submitted. """
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.TextField(max_length=100000)
#     score = models.IntegerField(null=True, blank=True)

