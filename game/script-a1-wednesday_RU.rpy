label ru_A10:

play music music_happiness fadein 2.0

scene bg school_scienceroom
with locationchange

"Этим утром я чувствую себя сильно утомлённым, возможно из-за того, что вчерашний день был столь утомительным. Кроме того, я сегодня проснулся раньше времени."

"Я поспешно здороваюсь с %(name_shizune)s и Мишей и принимаюсь решать задания с доски. Кажется, над примерами сегодня придётся попотеть."

"Но я не возражаю. %(name_shizune)s и Миша могут начать требовать от меня ответа по поводу вступления в Школьный совет, хоть и прошёл всего день."

"С них ведь станется. А ответить я пока не смогу, поэтому нынешняя ситуация вполне меня устраивает."

"Минут через десять после начала урока входит Ханако и молча занимает своё место. Никто не смотрит на неё, даже учитель не обращает внимания на её опоздание."

"Он объявляет, что мы снова делимся на группы."

show shizu behind_smile at tworight 
show misha perky_smile at twoleft 
with charaenter

"Повернувшись, я вижу, что %(name_shizune)s и Миша смотрят на меня. %(name_shizune)s мило, но в то же время угрожающе улыбается мне, как бы говоря: «Вот ты и попался. Теперь не уйдёшь»."

show misha hips_grin
with charachange

mi "%(name_hicchan)s~, выходит, мы снова вместе! Ур-ра~!"

show misha hips_grin_close
show shizu behind_smile_close
with characlose

"Миша поворачивается ко мне, а %(name_shizune)s тем временем передвигает свою парту поближе к моей. Действительно, сбежать теперь можно лишь прыгнув в окно."

"Увы, это неприемлемый вариант."

show shizu adjust_smug_close
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "Что-то не так, %(name_hicchan)s?"

show shizu adjust_happy_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "А! %(name_hicchan)s, ты уже решил по поводу вчерашнего? Ты ведь обещал подумать о вступлении в Школьный совет."

show misha hips_grin_close
with charachange

mi "Всё в порядке, %(name_hicchan)s. Вчера мы с %(name_sicchan)s решили, что было бы невежливо требовать от тебя ответа так скоро, верно? Верно~!"

show misha cross_laugh_close
with charachange

mi "Ха-ха-ха-ха-ха-ха~!"

"Очень рад, что вы нашли новую мишень для своих шуток. И ещё больше – тому, что вам известно, насколько настырными вы можете быть."

show shizu basic_normal2_close
with charachange

show misha perky_smile_close
with charachange

"Вновь переключившись в «серьёзный режим», %(name_shizune)s демонстративно хлопает по учебнику тыльной стороной ладони."

"Я пробегаю глазами по заданию: нам предстоит в основном чтение, собственно задачек там всего две."

"Меня так и подмывает высказать что-нибудь относительно того, насколько излишня её спешка, учитывая объём работы. Правда, %(name_shizune)s, видимо, известно, насколько он мал, но её это попросту не волнует."

"Похоже, её волнует не столько количество, сколько сам факт наличия работы. Она ко всему приступает с одинаковым рвением."

show hanako emb_downtimid at offscreenright 
with None

show hanako emb_downtimid at right 
show shizu basic_normal2_close at Transform(xalign=0.4) 
show misha perky_smile_close at Transform(xalign=-0.3) 
show bg school_scienceroom at bgleft 
with charamove

stop music fadeout 7.0

"Отвлекаясь от чтения, я натыкаюсь взглядом на Ханако. Она решает задачи. Судя по всему, в одиночку."

"Не припоминаю, чтобы она хоть раз работала с кем-нибудь."

"Неудивительно, учитывая, насколько она застенчива."

hi "Эй, а вон та девушка…"

show misha perky_confused_close
with charachange

mi "А? Кто, %(name_hicchan)s?"

hi "Вон та. Ханако. Она всегда работает одна?"

mi "Думаю, да, %(name_hicchan)s. Тебе её из-за этого жалко?"

hi "Я просто подумал, не могла бы она поработать с нами, например?"

show misha perky_sad_close
with charachange

mi "М-м-м-м… Нет, не думаю, что это хорошая идея, %(name_hicchan)s."

hi "Почему же?"

mi "%(name_sicchan)s с ней не поладит."

hi "Почему?"

show misha perky_confused_close
with charachange

"Миша уходит от ответа, издав странный смешок: нервный, но всё с той же обычной для неё скачущей интонацией."

mi "По кочану, %(name_hicchan)s."

"В этот момент %(name_shizune)s отвлекается на наш разговор; я только сейчас замечаю, что всё это время Миша беспрестанно жестикулировала."

show shizu basic_frown_close
with charachange

shi "…"

show misha perky_sad_close
with charachange

mi "Что, %(name_sicchan)s? «Друг моего врага – мой враг»? Звучит слишком резко, я не буду этого говорить."

hi "Ты это уже сказала."

show misha hips_grin_close
with charachange

mi "Знаю, %(name_hicchan)s, это ничего, что ты подслушал~!"

"Видимо, так Миша обеспечивает справедливость в общении, ведь без неё я бы ни за что не понял, что хочет сказать %(name_shizune)s. И наоборот."

"Выходит, ещё одна причина, по которой Миша постоянно жестикулирует, – она хочет, чтобы %(name_shizune)s была в курсе всех разговоров, идущих вокруг неё."

show shizu basic_normal_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "Как бы то ни было, пора решать задачи, %(name_hicchan)s."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 1.0

"Мы заканчиваем раньше времени, и я решаю спросить, есть ли поблизости местечко с меню поаппетитнее, чем в нашей столовой."

"На что %(name_shizune)s и Миша принимаются спорить о том, какой из местных ресторанов лучше. Все они находятся в городе, и мы вряд ли успеем сходить туда до начала следующего урока. И потом там наверняка дорого."

"Или они спорят ради удовольствия?"

"Они настолько увлечены, что не замечают начала большой перемены."

"Я смотрю в конец класса через плечо."

show hanako emb_downtimid at tworight 
with charaenter

"…Похоже, она пересматривает свои конспекты с прошлого урока."

"Странное зрелище, на фоне того, как остальные заняты перерывом на ланч."

"Болтают, сплетничают, сдвигают парты. Те, у кого еда была с собой, общаются с остальными, иногда прерываясь, чтобы отправить в рот очередную порцию."

"По мере наблюдения за Ханако начинает казаться, что я единственный, кто её замечает. Как будто она невидима для остальных; будто прячется у всех на виду."

"Над ней издеваются? Или она отгородилась ото всех по собственному желанию?"

show hanako emb_timid
with charachange

show hanako emb_downtimid
with charachange

"Я замечаю, как она смотрит через плечо на заднюю дверь класса."

"И она не перелистывает страницу с тех пор, как я начал за ней наблюдать."

"Думаю, она ждёт кого-то."


label ru_choiceA10a:
menu:
    with menueffect
    "Что же делать?"
    "Почитать свою книгу.":


        return m1
    "Попробовать заговорить с Ханако.":

        return m2
    "Подождать, пока %(name_shizune)s и Миша примут решение.":

        return m3


label ru_choiceA10b:
menu:
    with menueffect
    "Что же делать?"
    "Подождать, пока %(name_shizune)s и Миша примут решение.":


        return m1
    "Почитать свою книгу.":

        return m2

label ru_choiceA10c:
menu:
    with menueffect
    "Что же делать?"
    "Почитать свою книгу.":


        return m1       
    "Попробовать заговорить с Ханако.":

        return m2

label ru_A10a:

stop music fadeout 6.0

"Когда я не знаю, что делать, я стараюсь занять себя чем-нибудь привычным."

"Как и сейчас."

"Я уже начал читать одну из библиотечных книг и принёс её с собой в школу, чтобы скоротать время между уроками."

hide hanako
with charaexit

"Я нахожу страницу со сложенным уголком-закладкой и начинаю оттуда."

"Миша и %(name_shizune)s всё ещё возбуждённо спорят, может быть до сих пор о ресторанах."

"Если я сейчас попытаюсь заговорить с ними, они просто втянут меня в свой спор или, того хуже, опять попытаются затащить в Школьный совет."

"Поскольку поблизости нет никого, кто мог бы присоединиться к их беседе, Миша перестаёт озвучивать дискуссию."

"Интересно, почему её тянет переводить на язык жестов даже то, что %(name_shizune)s знать необязательно, или, что ещё удивительнее, когда её даже нет рядом? Любопытная привычка."

"Мне становится сложно сосредотачиваться на книге, перерыв манит меня прочь из скучного класса. Я повинуюсь его зову и отправляюсь в столовую."

"Миша и %(name_shizune)s, кажется найдя компромисс, следуют за мной, продолжая энергично разговаривать."

stop music fadeout 2.0

label ru_A10b:

"Я всё ещё чувствую себя виноватым за то, что спугнул её вчера, так что, думаю, будет лучше сказать ей что-нибудь."

show hanako emb_downtimid at center 
show bg school_scienceroom at bgleft 
with charamove

hi "Эм, привет, Ханако."

show hanako def_shock
with vpunch

ha "Хи… Хисао?"

"Что ж, по крайней мере, она помнит моё имя."

hi "Это… Я просто хотел извиниться за вчерашнее."

hi "Я не хотел тебя напугать, ничего такого."

hi "Просто я здесь новенький и думал, что надо бы познакомиться с одноклассниками."

show hanako basic_bashful
with charachange

"Ханако поднимает на меня взгляд, и я ещё раз замечаю её шрамы."

"Немного сбивает с толку то, что издалека они почти не заметны, а вблизи прямо-таки бросаются в глаза."

show hanako cover_bashful
with charachange

ha "В… Всё в порядке."

ha "Это… Это я виновата."

hi "Да нет, никто не виноват, просто так уж вышло."

hi "Ты кого-то ждёшь? Я заметил, как ты смотрела на дверь…"

show hanako basic_normal
with charachange

ha "Д-да… Лилли."

hi "А, ты имеешь в виду Лилли, слепую девушку?"

"Ханако слегка кивает в ответ, а я задаюсь вопросом, не является ли грубостью различать людей по типу их инвалидности или же здесь это считается нормальным?"

"Теперь понятно, почему Лилли вчера отправилась за ней."

hi "Мне она показалась приятной девушкой. Вы с ней подруги?"

show hanako basic_bashful
with charachange

ha "Д-да."

show hanako basic_distant
with charachange

"Она вновь глядит через плечо, будто в надежде увидеть Лилли."

stop music fadeout 6.0

"Кажется, она опять начинает из-за меня нервничать."

hi "Прости, если я снова тебя побеспокоил…"

show hanako basic_bashful
with charachange

ha "Н-не в этом дело."

ha "Просто лучше бы Лилли сюда не приходить…"

hi "А, потому что ей трудно найти класс?"

show hanako basic_distant
with charachange

ha "Нет… не совсем."

"Ханако переводит взгляд в сторону %(name_shizune)s."

hi "%(name_shizune)s?"

"Она молча кивает."

hi "При чём тут она? Они с Лилли не ладят?"

"Ханако качает головой. Очевидно, она не очень хочет рассказывать об этом."

"То, что Лилли не ладит с %(name_shizune)s, кажется в некотором роде естественным."

"Общение между ними не представляется возможным. С %(name_shizune)s и так трудно разговаривать через Мишу, даже если видишь, кто из них жестикулирует."

"Ханако так сосредоточена на %(name_shizune)s, что я первым замечаю Лилли в дверях."

hi "О, она тут."

show hanako defarms_shock
with charachange

"Ханако разворачивается и, увидев Лилли, бежит к двери."

show hanako defarms_shock at tworight 
show bg school_scienceroom at center 
with charamove

show lilly cane_weaksmile at twoleft 
with charaenter

play music music_lilly fadein 3.0

show hanako emb_smile
with charachange

ha "Лилли…"

show lilly cane_smile
with charachange

li "О, Ханако. Доброе утро. Президент здесь?"

show hanako emb_downtimid
with charachange

ha "Д-да."

show hanako basic_distant
with charachange

"Ханако опять бросает через плечо взгляд на %(name_shizune)s, словно пытаясь удостовериться, что та их не слышит, хотя это невозможно в принципе."

show lilly cane_sad
with charachange

li "Тогда, пожалуй, нам лучше уйти."

"Лилли вздыхает, и в её тяжёлом вздохе слышатся нотки отчаяния. Похоже, между ними действительно есть острая неприязнь."
























"Мне любопытно, но я не решаюсь спросить об этом. Они сами рассказали бы, если б захотели."

"Я здесь всего третий день; мне следует заводить друзей, а не пытаться выяснять причины чьей-либо вражды."

"В любом случае забавно узнать, что даже тут случаются распри, как и в моей прежней школе."

"Хоть люди здесь терпимее к другим, они всё равно умудряются досаждать друг другу."

hi "Привет, Лилли. Как ты? Извини, что вчера тебе пришлось так спешно из-за меня уйти…"

show lilly cane_surprised
with charachange

li "Боже мой, это Хисао? Я не знала, что ты здесь…"

"Лилли, кажется, немного смущена, что так разоткровенничалась в моём присутствии."

show hanako emb_sad
with charachange

ha "И-извини, Лилли. Я думала, ты поняла…"

show lilly cane_weaksmile
with charachange

li "Нет-нет, всё в порядке, Ханако."

li "Хисао, пожалуйста, не беспокойся о вчерашнем. Это было простое недоразумение."

hi "Ну… как скажешь. Я всё ещё не до конца освоился здесь."

show lilly cane_smile
with charachange

