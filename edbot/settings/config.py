import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import os


from dotenv import load_dotenv
load_dotenv()

vk_session = vk_api.VkApi(token=os.environ.get('GROUP_TOKEN'))


GROUP_ID = os.environ.get('GROUP_ID')
GROUP_TOKEN = os.environ.get('GROUP_TOKEN')


API_VERSION = '5.120'

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

vk_session = VkApi(token=os.environ.get('GROUP_TOKEN'), api_version=API_VERSION)
vk_ = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

# In settings/.environment, specify the token and the VK community id