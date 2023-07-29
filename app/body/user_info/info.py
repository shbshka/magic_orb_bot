#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:31:55 2023

@author: shbshka
"""
from loader import bot, dp
from aiogram import types

import markups as nav

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from body.magic_orb_model.model import generate_prediction

from datetime import datetime

class UserInfo(StatesGroup):
    user_name = State()

@dp.callback_query_handler()
async def get_user_data(call: types.CallbackQuery, state=FSMContext):
    if call.data == 'start':
        await bot.send_message(call.from_user.id,
                               '<i>Choose the zodiac sign under which you '
                               'or the person the prediction is for were born ✨</i>',
                               parse_mode='HTML',
                               reply_markup=nav.zodiacs)

    if call.data.startswith('zod.'):
        zodiac_sign = call.data
        zodiac_sign = zodiac_sign.replace('zod.', '')

        prediction = generate_prediction(datetime.now().strftime('%b %d, %Y'), zodiac_sign)
        await bot.send_message(call.from_user.id, f'<i><b>The truth-seeker, your prediction for today '
                               f'is the following: </b></i>\n{prediction}',
                               parse_mode='HTML')
        await bot.send_message(call.from_user.id, '<i>Do you want more truth? 🔮 </i>',
                               parse_mode='HTML',
                               reply_markup=nav.start)