li "Думаю, скоро ты поймёшь, что люди в этой школе снисходительнее, чем где-либо ещё."

li "Если ты озадачен чем-то, то, пожалуйста, не стесняйся спрашивать."

hi "Хорошо, буду знать."

show hanako emb_timid
with charachange

ha "Эм… Лилли…"

show lilly cane_weaksmile
with charachange

"Лилли понимающе кивает."

li "Извини, Хисао, но нам пора."

"Видно, что Ханако чувствует себя напряжённо, да и Лилли всё ещё немного смущена."

"Интересно, помогли ли хоть немного мои извинения?"

hi "Вы не против, если я присоединюсь к вам?"

show lilly cane_smile
with charachange

"Я, конечно, навязываюсь, но… Лилли, по-прежнему улыбаясь, тихонько хмыкает."

show lilly cane_weaksmile
with charachange

li "У нас наверняка найдётся для тебя местечко, правда, Ханако?"

show hanako emb_downsad
with charachange

show hanako basic_worry
with charachange

"Ханако переводит взгляд на Лилли, на меня, а затем замирает, широко раскрыв глаза."

ha "К… конечно."

show lilly cane_cheerful
with charachange

li "Что ж, тогда пойдёмте?"

"Уверен, что Лилли не согласилась бы с такой лёгкостью, если бы могла увидеть, насколько испугана её подруга."

"Впрочем, всё уже решено."

stop music fadeout 1.0




label ru_A10c:

hide hanako
with charaexit

show misha sign_smile at twoleft 
show shizu adjust_happy at tworight 
with charaenter

"Миша и %(name_shizune)s всё ещё спорят о местах, где можно перекусить, недостижимых для обычных школьников, которым пришлось бы добираться до города и обратно на такси."

hi "Вы что, ещё не закончили?"

show misha hips_grin
with charachange

mi "А, прости, %(name_hicchan)s! Ты нас ждал?"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

mi "У тебя нет никаких планов?"

hi "Планов?"

mi "На большую перемену."

hi "Ну… нет, я думал провести время с вами."

show misha sign_smile
with charachange

show misha perky_smile
with charachange

"Миша отмечает отсутствие у меня планов победоносной улыбкой, взволнованно передав мои слова %(name_shizune)s."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

stop music fadeout 5.0

mi "Раз ты свободен, не хочешь перекусить с нами? Правда, мы собираемся в город… Не волнуйся, %(name_hicchan)s, это совсем рядом!"

hi "Конечно, я не против."

"На этом мы и покидаем класс."





label ru_A11:

scene bg school_hallway3
with locationchange

play ambient sfx_emisprinting fadein 3.0

"Сразу за углом коридора удар в грудь с силой несущегося на полной скорости поезда чуть не сбивает меня с ног."

label ru_A11a:

stop ambient
play sound sfx_impact
with vpunch

scene black
with Dissolve(0.2)

hi "Ай!"

play music music_emi fadein 2.0

show ev emi_knockeddown_facepullout
with openeye

"Придя в себя, я встречаю взгляд двух зелёных глаз размером с блюдца, удивлённо уставившихся на меня снизу."

show ev emi_knockeddown_largepullout
with flash

"Они принадлежат виновнице столкновения – низенькой девочке, распластавшейся передо мной на полу."

"Она озабоченно хмурит брови. Она одета в физкультурную форму, что довольно странно для большой перемены."

"…Однако больше всего в её внешности меня поражает то, что у неё нет ног."

show ev emi_knockeddown_legs
with flash

"Точнее, есть, но ненастоящие. Её бледные ножки заканчиваются бёдрами, а голени и ступни заменяет устройство то ли из металла, то ли из пластика чёрного цвета."

"Это смотрится чрезвычайно неестественно. На мгновение я даже забываю о боли в груди."

show ev emi_knockeddown at center 
with flash

"Девочка морщится, трёт нос и вскакивает."

scene bg school_hallway3 at bgleft 
with locationchange

show emi sad_depressed_gym at center 
with easeinbottom

emi_ "Вот чёрт… Эй, ты в порядке? Прости, пожалуйста!"

emi_ "Я бежала, а ты вдруг появился из ниоткуда… Прости, я нечаянно!"

"Она смотрит на меня виноватыми глазами, будто наказанный щенок."

"Я тут же забываю о всяком негодовании, ведь щеночки с таким вот взглядом – моя слабость."

stop music fadeout 2.0

hi "Всё в порядке. Не волнуйся об этом… ай…"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"Хоть я и сказал, что всё в порядке, но понимаю, что подобный удар – одна из сильнейших опасностей; в моей груди растёт острая боль."

"Не перегружать себя, не забывать про лекарства и, самое главное, остерегаться ударов в грудь."

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"Я пытаюсь помассировать солнечное сплетение, чтобы ослабить боль, задерживаю дыхание, чтобы услышать сердцебиение."

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)
with Pause (1.0)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)
with Pause(1.0)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)
with Pause (1.0)

"Кажется, всё уже в порядке…"

show emi basic_shock_gym
with charachange

emi_ "Эй, позвать врача?"

play music music_emi fadein 0.2

"Взволнованный, пронзительный голосок девочки приводит меня в чувство."

"Простояв в оцепенении несколько секунд, я внезапно осознаю, что сложившийся пополам и с болезненной гримасой на лице я выгляжу куда хуже, чем чувствую себя на самом деле."

"Чёрт, я слишком беспокоюсь о своём сердце."

hi "Эм… не стоит, я уже в порядке."

"Я нахожу в себе силы выпрямиться, потирая напоследок рёбра, и делаю глубокий вдох."

"Она только что чуть не вышибла из меня дух. Но, похоже, обошлось."

show emi basic_hes_gym
with charachange

emi_ "Точно в порядке? Я тебя крепко стукнула."

hi "Всё нормально, я же сказал. Ничего не сломано. Жить буду."

show emi basic_happy_gym
with charachange

emi_ "Это хорошо! Я—"



label ru_A11b:

"Чья-то рука ложится мне на плечо; в тот же момент глаза девочки округляются от ужаса, а её реплика прерывается испуганным—{w=.9}{nw}"

show emi basic_hes_gym
with charachange

emi_ "И-и!"

show misha hips_frown at offscreenleft  behind emi
show shizu cross_rage at offscreenleft  behind emi
with None

show bg school_hallway3 at center 
show emi basic_hes_gym at right 
show shizu cross_rage at Position(xalign=0.4) 
show misha hips_smile at left 
with charamove

"Не успеваю я обернуться, как %(name_shizune)s отталкивает меня в сторону и нависает над девочкой, яростно жестикулируя."

show misha hips_grin
with charachange

mi "Мисс %(name_ibarazaki)s, я всё видела. Бегать по коридорам строго запрещено."

"Миша переводит стоя позади %(name_shizune)s, но её голос по-девчачьи игрив и совсем не выражает священного гнева, читающегося в жестах %(name_shizune)s."

show emi basic_closedsweat_gym
with charachange

emi_ "Э… извините, мне просто надо было забрать кое-что и я немного торопилась…"

show shizu adjust_angry
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Вам уже говорили об этом тысячу раз. Ваше неосмотрительное поведение подвергает опасности других учеников и, что ещё хуже, прямо противоречит школьным правилам."

show emi sad_depressed_gym
with charachange

"Девочка краснеет от стыда и начинает мяться на месте, как ребёнок, которого отчитывают за плохое поведение."

"Это выглядит так мило, что я не могу сдержать улыбку."

emi_ "Я знаю! Я-я… эм… я просто…"

show shizu cross_angry
with charachange

shi "…"

show misha cross_smile
with charachange

mi "Вы уж постарайтесь, чтобы подобное не повторилось… Хотя я уверена, что вы презираете правила и делать вам замечания – совершенно бессмысленная трата моих нервов."

show misha cross_grin
with charachange

mi "Поняла, Эми?"

show emi sad_annoyed_gym
with charachange

"В ответ маленькая девочка показывает язык."

show emi basic_hes_gym
with charachange

emi "А-а-а!"

emi "Мне надо спешить!"

emi "Учитель мне голову оторвёт! Я обещала помочь с распечатками, а вместо этого пошла бегать! Извините, но мне надо переодеться и всё такое!"

play sound sfx_emisprinting
stop music fadeout 1.0

hide emi
with easeoutleft

stop sound fadeout 1.5

"Прежде чем Миша, %(name_shizune)s или я успеваем что-либо сказать, она срывается с места и в одно мгновение оказывается на полпути к лестнице."

show shizu cross_angry at tworight 
show misha cross_grin at twoleft 
show bg school_hallway3 at bgright 
with charamove

play music music_normal fadein 3.0

"%(name_shizune)s выглядит так, будто готова взорваться от злости; я улыбаюсь в тщетной попытке успокоить её."

show shizu basic_frown
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Ты в порядке, %(name_hicchan)s? От этой %(name_ibarazaki)s вечно одни неприятности."

hi "Знаешь, я твёрдо уверен, что %(name_shizune)s не назвала бы меня «%(name_hicchan)s»."

show misha hips_grin
with charachange

mi "Да ладно тебе!"

"…"

hi "Ну, в общем, я в порядке. Меня просто слегка ушибли."

show shizu basic_normal
with charachange

shi "…"

show misha cross_grin
with charachange

mi "Это здорово, %(name_hicchan)s!"

"Я бы не сказал, что это «здорово», но на этот раз воздерживаюсь от комментариев."



label ru_A11x:



$ renpy.music.play(music_normal, fadein=3.0, if_changed=True)

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Ну что, давай скорей, %(name_hicchan)s~! На ланч!"

show misha hips_grin
with charachange

mi "Обещаем, будет здорово!"

hi "Ловлю тебя на слове. Что это за место?"

hi "Что-то вроде ресторана?"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Это чайный дом, %(name_hicchan)s~!"

"Чайный дом… может оказаться дороговато."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Почему ты смотришь в свой бумажник, %(name_hicchan)s? Ничего страшного, если у тебя нет денег, мы за тебя заплатим~!"

hi "Очень мило с вашей стороны. Спасибо."

show misha hips_smile
with charachange

mi "Всё в порядке, %(name_hicchan)s! Мы же всё-таки друзья, да, %(name_hicchan)s?"

"Мы знакомы всего три дня. Неужели мы так быстро сумели сдружиться?"

"Хе-хе. Но мне приятно это слышать."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "А, но это только на сегодня и только если ты согласишься прямо сейчас! Ты точно хочешь пойти, %(name_hicchan)s?"

"Я начинаю задумываться, не ловушка ли это. Этот поход предложила мне Миша или %(name_shizune)s? Это важно. Меня несколько тревожат возможные мотивы девочки, чья любимая забава – игра в мировое господство."

"…Нет, наверное я просто поддался паранойе. В конце концов, я не имею ничего против их компании. Иногда необходимо выбираться в город, так почему бы и не вместе с ними?"

"Я никогда раньше не был в чайном доме, только видел их по телевизору в исторических фильмах. Возможно, сейчас это всего лишь обычные кафе, в которых от тех «чайных домов» осталось одно название."

"Моё любопытство – лишь ещё одна причина, по которой я хочу пойти с ними."

hi "Конечно."

show misha hips_grin
show shizu behind_smile
with charachange

mi "Это здорово, %(name_hicchan)s~! Здорово, здорово! Ура~!"

"Миша несколько раз радостно подпрыгивает на месте, в очередной раз привлекая своим поведением посторонние взгляды. %(name_shizune)s лаконично, едва слышно аплодирует, прежде чем выражение её лица снова становится невозмутимым."

show shizu behind_blank
with charachange

hi "Тебе не помешало бы быть немного радостней, %(name_shizune)s."

show shizu basic_normal2
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "О-о! А я не знала, что %(name_hicchan)s у нас король. Ха-ха-ха-ха~!"

show shizu adjust_smug
with charachange

"%(name_shizune)s поправляет очки, пока Миша переводит её слова, причём без единой нотки сарказма. Полагаю, если бы она смогла передать интонацию %(name_shizune)s, эта насмешка могла бы меня задеть. В такие моменты я рад, что между нами существует подобный барьер."

hi "Я и не прошу тебя прыгать от радости из-за того, что решил к вам присоединиться. Я не столь высокомерен."

show shizu adjust_happy
show misha cross_grin
with charachange

stop music fadeout 2.0

"Думаю, %(name_shizune)s и так это понимает. Под её предводительством мы втроём направляемся в город."



label ru_A11y:



show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile
with charachange

mi "А теперь нам пора бежать: в Школьном совете важное собрание по поводу фестиваля. И мы наконец решили, где будем есть~!"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Жаль, но тебе нельзя с нами: это бизнес-ланч только для членов Совета."

show misha hips_grin
with charachange

mi "Мы обязательно позовём тебя в другой раз! О, но это было бы слишком похоже на свидание, не правда ли?"

show misha hips_laugh
with charachange

mi "Ва-ха-ха!~"

hide misha
hide shizu
with dissolve

stop music fadeout 4.0

"Девочки спускаются вниз по лестнице."

"Не успеваю я сделать и пары шагов по коридору, как меня буквально захлёстывает волна шума и суеты перемены. Мне тоже пора идти."

scene bg school_scienceroom
with shorttimeskip

"Больше за весь учебный день не происходит ничего интересного."

"Я успеваю прочесть большую часть книги, начатой вчера, и перекусить в столовой, с трудом что-то выбрав из совершенно непривлекательного меню."

"Уроки ужасно скучны."





label ru_A11c:

scene bg school_hallway3
with locationchange

"Мы втроём покидаем класс."

show hanako emb_downtimid at center 
show lilly cane_smile at twoleft 
with charaenter

