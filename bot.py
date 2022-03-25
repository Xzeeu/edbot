import vk_api, vk
import json
from datetime import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from edbot.settings import*
from edbot.keyboard import*
from edbot.maindef import *
from edbot.test import *


for event in longpoll.listen():

    aproftest(event)

    if event.type == VkBotEventType.MESSAGE_NEW:


        if event.obj.message['text'] != 'pt':
            if event.from_user:
                if 'callback' not in event.obj.client_info['button_actions']:
                    print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')
        
                new_m_send(event, keyboard_1.get_keyboard(), '👋Привет!) Я помогу тебе определиться с профессией, расскажу о том как поступить в университет и поделюсь списком полезных сайтов)\n Удачи в поступлении!👌 ')
        
        
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') in CALLBACK_TYPES:
            r = vk_.messages.sendMessageEventAnswer(
                      event_id=event.object.event_id,
                      user_id=event.object.user_id,
                      peer_id=event.object.peer_id,                                                   
                      event_data=json.dumps(event.object.payload))


        elif event.object.payload.get('type') == 'proftest':
                    proftest(event)
        

        elif event.object.payload.get('type') == 'dataege':
            event_m_send(event, keyboard_1.get_keyboard(), 'Расписание ЕГЭ 2022: \n\n    В основной период расписание ЕГЭ выглядит следующим образом:\n\n-26 мая - география, литература, химия;\n-30 и 31 мая - русский язык;\n-2 июня - математика профильного уровня;\n-3 июня - математика базового уровня;\n-6 июня - история, физика;\n-9 июня - обществознание;\n-14 июня - иностранные языки;\n-16 и 17 июня - раздел "Говорение" иностранных языков;\n-20 и 21 июня - информатика.' )

        elif event.object.payload.get('type') == 'kakpostupit':
            event_m_send(event, keyboard_1.get_keyboard(), '   Если вы поступаете в вуз после 11-го класса школы, то в большинстве случаев должны сдать Единый государственный экзамен (ЕГЭ). \
                \n📌Какие предметы нужны для поступления на выбранное вами направление или специальность, можно посмотреть на сайте учебного заведения\
                \n\n📌На бюджетную очную форму обучения бакалавриата и специалитета вузы начинают принимать документы не позднее 20 июня. Заканчивается прием документов не ранее 10 июля, если ВУЗ проводит дополнительные вступительные испытания и не позднее 20 июля, если вы поступаете по результатам ЕГЭ' )
            

            event_m_send(event, keyboard_1.get_keyboard(), '📌В 2022 году подать документы можно в 5 вузов, при этом каждый вуз вправе самостоятельно определить, на какое количество специальностей он примет документы от одного абитуриента. Количество специальностей может варьироваться от 2 до 10.')

            event_m_send(event, keyboard_1.get_keyboard(), 'При поступлении в вуз вам необходимо будет заполнить заявление о поступлении. Как правило, его можно скачать на сайте вуза. К заявлению нужно приложить:\
                            \n👉паспорт или другой документ, удостоверяющий личность и гражданство абитуриента;\
                            \n👉документ о предыдущем полученном образовании: аттестат об окончании школы, диплом о начальном, среднем или высшем профессиональном образовании;\
                            \n👉информацию о результатах ЕГЭ, если вы его сдавали;\
                            \n👉2 фотографии, если при поступлении вы будете проходить дополнительные вступительные испытания;\
                            \n👉приписное свидетельство или военный билет (при наличии);\
                            \n👉медицинскую справку формы 086/у - для медицинских, педагогических и некоторых других специальностей и направлений;' )\

        
        elif event.object.payload.get('type') == 'dopball':
            event_m_send(event, keyboard_1.get_keyboard(), '🏅За какие достижения могут добавить баллы к ЕГЭ?\
                \n- Аттестат с отличием\
                \n- Участие в школьных олимпиадах\
                \n- Призовые места в международных спортивных соревнованиях\
                \n- Наличие значка ГТО\
                \n- Другие спортивные достижения\
                \n- Победа в чемпионатах среди инвалидов\
                \n- Волонтерская деятельность\
                \n❕Список достижений, за которые абитуриент может получить дополнительные баллы, зависит от выбранного вуза. Не все высшие учебные заведения одинаково оценивают те или иные заслуги потенциального студента.')
        

        elif event.object.payload.get('type') == 'polres':
            event_m_send(event, keyboard_1.get_keyboard(), '👉Полезные сайты для поступающих:\
                \n    ФИПИ (http://fipi.ru/) - Открытый банк заданий — это демонстрационные варианты ЕГЭ от самих разработчиков КИМов.\
                \n    Официальный портал ЕГЭ (http://www.ege.edu.ru/ru/) - информация о результатах ЕГЭ, минимальных баллах для поступления в ВУЗы и таблица перевода первичных баллов в тестовые\
                \n    Учёба.ру (https://www.ucheba.ru/) - Это самый большой каталог учебных заведений и программ в России и за рубежом. Очень удобно подбирать вуз, так как вся информация сразу видна на одной странице\
                \n    Калькулятор баллов ЕГЭ ВШЭ (https://www.hse.ru/ege/calc.html) - Eдобный сервис для оценки шансов поступить в конкретный вуз')





                

if __name__ == '__main__':
    print()
