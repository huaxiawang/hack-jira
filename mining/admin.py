from django.contrib import admin
from .models import EpsCase, Comment, Customer


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 0


class EpsCaseAdmin(admin.ModelAdmin):
    list_display = ('case_key', 'case_summary', 'case_creator', 'case_status', 'case_create_date')
    list_filter = ['case_create_date']
    search_fields = ['case_creator', 'case_key']
    inlines = [CommentInline, CustomerInline]

# Register your models here.
admin.site.register(EpsCase, EpsCaseAdmin)
admin.site.register(Comment)
admin.site.register(Customer)
admin.AdminSite.site_header = "JIRA Mining Administration"