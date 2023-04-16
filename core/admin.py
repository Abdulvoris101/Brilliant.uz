from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

class IntroSlideContent(admin.TabularInline):
    model = IntroSlideContent
    extra = 1


class IntroSlideAdmin(admin.ModelAdmin):
    inlines = [IntroSlideContent]
    readonly_fields = ('title', )
    list_display = ('title', )

    def has_add_permission(self, request):
        # Check if the model already has an object
        model = self.model
        if model.objects.exists():
            # Return False if the model already has an object
            return False
        else:
            # Return True if the model does not have an object
            return True

@admin.register(BenefitCard)
class BenefitCardAdmin(admin.ModelAdmin):
    model = BenefitCard
    list_display = ('image_display', 'title', 'text')
    ordering = ('id', )

    def image_display(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_display.short_description = 'Image'  # Set the column name in the admin list view

    def has_add_permission(self, request):
        # Check if the model already has an object
        model = self.model
        if len(model.objects.all()) >= 2:
            # Return False if the model already has an object
            return False
        else:
            # Return True if the model does not have an object
            return True

admin.site.register(IntroSlide, IntroSlideAdmin)
