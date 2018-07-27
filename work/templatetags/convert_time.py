# テンプレートに渡したリストのインデックス表示
from django import template
register = template.Library()

@register.filter(name='convert_time')
def convert_time(value):
    CHOICE = {
        30:'00:30',
        60:'01:00',
        90:'01:30',
        120:'02:00',
        150:'02:30',
        180:'03:00',
        210:'03:30',
        240:'04:00',
        270:'04:30',
        300:'05:00',
        330:'05:30',
        360:'06:00',
        390:'06:30',
        420:'07:00',
        450:'07:30',
        480:'08:00'
    }

    return CHOICE.get(value)

