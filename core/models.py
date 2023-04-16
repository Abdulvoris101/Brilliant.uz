from django.db import models
from django.core.validators import MinLengthValidator



class IntroSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Intro Slide')

class IntroSlideContent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slides/')
    intro = models.ForeignKey(IntroSlide, on_delete=models.CASCADE)


class BenefitCard(models.Model):
    image = models.ImageField(upload_to='cards/')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class EquipmentSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Equipment Slide')


class EquipmentSlideContent(models.Model):
    image = models.ImageField(upload_to='slides/')
    subtitle = models.CharField(max_length=255, default='Комлектация для руллоных штор')
    title = models.CharField(max_length=255)
    text = models.TextField()
    slide = models.ForeignKey(EquipmentSlide, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Catalog(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TopBlindsSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Top Blinds')


class TopBlinds(models.Model):
    image = models.ImageField(upload_to='slides/')
    slide = models.ForeignKey(TopBlindsSlide, on_delete=models.CASCADE)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, validators=[MinLengthValidator(9)])
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

