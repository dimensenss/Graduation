from django.contrib import admin


from services.models import Course, Plan, Subscription, CourseModules, Lesson

admin.site.register(Course)
admin.site.register(CourseModules)
admin.site.register(Lesson)
admin.site.register(Plan)
admin.site.register(Subscription)

