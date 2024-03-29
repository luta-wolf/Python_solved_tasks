# Магический шар 8
'''
Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.
'''

import random

def play_game():
	n = 'да'
	while n.lower() == 'да' or n.lower == 'yes':
		s = input('Задай свой вопрос: ')
		print(random.choice(answers))
		s = input('Хочешь задать еще вопрос? (Да / Нет) ')
		if s.lower() == 'нет' or s.lower() == 'no':
			print('Возвращайся если возникнут вопросы!')
			break

answers = [
	'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
	'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
	'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
	'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно'
	]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Представься: ')
print(f'Привет {name}')
play_game()
