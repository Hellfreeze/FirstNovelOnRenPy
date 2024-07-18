# Вы можете расположить сценарий своей игры в этом файле.


init python:
    # Просто вспомогательный класс для хранения информации о вопросе, можно обойтись и картежом, но это было бы не сильно удобно
    class Question:
        def __init__(self, text, correct, *variants):
            if len(variants) != 4:
                raise Exception("Должно быть 4 варианта ответа")
            self.text = text
            self.correct = correct - 1
            self.variants = variants

define questions = (
Question(_('Cколько типов переменных в Python?'), 2, _("1"), _('4'), _('10'), _("Нет их")),
Question(_('Что такое def в Python?'), 2, _('Какая-то переменная'), _('Функция'), _('Класс'), _('Не знаю')),
Question(_('Что выведет следующая программа? a = [1,2,3,None,(),[],] print(len(a))'), 2, _('Ошибку'), _('6'), _('4'), _('7'))
) # Список вопросов. Сначала идёт текст вопроса, далее номер правильно ответа(начиная с 1), а затем варианты ответа
define variant_prefixes = (_('А'), _('Б'), _('В'), _('Г')) # Префиксы для вариантов ответа            
define test_hp = 2 # начальное количество жизней


$ current_question_python = 0
$ score_python = 0
$ ggname = None
# Определение персонажей игры.
define a = Character('Разработчик(Владислав)', color="#2ab92a")
define v = Character('Владислав', color="#b1d412")
define g = Character('Мику',color="#c01c76")
define z = Character("[ggname]",color="#0f2caa")

#Музыка и звуки
define audio.musmenu = "music/I-Still-Love-You.mp3"
define audio.sad = "music/sadshomyak.mp3"
define audio.cook1 = "music/egg.mp3"
define audio.home = "music/suzhet.mp3"
define audio.kit1 = "music/kit1.mp3"
define audio.kap = "music/kap1.mp3"
define audio.kni = "music/nozsh.mp3"
define audio.salt = "music/salt.mp3"
define audio.bath = "music/bath.mp3"
define audio.exit = "music/vihod.mp3"
define audio.st = "music/street.mp3"
define audio.foot = "music/ft.mp3"
define audio.magazin = "music/mag.mp3"
define audio.mg2 = "music/ma.mp3"
define audio.girl = "music/girl1.mp3"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Начало игры:
label start:

    scene bg sc1

    play music musmenu 
    
    ''' 
    Всем привет!

    Добро пожаловать в мой проект!)

    Данный проект представляет себя собственно говоря визуальную новеллу.

    Прошу не судить строго, так как это мой первый крупный проект на языке программирования Python.

    Перед началом.

    Добавлю некоторых персонажей и их мимику для демонстрации.

    '''
    with fade
    show 125_ta100 with moveinleft :
        xalign 0.5
        yalign 0.5
        zoom 1.5
    g "Приветствую пользователь!)))"
    
    hide 125_ta100
    show 198_tab101:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    g '''
    Я рада, что кто-то запустил данный проект!)

    Надеюсь, что Вам, уважаемая комиссия, понравится данный проект, который написал Шаханский Владислав Сергеевич! 
    '''
    hide 198_tab101

    show 207_tab111:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    g "А мы начинаем!)"
    hide 207_tab111 with moveoutleft
    
    menu:
        "Что будем делать дальше?"

        "Продолжить":
            jump go_start


        "Закончить":
            jump go_finish


    return

#Загрузка
label go_start:
    $ renpy.movie_cutscene('vid/LOAD.ogv')
    jump dalee

    return

#Грустный конец 
label go_finish:

    play music sad 
    scene sadhomyak:
        xalign 0.5
        yalign 0.5
        zoom 2.7

    "Печально, что не хотите продолжить прохождение."

    return

with fade

#Запись имени пользователя
screen name_input(prompt):
    modal True
    frame:
        background Frame("#c01c76")
        align(0.5, 0.5)
        xsize 400 ysize 220
        vbox:
            xfill True
            yfill True
            text prompt xalign 0.5
            input id "input" xalign 0.5
            hbox:
                xalign 0.5

