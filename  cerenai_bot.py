{\rtf1\ansi\ansicpg1254\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import openai\
import telebot\
\
# OpenAI API anahtar\uc0\u305 n\u305  buraya yap\u305 \u351 t\u305 r\
openai.api_key = "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"\
\
# Telegram Bot token'\uc0\u305  buraya yaz\
bot = telebot.TeleBot("7840586642:AAEp8ZEmp_IhMr1p3ktuJxC0wE1t_zCBcm4")\
\
# Mesajlar i\'e7in handler ekle\
@bot.message_handler(func=lambda message: True)\
def echo_all(message):\
    response = openai.Completion.create(\
      engine="text-davinci-003",  # GPT-3 modelini kullan\uc0\u305 yoruz\
      prompt=message.text,        # Kullan\uc0\u305 c\u305 n\u305 n mesaj\u305 n\u305  OpenAI'ye g\'f6nder\
      temperature=0.7,            # Yarat\uc0\u305 c\u305 l\u305 \u287 \u305  belirler, 0.7 iyi bir de\u287 er\
      max_tokens=100              # Yan\uc0\u305 t uzunlu\u287 u\
    )\
    bot.reply_to(message, response.choices[0].text)  # OpenAI yan\uc0\u305 t\u305 n\u305  Telegram'a g\'f6nder\
\
# Botu ba\uc0\u351 lat\
bot.polling()\
}