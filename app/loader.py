#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:44:17 2023

@author: shbshka
"""
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os
load_dotenv()


bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot=bot)
