from django.contrib import admin
from .models import FormEntry
from .models import EmailConfiguration

@admin.register(EmailConfiguration)
class EmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('email', 'active')
    list_filter = ('active',)

@admin.register(FormEntry)
class FormEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_field', 'second_field', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('first_field', 'second_field')
