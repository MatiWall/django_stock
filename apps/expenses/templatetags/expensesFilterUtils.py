from django import template

register = template.Library()

@register.filter(name='prettifyString')
def prettifyString(s):
    
    new_text = ''

    for i, letter in enumerate(s):
        if i and letter.isupper():
           new_text += ' '

        new_text += letter


    return new_text