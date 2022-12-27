from django.db import models

from users.models import User

# Create your models here.


class OntologyTable(models.Model):
    name = models.CharField(max_length=512, default='None')
    domain = models.CharField(max_length=512, blank=True, default='None')
    version = models.CharField(max_length=128, default='None')
    data = models.CharField(max_length=1048576, default='None')
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Онтологии'

    def __str__(self):
        return str(self.name) + " | " + str(self.version)


class UdcTable(models.Model):
    udc_code = models.CharField(max_length=64, unique=True, default='None')
    name_ru = models.CharField(max_length=512, blank=True, default='None')
    name_en = models.CharField(max_length=512, blank=True, default='None')
    #udc_map = models.FileField(upload_to='udc_map', blank=True, null=True)
    udc_map = models.CharField(max_length=1048576, default='None')
    exp_class_coefficient = models.CharField(max_length=4096, default='None')
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Карты UDC'

    def __str__(self):
        return self.udc_code


class ResourceDownloadStatus(models.Model):
    name_ru = models.CharField(max_length=128, unique=True, default='None')
    name_en = models.CharField(max_length=128, unique=True, default='None')

    class Meta:
        verbose_name_plural = 'Статусы ресурсов'

    def __str__(self):
        return self.name_en


class ArticleStatus(models.Model):
    name_ru = models.CharField(max_length=128, unique=True, default='None')
    name_en = models.CharField(max_length=128, unique=True, default='None')

    class Meta:
        verbose_name_plural = 'Статусы статей'

    def __str__(self):
        return self.name_en


class ResourceDownload(models.Model):
    name = models.CharField(max_length=128, unique=True, default='None')
    link = models.CharField(max_length=512, unique=True, default='None')
    last_connection = models.DateTimeField(null=True)
    status = models.ForeignKey(ResourceDownloadStatus, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Источники'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, blank=True)
    file = models.FileField(upload_to='articles_files')
    file_name = models.CharField(max_length=256, default='file')
    main_rec_udc = models.CharField(max_length=64, blank=True, default='None')
    other_rec_udc = models.CharField(max_length=256, blank=True, default='None')
    author_udc = models.CharField(max_length=256, blank=True, default='None')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    resource = models.ForeignKey(ResourceDownload, on_delete=models.PROTECT)
    #file_structure = models.FileField(upload_to='articles_structures', blank=True, null=True)
    file_structure = models.CharField(max_length=1048576, default='None')
    onto_math_pro_version = models.CharField(max_length=128, blank=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ArticleStatus, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.file_name


class UserStash(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Загрузки пользователей'

    def __str__(self):
        return f'{self.user.username} | Статья {self.article.file}'
