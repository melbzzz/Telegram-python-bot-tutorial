import telebot  # pip install pyTelegramBotAPI
import os

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# Exemple of an initial command. (/start)


@bot.message_handler(commands=['start'])
def test(message):
    bot.send_message(message.chat.id, "Bem vindo ao meu bot")

# Exemple of a command echoing a massgem provided by the user.
@bot.message_handler(commands=['echo'])
def test(message):
    messageText = message.text.replace("/echo", "")
    bot.send_message(message.chat.id, messageText)

# Exemple of a command sending a picture to the user.
@bot.message_handler(commands=['foto'])
def test(message):
    messageText = message.text.replace("/echo", "")
    bot.send_message(message.chat.id, messageText)
    photo = open('photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)

# Exemple of a command consuming a api to get a random dog image to the user
@bot.message_handler(commands=['bop'])
def bop(message):
    url = get_image_url('https://random.dog/woof.json','url')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)
    

# Exemple of a command consuming a api to get a random fox image to the user 
@bot.message_handler(commands=['fox'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/img/fox','link')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)
  
# Auxiliary methods 

def get_url(url, key):
    contents = requests.get(url).json()
    url = contents[key]
    return url


def get_image_url(url, key):
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url(url, key)
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    
bot.polling()
