
# hehe vk bot

## Описание
Данный бот для VK автоматически отправляет случайные видео из YouTube или Pornhub пользователям, которые напишут определённое сообщение. Бот имеет небольшую долю вероятности (5%) отправить видео из категории "для взрослых", что добавляет элемент неожиданности. Проект создан для веселья и экспериментов.

## Возможности
- Получение случайного видео с YouTube по популярным темам.
- Возможность отправки ссылки на случайное видео с Pornhub.
- Простое взаимодействие через личные сообщения в VK.
- Логирование работы для отладки.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/random-video-bot.git
   cd random-video-bot
   ```

2. Создайте группу в VK и получите токен группы:
   - Перейдите в настройки группы -> Работа с API.
   - Включите Long Poll API.
   - Скопируйте токен доступа.

3. Получите API-ключ для YouTube:
   - Перейдите в [Google Cloud Console](https://console.cloud.google.com/).
   - Создайте проект и включите API YouTube Data v3.
   - Сгенерируйте API-ключ.

4. Отредактируйте файл:
   - Вставьте ваш `GROUP_TOKEN`, `GROUP_ID` и `API_KEY` в соответствующие переменные.

5. Запустите бота:
   ```bash
   python bot.py
   ```

## Использование

1. Напишите боту сообщение **"мне повезёт"**:
   - С вероятностью 95% бот отправит случайное видео с YouTube.
   - С вероятностью 5% бот отправит случайное видео с Pornhub.

2. Все сообщения, логи и ошибки выводятся в консоль для удобства отладки.

## Пример логов
```
Лог: Запуск бота...
Лог: Ожидание событий...
Лог: Новое сообщение от 123456789: мне повезёт
Лог: Выбран Pornhub
Лог: Запущена функция get_random_pornhub_video()
Лог: Выбран поисковый запрос 'weird'
Лог: Ответ от Pornhub - Код 200
Лог: Случайное видео - 
Лог: Отправка сообщения пользователю 123456789: Вот тебе сюрприз: 
```

## Требования
- Python 3.7+
- Библиотеки:
  - `vk_api`
  - `requests`
  - `beautifulsoup4`

## Заметки
- **Для безопасности**: Не публикуйте токены группы и API-ключи в открытом доступе.
- Убедитесь, что ваш бот соблюдает правила VK и Google API.
- Проект создан исключительно для развлекательных целей. Используйте ответственно.

## Лицензия
Этот проект распространяется под лицензией MIT. Используйте, модифицируйте и делитесь свободно.
