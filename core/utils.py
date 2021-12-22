from django.conf import settings

from random import choice

from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

avaiable_chars = ascii_letters + digits


def create_random_code(chars=avaiable_chars):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    code = create_random_code()

    model = model_instance.__class__

    if model.objects.filter(short_url=code).exists():
        return create_shortened_url(model_instance)

    return code