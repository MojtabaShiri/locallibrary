from django.contrib import admin
from . import models


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    field_set = ('Information', {'fields':('book', 'imprint', 'id')},
                'Availability', {'fields':('status', 'due_back', 'borrower')})


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