#Ввод персонажа
label dalee:
    $ ggname = renpy.input("Введите имя персонажа", screen="name_input", length=12, allow = 'йёцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСЁМИТЬБЮ').strip()
    if ggname == "":
        $ ggname = "Владислав"

    jump suzhet

    return

with fade

#Начало
label suzhet:
    scene bg bl1
    a '''
    Приятной игры: [z] 
    '''
    $ renpy.movie_cutscene('vid/LOAD.ogv')

    jump home

#Начало сюжета дома
label home:
    play music home
    scene home 1:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    z '''
    Настало утро, пора уже вставать и заниматься своими делами.

    Иначе, ничего на свете не успею.

    Также, мне нужно незабыть и пройти тест на знание языка программирования Python.

    Но, сначала нужно привести себя в порядок. {w} А именно: умыться, поесть. 

    '''

    '''
    Наш герой идёт на кухню

    '''
    jump kitchen

with fade(4)


#Поход на кухню
label kitchen:
    play music kit1
    scene kitchen:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    z '''
    Так чтобы приготовить себе на завтрак

    '''
    menu:
        "Что будем есть на завтрак?"

        "Яичница":
            jump cooking_egg


        "Мясной салат":
            jump salat

#Готовка яичницы
label cooking_egg:
    play music cook1
    scene egg_cook:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    
    z '''

    Как вкусно получилось, теперь пойду умоюсь и почищу зубы.

    '''
    stop music
    jump bathroom    

#Готовка салата
label salat:
    z '''
    Так, какой там рецепт салата.

    Вспомнил.

    Сначала возьму листья капусты, затем нарежу и возьму другие ингредиенты.

    Главное не забыть посолить.

    ''' 
    play music kap
    scene black
    play music kap

    play music kni
    scene black
    play music kni

    play music salt
    scene black
    play music salt
    with fade
    stop music

    scene minutes:
        xalign 0.5
        yalign 0.5
        zoom 1.5

    with fade


    scene salat:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    z '''

    Ура, готово!

    '''

    z '''

    Как вкусно получилось, теперь пойду умоюсь и почищу зубы.

    '''

    jump bathroom


    

# Ванная комната    
label bathroom:
    with fade
    scene bathroom:
        xalign 0.5
        yalign 0.5
        zoom 2.4
    z '''
    Пора привести себя в порядок
    '''
    with fade

    scene black
    play music bath 

    '''
    ....

    '''

    scene bathroom:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    z '''
    
    Наконец-то я привел себя в порядок.

    Пора уже идти. 

    '''
    jump outhome


with fade(4)


# Наш главный герой вышел из дома
label outhome:
    play music exit

    stop music
    
    scene outhome 1:
        xalign 0.5
        yalign 0.5
        zoom 2.4

    play music st

    '''
    После, наш главный герой, вышел из дома и пошёл по своим делам 
    
    '''
    
    play music foot
    
    with fade
    jump market

