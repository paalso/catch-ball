# catch-ball
### Catch the ball game


The game is implemented using the [Pygame](https://en.wikipedia.org/wiki/Pygame) platform,
so its launch requires [installation of this library](https://www.pygame.org/wiki/GettingStarted)
as well as [the pygame-menu library](https://pygame-menu.readthedocs.io/en/4.1.6/):

```bash
python3 -m pip install -U pygame --user
python3 -m pip install -U pygame-menu --user
```

Launch the game:
```bash
puthon3 run.py
```

[![Watch the video]](https://www.youtube.com/watch?v=6yr6O_e4-Uo)


https://pygame-menu.readthedocs.io/en/4.1.6/

Игра реализуется как практическое задание по курсу

[Практика программирования на Python 2020](https://www.youtube.com/playlist?list=PLolqo5ko7kbnGGmzGrCoDW0H1Xq-Vk6Oz):

Описание и задания по проекту:

[Игра "Поймай шарик" (часть 1)](http://cs.mipt.ru/python/lessons/lab6.html)

[Игра "Поймай шарик" (часть 2)](http://cs.mipt.ru/python/lessons/lab7.html)

#### Задания

- **Сделать код читабельным и документированным.**

Не сделано ибо лень

- **Реализовать подсчёт очков.**

- **Сделать шарики двигающимися со случайным отражением от стен.**

- **Реализовать одновременное присутствие нескольких шариков на экране.**

- **Добавить второй тип мишени со своей формой и своим специфическим харктером движения.**

- **Выдавать за эти мишени другое количество очков.**

Сделано: два типа мишени - шарики и колечки.

Шарики  отражаются от стен и движутся регулярным предсказуемым образом - с постоянной скоростью и прямолинейно.
Колечки движутся хаотично: постоянно немножко меняют скорость и направление, раз в единицу времени (2 секунды) меняют направление и скорость совершенно произволным образом, аналогично при отражении от стенок.

- **Сделать таблицу лучших игроков, авматически сохраняющуюся в файл.**

Сделано
