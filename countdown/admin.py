from django.contrib import admin

from countdown.models import Event


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['heading_text']}),
        ('Date information', {'fields': ['date']})
    ]
    list_display = ('heading_text', 'date')
    list_filter = ['date']


admin.site.register(Event, QuestionAdmin)