"Лилли идёт вдоль стены, легонько постукивая по ней тростью, Ханако держится рядом, буквально обнимая её."

"Похоже, что Лилли намного труднее перемещаться подобным образом, но, несмотря на это, она вовсе не возражает."

show hanako defarms_shock
with charachange

"Как только мы сворачиваем за угол, удар в грудь с силой несущегося на полной скорости поезда едва не сбивает меня с ног. Ханако сдавленно вскрикивает от неожиданности. У меня в глазах начинает темнеть."

label ru_A11d:

show lilly cane_listen at offscreenleft  behind emi
show hanako defarms_worry at offscreenright  behind em
with None

show lilly cane_listen at left 
show hanako defarms_worry at right 
with charamove

li "Хисао, что случилось?"

"Конечно, Лилли не в курсе происходящего, но её голос звучит крайне взволнованно. Хотя в этой ситуации такое волнение излишне."

hi "Кое-кто в меня врезался, но вроде ничего серьёзного. Всего лишь небольшой ушиб."

show emi excited_sad_gym
with charachange

emi_ "Э… извини, я нечаянно. Мне просто надо было срочно забрать кое-что, и я очень торопилась."

show lilly cane_weaksmile
show hanako def_worry
with charachange

li "Этот «кое-кто» – Эми, не так ли?"

show emi basic_hes_gym
with charachange

"Маленькая девочка смущённо кашляет и шаркает «ногами», сделанными из какого-то металла или пластика, опуская на них взгляд, прежде чем что-либо ответить."

show emi basic_closedgrin_gym
with charachange

emi "…Привет, Лилли. Привет, Ханако."

"Похоже, они знакомы."

show lilly cane_sad
show hanako def_worry
with charachange

li "Пожалуйста, будь осторожнее. Ты достаточно крепкая, чтобы спокойно перенести такого рода происшествия, но в школе есть ученики, которые от подобного могут пострадать."

show emi sad_depressed_gym
with charachange

"Девочка краснеет со стыда и начинает мяться на месте, как ребёнок, которого отчитывают за плохое поведение."

"Это выглядит так мило, что я не могу сдержать улыбку."

emi "Я знаю! Я-я… эм… я просто…"

show emi basic_hes_gym
show lilly cane_surprised
show hanako defarms_shock
with charachange

emi "А-а-а! Мне надо спешить!"

emi "Учитель мне голову оторвёт! Я обещала помочь с распечатками, а вместо этого пошла бегать! Извините, но мне надо переодеться и всё такое!"

play sound sfx_emisprinting
stop music fadeout 1.0

hide emi
with easeoutleft

stop sound fadeout 1.5

"Не успеваем мы и слова произнести, как Эми срывается с места и бежит дальше по коридору, который без неё становится гораздо тише."

hi "И часто здесь такое случается?"

show lilly cane_concerned
show hanako def_worry
with charachange

show lilly cane_concerned at twoleft 
show hanako def_worry at tworight 
show bg school_hallway3 at center 
with charamove

li "Насчёт бега по коридорам в «Ямаку» особенно строгие правила."

show lilly cane_listen
with charachange

li "…но, похоже, это редко останавливает Эми."

show lilly cane_weaksmile
with charachange

"Она качает головой и сдержанно улыбается."

li "Боюсь, не в наших силах как-то повлиять на неё. Что ж, пойдёмте."

hide lilly
with charaexit

hide hanako
with charaexit

"Лилли отправляется дальше по коридору, и Ханако, спохватившись, следует за ней."

"Я легко восстанавливаю в памяти дорогу в комнату, которую эти двое используют для чаепитий, поскольку был там только вчера."




label ru_A12:

scene bg suburb_roadcenter
with locationskip

play music music_tranquil fadein 3.0

"Наблюдая за её походкой, я отмечаю, что она делает очень быстрые, тяжёлые и уверенные шаги."

"Возможно, такая походка была бы уместна, если бы мы пробирались сквозь снежную бурю, но на улице стоит ясный безветренный день. В любом случае я чувствую себя абсолютно выдохшимся лишь глядя на неё."

scene bg suburb_shanghaiext
with locationchange

"Вероятно, именно благодаря такому безумному темпу мы добираемся до чайного дома за время, которое Миша называет «рекордным». Мне слегка досадно оттого, что перед моим взглядом не предстаёт здание феодальной эпохи с татами на полу и женщинами в кимоно, разливающими чай."

"Чайный дом оказывается самым обычным кафе. Впрочем, это не так уж и плохо – выглядит довольно уютно."

play sound sfx_storebell

scene bg suburb_shanghaiint
with locationchange

"Как только мы оказываемся внутри, к нам немедленно подбегает девушка, будто поджидавшая нас всё это время."

show yuukoshang closedhappy_down at center 
with charaenter

yu "Добро пожаловать! Спасибо, что выбрали наше заведение!"

"Она кланяется резким движением, будто рубит топором дрова."

"Я с удивлением узнаю в ней Юко, нашего библиотекаря."

hi "Привет. Я не знал, что ты работаешь и здесь."

show yuukoshang smile_down
with charachange

yu "А… Да, работаю. Официанткой… Уже год, шесть месяцев и две недели… Спасибо, что выбрали именно наше заведение. Я могу вам чем-нибудь помочь?"

show yuukoshang smile_down at twoleft 
show bg suburb_shanghaiint at bgleft 
with charamove

show shizu behind_smile at Position(xalign=1.2) 
show misha hips_grin at tworight 
with charaenter

mi "Привет, %(name_uchan)s~!"

show yuukoshang neutral_down
with charachange

yu "Приветствую."

hi "Миша, вы обе тоже с ней знакомы?"

show misha perky_smile
with charachange

mi "Конечно, %(name_hicchan)s~! %(name_uchan)s у нас в библиотеке работает, в конце концов~! Я редко хожу туда, но %(name_sicchan)s её знает! И~! Мы часто приходим сюда, поэтому получается, что постоянно с ней видимся!"

show yuukoshang neurotic_up
with charachange

yu "Эм… Да… Я принесу вам всё, что вы обычно заказываете. И… если ещё что-нибудь понадобится, пожалуйста, просто позовите меня."

hi "Тебе не обязательно говорить с нами в таком формальном тоне. Мы ведь все знакомы."

"К тому же народу в кафе совсем мало, она могла бы чувствовать себя и посвободнее."

"Я надеялся, что мои слова помогут ей расслабиться, но они оказывают обратный эффект."

show yuukoshang panic_up
with charachange

yu "Нет… Я же официантка, это моя работа, поэтому я должна… выполнять её как подобает."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Ладно, ладно~! %(name_sicchan)s не возражает! %(name_uchan)s, принеси, пожалуйста, %(name_sicchan)s то же, что и всегда, а мне – зелёный чай с молоком и мёдом."

hi "Не переживай так."

show yuukoshang neurotic_up
with charachange

yu "Эм, да… но… это же моя работа, и… всегда есть из-за чего переживать. Извините, я не должна спорить с клиентом… Извините! Извините!"

"Юко снова начинает стремительно кланяться. Я сдаюсь и присоединяюсь к %(name_shizune)s и Мише за их столиком."

scene bg suburb_shanghaiint at bgleft 
with shorttimeskip

"Когда я располагаюсь в кресле, ко мне подходит Юко, выглядящая ещё более расстроенной, чем во время предыдущего разговора."

show yuukoshang panic_up
with charachange

yu "Извините! Мне правда очень, очень жаль! Я забыла принять ваш заказ… Я… невнимательна к посетителям, так нельзя… Простите меня… Если я могу как-то загладить свою вину, пожалуйста, только скажите…"

scene ev shizu_shanghai
with dissolve

shi "…"

mi "Всё в порядке, %(name_uchan)s, просто %(name_hicchan)s ещё ничего не заказал. Ты ни в чём не провинилась, незачем так расстраиваться."

"Действительно, пора бы и мне сделать заказ. Но я не знаю, что здесь подают, и меню нигде не видно."

hi "Миша права. Мне, пожалуйста, кофе и… сэндвич, если у вас есть. Самый вкусный, на твой выбор, раз уж %(name_shizune)s за меня платит."

scene ev shizu_shanghai_borednormal
with dissolve

"%(name_shizune)s одаряет меня взглядом, в котором смешиваются удивление, негодование и шок. Она явно не может решить, на чём ей остановиться."

shi "…"

scene ev shizu_shanghai_boredlaugh
with dissolve

mi "%(name_hicchan)s, вот у тебя в бумажнике сколько денег? Ведь что-то точно есть, да? Нам надо разделить сумму заказа на троих, чтобы было честно~! Да, и на другое я не согласна~!"

"Миша поворачивается к Юко."

show ev shizu_shanghai_borednormal
with dissolve

mi "%(name_uchan)s, %(name_sicchan)s говорит, что хочет три порции самого дорогого блюда из меню~"

hi "Нет!"

show ev shizu_shanghai_boredlaugh
with dissolve

mi "Ха-ха-ха~! Мы шутим, %(name_hicchan)s…"

scene bg suburb_shanghaiint
show yuukoshang neurotic_up at center 
with dissolve

yu "Эм… хорошо… Думаю, сэндвич с индейкой здесь самый вкусный… К тому же к нему подаётся бесплатный суп… Хотя хороший работник должен был бы порекомендовать блюдо, которого у нас в избытке, ну… или самое дорогое блюдо…"

show yuukoshang worried_up
with dissolve

yu "У меня плохо получается?"

hi "Вовсе нет! Звучит отлично, я беру. И кофе, пожалуйста."

show yuukoshang smile_down
with dissolve

yu "Хорошо."

hide yuukoshang
with charaexit

scene bg suburb_shanghaiint
show yuukoshang neutral_down at center 
with shorttimeskip

"Через несколько минут она приносит напитки и сэндвич. %(name_shizune)s обходится одним только чаем, а Миша заказала ещё и парфе. Не представляю, почему именно его: сложно придумать более неподходящий десерт к чаю."

"Ну да ладно. Я кусаю сэндвич. Он на удивление сочный и вкусный."

scene ev shizu_shanghai
with locationchange

shi "…"

mi "%(name_hicchan)s, ты уже подумал о вступлении в Школьный совет?"

stop music fadeout 3.0

hi "Хм?"

show ev shizu_shanghai_borednormal
with dissolve

shi "…"

mi "%(name_hicchan)s, не говори с набитым ртом…"

scene bg suburb_shanghaiint at bgleft 
with dissolve

"Я запиваю еду глотком кофе, который тоже весьма неплох. Но сейчас не время хвалить это заведение."

hi "Вы же сами признали, что мне ещё рано принимать такое серьёзное решение! И было это всего три часа назад!"

play music music_comedy fadein 0.5

show shizu adjust_smug_close at offscreenleft 
show misha hips_grin_close at offscreenright 
with None

show shizu adjust_smug_close at center 
show bg suburb_shanghaiint at bgright 
with charamove

shi "…"

show bg suburb_shanghaiint at center 
show shizu adjust_smug_close at twoleft 
show misha hips_grin_close at tworight 
with charamove

mi "Мужчина должен быть решительным, %(name_hicchan)s!"

show shizu behind_blank_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "Тебе правда стоит вступить, %(name_hicchan)s. Давай же, будет весело!"

hi "«Будет весело», как правило, говорят о том, что на самом деле ни капли не весело."

show shizu behind_frown_close
with charachange

shi "…"

show misha cross_grin_close
with charachange

mi "Ты что, мне не веришь, %(name_hicchan)s?"

"Кто из них это сказал? Такое серьёзное давление в словах Миши – и такая невинная улыбка на лице. Похоже на раздвоение личности."

hi "Эм-м…"

show shizu basic_normal_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "Это обидно, %(name_hicchan)s. Мы ведь просто хотим проводить с тобой время…"

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Вот именно, %(name_sicchan)s! И это тоже!"

show shizu adjust_smug_close
with charachange

shi "…"

mi "Все оказываются в плюсе, решаются все наши проблемы~"

show shizu behind_frown_close
with charachange

shi "…"

show misha perky_sad_close
with charachange

mi "Я тоже думала, что %(name_hicchan)s это хоть немножко оценит… Обидно!"

"Моего мнения опять никто не спрашивает."

hi "Эй, прекратите разговаривать так, будто меня тут нет."

show shizu adjust_happy_close
with charachange

"%(name_shizune)s поправляет очки и смеётся про себя."

shi "…"

mi "У-у, но ведь правда же, %(name_hicchan)s~! Ты бы нас очень выручил, в этом году у нас совсем мало людей."

hi "Насколько мало?"

show misha sign_confused_close
with charachange

mi "О, а это секрет, %(name_hicchan)s."

hi "Нет, я хочу знать. Насколько мало ваше «мало»?"

mi "А-ха-ха…"

hi "Пятеро?"

show shizu behind_blank_close
with charachange

shi "…"

hi "Меньше?"

show misha perky_sad_close
with charachange

mi "Ну-у…"

hi "Ноль?"

show shizu basic_normal_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Ва-ха-ха~! %(name_hicchan)s, неважно сколько. Важно, что мало, и поэтому мы были бы рады твоей помощи. Особенно когда фестиваль на носу, да и вообще год нас ждёт очень занятой."

hi "То есть ты не хочешь отвечать?"

show shizu adjust_smug_close
with charachange

shi "…"

mi "Нет~"

"Я вздыхаю и выпрямляю спину, пытаясь придать себе деловой вид. Это кажется серьёзным решением, и мне не хочется вот так запросто сдаваться. Хотя чувствую я себя глупо, словно надутая рыба-ёж."

