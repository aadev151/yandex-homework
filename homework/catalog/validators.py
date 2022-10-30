from functools import wraps

from django.core.exceptions import ValidationError


def validate_weight(value):
    if not 0 < value < 32767:
        raise ValidationError(
            'The weight range is [1, 32766]'
        )

    return value


def validate_must_be_param(*necessary_words):

    @wraps(validate_must_be_param)
    def validate_params(value):
        for word in necessary_words:
            if word in value:
                break
        else:
            raise ValidationError(
                'Нужно использовать хотя бы одно из этих слов: '
                f'{necessary_words}'
            )
        return value

    return validate_params
