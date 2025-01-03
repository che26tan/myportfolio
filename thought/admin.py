from django.contrib import admin
from thought.models import Thought, ThoughtStat

class ThoughtAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'thought']

class ThoughtStatAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'comments', 'like', 'dislike']

admin.site.register(Thought, ThoughtAdmin)
admin.site.register(ThoughtStat, ThoughtStatAdmin)