import telebot
from mainforeal import Text2ImageAPI
from mainseriouslynotforeal import TOKEN, API_KEY, SECRET_KEY

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text

    # Используем Text2ImageAPI для генерации изображения
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    # Сохраняем изображение
    file_path = "generated_image.jpg"
    api.save_image(images, file_path)

    # Отправляем изображение пользователю
    with open(file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

# Запуск бота
bot.polling()