from django.apps import AppConfig


class PlanetyConfig(AppConfig):
    name = 'planety'

    def ready(self):
        import planety.signals