hi "Ладно, тогда скажите хотя бы, сколько человек в Школьном совете? Всего?"

show shizu behind_blank_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "Эм, ну, %(name_hicchan)s, нас достаточно, чтобы выполнять необходимую работу, но явно меньше, чем хотелось бы. Да-да-да~!"

hi "Только не говори мне, что вас там всего двое."

show misha cross_laugh_close
with charachange

mi "Ха-ха-ха~! Забавно, %(name_hicchan)s~!"

show shizu basic_normal2_close
with charachange

shi "…"

show misha cross_smile_close
with charachange

mi "Но~! В нём точно не только мы одни."

hi "Вы уверены? Абсолютно уверены?"

show misha cross_grin_close
with charachange

mi "Угу~!"

"Я всматриваюсь в их лица, рассчитывая на то, что они чем-нибудь выдадут себя, подтверждая мои худшие опасения."

show misha perky_sad_close
with charachange

"Миша хмурится. Ей явно не по себе, но это, скорее всего, связано с тем, что я столь пристально на неё уставился."

show shizu basic_happy_close
with charachange

"%(name_shizune)s, напротив, отвечает мне одним из своих фирменных взглядов. Может быть, она бросает мне вызов, вот так уставившись на меня поверх очков. Её взгляд так и дразнит меня; он на удивление детский, словно она маленькая девочка, которая пытается втянуть кого-то в свою игру."

show shizu basic_normal_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "%(name_hicchan)s, две прелестные представительницы Школьного совета оказывают тебе радушный приём и даже угощают ланчем. Тебе следовало бы выразить свою признательность, вступив в Совет, чтобы помочь им."

mi "Да, было бы здорово, если бы ты помог нам заполнить кое-какие бумаги, и… скоро фестиваль, так что надо построить несколько киосков для аттракционов и продажи еды, так что, если бы ты вступил, нам было бы куда проще…"

show misha perky_sad_close
with charachange

mi "Ну, пожалуйста, %(name_hicchan)s?"

"Забавно, как хорошо у них получается разыгрывать роли плохого и хорошего полицейского."

"В принципе, я могу попробовать."

"Почему бы и нет? Просто чтобы присмотреться."

hi "Ладно, я согласен попробовать. Но это не значит, что я уже определился со вступлением. Я помогу немного, а потом посмотрим. И таким образом, кстати, я расквитаюсь за этот обед. Я соглашаюсь не потому, что хочу."

show misha perky_smile_close
show shizu basic_frown_close
with charachange

"Я доедаю сэндвич, и это заставляет Мишу вспомнить, что перед ней стоит парфе. Она берётся за него, чем сильно огорчает %(name_shizune)s: ей явно ещё многое хочется высказать."

stop music fadeout 12.0

show shizu behind_blank_close
with charachange

"Всякий раз, как я гляжу на %(name_shizune)s, она отвечает мне весьма сосредоточенным горящим взором. И сейчас тоже. Несколько секунд выражение лица %(name_shizune)s остаётся непроницаемым: наверное, она о чём-то размышляет. Через некоторое время на её губах появляется улыбка."

show shizu adjust_happy_close
with charachange

shi "…"

"Она что-то жестикулирует мне, и я, само собой, не понимаю, что она хочет сказать. Причём она это знает. Она повторяет ещё раз, энергично и по-детски игриво."

show shizu adjust_smug_close
with charachange

shi "…"

show shizu adjust_happy_close
with charachange

hi "Миша, что она сказала?"

show misha perky_confused_close
with charachange

mi "…?"

"Миша отвлекается от парфе явственно разрываясь между желанием помочь и желанием вернуться к сладкому."

hi "Что это значит?"

"Я изо всех сил пытаюсь повторить жесты %(name_shizune)s – это оказывается очень нелегко. Страшно подумать, каково было бы использовать их постоянно, изо дня в день за неимением других средств общения."

show misha perky_smile_close
with charachange

mi "Хм~… Прости, %(name_hicchan)s, не скажу."

hi "Почему? Это что-то обидное?"

show misha hips_grin_close
with charachange

mi "Нет, %(name_hicchan)s, потому что~! Это что-то хорошее."

"Что-то хорошее, значит? Они возвращаются к своим напиткам и еде, так что, я полагаю, разговор пока окончен."

hide misha
hide shizu
with charaexit

"Я не совсем понимаю. Но от этого во мне разгорается желание понимать. Может, попытаться выучить язык жестов? В этой школе должны быть курсы."

"Пойду ли я на такой шаг? Я допиваю кофе, размышляя об этом. Не знаю, с чего я вдруг вообще задумался о подобном."

"Я так хорошо провожу здесь время, что упускаю из виду одну важную деталь: десять минут назад наша прогулка превратилась в прогул."

"Если мы выйдем прямо сейчас, то будем в школе… минут через тридцать? Наверное. В моём состоянии не стоит бегать, поэтому вряд ли сможем добраться быстрее."

"Хотя мы всё равно уже опоздали на десять минут, так что даже телепортация не спасла бы."

show shizu behind_blank_close at twoleft 
show misha perky_confused_close at tworight 
with charaenter

mi "Что-то не так, %(name_hicchan)s?"

hi "Перерыв кончился десять минут назад. Я тут всего третий день и уже прогуливаю."

play music music_running fadein 4.0

show shizu adjust_smug_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Угу~! Ты прогулял."

hi "Эй, это не смешно! Вы тоже! Кстати, разве вы не члены Школьного совета? Вы подаёте дурной пример."

show misha perky_sad_close
with charachange

mi "%(name_hicchan)s у нас такой моралист…"

show shizu basic_normal_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Но~! %(name_hicchan)s прав, он опоздал и~ не торопится идти на урок."

mi "Как представители Школьного совета мы позаботимся, чтобы тебя наказали за это~!"

hi "Но ведь это вы меня сюда притащили, поэтому вина лежит на вас! Будьте поответственней!"

show shizu behind_frown_close
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "%(name_hicchan)s, мы вербовали потенциального члена Совета. Уважительная причина~! Но… ты не член Совета, поэтому у тебя нет оправдания!"

hi "Есть. Этот «потенциальный член Совета» – я."

show shizu basic_happy_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Да~! Ты вступаешь в Школьный совет, %(name_hicchan)s?"

"%(name_shizune)s торжествующе поднимает чашку, оттопырив мизинчик и помахивая им."

show shizu behind_blank_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "Эх, %(name_hicchan)s, если бы только ты был членом Школьного совета… Но~! У тебя ещё есть шанс согласиться! Присоединишься сейчас – избежишь проблем и сможешь совершать такие маленькие прогулки с нами ещё много-много раз! Будет весело~!"

"Я начинаю подозревать, что угодил в заранее расставленную хитроумную западню. Вероятно, %(name_shizune)s заманила меня сюда, рассчитывая на то, что я забуду о времени и окажусь в подобной ситуации. Коварно…"

"Что ж, учитывая всё то, что мне о ней известно, мне стоило оставаться настороже. Но если я признаю то, что сам виноват в сложившейся ситуации, то никогда не смогу простить себя."

"Я пытаюсь прочесть намерения %(name_shizune)s по её глазам, но она просто смотрит на меня ничего не выражающим невинным взглядом. Она делает глоток чая, будто насмехаясь надо мной."

show shizu basic_normal_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Кстати, %(name_hicchan)s, я не планировала ничего подобного, это вышло само собой~!"

"Я уже собирался списать эту теорию на паранойю, но эта фраза порождает новый виток подозрений. Я чуть не падаю со стула от ужаса, когда осознание накрывает меня с головой."

"Итак, всё и вправду было умело подстроено. С самого начала. Всё ради того, чтобы в тот миг, когда я начну сгорать со стыда, заставить меня присоединиться к Школьному совету."

show shizu adjust_smug_close
with charachange

shi "…"

show misha cross_laugh_close
with charachange

mi "А-ха-ха-ха-ха~! Ты что, нервничаешь, %(name_hicchan)s~? Ты ведь не думаешь, что мы всё это время играли с тобой?"

hi "Разве нет?"

show misha perky_sad_close
with charachange

mi "%(name_hicchan)s, ты действительно так думал?.."

show shizu behind_frown_close
with charachange

"Миша понуро опускает голову, и %(name_shizune)s тут же вторит ей. Как синхронно. Прекрасная пара. Точно близнецы."

shi "…"

mi "%(name_hicchan)s, %(name_sicchan)s говорит, что она польщена, но такой поступок был бы неприемлемым злоупотреблением властью и посягательством на твою свободу воли~! И~! Это было бы шантажом! %(name_sicchan)s никогда бы так не поступила, никогда!"

"Меня так и подмывает спросить Мишу, уверена ли она в этом, но я сдерживаюсь."

show shizu basic_normal_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "И %(name_sicchan)s сказала правду о том, что, раз ты с нами и мы выполняем работу для Совета, нет ничего страшного в пропуске пары уроков."

show shizu basic_normal_close
with charachange

shi "…"

show misha perky_confused_close
with charachange

mi "Не то чтобы это было таким уж хорошим оправданием…"

shi "…"

show shizu behind_blank_close
with charachange

mi "…И не то чтобы так можно было поступать чаще трёх раз в месяц…"

show shizu basic_normal_close
with charachange

shi "…"

mi "И не то чтобы этим можно и нужно было бы злоупотреблять…"

show shizu adjust_happy_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Поэтому~! Нам обязательно, обязательно нужно вернуться в класс! Когда-нибудь~!"

show misha cross_laugh_close
with charachange

mi "Ва-ха-ха!~"

"%(name_shizune)s машет Юко и указывает на пустую чашку, прося повторить заказ. Миша второпях доедает парфе, явно не собираясь на нём останавливаться. Может быть, и мне стоит взять ещё что-нибудь?"

"Сэндвич был чрезвычайно мал, и я не наелся, а раз %(name_shizune)s за всё платит, то можно попросить принести ещё один."

scene bg suburb_shanghaiext
with locationchange

stop music fadeout 5.0

"…Мы покидаем чайный дом, просидев в нём не один, а целых два урока."

scene bg suburb_roadcenter
with locationchange

"%(name_shizune)s и Миша, кажется, не возражают против того, чтобы прогулять их все. Они придумывают новый повод потянуть время, предлагая экскурсию по городку, которая выливается в прогулку по двум ближайшим кварталам."

scene bg school_scienceroom
with shorttimeskip

"Через какое-то время мы всё же возвращаемся в школу, и остаток учебного дня проходит как обычно. После уроков %(name_shizune)s и Миша собираются и покидают класс раньше меня. Если подумать, это первый раз, когда они оставили меня одного."

"Странно, мне даже как будто бы не хватает их компании. Класс быстро пустеет, и я покидаю кабинет последним."

scene bg school_lobby
with locationchange

"Однако в вестибюле передо мной резко опускается, словно шлагбаум, знакомая рука."

show shizu behind_blank at center 
with charaenter

shi "…"

hi "О, привет, %(name_shizune)s."

scene black
with hands_in

"И знакомые ладошки закрывают мои глаза под взрыв озорного смеха."

mi "Эй, %(name_hicchan)s~! Угадай кто?"

"Миша задаёт этот вопрос без малейшего намёка на сарказм, что означает её искреннюю веру в то, что я не способен узнать её по ряду совершенно очевидных признаков."

hi "Кто бы это мог быть? Ну уж точно не Миша…"

mi "Ха-ха-ха~! Именно она!"

scene bg school_lobby
show shizu behind_blank at center 
show misha hips_grin at offscreenleft 
with hands_out

play music music_shizune fadein 1.0

scene bg school_lobby at bgright 
show shizu behind_blank at tworight 
show misha hips_grin_close at twoleft 
with charamove

"Она подскакивает к %(name_shizune)s и встаёт рядом."

show shizu basic_normal2
with charachange

shi "…"

show misha cross_smile_close
with charachange

mi "%(name_hicchan)s, ты сейчас занят?"

hi "Занят, направляюсь в свою комнату. Увидимся завтра!"

show misha cross_smile_close at offscreenleft 
show shizu basic_normal2 at twoleft 
show bg school_lobby at bgleft 
with ease

hide misha
show misha cross_smile_close at offscreenleft behind shizu

show shizu basic_normal2 at offscreenright 
show bg school_lobby at center 
with ease_accel

show shizu behind_blank_close at tworight 
show misha perky_smile at twoleft 
show bg school_lobby at bgright 
with ease_decel

"Я пытаюсь их обойти, но %(name_shizune)s проворно меня останавливает. Похоже, годы игры в футбол прошли даром. Наше поведение привлекает слишком много лишних взглядов. Лучше бы сдаться, пока я совсем не опозорился."

show shizu adjust_happy_close
with charachange

shi "…"

show misha hips_grin
with charachange

mi "%(name_hicchan)s, не мог бы ты подняться наверх и принести кое-что из кабинета кружка рисования?"

hi "Почему я?"

show misha cross_laugh
with charachange

mi "Ха-ха-ха~! %(name_sicchan)s считает, что если мы встретим учителя рисования, то он начнёт с нами здороваться, а он ей не нравится!"

hi "Пусть не обращает на него внимания."

show shizu behind_blank_close
with characlose

shi "…"

show misha hips_grin
with charachange

mi "Она пыталась, но, несмотря на то что %(name_sicchan)s глухая, он всё равно говорит: «Привет~!»"

hi "А убежать?"

show shizu cross_angry_close
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Я никогда не бегу с поля боя!"

"Резкость этих слов заметна даже через Мишин перевод. Спорить об этом дальше с %(name_shizune)s бесполезно."

