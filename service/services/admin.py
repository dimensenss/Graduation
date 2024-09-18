from django.contrib import admin


from services.models import Course, Plan, Subscription, CourseModules, Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'cat', 'full_price', 'is_published',)
    list_editable = ('is_published',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    # prepopulated_fields = {'slug': ('course_name',)}

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModules)
admin.site.register(Lesson)
admin.site.register(Plan)
admin.site.register(Subscription)

