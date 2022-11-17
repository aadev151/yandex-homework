from functools import wraps
import re
from string import punctuation

from django.core.exceptions import ValidationError


def validate_weight(value):
    if not 0 < value < 32767:
        raise ValidationError(
            'Вес должен быть в пределах [1, 32766]'
        )

    return value


def validate_must_be_param(*necessary_words):

    @wraps(validate_must_be_param)
    def validate_params(value):
        regex_no_tags = re.compile('<.*?>')
        value_without_tags = re.sub(regex_no_tags, '', value)

        set_value = set(
            value_without_tags
            .translate(str.maketrans('', '', punctuation)).lower().split(),
        )

        if not set_value.intersection(necessary_words):
            raise ValidationError(
                'Нужно использовать хотя бы одно из этих слов: '
                f'{necessary_words}'
            )
        return value

    return validate_params
