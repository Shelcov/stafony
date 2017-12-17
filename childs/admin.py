from django.contrib import admin
from .models import *


class ChildInLineAdmin(admin.TabularInline):
    model = Child
    extra = 0


class ChildAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'gender',
        'birthdate',
        'group',
        'is_studying',
        'created',
        'updated',
    ]

    class Meta:
        model = Child


admin.site.register(Child, ChildAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Log._meta.fields]

    class Meta:
        model = Log


admin.site.register(Log, LogAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]
    inlines = [ChildInLineAdmin]

    class Meta:
        model = Group


admin.site.register(Group, GroupAdmin)