hi "Миша, а почему ты не сходишь?"

show misha sign_smile
with charachange

mi "У меня от лестниц голова кружится, %(name_hicchan)s!"

show shizu basic_normal_close
with charachange

hi "…"

"%(name_shizune)s кивает в подтверждение её слов."

show misha perky_sad
with charachange

mi "Ну, пожалуйста, %(name_hicchan)s! Нам нужны эти материалы, чтобы построить киоски для фестиваля! Ты же обещал немного помочь, ведь так? Так?"

"Не стоило бы этого делать, но разок можно и помочь."

hi "Ладно."

show shizu adjust_happy
with charadistant

shi "…"

show misha hips_grin
with charachange

mi "Отлично, %(name_hicchan)s! Спасибо~!"

show misha perky_smile
with charachange

mi "Вот что нам нужно!"

"Она передаёт мне бумажку."

"Список явно составляла %(name_shizune)s. Он написан от руки, но каждый символ вычерчен с безупречной точностью, как будто набран на компьютере, а сам список предельно подробен, с пунктами, подпунктами и даже клеточками для галочек."

"Им нужны краски, кисти, листы ватмана и мольберты разных типов и в разных количествах. Интересно, как я протащу всё это вниз по лестнице, не сломав шею?"

stop music fadeout 4.0



label ru_A13:

play music music_dreamy fadein 2.0

scene bg school_miyagi
with locationchange

"Лилли и Ханако немедля принимаются за подготовку к ланчу."

"Не успеваю я развязать свой узелок с едой, как Лилли достаёт термос и чайные пакетики, а Ханако раскладывает ланч."

show lilly basic_smile at center 
with charaenter

hi "Так вот зачем вы приходите сюда почти каждый день."

show lilly basic_smileclosed
with charachange

li "Да, мы с Ханако обычно едим здесь. Для нас обеих это место – лучшее, что можно найти."

"Учитывая то, как Ханако реагировала на мои попытки пообщаться последние пару дней, я понимаю, что она права. К тому же так Лилли удаётся урвать несколько минут тишины вдали от своего класса."

"Я сажусь за стол последним, когда мой чай уже налит."

scene bg tearoom_everyone_noon
show tearoom_hisaoe lsmile
show tearoom_lillye smileclosed
show tearoom_hanae sad
with fade

"Чем больше времени провожу я с ними, тем больше вижу в них полную противоположность Мише и %(name_shizune)s."

"Резкая и прямолинейная манера общения %(name_shizune)s заметна даже без голоса, а Миша может найти общий язык с кем угодно. В то время как Лилли являет собой воплощение мягкости и учтивости, а Ханако – самая застенчивая девочка из всех, кого я знаю."

li "Как тебе живётся в «Ямаку», Хисао? Кажется, тебя что-то беспокоило."

show tearoom_hisaoe sigh
with charachange

hi "Я время от времени теряюсь, и на меня налетают в коридорах. В остальном всё не так уж и плохо…"

show tearoom_lillye smileclosed
show tearoom_hanae shy
with charachange

ha "Ты… ты очень плохо выглядел после столкновения. Ты точно… в порядке?"

"На какой-то момент меня охватывает желание рассказать им о своей болезни, но я сдерживаюсь."

"Почему-то мне неловко говорить об этом малознакомым людям, пусть они и настолько дружелюбны."

show tearoom_hisaoe hrelief
with charachange

hi "Ерунда, просто опешил от неожиданности."

show tearoom_lillye thinking
show tearoom_hanae sad
show tearoom_hisaoe lthink
with charachange

"Судя по выражению их лиц, они не верят мне. Но всё равно не настаивают. Должно быть, из уважения к моей частной жизни."

"Полагаю, это одно из местных негласных правил: «не спрашивай». Даже если проблема очевидна, как, например, у Ханако, всё равно есть рамки и история её возникновения находится за ними."

"У каждого есть что-то, о чём ему неудобно говорить, и, думаю, все здесь это понимают."

show tearoom_hisaoe lsmile
with charachange

hi "Так, эм… вы давно здесь учитесь? Похоже, вы тут неплохо ориентируетесь."

show tearoom_lillye smileclosed
with charachange

li "Хм… ну, я здесь с начала старшей школы, но переехала в общежитие только год назад."

li "Ханако тоже перевелась в начале старшей школы и сразу переехала в общежитие, если мне не изменяет память."

show tearoom_hanae shy
with charachange

ha "Верно. Со… старшей школы."

hi "Тогда же вы и познакомились?"

show tearoom_lillye ara
with charachange

li "Именно. Ханако живёт в соседней комнате, так что это вполне естественно, правда?"

ha "П-правда."

show tearoom_hisaoe calm
with charachange

hi "Да, конечно."

"Соседство с кем-то, возможно, является уже достаточной причиной, чтобы подружиться, хотя думаю, что слепота Лилли тоже сыграла в этом не последнюю роль."

"Не могу себе представить, чтобы Ханако легко подружилась с кем-то, кому пришлось бы нарочно отводить взгляд от её шрамов."

"Беседа иссякает, и мы принимаемся за ланч."

scene bg tearoom_everyone_noon
show tearoom_hisaoe lsmile
show tearoom_lillye weaksmile
show tearoom_hanae sad
with shorttimeskip

play sound sfx_warningbell

"Проходит немного времени, и звон колокола возвещает окончание перерыва. Девушки убирают свои ланчи так же быстро, как и доставали, и я следую их примеру."

show tearoom_lillye smileclosed
with charachange

li "Думаю, мне пора идти. Ты пойдёшь с Хисао, Ханако?"

show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange

"Ханако смотрит на меня, и несколько мгновений ясно видно, что она подумывает пропустить урок, просто чтобы не входить в класс вместе со мной."

show tearoom_hanae sad
with charachange

ha "Д-да."

"Даже не знаю, что и думать. Ханако действительно очень легко задеть, если неправильно взглянуть на неё. От этого я тоже начинаю немного нервничать, но стараюсь отогнать это чувство, пытаясь вести себя как можно более естественно."

show tearoom_hisaoe hsmile
with charachange

hi "Тогда нам надо торопиться. Судя по звонку, урок уже начался."

"Наклоняясь за тростью, Лилли кивает нам на прощание, и мы с Ханако выходим первыми."

scene bg school_hallway3
with locationchange

"Мы быстро идём пустыми коридорами к нашим классам."

"Когда мы достигаем дверей класса 3-2, в котором учится Лилли, та поворачивается ко мне."

show lilly cane_smileclosed at twoleft 
show hanako emb_timid at tworight 
with charaenter

li "Хисао, спасибо за то, что разделил с нами сегодня трапезу."

hi "И тебе спасибо, Лилли."

hide lilly
with charaexit

stop music fadeout 8.0

show hanako emb_timid at center 
show bg school_hallway3 at bgleft 
with charamove

"На этом наши пути расходятся; Лилли заходит в свой класс, оставив нас с Ханако, которая всё ещё выглядит так, будто хочет сбежать."

hi "Ну что, ты уверена, что хочешь пойти на урок?"

show hanako basic_worry
with charachange

ha "Д-да."

hi "Тогда ладно."

"Мне хочется сказать ей что-нибудь ещё, но сложно придумать что-то уместное, да к тому и безопасное."

"И Лилли была права: чем дольше мы будем мешкать, тем больше потом придётся объяснять."

play sound sfx_dooropen

"Я открываю заднюю дверь класса и вхожу."

scene bg school_scienceroom
show muto irritated at center 
with locationchange

"Учитель смотрит на меня и открывает рот, чтобы что-то сказать."

show muto normal
with charachange

"Но, когда за мной входит Ханако, он просто кивает нам и продолжает урок."

"Вот уже в третий раз опоздание Ханако игнорируется. Определённо, этому должно быть какое-то объяснение."

hide muto
with charaexit

"Мы идём к своим местам, и я замечаю, что Миша и %(name_shizune)s тоже отсутствуют."

"Интересно, это какое-то неофициальное соглашение с персоналом или своего рода прерогатива для особых учеников этой школы?"

"Стараясь не шуметь, я достаю из портфеля нужный учебник и начинаю нагонять остальных."

"Урок проходит спокойно."










label ru_A15:

scene bg school_scienceroom
with None

"Вопреки моему первому впечатлению, Муто оказался неплохим учителем: ему удаётся интересно подать материал."

"Однако методика преподавания у него всё же странная. Он как будто считает, что все мы гении от рождения."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

play music music_tranquil fadein 3.0

"С последним звонком я понимаю, что до конца дня мне абсолютно нечем заняться."

"Странно: в больнице у меня целые дни были свободными, но в этой школе задача по заполнению значительно меньшего количества времени кажется более трудной."

"Все остальные ученики покидают класс, оставляя меня наедине с учителем."

"Муто проверяет листки с заданиями, над которыми мы сегодня работали, и делает в них пометки красной ручкой."

"На секунду оторвав взгляд от бумаг, он замечает меня и морщит лоб."

show muto normal at center 
with charaenter

mu "Ты что-то хотел, Накай?"

"Я вздрагиваю от неожиданного обращения ко мне. Но, наверное, это естественно, что у нас завязалась беседа, ведь больше в классе никого нет."

hi "Эм-м… ничего. Я думал, чем бы заняться после школы."

"Учитель закрывает ручку колпачком и ровняет стопку бумаг, дважды стуча ей по столу."

"В этот момент своей педантичностью он напоминает мне %(name_shizune)s. Впрочем, его неторопливость и расслабленность сразу же стирают это впечатление."

mu "И что надумал?"

hi "Я хочу вступить в кружок, но пока не решил в какой."

mu "Походи на собрания разных кружков – может, что и понравится."

hi "Пожалуй…"

hi "Но я…"

"Я не знаю, стоит ли спрашивать об этом."

show muto irritated
with charachange

"А от пристального взгляда Муто желание говорить и вовсе пропадает."

"Но рано или поздно мне всё равно придётся коснуться этой темы."

hi "Я не знаю, как вести себя с людьми… то есть с остальными учениками в этой школе."

hi "Я с ними общаюсь и всё такое, так что не подумайте, что я от них закрываюсь."

hi "Просто не могу взять в толк, как мне относиться к их инвалидности? Совсем не обращать на это внимания было бы невежливо, а игнорировать – как-то странно."

hi "В обоих случаях получится, что я веду себя неправильно."

"Учитель рассеянно чешет щёку."

show muto normal
with charachange

mu "Не стоит делать из этого проблему, вот и всё. Она существует лишь у тебя в голове."

mu "Ведь ты можешь нормально говорить с человеком независимо от того, слеп он или нет."

show muto smile
with charachange

mu "Прекрати постоянно думать об инвалидности собеседника. Все здешние ученики – обычные дети, что бы тебе ни казалось на первый взгляд."

"Вчера Юко говорила мне то же самое."

"Конечно, они правы, но не думать об этом слишком тяжело. Как можно игнорировать, например, глухоту %(name_shizune)s, если общаться с ней возможно только через Мишу?"

"Или Ханако… как посмотреть ей в лицо, не обратив внимания на шрамы?"

hi "Но…"

play sound sfx_doorslam
stop music fadeout 0.3

show muto irritated
with vpunch

"Меня прерывает грохот распахнувшейся двери."

show misha hips_grin at offscreenright 
with None

show muto irritated at twoleft 
show bg school_scienceroom at bgleft 
show misha hips_grin at tworight 
with ease

play music music_comedy fadein 0.5

mi "Учитель~!"

"Миша вламывается в кабинет, вскинув руку в бойком приветствии; её оглушительный возглас мог бы поднять мёртвых из могил."

"Она марширует к учительскому столу, размахивая руками в такт шагам."

"Муто, оторопевший от громозвучного Мишиного вторжения, откидывается на спинку стула."

mu "Микадо."

"Миша замирает, оглядываясь по сторонам: она явно не понимает, чем вызван его сердитый тон."

show misha perky_confused
with charachange

mi "Да~?"

mu "Я уже неоднократно просил тебя убавить громкость."

show misha perky_smile
with charachange

mi "Да~!"

"Ответ её не менее громогласный, нежели приветствие; Муто сдаётся и устало потирает глаза."

mu "Ну, так что ты хотела?"

show misha perky_sad
with charachange

mi "Мне… нам нужна помощь! У нас кончились материалы для фестивальных стендов!"

show misha sign_sad
with charachange

mi "Это беда!"

"Она размахивает розовой полоской бумаги."

mu "Ну так… принесите ещё из кабинета рисования. В чём проблема?"

show misha perky_sad
with charachange

mi "Фанера! Вся проблема в фанере! В прошлый раз, когда нам понадобилось больше, её запасы там уже подходили к концу и мы просто взяли всю оставшуюся. Нам вроде бы хватило."

mi "А теперь её там совсем не осталось. Вы случайно не знаете, где есть ещё?"

mu "Нет. Случайно не знаю."

show misha perky_confused
with charachange

mi "%(name_sicchan)s… то есть президент, сказала, что учитель сможет помочь. Она ошиблась?"

"Миша не замечает, что у Муто крайне страдальческий вид: будто он морщится всем своим существом."

"На Муто больно смотреть. Словно ему сверлят череп, при этом включив на полную громкость поп-музыку."

mu "Увы, я не в курсе, есть ли в школе фанера вообще. И я понятия не имею, где она может лежать."

show misha perky_sad
with charachange

mi "Ох-ох-о-о… что же мне делать?"

mu "Попробуй разыскать господина Номию: он должен знать."

mu "Он, правда, скорее умрёт, чем расстанется с ней… но это уже отдельный вопрос."

mi "А-а-а! Но я спешу! Мы слишком заняты!"

