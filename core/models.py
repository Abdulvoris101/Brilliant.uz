from django.db import models




class IntroSlide(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, default='Inro Slide')

class IntroSlideContent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slides/')
    intro = models.ForeignKey(IntroSlide, on_delete=models.CASCADE)


class BenefitCard(models.Model):
    image = models.ImageField(upload_to='cards/')
    title = models.CharField(max_length=255)
    text = models.TextField()
