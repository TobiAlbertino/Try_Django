from django.contrib import admin

# Register your models here.
from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
        'updated',
        'published',
        'slug',
    ]

    def get_readonly_fields(self, request, obj=None):

        # print(request.user.is_superuser)
        current_user = request.user

        if obj != None:
            if current_user.has_perm('blog.publish_artikel'): # ini untuk Editor
                # print('Benar dia adalah aditor')
                readonly_fields = [
                    'created',
                    'updated',
                    'published',
                    'slug',
                ]
                return readonly_fields

            elif current_user.has_perm('blog.add_artikel'): # ini untuk penulis

                if obj.is_published:
                    # SEMUANYA readonly
                    return [data.name for data in self.model._meta.fields]

                else:
                    readonly_fields = [
                        'created',
                        'updated',
                        'is_published',
                        'published',
                        'slug',
                    ]
                return readonly_fields
        else:
            readonly_fields = [
                    'created',
                    'updated',
                    'is_published',
                    'published',
                    'slug',
                ]
            return readonly_fields

admin.site.register(Artikel, ArtikelAdmin)