class CourseService:
    def __init__(self, repository):
        self.repository = repository

    def update_course(self, course_id, validated_data):
        course = self.repository.get_by_id(course_id)

        info_data = validated_data.pop('info', {})
        if info_data:
            self.repository.update_related_info(course.info, info_data)

        self.repository.update(course, validated_data)

        return course

    def update_authors(self, course_info, authors, is_delete=False):
        self.repository.update_related_authors(course_info, authors, is_delete)
