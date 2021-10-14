import vk
from time import sleep
from vk_api import VkApi
from settings import OWNER_ID, POST_ID, TOKENS, DELETE_COMMENTS, DELAY_BEFORE_DELETION


def main():
    print('Цикл запущен...')

    for i, token in enumerate(TOKENS, start=1):
        print(f'Работаем с {i} токеном...')

        # Создаём объект для подключения к VK API
        vk_session: VkApi = VkApi(token=token)

        # Получаем объект для работы с API
        session = vk.Session(access_token = token)

        api = vk.API(session, v = "5.95")

        # Отправляем комментарий
        try:
            api.account.setOnline(voip =1)
        except Exception as error:
            print(f'При отправке коментария произошла ошибка!\n'
                  f'Информация: {type(error)} -> {error}')
            continue

        # Если коментарий нужно удалить, удаляем
        if DELETE_COMMENTS:
            # Ждём перед удалением...
            sleep(DELAY_BEFORE_DELETION)

            # Удаляем коментарий
            try:
                api.wall.deleteComment(owner_id=OWNER_ID, comment_id=comment['comment_id'])
            except Exception as error:
                print(f'При удалений коментария произошла ошибка!\n'
                      f'Информация: {type(error)} -> {error}')
                continue


if __name__ == '__main__':
    main()
