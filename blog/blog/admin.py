from django.contrib import admin
from .models import Post, Author

# 設定作者的後台介面
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",) # 表格只顯示名字

# 設定文章的後台介面
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")

# 註冊這兩個類別
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)