from django.db import models


STATES = [
    ("ready", "Ready to execute"),
    ("in_progress", "In progress"),
    ("done", "done"),
]

SUPER_USER_ID = 1


class Task(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    # write_date = models.DateTimeField(auto_now_add=True)
    # write_id = models.ForeignKey('auth.User', related_name='written_tasks', on_delete=models.CASCADE, blank=True)
    creator = models.ForeignKey('auth.User', related_name='created_tasks', on_delete=models.CASCADE, default=SUPER_USER_ID)

    title = models.CharField(max_length=100, default='Task title mask(please change it)')
    description = models.TextField(default="Should be done!")
    state = models.CharField(choices=STATES, default="ready", max_length=50)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ['create_date']
