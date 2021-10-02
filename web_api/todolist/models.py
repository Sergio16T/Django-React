from django.db import models


# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=256)

    creation_date = models.DateTimeField(auto_now_add=True, )

    last_updated = models.DateTimeField(auto_now=True)

    status = models.BooleanField()  # 1 or 0 for complete or incomplete

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'todo'
