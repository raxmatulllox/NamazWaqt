from django.apps import AppConfig


class WaqtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Waqt'

    def ready(self):
        import Waqt.signals