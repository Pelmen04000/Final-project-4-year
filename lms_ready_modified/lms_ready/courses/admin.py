from django.contrib import admin
from .models import User, Course, Module, Lesson, Assignment, Grade, Certificate
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_by', 'created_at')

admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Certificate)
