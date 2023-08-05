from django.db import models

# Create your models here.
class Molel1(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=45)
    pole3 = models.TextField()

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole2) + " " + str(self.pole1)


class Molel2(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=45)
    pole4 = models.ManyToManyField(Molel1)


    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole2) + " " + str(self.pole1)


class Molel3(models.Model):
    pole1 = models.CharField("Название статьи",max_length=45)
    pole2 = models.TextField("Текст статьи")

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole1) + " " + str(self.pole2)


class Molel4(models.Model):
    pole1 = models.CharField("Название",max_length=45)
    pole2 = models.TextField("Описание")

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole1)

class Molel5(models.Model):
    pole1 = models.CharField("Наши контакты",max_length=45)
    pole2 = models.TextField("Наши контакты")

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole1)




