from voice import voice
import requests
import sys
def thanks(text):
    option = ('Всё для тебя, душенька')
    voice.text_to_speech(option)
    sys.exit()

def create(text):
    response = requests.get(f' https://v2.jokeapi.dev/joke/Any?safe-mode')
    data = dict(response.json())
    if data['type'] == 'twopart':
        print(data['setup'],'\n', data['delivery'])
    if data['type'] == 'single':
        print(data['joke'])

def write_down(text):
    f = open('jokes.txt', 'a')
    f.write('\n')
    response = requests.get(f' https://v2.jokeapi.dev/joke/Any?safe-mode')
    data = dict(response.json())
    if data['type'] == 'twopart':
        f.write(data['setup'])
        f.write('\n')
        f.write(data['delivery'])
    if data['type'] == 'single':
        f.write(data['joke'])

def category(text):
    response = requests.get(f' https://v2.jokeapi.dev/joke/Any?safe-mode')
    data = dict(response.json())
    if data['type'] == 'twopart':
        print(data['setup'], '\n', data['delivery'])
    if data['type'] == 'single':
        print(data['joke'])
    print('Category:', data['category'])

def type(text):
    response = requests.get(f' https://v2.jokeapi.dev/joke/Any?safe-mode')
    data = dict(response.json())
    if data['type'] == 'twopart':
        print(data['setup'], '\n', data['delivery'])
    if data['type'] == 'single':
        print(data['joke'])
    print('Type:', data['type'])
