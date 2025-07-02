from django.db import models


class Category(models.Model):
    """
    Category model for organizing tasks
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Category name (must be unique)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when category was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when category was last updated"
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Task model for managing individual tasks
    """
    title = models.CharField(
        max_length=200,
        help_text="Task title or description"
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        help_text="When the task is due (optional)"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Task completion status"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="Category this task belongs to"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when task was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when task was last updated"
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['due_date', 'created_at']
        indexes = [
            models.Index(fields=['due_date']),
            models.Index(fields=['completed']),
            models.Index(fields=['completed', 'due_date']),
        ]

    def __str__(self):
        status = "✓" if self.completed else "○"
        due_text = f" (due: {self.due_date})" if self.due_date else ""
        return f"{status} {self.title}{due_text}"

    @property
    def is_overdue(self):
        """Check if task is overdue"""
        if not self.due_date or self.completed:
            return False
        from django.utils import timezone
        return self.due_date < timezone.now().date()

    @property
    def status_display(self):
        """Get human-readable status"""
        if self.completed:
            return "Completed"
        elif self.is_overdue:
            return "Overdue"
        else:
            return "Pending"
