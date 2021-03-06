# Copyright (c) 2018 Dolphin Emulator Website Contributors
# SPDX-License-Identifier: MIT

from django import template
from django.conf import settings
from dolweb.utils.monkey import TO_FULL

register = template.Library()

EXCEPTIONS = {
    'pt': ['br'],
    'zh': ['cn'],
}

@register.filter
def short(lang_code):
    parts = lang_code.split('-')
    code = parts[0]
    if code in EXCEPTIONS and len(parts) > 1 and parts[1] in EXCEPTIONS[code]:
        code = parts[1]
    return code

@register.filter
def langname(lang_code):
    code = short(lang_code)
    langs = {}
    for c, n in settings.LANGUAGES:
        langs[c] = n
    return langs.get(code, code)

@register.filter
def to_subdomain(lang_code):
    if lang_code == settings.LANGUAGE_CODE.split('-')[0]:
        return settings.DEFAULT_HOST
    else:
        return '%s.%s' % (lang_code, settings.DEFAULT_HOST)

@register.filter
def langdir(lang_code):
    code = short(lang_code)
    if code in settings.RTL_LANGUAGES:
        return 'rtl'
    else:
        return 'ltr'

@register.filter
def langcode(short_lang):
    return TO_FULL.get(short_lang, short_lang)
