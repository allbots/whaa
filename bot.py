from time import sleep
from vk_api import VkApi
from settings import OWNER_ID, POST_ID, TOKENS, DELETE_COMMENTS, DELAY_BEFORE_DELETION

try:
    session = vk.Session(access_token = token)
    api = vk.API(session, v = "5.95")
    api.account.setOnline(voip = 1)
    except(vk.exceptions.VkAPIError):
    print("Токен не работает. Возможно, пользователь сменил пароль учётной записи. \n Удаление токена из временного списка.")


if __name__ == '__main__':
    main()