"Она хватается за голову и в отчаянии мечется взглядом из стороны в сторону, даже не замечая, что мнёт записку у себя в руках."

mi "У меня даже нет времени искать всё это! Мы выбиваемся из графика, у нас и так полно работы!"

show muto smile
with charachange

stop music fadeout 2.0

"Муто пристально смотрит на неё и вдруг улыбается. Лучше бы он этого не делал: улыбка ему совершенно не к лицу."

mu "Может, вам найти временного помощника?"

show muto normal
with charachange

"Он переводит на меня сосредоточенный взгляд, как бы говоря: «Ну же, ступай, заведи друзей»."

"…"

hi "Э… Думаю, я мог бы вам помочь."

play music music_running fadein 0.5

show misha hips_grin
with charachange

mi "Правда? Спасибо, %(name_hicchan)s, ты такой милый!"

show misha sign_confused
with charachange

"Она вдруг озадаченно замирает, глядя так, будто только что заметила моё присутствие, и даже удивлённо вскрикивает, указывая на меня пальцем."

mi "А что %(name_hicchan)s делает здесь в такое время? Ведь уроки кончились, пора гулять и веселиться~!"

mu "У нас был небольшой разговор."

show misha perky_sad
with charachange

mi "Только не это! Тебя оставили после уроков? У тебя неприятности, %(name_hicchan)s?"

hi "Нет, у меня всё в порядке."

mi "Учитель, у %(name_hicchan)sа неприятности?"

mu "Ничего подобного."

"Муто тяжело вздыхает, и я понимаю, что сейчас самое время избавить его от назойливой Миши."

hi "Итак, что вам нужно?"

show misha hips_smile
with charachange

mi "Вот список. Если в кабинете рисования нет фанеры, я попробую поискать где-нибудь ещё."

"Я неуверенно беру протянутую записку."

hi "Я помогу вам, но это не значит, что я готов вступить в Совет, ясно?"

show misha perky_sad
with charachange

mi "Ясно…"

show misha hips_grin
with charachange

mi "Всё равно спасибо, %(name_hicchan)s. Только побыстрей: мы строим киоски прямо сейчас – надо спешить-спешить-спешить!"

hide misha
with easeoutright

"Она вылетает за дверь, а мы с учителем смотрим друг на друга в молчаливом согласии."

show muto normal at center 
show bg school_scienceroom at center 
with charamove

mu "Радуйся, Накай, теперь тебе есть чем заняться."

"Пожалуйста, не так самодовольно."

"Мелким, аккуратным почерком, принадлежащим, без сомнения, %(name_shizune)s, на смятом листке написан перечень необходимых для фестиваля материалов, от краски до фанеры. Я тяжело вздыхаю."

hi "Тогда я пойду."

stop music fadeout 4.0

"Я машу списком учителю и выхожу в коридор."





label ru_A16:

scene bg school_hallway3
with locationchange

"По соседству с нашим кабинетом располагаются классы 3-1 и 3-2 по правой стороне и 3-4 – по левой, и все двери выглядят совершенно одинаково."

"Дальше по коридору с одинаковыми дверьми находятся кабинеты, для проведения уроков, как я считал, не используемые."

"Наверное, кабинет кружка рисования – один из них."

"Я аккуратно открываю последнюю в коридоре дверь и заглядываю внутрь."

scene bg school_classroomart at bgleft 
with locationchange

"За ней оказывается классная комната, но либо неубранная, либо вообще неиспользуемая. Я не ошибся дверью?"

"Парты и стулья, покрытые тонким слоем пыли, в беспорядке расставлены по комнате. В углу стоит несколько мольбертов – похоже, я не ошибся."

"Комната залита светом из огромных окон, на партах лежат тени."

"Облачка пыли танцуют в недвижимом воздухе, делая солнечные лучи почти осязаемыми."

"Ради смеха я обращаюсь к пустой комнате."

hi "Есть кто до—{w=.5}{nw}"

"Заметив что-то краем глаза, я останавливаюсь на середине фразы."

scene ev rin_eating_zoomout
with flash

play music music_rin fadein 0.5

"На парте сидит коротко стриженая девушка; к моему удивлению, она одета в мужскую школьную форму и держит пальцами ног вилку, на которую нанизан кусочек еды."

"Такой необычный способ принятия пищи вызван очевидным отсутствием у неё рук, но ещё больше меня ошеломляет само её присутствие здесь."

"Как же я её раньше не заметил? Она сидит в углу неподвижно и на первый взгляд кажется предметом обстановки или статуей."

"Я сегодня совсем невнимательный."

"Девушка застыла на месте, уставившись на меня огромными зелёными глазами, как кролик в свете фар."

"Её вилка так и замерла у открытого рта."

"Я смотрю на неё, разинув рот, внезапно вспомнив, что остановился на полуслове, и пытаясь решить, стоит ли заканчивать фразу."

"Мы застыли в тишине, нарушаемой лишь ритмичным тиканьем настенных часов."

rin_ "Привет."

"Девушка отправляет вилку в рот и выжидательно на меня смотрит, пережёвывая еду. Я чувствую себя неловко."

hi "М-м… привет. Меня попросили забрать отсюда кое-что. Для фестивальных киосков, в смысле. Я не думал, что тут кто-то есть."

rin_ "Никого нет. Именно поэтому я тоже сюда пришла."

"Она накалывает на вилку следующую порцию."

hi "Тогда разве это не значит, что здесь есть ты?"

scene bg school_classroomart at bgleft 
show rin relaxed_surprised at center 
with locationchange

"Она приподнимает брови, как бы сомневаясь в верности моего замечания."

rin_ "А ты наблюдательный. Полагаю, что так. А ты кто?"

"Прямолинейная девушка, не правда ли?"

hi "Меня зовут Накай, Хисао Накай. Я только в понедельник перевёлся."

show rin basic_absent
with charachange

rin_ "А меня – Рин. %(name_tezuka)sа Рин. Рин %(name_tezuka)sа."

show rin basic_deadpandelight
with charachange

rin "Руку я тебе не пожму, но теперь мы хотя бы знаем, кто есть кто."

rin "Это здорово."

"По её серьёзной манере разговора трудно определить, шутит ли она насчёт рукопожатия."

"Шутки на эту тему кажутся совсем неуместными, и это меня беспокоит."

show rin relaxed_nonchalant
with charachange

"Пока я пытаюсь выяснить, что уместно, а что нет, девушка теряет ко мне интерес и переводит голодный взгляд на еду."

show rin basic_deadpan
with charachange

rin "Могу я продолжать ланч? Если ты не против моего присутствия, я не против твоего."

rin "Если тебе нужно что-то взять, то всё хранится в конце класса."

hi "Конечно, продолжай. Но… ланч? Учебный день уже кончился."

show rin basic_awayabsent
with charachange

rin "Тогда как бы ты это назвал? Нет специального слова для приёма пищи между ланчем и обедом, ведь так? Меня это тоже беспокоит, но я не знаю, какое слово подобрать."

hi "Не думаю, что между ланчем и обедом следует что-то есть."

show rin negative_spaciness
with charachange

rin "Но я голодная, и иначе мою восхитительную еду пришлось бы выбросить."

show rin basic_delight
with charachange

rin "У меня тут карри. Очень вкусное."

"Решительным движением Рин снова поднимает зажатую между пальцами ноги вилку и по меньшей мере неучтиво указывает ею прямо на меня."

scene ev rin_eating
with locationchange

rin "Так что, Накай, какими судьбами ты здесь оказался?"

hi "Как я уже сказал, мне поручили поискать некоторые вещи."

stop music fadeout 5.0

rin "Нет, в школе. Судя по внешнему виду, ты вроде здоров. Проблема где-то внутри?"

"Я в полном замешательстве, не могу из себя ничего выдавить."

hi "Я…"

rin "Попробую угадать. Я хорошо угадываю. Лучше, чем большинство людей."

"Рин обрывает меня на полуслове прежде, чем я успеваю ответить на вопрос или как-то его обойти. Не знаю, что бы я выбрал."

"Я снова оказываюсь перед этой проблемой. Я ещё никому не рассказывал здесь о своём недуге. Впрочем, возможно, лишь потому, что об этом никто не спрашивал."

"У меня сложилось впечатление, что игнорирование таких вопросов – часть здешних общественных норм, как сказал учитель."

"Интересно, могут ли люди здесь найти общий язык? Наверное, не легче, чем обычные люди."

"Я не могу понять условия, в которых находятся %(name_shizune)s или Лилли."

scene bg school_classroomart at bgleft 
show rin basic_absent at center 
with locationchange

"Разумеется, пока я об этом размышляю, Рин с глубокомысленным выражением лица продолжает обдумывать, что со мной не так."

"Она помещает вилку в рот и откидывается назад, устремив взгляд в потолок, как если бы там был написан ответ."

"Луч света из окна освещает её лицо, создавая на другой его половине маску тени."

show rin basic_lucid
with locationchange

rin "Вряд ли дело в твоей голове, а какая-нибудь кишечная проблема была бы банально-скучной, как мой обед. Да вдобавок пресной."

show rin basic_deadpandelight
with charachange

rin "Должно быть, проблема у тебя в штанах!"

play music music_rin fadein 0.5

"Такое утверждение в духе пьяного Шерлока Холмса, а также полное отсутствие такта, с которым это произносится, застаёт меня врасплох."

"Наверное, я неосознанно отшатываюсь, потому что глаза Рин расширяются от изумления и восторга."

show rin relaxed_surprised
with charachange

rin "Так, значит, я права! У тебя что-то не в порядке с причиндалами?"

"Всё ещё в шоке, но осознавая необходимость как-то отреагировать, я выдаю первое, что приходит в голову."

hi "Нет! Ничего подобного! У меня проблемы с сердцем. Аритмия."

"…"

"Я произнёс это. Скорее, конечно, выпалил, но всё же сказал вслух."

show rin negative_spaciness
with charachange

"Девушка кривит губки и сердито на меня смотрит, будучи явно очень расстроенной."

rin "Как скучно. Проблема в штанах была бы куда более позорной."

"Что это за реакция?"

hi "Извини, что подвёл."

show rin basic_awayabsent
with charachange

rin "Я тебя прощаю. Просто я коллекционирую людей, и иметь человека с… ну, знаешь, такой проблемой было бы очень здорово."

hi "Коллекционируешь людей?"

show rin basic_absent
with charachange

rin "Людей с разными проблемами."

hi "Ты что, просто… ходишь и спрашиваешь у всех, что с ними не так?"

show rin basic_deadpannormal
with charachange

rin "Именно."

hi "Понятно."

"…"

stop music fadeout 8.0

hide rin
with charaexit

"Разговор затухает, и Рин возобновляет приём пищи, а я продолжаю думать над тем, что она сказала."

"Я впервые поведал кому-то о своём недуге. Все остальные либо уже знали, либо слышали о нём от кого-то ещё."

"Или же им до настоящего момента необязательно было знать об этом, как и всем прочим ученикам этой школы."

"Мне следует упоминать его при знакомстве? От меня этого ожидают?"

"«Привет, меня зовут Хисао. У меня серьёзные проблемы с сердцем»."

"Так мне теперь представляться людям?"

"Как будто наши болезни характеризуют нас. Что за мерзкая идея?"

"Или, может быть, у этой %(name_tezuka)sи просто странный интерес к подобным вещам?"

play music music_dreamy fadein 8.0

show bg school_classroomart at bgright 
with charamove

show rin basic_awayabsent at right 
with charaenter

"Пока я иду в конец кабинета за вещами из Мишиного списка, мне представляется шанс краем глаза понаблюдать за Рин."

"У неё светло-каштановые, почти рыжие, коротко стриженые волосы. Без рук с длинными волосами было бы, наверное, трудно управиться."

"Из-за мужской школьной формы и отсутствия рук она выглядит очень худой, почти тощей."

"Она ничем особо не привлекательна, разве что тёмно-зелёными глазами, которыми беспрестанно моргает из-под короткой чёлки, даже когда ест."

"Из-за теней и расстояния создаётся ощущение, что они вообще не отражают свет, а, наоборот, поглощают его полностью, как глубокие колодцы."

"Движения её ног так же ловки, как и движения рук обычных людей."

"Однако, когда смотришь на это, может стать не по себе, особенно когда ногами едят. Во всяком случае, я себя чувствую немного неловко."

"Я стараюсь не думать о слове «неестественный», но уже поздно, да?"

"Я продолжаю шарить по ящикам и полкам, но со временем молчание становится слишком неудобным, поэтому я пробую разговорить эту странную девушку."

hi "Ты всегда ешь одна и так поздно? Или заходят случайные посетители?"

show rin basic_absent
with charachange

show rin basic_absent at center 
show bg school_classroomart at bgleft 
with charamove

rin "Посетители… Наверное, ты – мой первый случайный посетитель. Но я не всегда ем одна."

rin "Иногда я ем с определённым человеком на крыше, если она не носится где-нибудь."

hi "Носится?"

show rin basic_deadpan
with charachange

rin "Она увлекается спортом."

hi "А…"

"Это всё, что приходит мне в голову в качестве ответа."

"Мы снова погружаемся в молчание, пока Рин доедает остатки своей еды."

"Я смотрю на свою поклажу, сверяясь с Мишиным списком. Похоже, я достал всё, за исключением фанеры."

hi "Эм-м… ну, думаю, я всё нашёл."

show rin basic_deadpannormal
with charachange

rin "Молодец. Можешь идти, я не возражаю. Я всё равно собиралась вздремнуть."

rin "Тебе ведь нужно делать с этими вещами то, что собирался?"