# Диалог с другом и поход в магазин 
label market:
    play music magazin
    scene magazine: 
        xalign 0.5
        yalign 0.5
        zoom 2

    '''

    Наш главный герой пришёл в библиотеку/магазин

    '''
    z '''
    Наконец-то я пришёл сюда, долгий маршрут однако выбрал.

    Надеюсь, то что мне нужно, в наличии есть.

    '''

    '''
    Но вдруг откуда не возьмись появился давний друг, с которым наш главный герой не виделся 2 года
    
    '''

    show f_kyo_1a0101 with moveinright :
        xalign 0.5
        yalign 1
        zoom 0.5
    v '''

    Хээээй, давно не виделись, [ggname]!
    '''
    z '''
    Привет, да.{w} Какими ты судьбами здесь?
    '''
    hide f_kyo_1a0101

    show f_kyo_1a0300:
        xalign 0.5
        yalign 1
        zoom 1

    v'''
    Отпуск у меня, решил навестить свою родню.
    '''
    hide f_kyo_1a0300
    
    show f_kyo_1a0200:
        xalign 0.5
        yalign 1
        zoom 1
    v '''
    Всё равно могу даже на удалёнке работать.
    '''

    z '''
    Напомни пожалуйста, а кем ты работаешь?
    '''


    '''
    У твоего давнего друга поменялась интонация и синтез речи 
    '''
    hide f_kyo_1a0200

    show f_kyo_1b0200:
        xalign 0.5
        yalign 1
        zoom 1
    a '''
    Забывчивый ты конечно, я программист. {w} *Смеется*
    '''
    hide f_kyo_1b0200

    show f_kyo_1b0400:
        xalign 0.5
        yalign 1
        zoom 1   
    a '''
    Пробовал себя различных айтисферах, теперь по итогу занимаюсь разработками игр.
    '''

    hide f_kyo_1b0400

    show f_kyo_1b0700:
        xalign 0.5
        yalign 1
        zoom 1   
    z '''
    Интересно.
    '''

    a '''
    Но, и ещё на другом языке программирования. {w} На котором собcтвенно говоря можно заниматься веб разработкой. 

    У тебя как успехи друг мой? 

    '''

    z '''
    Только начинаю вливаться в айтисферу, думаю какой язык изучать.

    Посоветуешь? 
    '''
    hide f_kyo_1b0700
    show f_kyo_1b1801:
        xalign 0.5
        yalign 1
        zoom 1   

    a '''
    Конечно.

    Для начала, посоветую язык программирования Python. {w} Он достаточно прост для новичков, легко его изучить.

    '''
    z '''
    Я когда-то что-то пробовал делать на данном языке.

    Забыл я его, скорее всего. 

    '''

    a ''' 
    Так пройди тест на его знание, может вспомнишь. {w} Но перед этим, купи самоучитель в данном магазине.
    '''
    z '''
    Хорошо, спасибо за совет. 

    Ладно, я пойду тогда, очень рад был видеть тебя спустя долгое время. 

    '''
    hide f_kyo_1b1801
    show f_kyo_1b0300:
        xalign 0.5
        yalign 1
        zoom 1  

    
    a '''
    Да, взаимно. Удачи! 

    '''
    hide f_kyo_1b0300 with moveoutleft
    '''

    После длительного диалога, главный герой вошёл в магазин 

    '''
    jump insidemag

with fade

label insidemag:
    play music mg2
    scene lib1:
        xalign 0.5
        yalign 0.5
        zoom 1.5

    
    z '''
    Теперь пора взять, то за тем, чем я пришёл.

    '''
    with fade

    '''
    Спустя некоторое время поисков.

    '''
    with fade

    '''
    К сожалению наш герой не нашёл, то что искал.

    '''
    z '''
    Вот зараза, к сожалению не повезло мне сегодня. 

    '''

    '''
    Уходя, наш герой заметил свою одногруппницу.

    И решается к ней подойти. 

    '''
    with fade
    play music girl
    scene girl_stay:
        xalign 0.5
        yalign 0.5
        zoom 1.5

    z '''
    Привет, Мику, а ты что здесь делаешь?

    '''

    '''
    Мику посмотрела на тебя и начала ввести с тобой диалог.

    '''
    with fade


    scene lib1:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    show 125_ta100:
        xalign 0.5
        yalign 0.5
        zoom 1.5

    g '''
    Тебя ждала, [ggname].

    Влад предупредил меня, что здесь находится последний самоучитель по Python.

    '''
    hide 125_ta100
    show 198_tab101:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    g '''
    Я как раз была здесь и решила взять его для тебя!
    '''
    g '''
    Ну что, может к тебе пойдем? 
    '''
    hide 198_tab101
    show 138_ta114:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    z '''
    Блин я даже не знаю.
    '''
    g '''
    Ты сомневаешься в том, чтобы пойти вместе со мной ? 
    Или же нет?

    '''
    with fade 

    menu:
        "Что будем делать дальше?"

        "Взять и пойти вместе с ней":
            jump go_next1


        "Ничего не отвечать":
            jump go_next2



