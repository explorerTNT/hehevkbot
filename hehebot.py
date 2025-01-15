import random
import vk_api
import requests
from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Токены и ID
GROUP_TOKEN = ""  # Вставь токен своей группы
GROUP_ID = ""  # ID группы
API_KEY = ""  # Твой API-ключ YouTube

# Функция для получения случайного видео с YouTube
def get_random_youtube_video():
    print("Лог: Запущена функция get_random_youtube_video()")
    search_terms = ['funny', 'music', 'tech', 'animals', 'gaming', 'news']
    search_term = random.choice(search_terms)
    print(f"Лог: Выбран поисковый запрос '{search_term}'")
    
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": search_term,
        "type": "video",
        "maxResults": 50,
        "key": API_KEY
    }
    
    response = requests.get(url, params=params)
    print(f"Лог: Ответ от YouTube API - Код {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        print(f"Лог: Найдено {len(items)} видео")
        if items:
            random_video = random.choice(items)
            video_id = random_video["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"Лог: Случайное видео - {video_url}")
            return video_url
        else:
            print("Лог: Видео не найдены")
            return "Не удалось найти видео."
    else:
        print(f"Лог: Ошибка API: {response.status_code}, {response.text}")
        return f"Ошибка API: {response.status_code}, {response.text}"

# Функция для получения случайного видео с Pornhub
def get_random_pornhub_video():
    print("Лог: Запущена функция get_random_pornhub_video()")
    query = random.choice(["hot", "amateur", "funny", "weird", "random"])
    print(f"Лог: Выбран поисковый запрос '{query}'")
    url = f"https://www.pornhub.com/video/search?search={query}"

    try:
        response = requests.get(url)
        print(f"Лог: Ответ от Pornhub - Код {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            videos = soup.find_all("a", href=True)
            video_links = [
                f"https://www.pornhub.com{video['href']}" for video in videos if "/view_video.php?" in video["href"]
            ]
            if video_links:
                random_video = random.choice(video_links)
                print(f"Лог: Случайное видео - {random_video}")
                return random_video
        print("Лог: Видео не найдены")
        return "Не удалось найти видео, попробуй позже!"
    except Exception as e:
        print(f"Лог: Ошибка при запросе к Pornhub - {e}")
        return "Ошибка при запросе к Pornhub."

# Функция для отправки сообщений
def send_message(vk, user_id, message):
    try:
        print(f"Лог: Отправка сообщения пользователю {user_id}: {message}")
        vk.messages.send(user_id=user_id, message=message, random_id=random.randint(1, 1_000_000))
    except Exception as e:
        print(f"Лог: Ошибка при отправке сообщения: {e}")

# Основна
def main():
    try:
        print("Лог: Запуск бота...")
        vk_session = vk_api.VkApi(token=GROUP_TOKEN)
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, GROUP_ID)
        print("Бот запущен успешно")
    except vk_api.exceptions.ApiError as e:
        print(f"Лог: Ошибка API при инициализации: {e}")
        return
    except Exception as e:
        print(f"Лог: Общая ошибка при подключении к LongPoll: {e}")
        return

    print("Лог: Ожидание событий...")
    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_message = event.message.text.lower()
                user_id = event.message.from_id
                print(f"Лог: Новое сообщение от {user_id}: {user_message}")
                if user_message == "мне повезёт":
                    if random.randint(1, 100) <= 5:
                        print("Лог: Выбран Pornhub")
                        video = get_random_pornhub_video()
                        send_message(vk, user_id, f"Вот тебе сюрприз: {video}")
                    else:
                        print("Лог: Выбран YouTube")
                        video = get_random_youtube_video()
                        send_message(vk, user_id, f"Держи случайное видео: {video}")
        except Exception as e:
            print(f"Лог: Ошибка при обработке события: {e}")

if __name__ == "__main__":
    main()
