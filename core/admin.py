from django.contrib import admin
from .models import Page, Component

class ComponentInline(admin.StackedInline):
    # Will allow editing of Components directly within the Page admin interface.
    model = Component

    # The fields to show in the form.
    fields = ('position', 'category', 'text', 'url', 'file', 'inline', 'width')

    # Shows 1 extra blank form for adding a new component by default.
    extra = 1

# This customizes the admin interface for the Page model itself.
class PageAdmin(admin.ModelAdmin):
    # Defines which fields are displayed on the main list view of all pages.
    list_display = ('title', 'slug', 'subject', 'grade', 'skill')

    # Adds sidebar filters for these fields.
    list_filter = ('skill', 'subject', 'grade')

    # Adds a search bar that will search the title and slug fields.
    search_fields = ('title', 'slug')

    # Auto-fills the slug field as you type in the title field.
    prepopulated_fields = {'slug': ('title',)}

    # adds the inline editable components (defined above) to the Page admin
    inlines = [ComponentInline]

# Add these to Django's built-in admin interface
admin.site.register(Page, PageAdmin)