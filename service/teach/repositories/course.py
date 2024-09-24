from clients.models import Client
from services.models import Course


class CourseRepository:
    def __init__(self):
        self.model = Course

    def get_by_id(self, course_id):
        return self.model.objects.get(pk=course_id)

    def update(self, instance, data):
        for field, value in data.items():
            setattr(instance, field, value)
        instance.save()

    def update_related_authors(self, course_info, authors):
        if authors:

            if not Client.objects.filter(id=authors).exists():
                raise ValueError(f"Автора с ID {authors} не знайдено.")

            exsisting_authors = set(course_info.authors.all().values_list('id', flat=True))
            new_authors = exsisting_authors.copy()
            new_authors.add(int(authors))

            if new_authors != exsisting_authors:
                course_info.authors.set(list(new_authors))
                course_info.save()

    def update_related_info(self, course_info, info_data):
        try:
            if 'authors' in info_data:
                self.update_related_authors(course_info, info_data.pop('authors'))
        except ValueError:
            pass

        for field, value in info_data.items():
            setattr(course_info, field, value)

        course_info.save()
