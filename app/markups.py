#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:35:21 2023

@author: shbshka
"""
from aiogram.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)

#===========REGISTER==========
start_registration = InlineKeyboardButton('Learn the truth', callback_data='start')

start = InlineKeyboardMarkup().add(start_registration)

#==========ZODIAC SIGNS=======
airies = InlineKeyboardButton('Airies', callback_data='zod.Airies')
taurus = InlineKeyboardButton('Taurus', callback_data='zod.Taurus')
gemini = InlineKeyboardButton('Gemini', callback_data='zod.Gemini')
cancer = InlineKeyboardButton('Cancer', callback_data='zod.Cancer')
leo = InlineKeyboardButton('Leo', callback_data='zod.Leo')
virgo = InlineKeyboardButton('Virgo', callback_data='zod.Virgo')
libra = InlineKeyboardButton('Libra', callback_data='zod.Libra')
scorpio = InlineKeyboardButton('Scorpio', callback_data='zod.Scorpio')
sagittarius = InlineKeyboardButton('Sagittarius', callback_data='zod.Sagittarius')
capricorn = InlineKeyboardButton('Capricorn', callback_data='zod.Capricorn')
aquarius = InlineKeyboardButton('Aquarius', callback_data='zod.Aquarius')
pisces = InlineKeyboardButton('Pisces', callback_data='zod.Pisces')

zodiacs = InlineKeyboardMarkup().add(airies, taurus, gemini, cancer,
                                     leo, virgo, libra, scorpio, sagittarius,
                                     capricorn, aquarius, pisces)
