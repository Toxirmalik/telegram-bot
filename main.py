import telebot
from telebot import types
bot = telebot.TeleBot('2039331525:AAG6LinwbZQncRapZ90e6cIlwXQo-eDl-r8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('āļø  So\'rovnomani to\'ldirish')
    btn2 = types.KeyboardButton('š  Ijtimoiy tarmoqlarimiz')
    btn3 = types.KeyboardButton('š  Bot haqida')
    btn4 = types.KeyboardButton('Kurs haqida')
    markup.add(btn1, btn4, btn2, btn3)
    send_mess = f"Assalomu alaykum va Rohmatulloh !!! \n{message.from_user.first_name} arabtilidan online botimizga hush kelibsiz!\n" \
                f"\nHurmatli tolibi ilmlar biz yana samarali,tezkor kurslarimizga yangidan qabul boshladik. \n \n" \
                f"š Bizning kurslarimizda :\n\n1ļøā£ - Arab tili harflari noldan o'rgatiladi.\n2ļøā£ - Arab tili fonetikasidan saboq beriladi.\n3ļøā£ - Arabcha matnlarini o'rtacha tezlikda o'qiy olasiz.\n4ļøā£ - Arabiy husnixat ham o'rgatiladi.\n" \
                f"5ļøā£ - Arabtili gramatikasi o'rgatiladi.\n" \
                f"\nš   Kurslarimiz o'rganuvchining darajasiga qarab, ayollar va erkaklar alohida guruhlarga bo'lingan holatda  o'tiladi .\nāļø Shu sababli quyidagi so'rovnomani to'ldirishizni so'rab qolamiz. \nShoshiling joylar soni cheklangan ššāāļø\n" \
                f"\n Alloh boshlamoqchi bo'lgan ishlaringizni manfaatli qilsin!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "āļø  so\'rovnomani to\'ldirish":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('šØāāļø Erkak (muzakkar)')
        btn2 = types.KeyboardButton('š§ Ayol (muannas)')
        btn3 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1,btn2,btn3)
        final_mess = f"Guruhlarimizda erkaklar alohida, ayollor alohida holatda tahsil oladi shu sababli o'zingizga tegishli tugmani tanlang."
        bot.send_message(message.chat.id, final_mess , parse_mode='html', reply_markup=markup)

    elif get_message_bot == "kurs haqida":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1)
        final_mess = f"Kurslarimiz haqida :\n" \
                     f"Kurslar haftada 3 kun 1,5 soatdan tashkil etiladi\n" \
                     f"Online Zoom platformasida olib boriladi\n" \
                     f"Dars vaqtlari ustoz bilan kelishgan holatda guruh shakllangandan so'ng belgilanadi\n" \
                     f"5 kishilik kurslarimiz 300 ming so'mdan\n" \
                     f"8 kishilik kurslarimiz 200 ming so'mdan\n" \
                     f"\n" \
                     f"Ushbu Telegram guruhlarda oŹ»quvchilardan tashqari 3 kishi boŹ»ladi, ular:\n" \
                     f"Ustoz - sizlarga dars oŹ»tadi\nAdmin - toŹ»lov va boshqa masalalar bilan shugŹ»ullanadi\nTexnik - guruhda yoki botda texnik muammolar boŹ»lsa bartaraf etadi\n" \
                     f"Darslar O'zbekiston Xalqaro Islom akademiyasi bitiruvchilari ,cefr sertifikati bor, malakali o'qtuvchilarimiz tomonidan o'tiladi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "š  bot haqida":
        final_mess = f"ā”ļøBotning vazifasi : arab tili o'rganmoqchi bo'lgan tolibi ilmlarni darajasiga qarab o'z guruhlariga joylashishiga yordam beradi.\n" \
                     f"\n āļø Hurmatli tolibi ilmlar @ArabtiliOnlaynBot botimiz sizga foydasi tegayotgan bo'lsa xursandmiz.\n\n" \
                     f"š“ Bot bo'yicha takliflaringiz,shikoyatlaringiz bo'lsa : @Toxirmalik12  ga murojat qilishingiz mumkin.\n\n" \
                     f"Sizga berilgan imkoniyatdan unumli foydalaningāļøāļøāļø"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "š  ijtimoiy tarmoqlarimiz":
        final_mess = f"ā”ļø Arab tili online kanalimiz : https://t.me/arabtilionline\n\n" \
                     f"ā”ļø Instagram :  Instagram.com/arabtilionline\n\n" \
                     f"ā”ļø Tiktok  :  Tiktok.com/@arabtilionline\n\n" \
                     f"ā”ļø Youtube  : Youtube.com/channel/UCvMbEInCiqqsv1eGwV9hwog"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "š    bosh menyu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('āļø  So\'rovnomani to\'ldirish')
        btn2 = types.KeyboardButton('š  Ijtimoiy tarmoqlarimiz')
        btn3 = types.KeyboardButton('š  Bot haqida')
        btn4 = types.KeyboardButton('Kurs haqida')
        markup.add(btn1,btn4,btn2,btn3)
        send_mess = f"Assalomu alaykum va Rohmatulloh !!! \n{message.from_user.first_name} arabtilidan online botimizga hush kelibsiz!\n" \
                    f"\nHurmatli tolibi ilmlar biz yana samarali,tezkor kurslarimizga qaytadan qabul boshladik. \n \n" \
                    f"š Bizning kurslarimizda :\n\n1ļøā£ - Arab tili harflari noldan o'rgatiladi.\n2ļøā£ - Arab tili fonetikasidan saboq beriladi.\n3ļøā£ - Arabcha matnlarini o'rtacha tezlikda o'qiy olasiz.\n4ļøā£ - Arabiy husnixat ham o'rgatiladi.\n" \
                    f"5ļøā£ - Arabtili gramatikasi o'rgatiladi.\n" \
                    f"\nš   Kurslarimiz o'rganuvchining darajasiga qarab, ayollar va erkaklar alohida guruhlarga bo'lingan holatda  o'tiladi .\nāļø Shu sababli quyidagi so'rovnomani to'ldirishizni so'rab qolamiz. \nShoshiling joylar soni cheklangan ššāāļø\n" \
                    f"\n Alloh boshlamoqchi bo'lgan ishlaringizni manfaatli qilsin!"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    #Erkaklar

    elif get_message_bot == "šØāāļø erkak (muzakkar)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        btn1 = types.KeyboardButton('5 kishilik guruh muzakkar (300 ming)')
        btn2 = types.KeyboardButton('8 kishilik guruh muzakkar (200 ming)')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1,btn2,btn4)
        final_mess = f"Siz qanday guruhda tahsil olmoqchisiz, iltimos quyidagi guruhlardan birini tanlang!"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    # 300 minlik

    elif get_message_bot == "5 kishilik guruh muzakkar (300 ming)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('0ļøā£ Arab tilini noldan o\'rganmoqchiman')
        btn2 = types.KeyboardButton('š Arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman')
        btn3 = types.KeyboardButton('šŖ Arab tili gramatikasini o\'rganmoqchiman ')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1, btn2,btn3, btn4)
        final_mess = f"Siz qaysi yo'nalish bo'yicha tahsil olishni hohlaysiz"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "0ļøā£ arab tilini noldan o\'rganmoqchiman":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/H62oebVKkFhkZDMy"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "š arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/H62oebVKkFhkZDMy"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "šŖ arab tili gramatikasini o\'rganmoqchiman":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/iWdKyJlxYo9kNTVi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    # 200 minglik

    elif get_message_bot == "8 kishilik guruh muzakkar (200 ming)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('0ļøā£ Arab tilini noldan o\'rganmoqchiman(2)')
        btn2 = types.KeyboardButton('š Arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman(2)')
        btn3 = types.KeyboardButton('šŖ Arab tili gramatikasini o\'rganmoqchiman(2)')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1, btn2, btn3, btn4)
        final_mess = f"Siz qaysi yo'nalish bo'yicha tahsil olishni hohlaysiz"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "0ļøā£ arab tilini noldan o\'rganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/_k-qHcf--c4yMDNi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "š arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/_k-qHcf--c4yMDNi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "šŖ arab tili gramatikasini o\'rganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring" \
                     f"\nTelegram guruh:  https://t.me/joinchat/kBynN5CEIRplNDhi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    # Ayollar

    elif get_message_bot == "š§ ayol (muannas)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('5 kishilik guruh muannas (300 ming)')
        btn2 = types.KeyboardButton('8 kishilik guruh muannas (200 ming)')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1, btn2, btn4)
        final_mess = f"Siz qanday guruhda tahsil olmoqchisiz, iltimos quyidagi guruhlardan birini tanlang!"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    # 300 minglik

    elif get_message_bot == "5 kishilik guruh muannas (300 ming)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Arab tilini noldan o\'rganmoqchiman')
        btn2 = types.KeyboardButton('Arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman')
        btn3 = types.KeyboardButton('Arab tili gramatikasini o\'rganmoqchiman')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1, btn2,btn3, btn4)
        final_mess = f"Siz qaysi yo'nalish bo'yicha tahsil olishni hohlaysiz"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "arab tilini noldan o\'rganmoqchiman":
           final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                        f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                        f"Telegram guruh:  https://t.me/joinchat/d_BXUeSZri1mMTIy"
           bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman":
           final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                        f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                        f"Telegram guruh:  https://t.me/joinchat/d_BXUeSZri1mMTIy"
           bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "arab tili gramatikasini o\'rganmoqchiman":
           final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                        f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                        f"Telegram guruh:  https://t.me/joinchat/atsKXHnUdMAwZTAy"
           bot.send_message(message.chat.id, final_mess, parse_mode='html')


    # 200 minglik

    elif get_message_bot == "8 kishilik guruh muannas (200 ming)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Arab tilini noldan o\'rganmoqchiman(2)')
        btn2 = types.KeyboardButton('Arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman(2)')
        btn3 = types.KeyboardButton('Arab tili gramatikasini o\'rganmoqchiman(2)')
        btn4 = types.KeyboardButton('š    Bosh menyu')
        markup.add(btn1, btn2, btn3, btn4)
        final_mess = f"Siz qaysi yo'nalish bo'yicha tahsil olishni hohlaysiz"
        bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "arab tilini noldan o\'rganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                     f"Telegram guruh:  https://t.me/joinchat/Ebd9shyViaU4NjMy"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "arab tilida talaffuzlarni chiqarishni o\'ganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                     f"Telegram guruh:  https://t.me/joinchat/Ebd9shyViaU4NjMy"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')

    elif get_message_bot == "arab tili gramatikasini o\'rganmoqchiman(2)":
        final_mess = f"š“ Hurmatli tolibi ilmlarlar quyidagi link orqali siz guruhga qo'shilishingiz mumkin, darslarimiz online tarzda, zoom hamda telegram guruhlarimizda olib boriladi !!!\n" \
                     f" š“ Guruhlarda darslar guruh to'la shakillanganidan so'ng boshlanadi.\n" \
                     f"Hurmatli foydalanuvchi agarda siz o'qimoqchi bo'lgan guruh to'lib qolgan bo'lsa, boshqa narxdagi kurslarimizga yozilishga harakat qilib ko'ring\n" \
                     f"Telegram guruh:  https://t.me/joinchat/YkT4DOw1L-01ODdi"
        bot.send_message(message.chat.id, final_mess, parse_mode='html')


bot.polling(none_stop=True)
