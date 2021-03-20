from django.contrib import admin
from books.models import RequestBook


class RequestBookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipient',
        'book',
        'created',
        'status',
    )
    readonly_fields = ('recipient', 'book')
    list_filter = ('status', 'created', )
    search_fields = ('recipient__username', 'recipient__last_name')
    # list_select_related = ('recipient', 'book')  # objects.select_related('recipient', 'book')

    # def get_readonly_fields(self, request, obj=None):
    #     readonly_fields = super().get_readonly_fields()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(RequestBook, RequestBookAdmin)
