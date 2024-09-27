from clients.models import Client
from services.models import Course
# from teach.tasks import compress_video


class CourseRepository:
    def __init__(self):
        self.model = Course

    def get_by_id(self, course_id):
        return self.model.objects.get(pk=course_id)

    def update(self, instance, data):
        for field, value in data.items():
            setattr(instance, field, value)
        instance.save()

    def update_related_authors(self, course_info, authors, is_delete=False):
        if authors:
            if not Client.objects.filter(id=authors).exists():
                raise ValueError(f"Автора с ID {authors} не знайдено.")

            exsisting_authors = set(course_info.authors.all().values_list('id', flat=True))
            new_authors = exsisting_authors.copy()

            if is_delete:
                new_authors.remove(int(authors))
            else:
                new_authors.add(int(authors))

            if new_authors != exsisting_authors:
                course_info.authors.set(list(new_authors))
                course_info.save()

    def update_related_info(self, course_info, info_data):
        try:
            if 'authors' in info_data:
                self.update_related_authors(course_info, info_data.pop('authors'))
            # if 'preview_video' in info_data:
            #     video = info_data.pop('preview_video')
            #     compress_video(course_info.id, video.temporary_file_path())

        except ValueError:
            pass

        for field, value in info_data.items():
            setattr(course_info, field, value)

        course_info.save()
