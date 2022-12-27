from django.contrib import admin

# Register your models here.

from udc_rec_sys.models import *

admin.site.register(OntologyTable)
admin.site.register(UdcTable)
admin.site.register(ResourceDownloadStatus)
admin.site.register(ArticleStatus)
admin.site.register(ResourceDownload)
admin.site.register(Article)


@admin.register(UserStash)
class UserStashAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article', 'created_timestamp')
    fields = (('user', 'article', 'created_timestamp'), )
    readonly_fields = ('user', 'article', 'created_timestamp')
    ordering = ('-created_timestamp',)


class UserStashAdminInline(admin.TabularInline):
    model = UserStash
    fields = (('user', 'article', 'created_timestamp'), )
    readonly_fields = ('user', 'article', 'created_timestamp')
    extra = 0
