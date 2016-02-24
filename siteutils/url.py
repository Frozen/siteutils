

def make_global_url(path) -> str:
    """
    Делаем глобальную ссылку
    :param path: string
    :return: sting
    """
    from django.conf import settings
    return "{}://{}{}".format(settings.SCHEMA, settings.DOMAIN, path)
