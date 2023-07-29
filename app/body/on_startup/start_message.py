#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:56:08 2023

@author: shbshka
"""
import os

# os.chdir("../..")

from loader import bot, dp
from aiogram import types
import markups as nav

@dp.message_handler(commands=["start"])
async def send_start_message(message: types.Message):
    await bot.send_message(message.from_id,
                           '<i>Welcome, the truth-seeker!</i>\n' \
                           '<i><b>The Magic Orb</b> 🔮 will tell you everything you are looking for...</i>',
                           parse_mode='HTML',
                           reply_markup=nav.start)
