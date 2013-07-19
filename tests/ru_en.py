# -*- coding: utf-8 -*-
from sluggee.six import u

CASES = {
# Test russian words.
    'azbuka'    : u('Азбука'),
    'dezhurnyi' : u('Дежурный'),
    'soloma'    : u('Солома'),
    'ekskursiya': u('Экскурсия'),
    'gipoteza'  : u('Гипотеза'),
    'kvarc'     : u('Кварц'),
    'ficha'     : u('Фича'),
    'vahter'    : u('Вахтер'),
    'shlyapa'   : u('Шляпа'),
    'schuka'    : u('Щука'),
    'mel'       : u('Мель'),
    'yula'      : u('Юла'),
    'objezd'    : u('Объезд'),
# Test complex sentence.
    'moi-dyadya-samyh-chestnyh-pravil-kogda-ne-v-shutku-zanemog':
        '"Мой дядя самых честных правил, когда не в шутку занемог..."',
    'tovarisch-ver-vzoidet-ona-zvezda-plenitelnogo-schastya':
        'Товарищ, верь: взойдет она, звезда пленительного счастья...',
}
