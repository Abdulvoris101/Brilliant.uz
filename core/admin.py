from django.contrib import admin
from .models import *


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

admin.site.register(IntroSlide, IntroSlideAdmin)
