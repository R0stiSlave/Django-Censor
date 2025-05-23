from django import template
import re

register = template.Library()


BAN_WORDS = ['редиска', 'дурак', 'грубиян']


@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise TypeError("Фильтр 'censor' можно применять только к строкам.")

    def replace_bad_word(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)

    for word in BAN_WORDS:
        pattern = rf'\b[{word[0].lower()}{word[0].upper()}]{word[1:]}\b'
        value = re.sub(pattern, replace_bad_word, value)

    return value