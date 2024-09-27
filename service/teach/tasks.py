# import os
# import tempfile
# from django.core.files import File
# from moviepy.editor import VideoFileClip
# from services.models import CourseInfo
#
#
# def compress_video(course_info_id, video_path):
#     try:
#         # Создаём временный файл для сжатого видео в системной временной директории
#         with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_compressed_file:
#             temp_compressed_file_path = temp_compressed_file.name
#
#         # Открываем исходное видео для сжатия
#         with VideoFileClip(video_path) as clip:
#             # Сжимаем видео и записываем его в временный файл
#             clip.write_videofile(temp_compressed_file_path, codec='libx264', preset='medium',
#                                  ffmpeg_params=["-crf", "28"])
#
#         # Находим запись CourseInfo
#         course_info = CourseInfo.objects.get(pk=course_info_id)
#
#         # Открываем сжатое видео и сохраняем его в поле preview_video модели CourseInfo
#         with open(temp_compressed_file_path, 'rb') as f:
#             # Сохраняем видео в нужную директорию (Django сам сгенерирует нужный путь)
#             course_info.preview_video.save(f"compressed_{os.path.basename(video_path)}", File(f), save=True,)
#         os.remove(video_path)
#
#     except Exception as e:
#         raise RuntimeError(f"Ошибка сжатия видео: {str(e)}")
#
#     finally:
#         # Удаляем временный файл после завершения операции
#         if os.path.exists(temp_compressed_file_path):
#             os.remove(temp_compressed_file_path)
