from django.contrib import admin


from services.models import Course, Plan, Subscription, CourseSubcategory, Lesson

admin.site.register(Course)
admin.site.register(CourseSubcategory)
admin.site.register(Lesson)
admin.site.register(Plan)
admin.site.register(Subscription)

