{{ unicode_literals }}from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ project_name }}.src.apps.{{ app_name }}'