label go_next1:
    z '''
    Нет, пошли.

    '''
    hide 138_ta114
    show 198_tab101:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    g '''
    Ура, пошли!
    '''

    '''
    Ты вместе с Мику пошли к тебе домой.

    '''
    with fade
    jump comehome




label go_next2:
    ''' 
    Мику поменялась в лице.
    '''
    hide 138_ta114
    show 133_ta108:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    
    '''
    Мику схватила тебя за руку и сказала: 
    '''
    hide 133_ta108
    show 132_ta107:
        xalign 0.5
        yalign 0.5
        zoom 1.5

    g '''
    Пошли, нечего здесь стоять и время просто напросто терять!
    '''

    '''
    Ты вместе с Мику пошли к тебе домой.

    Не нужно девушек обижать, уважаемый пользователь!

    '''
    jump comehome

    


label comehome:
    scene home 1:
        xalign 0.5
        yalign 0.5
        zoom 2.4
    with fade 


    '''
    Вы пришли домой.

    '''
    scene home 1:
        xalign 0.5
        yalign 0.5
        zoom 2.4
    
    show 127_ta102:
        xalign 0.5
        yalign 0.5
        zoom 1.5
     
    g '''
    Что-ж, мало ли ты забыл. 
    Но мне Влад сказал, чтобы я напомнила тебе.
    Ты должен пройти тест на знание Python.
    '''
    hide 127_ta102
    show 135_ta111:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    z '''
    Хорошо. 

    '''


    '''
    Ты подошёл к своему компьютеру и начал выполнять тест.
    '''
    stop music
    jump start_quiz_python



screen question_screen(question_index, question):
    frame:
        padding (8, 8, 8, 8)
        xalign .5
        yalign .5
        xsize 800
        vbox:
            spacing 40
            text "%s. %s" % (question_index + 1, (question.text))
            grid 2 2:
                xfill True
                # экран должен возвращать индекс выбранного ответа
                for i, variant in enumerate(question.variants):
                    textbutton "%s. %s" % ((variant_prefixes[i]), __(variant)) action Return(i)

image gray = Solid('#333')

label start1:
    stop music
    scene gray
    "Время пройти тест!"
    jump start_quiz_python


image gray = Solid('#333')

label start_quiz_python:
    scene gray
    "Время пройти тест!"
    jump test

label test:
    $ question_count = len(questions)
    $ questions_order = list(range(0, question_count)) # создаём список в котором хранятся индексы(номера) вопросов
    $ renpy.random.shuffle(questions_order) # перемешиваем индексы вопросов
    $ question_index = 0

    $ score = 0
    $ hp = test_hp

    jump test_loop

label test_loop:
    # если вопросы закончились, то прыгаем в лейбл test_complete
    if question_index >= question_count:
        jump test_complete

    $ question = questions[questions_order[question_index]] # получаем текущий вопрос по его индексу
    call screen question_screen(question_index, question) # вызываем экран, в котором будет отображён текст вопроса и варианты ответа
    # экран возвращает индекс ответа(хранится в переменной _return), который выбрал игрок
    if _return == question.correct:
        "Верно!"
        $ score += 1
    else:
        "Неверно!"
        $ hp -= 1

    $ question_index += 1

    # если жизни закончились, то прыгаем в test_failed
    if hp == 0:
        jump test_failed

    jump test_loop

label test_failed:
    "У вас закончились жизни. Количество набранных очков сброшено до нуля."
    # сбрасываем счёткик жизней и очков
    $ score = 0
    $ hp = test_hp
    jump test_loop

label test_complete:
    "Тест пройден. Количество набранных очков: [score]."

    jump fin


label fin:
    '''
    Поздравляю тебя [ggname], игра пройдена!

    '''

    $ renpy.movie_cutscene('vid/End.ogv')
    $ renpy.movie_cutscene('vid/LOAD.ogv')
    return














  







    