show rin relaxed_surprised
with charachange

rin "Или, может быть, тебе нравится наблюдать за спящими девушками?"

hi "Э…"

"Я не уверен, как это следует понимать, но Рин выглядит серьёзной."

hi "Даже если бы и нравилось, полагаю, что мне пора."

hi "Ещё… Ещё увидимся, %(name_tezuka)sа."

show rin basic_absent
with charachange

rin "Можешь звать меня Рин."

show rin basic_awayabsent
with charachange

rin "Думаю, на данном этапе наших отношений я могу тебе такое позволить."

"Я собираюсь уйти, но поддаюсь внезапно нахлынувшему на меня желанию сказать что-то ещё."

hi "Хорошо, тогда я – Хисао."

show rin basic_deadpannormal
with charachange

rin "Тогда да."

"…"

"Рин смотрит на меня прямо в упор, но угрожающего чувства, которое обычно бывает в такой ситуации, не возникает."

"Будто она на меня и вовсе не смотрит."

"Она пару раз моргает, и я не могу понять, почему внезапно между нами повисла пауза."

show rin basic_deadpandelight
with charachange

rin "До встречи, Хисао."

"Кажется, на её лице мелькает тень улыбки."

scene bg school_hallway3
with locationchange

play sound sfx_doorclose

"Я тихо пячусь вон из комнаты. Закрыв перед лицом дверь, я шепчу:"

hi "Какая загадочная девушка…"

"Из класса приглушённо, нараспев слышится:"

rin "А я слы~шала!"

stop music



label ru_A17:

scene bg school_hallway3
with None

show shizu behind_blank
show misha hips_grin_close
with hpunch

mi "Что она слышала?"

play music music_comedy

"Я вздрагиваю от неожиданного появления Миши, чьего приближения я не услышал, несмотря на тишину, царившую в коридоре."

"Каким-то образом она подобралась ко мне на расстояние прыжка, не издав ни звука. У меня от этого мурашки по коже бегут. На мгновение я вспоминаю про сумасбродную теорию %(name_kenji)s о всемирном тайном обществе феминисток, но тут же отбрасываю эту мысль подальше."

show misha hips_grin_close at twoleft 
show shizu behind_blank at tworight 
with charamove

"%(name_shizune)s, стоящая чуть поодаль от Миши, выглядит озадаченной, поскольку не могла услышать замечания, привлёкшего внимание Миши, но Миша явно возбуждена."

show misha perky_confused_close
with charachange

mi "Нет, постой, а кто там? Сегодня в кружке нет занятий."

"Она пытается с любопытством выглянуть из-за меня, несмотря на то что закрытая дверь всё равно не даст ей ничего увидеть."

hi "Что вы здесь делаете?"

mi "Тебя так долго не было, что нам пришлось прийти и проверить, что стряслось. Нехорошо, %(name_hicchan)s~"

show misha hips_frown_close
with charachange

"Она грозит мне пальцем."

mi "Я нашла фанеру, но остального до сих пор не хватает, потому что ты – копуша."

hi "А, прости. Э… я всё нашёл, как раз собирался принести."

show misha cross_frown_close
with charachange

mi "Думаю, ты нас малость подвёл, %(name_hicchan)s~! Интересно, кто это там с тобой был…"

"Миша что-то быстро говорит %(name_shizune)s, пару раз указав на своё ухо."

show shizu basic_angry
with charachange

show shizu basic_angry at right 
with charamove

play sound sfx_dooropen

"%(name_shizune)s тут же протискивается мимо меня к двери и открывает её."

"Могу только представить тот шок, который она сейчас испытает."

"С её трудолюбием и жизненными принципами ей не под силу вынести дерзость, с которой некто осмелился надругаться над школьным имуществом, используя его в качестве поверхности для сна."

show shizu basic_frown
with charachange

"И действительно, она смотрит на Рин, застыв на месте, и только её плечи едва заметно дрожат, как мне кажется из-за подавляемой ярости."

"Вместо того чтобы взорваться, %(name_shizune)s, сделав несколько глубоких вдохов, поправив очки и с шумом захлопнув дверь, принимается неистово жестикулировать Мише."

play sound sfx_doorslam

show shizu cross_angry
with vpunch

"Может быть, она и взорвалась, только я этого не понял."

show shizu behind_frown
with charachange

"На меня она тоже бросает тяжёлый взгляд, как будто я был каким-то образом виноват в том, что Рин спит на одном из столов."

"Надеюсь, у неё не возникло никаких сомнительных идей насчёт причин моей задержки."

rin "Эй."

"Голос Рин доносится из-за закрытой двери, и через пару мгновений я понимаю, что для неё может быть проблематично открыть её."

play sound sfx_dooropen

"Я открываю дверь. Рин стоит в проходе и полузаинтересованно-полусонно глядит на нас."

show rin relaxed_sleepy at offscreenright 
with None

show shizu basic_frown at right 
with charachange

show shizu basic_frown at Transform(xanchor=0.5, xpos=0.55) 
show rin relaxed_sleepy at right 
with charamove

rin "Привет."

show shizu basic_frown
with charachange

shi "…"

show misha cross_frown
with charadistant

mi "Мисс %(name_tezuka)sа, что это вы вытворяете? У вас нет абсолютно никакого права использовать школьное имущество для таких… э… постыдных?.. занятий!"

show rin negative_confused
with charachange

rin "Как внезапно народу-то прибыло. Не знала, что я так популярна."

"Сложно сказать, довольна она таким поворотом событий или нет."

"Во всяком случае, она игнорирует выговор %(name_shizune)s/Миши, так что им ничего не остаётся, кроме как оставить эту тему."

show shizu behind_frown
with charachange

"%(name_shizune)s стучит Мишу по плечу, указывает на Рин и делает несколько быстрых жестов."

shi "…"

show misha sign_smile
with charachange

mi "Неважно, насколько вы популярны, пожалуйста, больше так не делайте."

show shizu basic_angry
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Кстати, как продвигается ваш проект? К фестивалю всё будет готово?"

show rin basic_awayabsent
with charachange

"Невзирая на давление, оказываемое ледяным взглядом %(name_shizune)s, Рин смотрит на них вполне непринуждённо и вообще безучастно."

rin "Я тоже постоянно об этом размышляю."

show shizu behind_frustrated
with charachange

shi "…"

mi "И?"

show rin relaxed_boredom
with charachange

rin "Задумаюсь над этим серьёзнее."

"Когда %(name_shizune)s получает ответ Рин от Миши, она неудовлетворённо хмурится."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Мисс %(name_tezuka)sа, пожалуйста, попытайтесь подойти к этому ответственнее. Будет катастрофой, если стена будет выглядеть так, будто кого-то стошнило на неё обедом."

show rin basic_absent
with charachange

"Рин утвердительно кивает."

rin "Обязательно задумаюсь серьёзнее."

show misha cross_grin
with charachange

"Миша в ответ хихикает, но на лице %(name_shizune)s не появляется и намёка на улыбку даже после перевода."

hide shizu
hide misha
with charaexit

"Она только качает головой, забирает у меня материалы и в сопровождении Миши уходит."

show rin basic_deadpanupset
with charachange

"Рин задумчиво хмурится, наблюдая за удаляющимся дуэтом Школьного совета."

rin "Как грубо."

rin "Однако это правда. Мне надо закончить проект до выходных. Если не закончу, последствия будут печальными."

rin "Конец того мира, который мы знаем.{w} Как конец недели, только ещё печальнее."

rin "Гора-аздо печальнее."

show rin relaxed_nonchalant
with charachange

rin "Наверное, отложу свой сон. На необозримое будущее."

hide rin
with charamoveoutright

stop music fadeout 6.0

"Я уже собираюсь спросить, над каким проектом она работает и что за апокалиптические последствия, но она уходит обратно в кабинет."

rin "Не мог бы ты мне помочь, раз ничем не занят?"

scene bg school_classroomart
show rin basic_absent at center 
with locationchange

rin "Банка с краской не влезает в мою сумку, но она мне нужна."

"Она легонько пинает огромную банку краски, стоящую на полу рядом со столом, на котором она сидела и спала."

"Та в ответ издаёт глухой звон."

"Будучи джентльменом, я, естественно, поднимаю её."

"Тяжёлая."

hi "Да, конечно. Куда её нужно отнести?"

show rin basic_awayabsent
with charachange

rin "В другое место."

hide rin
with charaexit

"С этими словами она выходит в коридор, и мы с банкой следуем за ней, поскольку особого выбора у нас нет."

scene bg school_hallway3
with locationchange

"Теперь, когда %(name_shizune)s и Миша ушли, коридор тих и пуст, и мы тоже направляемся к лестнице на другом его конце."

scene bg school_staircase2
with locationchange

"Каждые десять, или пятнадцать, или двадцать шагов мне приходится перекладывать банку из одной руки в другую, потому что её тонкая ручка врезается мне в ладонь. Ну, хоть руки благодаря этому меньше устают."

"Рин идёт передо мной неровной походкой, под которую трудно подстроиться, или, может быть, это я иду странно из-за лишнего веса."

"Кажется, что кто-то из нас постоянно идёт то ли слишком медленно, то ли слишком быстро, и я не могу понять, кто именно."

scene bg school_lobby at bgright 
with locationchange

"Через два лестничных пролёта появляется проблема в виде фельдшера с его лисьей ухмылкой."

show nurse grin at center 
with charaenter

play music music_nurse fadein 0.5

nk "О, Накай, какое совпадение! И %(name_tezuka)sа, конечно."

show nurse grin at twoleft 
show bg school_lobby at center 
with charamove

show rin basic_awayabsent at tworight 
with charaenter

"Он любезно кивает Рин, которая не отвечает на его приветствие, и поворачивается ко мне, потому что явно хочет поговорить именно со мной."

show nurse concern
with charachange

nk "Я кое-что забыл упомянуть в понедельник."

"Я киваю и невозмутимо жду, потому что мне и в голову не приходит, чего бы он мог там забыть. Однако врезающаяся всё глубже в кожу ручка также не добавляет мне энтузиазма."

nk "Насчёт твоих лекарств. Поскольку ты перешёл на них не так давно, могут быть неожиданные побочные эффекты, в зависимости от которых нужно будет подкорректировать дозы или даже сменить лекарство."

show nurse neutral
with charachange

nk "Я буду регулярно брать у тебя анализы, но хочу, чтобы ты сообщал мне об отклонениях в своём состоянии, – если ты понимаешь, о чём я."

nk "Тошнота, головная боль – что угодно. Приходи на приём, если что-нибудь случится."

show rin basic_absent
with charachange

hi "Хорошо."

show nurse fabulous
show rin basic_awayabsent
with charachange

nk "Так как дела? Всё в порядке?"

"Я сдаюсь и опускаю банку на пол, прежде чем ответить. Видимо, это займёт больше времени, чем могут выдержать мои бицепсы."

"Я собираюсь ответить общей фразой, но осознаю, как часто я это делал в последнее время."

"Другие люди у меня тоже об этом спрашивали. Учителя и ученики. Мои родители, посетители, медсёстры и врачи в больнице."

"Все кажутся обеспокоенными этим вопросом. Это естественно для больницы, но для школы – не очень.{w} Но эта школа – исключение."

"Она невелика, и отношения между учениками и преподавателями здесь очень близкие."

"Во всяком случае такое у меня чувство."

"И в такую школу ученики переводятся нечасто."

show rin basic_absent
with charachange

"От этой мысли у меня бегут по спине мурашки, но я всё равно даю стандартный ответ."

"…"

show nurse grin
show rin basic_awayabsent
with charachange

nk "Это замечательно. И ещё кое-что."

show nurse fabulous
with charachange

nk "Мои источники сообщили, что ты не был ни на школьном стадионе, ни в бассейне, так что хочу поинтересоваться: выполняешь ли ты упражнения, которые я рекомендовал?"

"Конечно нет, но такая постановка вопроса вызывает ощущение, что я должен был с самого первого дня прямо-таки надрываться на беговых дорожках."


show rin basic_absent
with charachange

hi "У вас есть люди, которые шпионят за мной?"

show nurse grin
show rin basic_awayabsent
with charachange

nk "Не совсем. Просто я со многими знаком. Но у нас другая тема разговора, не пытайся от неё увильнуть."

show rin basic_absent
with charachange

hi "Ну, я вот как раз выполнял импровизированные упражнения – подъём тяжестей."

"Я несколько раз поднимаю и опускаю банку, изображая жалкую пародию на культуриста, хоть ручка и врезается болезненно мне в ладонь."

show nurse neutral
show rin basic_awayabsent
with charachange

"Глупая ухмылка на секунду исчезает с его лица, а потом, как ни в чём не бывало, возвращается на место."

show nurse grin
with charachange

nk "%(name_tezuka)sа, позволь, мы с ним наедине поговорим?"

stop music fadeout 1.0

show nurse neutral:
    ease 1.0 center 

show rin basic_awayabsent:
    ease 1.0 offscreenright 

show bg school_lobby:
    ease 1.0 bgright 

with None

show nurse neutral_close:
    ease 1.0 center 

show bg school_lobby:
    ease 1.0 bgright 

hide rin

with characlose

"Фельдшер хватает меня за плечо и, не дожидаясь разрешения Рин, в котором он и не нуждается, тащит меня в сторону."

show bg school_lobby at bgright 
show nurse concern_close at center 
with characlose

nk "Когда я говорил тебе про упражнения, я не шутил."

nk "Я понимаю, что это только твоя первая неделя, но, пожалуйста, не умаляй их значимости."

