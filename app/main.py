    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:44:10 2023

@author: shbshka
"""
from loader import bot
from aiogram import executor

from body import dp

import nest_asyncio
nest_asyncio.apply()



if __name__ == "__main__":
        executor.start_polling(dp)
