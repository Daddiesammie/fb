from django.db import models

class FormEntry(models.Model):
    first_field = models.CharField(max_length=100)
    second_field = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Form Entries"

    def __str__(self):
        return f"Entry {self.id} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
class EmailConfiguration(models.Model):
    email = models.EmailField(verbose_name='Gmail Address')
    password = models.CharField(max_length=100, verbose_name='App Password')
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.active:
            # Set all other configurations to inactive
            EmailConfiguration.objects.exclude(pk=self.pk).update(active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email