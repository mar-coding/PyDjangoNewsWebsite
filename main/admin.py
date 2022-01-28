from django.contrib import admin

from .models import Category, News, Comment, Member


class AdminCate(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Category,AdminCate)


class AdminMember(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_interest')

    def get_interest(self, obj):
        return "\n".join([i.title for i in obj.interest.all()])

    get_interest.short_description = "Interest"


admin.site.register(Member, AdminMember)


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'time', 'view')


admin.site.register(News, AdminNews)


class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'email', 'body', 'time', 'status')


admin.site.register(Comment, AdminComment)
