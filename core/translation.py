from modeltranslation.translator import register, TranslationOptions
from .models import IntroSlide, IntroSlideContent, BenefitCard, EquipmentSlide,  EquipmentSlideContent, Catalog, TopBlindsSlide


@register(IntroSlide)
class IntroSlideTranslation(TranslationOptions):
    fields = ('title', )


@register(IntroSlideContent)
class IntroSlideContentTranslation(TranslationOptions):
    fields = ('title', )


@register(BenefitCard)
class BenefitCardTranslation(TranslationOptions):
    fields = ('title', 'text' )


@register(EquipmentSlide)
class EquipmentSlideTranslation(TranslationOptions):
    fields = ('title',  )


@register(EquipmentSlideContent)
class EquipmentSlideContentTranslation(TranslationOptions):
    fields = ('title',  'subtitle', 'text')



@register(Catalog)
class CatalogTranslation(TranslationOptions):
    fields = ('title', )


@register(TopBlindsSlide)
class TopBlindsSlideTranslation(TranslationOptions):
    fields = ('title', )