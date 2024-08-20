from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from clients.models import Client
from services.tasks import set_sub_price


class Course(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=255)
    full_price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_price = self.full_price

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.full_price != self.__full_price:
            for sub in self.subscriptions.all():
                set_sub_price.delay(sub.id)


class CourseSubcategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subcategories')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # Порядок отображения

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Course: {self.course} - Cat: {self.title}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)
    course_subcategory = models.ForeignKey(CourseSubcategory, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # Основной текст урока
    video_url = models.URLField(blank=True, null=True)  # URL для видео

    def __str__(self):
        return f'Course: {self.course} - Cat: {self.course_subcategory} - Lesson: {self.title}'


# class TextTest(models.Model):
#     lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='text_tests')
#     question = models.CharField(max_length=255)
#     answer = models.TextField()
#
#     def __str__(self):
#         return self.question


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Повний'),
        ('student', 'Студентський'),
        ('discount', 'Акційний')
    )
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=20)
    discount_percent = models.IntegerField(default=0, validators=[MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_type

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.discount_percent != self.__discount_percent:
            for sub in self.subscriptions.all():
                set_sub_price.delay(sub.id)


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='subscriptions')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='subscriptions')
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client} - {self.plan} - {self.course}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        creating = not self.pk
        if not creating:
            self.__plan = self.plan

    def save(self, *args, **kwargs):
        creating = not self.pk

        result = super().save(*args, **kwargs)

        if creating or self.plan != self.__plan:
            set_sub_price.delay(self.id)
        return result

    # def delete(self, **kwargs):
    #     cache.delete(settings.PRICE_CACHE_NAME)
    #     super().delete(**kwargs)

