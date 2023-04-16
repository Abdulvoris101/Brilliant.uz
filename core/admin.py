from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


class IntroSlideContent(admin.TabularInline):
    model = IntroSlideContent
    extra = 1

@admin.register(IntroSlide)
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


class TopBlindsAdmin(admin.TabularInline):
    model = TopBlinds
    extra = 1


@admin.register(TopBlindsSlide)
class TopBlindsSlideAdmin(admin.ModelAdmin):
    inlines = [TopBlindsAdmin]
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

class EquiepmentSlideContentAdmin(admin.TabularInline):
    model = EquipmentSlideContent
    extra = 1

@admin.register(EquipmentSlide)
class EquiepmentSlideAdmin(admin.ModelAdmin):
    inlines = [EquiepmentSlideContentAdmin]
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

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('image_display', 'title')

    def image_display(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_display.short_description = 'Image'  # Set the column name in the admin list view



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

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ('first_name', 'phone_number', 'message')