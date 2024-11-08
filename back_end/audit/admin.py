from django.contrib import admin
from .models import User, Notification, Prompt, Audit, Audit_Result, Log, Report, AI_Recommendation

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Prompt)
admin.site.register(Audit)
admin.site.register(Audit_Result)
admin.site.register(Log)
admin.site.register(Report)
admin.site.register(AI_Recommendation)
