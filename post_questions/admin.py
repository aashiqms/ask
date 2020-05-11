from django.contrib import admin
from post_questions.models import Post, Comment


class PostQuestionAdmin(admin.ModelAdmin):

    fields = ['author', 'questions', 'created_date', 'published_date']


class CommentAdmin(admin.ModelAdmin):

    fields = ['post', 'author', 'text', 'created_date', 'approved_date']


admin.site.register(Post, PostQuestionAdmin)
admin.site.register(Comment)
