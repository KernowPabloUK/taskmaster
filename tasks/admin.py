from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model
    """
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Category Information', {
            'fields': ('name',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin interface for Task model
    """
    list_display = ['title', 'category', 'due_date', 'completed', 'status_display', 'created_at']
    list_filter = ['completed', 'category', 'due_date', 'created_at']
    search_fields = ['title', 'category__name']
    readonly_fields = ['created_at', 'updated_at', 'is_overdue', 'status_display']
    list_editable = ['completed']
    date_hierarchy = 'due_date'

    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'category', 'due_date', 'completed')
        }),
        ('Status', {
            'fields': ('status_display', 'is_overdue'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')
