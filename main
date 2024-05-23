import time
from recognition import Recognaizer
from voice import voice
from commands import Command

rec = Recognaizer()
text_gen = rec.listen()
rec.stream.stop_stream()
voice.text_to_speech('Привет! Я голосовой ассистент')
print('Перечень команд: \n 1. Команда "Шутка": создать шутку и вывести её \n 2. Команда "Записать": создать шутку и записать её в конец файла \n 3. Команда "Тип": создать шутку и сказать её тип \n 4. Команда "Категория": создать шутку и сказать её категорию \n 5. Команда "Спасибо": завершить работу')
time.sleep(0.5)
rec.stream.start_stream()
for text in text_gen:
    print(text)

    rec.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    rec.stream.start_stream()