nk "Привычки трудно сформировать, поэтому я так настойчиво этого от тебя требую."

nk "Чем больше ты будешь увиливать и откладывать, тем труднее потом придётся. И так со всем, например с диетой."

label ru_choiceA17:
menu:
    nk "Можешь пообещать мне впредь относиться к этому серьёзнее?"
    with menueffect
    "Да.":


        return m1
    "Может быть.":

        return m2

label ru_A17a:

hi "Да, я обещаю. Определённо."



label ru_A17b:

hi "Может быть, но… то есть…"

"После моей фразы в его глазах появляется что-то похожее на угрозу, отчего мне хочется взять свои слова обратно."

hi "То есть я не знаю… я всё ещё пытаюсь привыкнуть к школе."

hi "Однако я обещаю попробовать."

nk "Звучит не очень убедительно, Хисао. Совет первый: медработники не любят, когда к их рекомендациям относятся несерьёзно."

"Да что с ним такое? Как будто день или два сыграют большую роль."

"Я и в больнице ничего не делал."

hi "Да, хорошо. Извините."



label ru_A17c:

"Он окидывает меня изучающим взглядом, а затем пожимает плечами, снова улыбаясь."

play music music_nurse fadein 0.5

show nurse neutral_close
with charachange

nk "Хорошо. Вот так-то лучше."

nk "Если ты завтра с утра придёшь на стадион, то встретишься с моим «шпионом», который наверняка не откажет тебе в консультации, если ты захочешь немного побегать."

hi "Консультации?"

show nurse fabulous_close
with charachange

nk "Ещё увидимся."

stop music fadeout 2.0

hide nurse
with charaexit

show bg school_lobby at bgleft 
show rin basic_awayabsent at Alphain(1.0), Slide(0.8,0.5,0.5,0.5,1.0,_ease_time_warp) 
with charamove

"Он уходит без ответа, помахав рукой, а я подхожу к Рин, которая ждёт, праздно оперевшись о стену коридора и разглядывая тусклые светильники на потолке."

"Даже когда я подхожу, она не отводит от них взгляда."

rin "Ты принимаешь лекарства от своей сердечной болячки?"

hi "Ты подслушивала?"

"Мой тон более обвиняющий, чем я планировал, будто я на неё ругаюсь."

"Но, даже пускай и так, я не хочу об этом говорить. Я только что её встретил и не знаю её. Это не её дело."

"Фельдшер, похоже, тоже не знаком с понятием врачебной тайны, раз говорит о таких вещах на людях."

"Но Рин ведь в этом не виновата."

"Я гляжу на неё, внезапно почувствовав укол вины, но Рин лишь задумчиво смотрит куда-то через моё плечо, по-птичьи наклонив голову."

"Эх."

"Не знаю, почему для меня это так сложно. Такое чувство, что у меня в голове есть какой-то непонятный сдерживающий механизм, который не позволяет мне говорить об этом более откровенно."

hi "…Да. Они для моего сердца."

show rin basic_absent at center 
with charachange

rin "Тебе от них лучше?"

hi "…Нет, не особо."

hi "Просто чуть менее плохо."

"Рин смотрит на меня ещё немного, ничего не говоря и без каких-либо различимых эмоций."

"Я благодарен ей за это. Кажется, я ещё не вполне привык к переменам в моей жизни."

"В больнице с этим было проще, но я ещё не разобрался, как жить «нормальной» жизнью со своим недугом."





label ru_A18:

play music music_soothing fadein 4.0

scene bg school_courtyard
with locationchange

"Мы выходим из главного здания, Рин ведёт меня в сторону общежитий."

scene bg school_dormext_start
with locationchange

"Мы останавливаемся у небольшого клочка зелени перед зданием общежития."

"Оно построено на небольшом возвышении, окружено стеной и несколькими деревьями, которые всем каждый раз приходится обходить. Это, наверное, единственный просчёт в планировке школы."

"Вся стена, сложенная из таких же кирпичей, что и само здание, покрыта своего рода картиной."

"Большая её часть – не более, чем набросок – быстрые мазки, сделанные чёрной и белой красками по серой штукатурке, покрывающей практически всю длину стены, – но некоторые места выглядят более законченными."

"Тут лица людей, ноги и руки. Однако я не могу с уверенностью сказать, что именно изображает картина в целом."

"Стопки чего-то, напоминающего банки с красками, штабелями располагаются на земле вдоль стены."

show rin basic_awayabsent at tworight 
with charachange

rin "Видишь, работа над левой частью едва сдвинулась."

show rin basic_deadpannormal
with charachange

rin "Всё потому, что вчера у меня не было настроения и я сдалась, а взамен пошла медитировать. И тут внезапно настало утро."

show rin negative_spaciness
with charachange

rin "Надо бы мне над ней поработать, но ребята из кружка рисования помогают с фонами и основными поверхностями лишь от случая к случаю – вот в чём проблема."

rin "Легче рисовать большие участки, когда много народу, с руками."

show rin basic_deadpan
with charachange

rin "Им проще дотянуться до верха, и дело идёт быстрее."

"Совсем отходя от прежней темы, она машет рукой… ну, или той её частью, которая у неё есть, чтобы наглядно продемонстрировать, хотя я и так уже всё понял."

"Её белый рукав развевается, и мне приходит в голову мысль, что зрелище могло выйти печальнее, чем получилось."

"Но всё же это заставляет меня чувствовать себя не в своей тарелке, как и практически любое напоминание об… особенностях учеников «Ямаку», которые я получал в течение последних нескольких дней."

"Девушка, конечно, не замечает моих мрачных чувств, как и того, что я перестал её слушать… и продолжает болтать."

rin "…и поэтому я пытаюсь выяснить, есть ли что-то, что нужно выяснять, и выяснить это прежде, чем будет слишком поздно и всякая надежда будет потеряна."

hi "А почему надежда может потеряться?"

show rin basic_awayabsent
with charachange

rin "Потому что краску надо нанести, потом она должна высохнуть, а потом быть закрашена слоем другой краски."

show rin basic_absent
with charachange

rin "На это нужно время."

"Она наконец останавливается, по-видимому думая, что пришла к какому-то логическому заключению."

"Полагаю, лучше начать сначала."

hi "Так, значит, это твой проект? Ты сделала… это?"

show rin basic_deadpan
with charachange

rin "Да. Да."

hi "Всё целиком?"

rin "Да."

hi "Очень здорово. Но…"

"Я запинаюсь, вдруг почувствовав, что забрёл прямо в центр минного поля неполиткорректности."

show rin basic_deadpanamused
with charachange

rin "Всё нормально, можешь сказать это вслух. Может быть, я даже не разозлюсь."

"Я сильно краснею. Даже не знаю, что правильнее будет сказать, если вообще стоит говорить хоть что-то. Однако кажется, что я куда более чувствительный, чем Рин."

"Неловкая ситуация."

show rin basic_deadpansurprised
with charachange

rin "Ты не хочешь спросить?"

hi "…Как ты рисуешь без рук?"

show rin basic_amused
with charachange

rin "Видишь, со мной легко говорить, правда? Рисую ногами."

hi "Я, в общем-то, догадался, но разве это не трудно?"

show rin basic_delight
with charachange

rin "Ты догадлив. Как бы то ни было, думаю, что не трудно. Но, может быть, я просто уже привыкла."

"Я и представить себе не мог, что она может быть художницей, но, вспомнив, как мастерски она управлялась с вилкой, решаю, что и рисование, возможно, не представляет проблем."

"Больше по этому поводу нам сказать нечего."

show rin basic_awayabsent
with charachange

rin "А при свете дня довольно неплохо. Я боялась, что будет выглядеть слишком плоско, но в конце концов оказалось, что нет."

show rin basic_absent
with charachange

rin "Вообще, мне кажется, она довольно интересная. Я хотела посмотреть, как она выглядит при тусклом свете. Как по-твоему, не слишком плоская?"

hi "Э… ну, картины обычно плоские."

show rin basic_deadpan
with charachange

rin "Не в этом смысле плоская. Понимаешь, плоская. Как некоторые люди – без содержимого, без мяса там, где оно должно быть."

rin "Я знаю нескольких девочек, у которых—{w=.5}{nw}"

hi "Ладно, я понял. Но я ничем не могу помочь, потому что не слишком хорошо разбираюсь в искусстве. Я не способен перечислить так уж много художников или специальных терминов."

hi "Так что мне нечего сказать."

show rin relaxed_nonchalant
with charachange

"Рин пожимает плечами, как бы говоря: «Ну, как знаешь», – и смотрит в небо, как будто выискивая там что-то."

rin "Я не думала, что буду сегодня над ней работать, но если ты мне поможешь с красками, то дотемна успею что-нибудь сделать."

show rin basic_awayabsent
with charachange

rin "Я хотела раздобыть галогенную лампу, как на стадионах, но тут нет ни одной."

"Рин быстро привлекает меня к работе, как и %(name_shizune)s. Складывается ощущение, что фестиваль – действительно серьёзное мероприятие, для которого дорога каждая пара рук."

hi "Почему бы и нет? Правда, не знаю, смогу ли я тебе чем-то помочь."

show rin basic_absent
with charachange

rin "Просто посмешиваешь краски, ты это сможешь. Наверное. У тебя есть проблемы с моторикой, как у… ну, знаешь, людей с такими проблемами?"

show rin basic_deadpan
with charachange

rin "Может быть, церебральный паралич?"

hi "Вроде бы нет."

show rin basic_deadpanamused
with charachange

rin "Ясно. Твоя сердечная болячка на это не влияет."

"Ни с того ни с сего она бросает на меня лукавый взгляд."

hi "Никоим образом."

show rin basic_amused
with charachange

rin "Ну, тогда начнём."

hide rin
with charaexit

stop music fadeout 7.0

"И вот она садится на пустой деревянный ящик и совершенно естественным жестом берёт толстую кисть босой правой ногой."

"Я открываю несколько банок и выливаю немного их содержимого в пустые чаши для смешивания."

"Краска густо струится из банки в чашу, как патока."

"Я мешаю их, создавая забавные, гипнотизирующего вида спиральные узоры, которые быстро тают друг в друге, образуя новый однородный цвет."

"Рин приступает к работе, то и дело прося у меня той или иной помощи."

"…"

"Находить разные кисти легко, а вот смешивать краски для получения определённого тона, который эта девушка, вероятно, видит у себя в голове, кажется сущим адом."

"Она хочет точности до последнего миллиметра, прежде чем удовлетворяется, но её инструкции по меньшей мере туманны."

play music music_another fadein 1.0

scene bg mural_start
show rin basic_deadpan_close at tworight 
with locationchange

rin "Добавь пол-ливка зелёного."

show rin negative_spaciness_close
with charachange

"Я приседаю подобрать банку ярко-зелёной краски."

show rin basic_deadpan_close
with charachange

rin "Другого зелёного. Этого зелёного."

show rin negative_spaciness_close
with charachange

"Я аккуратно наливаю немного «другого зелёного» в чашу."

show rin basic_deadpan_close
with charachange

rin "Нет, это почти целый ливок. Больше белого."

rin "А зелёный сюда вообще подойдёт?"

hi "Без понятия. Это же ты у нас художник."

show rin basic_deadpanamused_close
with charachange

"В уголках её губ появляется тень улыбки."

rin "У тебя нет своего мнения?"

hi "Нет, просто не знаю, как будет лучше."

show rin basic_deadpandelight_close
with charachange

rin "Это ничего, потому что я только что поняла, как будет лучше. Добавь ещё белого."

"После этого восклицания я наливаю немного белого в чашу и перемешиваю. Цвет становится чуть-чуть… белее."

show rin basic_deadpanupset_close
with charachange

rin "Так не пойдёт. Он должен быть как… как цвет, когда ты просыпаешься и {b}знаешь{/b}, что ты видел во сне смысл жизни, но не можешь его вспомнить."

rin "Может быть, это жёлтый…"

show rin negative_spaciness_close
with charachange

"…"

"Несмотря на неспособность намешать цвет «смены времён года» или ещё какой-нибудь вздор, который от меня требуется, я наслаждаюсь процессом больше, чем мог ожидать."

stop music fadeout 7.0

scene bg school_dormext_start_ss
with shorttimeskip

"Рождение картины на оштукатуренной стене похоже на чудо."

"Я провожу время между смешиванием красок, сидя на тротуаре и просто созерцая её работу."

"Поначалу возникает чувство, будто я стою у неё над душой, вторгаюсь в интимность акта творчества, но Рин, кажется, нет до этого никакого дела. Наверное, я сам себе надумал, что могу ей помешать."

"От неё исходит совсем иная аура, когда она терпеливо работает над деталями, покрывая слои краски новыми слоями и уверенно двигает ногой вдоль стены, добавляя новые формы."

"Когда мне удаётся добиться приемлемого цвета смеси красок, улыбка, которая при этом возникает на её лице, становится, как ни странно, наградой для меня."

"Не считая редких реплик во время обсуждения смесей, никто из нас подолгу не произносит ни слова."

"И даже эти короткие дискуссии вскоре превращаются в кодовый язык: мы оба придумываем и используем странные импровизированные слова для обозначения разных красок и оттенков."

"Как если бы была какая-то необходимость беречь слова, дыхание и звуки."

window hide

$ renpy.music.set_volume(0.10000000000000001, 0.0, channel='ambient')
play ambient sfx_cicadas fadein 4.0

scene bg school_dormext_half_ni
with Dissolve(4.0)

window show

"Мы задерживаемся здесь до позднего вечера, пока не становится слишком темно, чтобы рисовать."

stop ambient fadeout 3.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
