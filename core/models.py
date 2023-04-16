from django.db import models




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


class EquipmentSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Equipment Slide')


class EquipmentSlideContent(models.Model):
    image = models.ImageField(upload_to='slides/')
    subtitle = models.CharField(max_length=255, default='Комлектация для руллоных штор')
    title = models.CharField(max_length=255)
    text = models.TextField()
    slide = models.ForeignKey(EquipmentSlide, on_delete=models.CASCADE)


class Catalog(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255)


class TopBlindsSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Top Blinds')


class TopBlinds(models.Model):
    image = models.ImageField(upload_to='slides/')
    slide = models.ForeignKey(TopBlindsSlide, on_delete=models.CASCADE)