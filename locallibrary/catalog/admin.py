from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Genre 
from .models import Book
from .models import Author 
from .models import BookInstance

admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )



   
admin.site.register(Genre) 
admin.site.register(Book) 
admin.site.register(BookInstance) 
admin.site.register(Author) 

'''
# Create user and save to the database
user = User.objects.create_user('test1', 'myemail@gmail.com', 'admin123')
# Update fields and then save again
user.first_name = 'test'
user.last_name = 'user1'
user.save()
'''
