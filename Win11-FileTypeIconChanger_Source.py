from typing import Dict, Any
import winreg as reg
import re, os

langs: Dict[str, Any] = {
	"eng": {
		'instruction':         "Welcome to the application for semi-manually changing icons of file extension types/formats! \nI've sometimes had difficulties with the fact that most project files in the working directory are displayed as <unrecognized> or <other> file types.\nThis application is designed, of course, not as a panacea, but still partially solve the problem! \nHow it works: You write the format of the file to which you want to declare an icon, for example - .py .js .java .cpp .json and others.\nAnd in the second line write the path to the file, for example - C\\Users\\Your user name\\Documents\\Code\\JavaScript\\JScript\\icon-js.ico (you can with quotes, which happens with the standard <copy as path>)\nVuala! Everything works, as long as the icons don't overlap the applications you configured as <open always through>.\nIf there are any errors, try to fix them. You may still have to dig into the case manually :(\n But I hope you don't have to! Thank you for using my app.\n",
		'input':              ["File extension/format:", "Path to new icon file:"],
		'success':            ["Icon for files with extension",  "successfully changed!", "A computer restart will be required to apply system variable changes*"],
		'errorNotFound':      ["Error: File type",               "not found in registry :("],
		'errorNotPermissions': "Error: Insufficient permissions to modify registry. Run application as administrator!",
		'errorOther':          "There's been some kind of unforeseen error! Here are details:"
	},
	"ukr": {
		'instruction':         "Вітаємо в додатку для напів-ручної зміни іконок типів розширень/форматів файлів!\nІнколи під час роботи в мене виникали труднощі, пов'язані з тим, що більшість файлів проєкту в робочій директорії відображаються як <не розпізнані> або <інші> типи файлів.\nЦей застосунок створений, звісно не як панацея, але все ж таки частково розв'язати проблему! \nЯк це працює: Ви пишете формат файлу, якому хочете оголосити іконку, наприклад - .py .js .java .cpp .json тощо.\nА у другому рядку вписуєте шлях до файлу, наприклад - C\\Users\\Ім'я вашого користувача\\Documents\\Code\\JavaScript\\icon-js.ico (можна в лапках, що відбувається за умови стандартного <копіювати як шлях>)\nВуаля! Все працює, тільки якщо іконки не перекрили додатки, які ви налаштували як <відкривати завжди через>. \nЯкщо трапляються якісь помилки, спробуйте їх виправити. Можливо, вам все ж доведеться копатися в регістрі вручну :(\n Але сподіваюся, у вас до цього не дійде! Спасибі що використовуєте мій додаток.\n",
		'input':              ["Розширення/формат файлу:", "Шлях до файлу нової іконки:"],
		'success':            ["Іконка для файлів із розширенням",  "успішно змінена!", "Для застосування змін системних змінних потрібен перезапуск комп'ютера*"],
		'errorNotFound':      ["Помилка: Тип файлу",                "не знайдено в реєстрі :("],
		'errorNotPermissions': "Помилка: Недостатньо прав для зміни реєстру. Запустіть додаток від імені адміністратора!",
		'errorOther':          "Сталася якась непередбачена помилка! Ось її подробиці:"
	},
	"zho": {
		'instruction':         "欢迎使用半手动更改文件扩展类型/格式图标的应用程序！\n我有时会遇到这样的困难：工作目录中的大多数项目文件都显示为<未识别>或<其他>文件类型。 \n当然，这个应用程序并不是万能的，但还是可以部分地解决这个问题！ \n它是如何工作的：你写一个你想要声明图标的文件格式，例如--.py .js .java .java .cpp .json 和其他。\n在第二行中，你要写入文件的路径，例如 - C\\Users\\您的用户名\\Documents\\Code\\JavaScript\\icon-js.ico （你可以使用倒逗号，这在标准的 <复制为路径> 中会出现）！如果有任何错误，请尝试修复。不过我希望不会出现这种情况！感谢您使用我的应用程序。\n",
		'input':              ["文件扩展名/格式:", "新图标文件的路径:"],
		'success':            ["扩展名为",       "的文件图标 成功更改!", "需要重新启动计算机才能应用系统变量更改*"],
		'errorNotFound':      ["错误：文件类型",  "在注册表中找不到 :("],
		'errorNotPermissions': "错误：修改注册表的权限不足。以管理员身份运行应用程序",
		'errorOther':          "发生了一些意外错误！详情如下:"
	},
	"hin": {
		'instruction':         "एक्सटेंशन प्रकार/फ़ाइल प्रारूपों के अर्ध-मैन्युअल रूप से बदलने वाले आइकन के लिए एप्लिकेशन में आपका स्वागत है!\nकभी-कभी मुझे इस तथ्य के कारण काम करते समय कठिनाइयों का सामना करना पड़ता था कि कार्यशील निर्देशिका में अधिकांश प्रोजेक्ट फ़ाइलें <अज्ञात> या <अन्य> फ़ाइल प्रकारों के रूप में प्रदर्शित होती थीं .\nयह एप्लिकेशन निश्चित रूप से रामबाण के रूप में नहीं बनाया गया था, लेकिन यह अभी भी समस्या को आंशिक रूप से हल करता है!\nयह कैसे काम करता है: आप वह फ़ाइल प्रारूप लिखते हैं जिसमें आप एक आइकन घोषित करना चाहते हैं, उदाहरण के लिए - .py .js .java .cpp .json और अन्य।\nऔर दूसरी पंक्ति में फ़ाइल का पथ दर्ज करें, उदाहरण के लिए - C\\Users\\आपका उपयोगकर्ता नाम\\Documents\\Code\\JavaScript\\icon-js.ico (आप उद्धरणों का उपयोग कर सकते हैं, जो मानक <पथ के रूप में कॉपी करें>) के साथ होता है)\nवोइला! सब कुछ तभी काम करता है जब आइकन उन एप्लिकेशन को ओवरलैप नहीं करते हैं जिन्हें आपने <हमेशा ओपन थ्रू> के रूप में कॉन्फ़िगर किया है।\nयदि कोई त्रुटि होती है, तो उन्हें ठीक करने का प्रयास करें। आपको अभी भी रजिस्टर को मैन्युअल रूप से खोदना पड़ सकता है :(\nलेकिन मुझे आशा है कि यह उस तक नहीं पहुंचेगा! मेरे एप्लिकेशन का उपयोग करने के लिए धन्यवाद।\n",
		'input':              ["फ़ाइल एक्सटेंशन/प्रारूप:", "नई आइकन फ़ाइल का पथ:"],
		'success':            ["",                 "एक्सटेंशन वाली फ़ाइलों का आइकन सफलतापूर्वक बदल दिया गया है!", "सिस्टम वेरिएबल्स में परिवर्तन लागू करने के लिए आपको अपने कंप्यूटर को पुनरारंभ करना होगा*"],
		'errorNotFound':      ["त्रुटि: फ़ाइल प्रकार", "रजिस्ट्री में नहीं मिला :("],
		'errorNotPermissions': "त्रुटि: रजिस्ट्री को संशोधित करने के लिए अपर्याप्त अधिकार. एप्लिकेशन को व्यवस्थापक के रूप में चलाएँ!",
		'errorOther':          "कुछ अप्रत्याशित त्रुटि हुई है! यहां इसका विवरण दिया गया है"
	},
	"spa": {
		'instruction':         "Bienvenido a la aplicación para cambiar semi-manualmente los iconos de los tipos/formatos de extensión de archivos! \nA veces he tenido dificultades con el hecho de que la mayoría de los archivos de proyecto en el directorio de trabajo se muestran como <no reconocidos> u <otros> tipos de archivo.\nEsta aplicación está diseñada, por supuesto, no como una panacea, ¡pero aún así resuelve parcialmente el problema! \nCómo funciona: Usted escribe el formato de archivo al que desea declarar el icono, por ejemplo - .py .js .java .cpp .json y otros.\nY en la segunda línea escriba la ruta al archivo, por ejemplo - C\\Users\\Su nombre de usuario\\Documents\\Code\\JavaScript\\icon-js.ico (puede con comillas, lo que sucede con el estándar <copy as path>)\n¡Vuala! Todo funciona, siempre y cuando los iconos no se superpongan a las aplicaciones que configuraste como <abrir siempre a través de>.\nSi se produce algún error, intenta solucionarlo. Puede que todavía tenga que indagar en el caso manualmente :(\n¡Pero espero que no llegue a eso! Gracias por usar mi aplicación.\n",
		'input':              ["Extensión/formato de archivo:", "Ruta de archivo del nuevo icono:"],
		'success':            ["Icono para archivos con extensión",  "cambiado con éxito!", "Será necesario reiniciar el ordenador para aplicar los cambios en las variables del sistema*"],
		'errorNotFound':      ["Error: Tipo de archivo",             "no encontrado en el registro :("],
		'errorNotPermissions': "Error: Permisos insuficientes para modificar el registro. Ejecute la aplicación como administrador!",
		'errorOther':          "Se ha producido un error inesperado. Aquí están los detalles:"
	},
	"ara": {
		'instruction':         "مرحباً بكم في تطبيق لتغيير أيقونات أنواع/تنسيقات امتدادات الملفات بشكل شبه يدوي! \nلقد واجهت أحياناً مشكلة في حقيقة أن معظم ملفات المشروع في دليل العمل يتم عرضها على أنها <غير معترف بها> أو <غير ذلك> من أنواع الملفات.\nهذا التطبيق مصمم بالطبع ليس حلاً سحرياً للمشكلة ولكنه يحل المشكلة جزئياً! \nكيفية العمل: تكتب تنسيق الملف الذي تريد الإعلان عن الأيقونة، على سبيل المثال - .py .js .java .cpp .json وغيرها.\nوفي السطر الثاني اكتب المسار إلى الملف، على سبيل المثال - C\\Users\\اسم المستخدم الخاص بك\\Documents\\Code\\JavaScript\\con-js.ico (يمكنك ذلك مع علامات الاقتباس، وهو ما يحدث مع <copy as path> القياسي)\nفيما يلي! كل شيء يعمل، طالما أن الأيقونات لا تتداخل مع التطبيقات التي قمت بتكوينها كـ <مفتوحة دائمًا من خلال>.\nإن كان هناك أي أخطاء، حاول إصلاحها. قد لا يزال يتعين عليك البحث في الحالة يدويًا : \nلكن آمل ألا يصل الأمر إلى ذلك! شكراً لاستخدامك تطبيقي\n",
		'input':              ["امتداد الملف/التنسيق:", "مسار ملف الأيقونة الجديد:"],
		'success':            ["تم التغيير بنجاح!",     "أيقونة للملفات ذات الامتداد", "ستكون هناك حاجة إلى إعادة تشغيل الكمبيوتر لتطبيق تغييرات متغير النظام*"],
		'errorNotFound':      ["غير موجود في السجل :(", "خطأ: نوع الملف"],
		'errorNotPermissions': "خطأ: الأذونات غير كافية لتعديل السجل. قم بتشغيل التطبيق كمسؤول",
		'errorOther':          "حدث خطأ غير متوقع! فيما يلي التفاصيل:"
	},
	"pol": {
		'instruction':         "Witam w aplikacji do pół-ręcznej zmiany ikon typów/formatów rozszerzeń plików! \nCzasami miałem problem z tym, że większość plików projektu w katalogu roboczym jest wyświetlana jako <nierozpoznane> lub <inne> typy plików.\nTa aplikacja została zaprojektowana, oczywiście, nie jako panaceum, ale jednak częściowo rozwiązuje problem! \nJak to działa: wpisujesz format pliku, do którego chcesz zadeklarować ikonę, na przykład - .py .js .java .cpp .json i inne.\nA w drugiej linii wpisujesz ścieżkę do pliku, na przykład - C\\Users\\Nazwa użytkownika\\Documents\\Code\\JavaScript\\icon-js.ico (możesz z cudzysłowami, co dzieje się ze standardowym <copy as path>).\nVuala! Wszystko działa, o ile ikony nie nakładają się na aplikacje skonfigurowane jako <otwieraj zawsze przez>.\nJeśli występują jakieś błędy, spróbuj je naprawić. Być może nadal będziesz musiał ręcznie zagłębić się w sprawę :(\n Ale mam nadzieję, że do tego nie dojdzie! Dziękuję za korzystanie z mojej aplikacji.\n",
		'input':              ["Rozszerzenie/format pliku:", "Nowa ścieżka pliku ikony:"],
		'success':            ["Ikona dla plików z rozszerzeniem",  "została pomyślnie zmieniona!", "W celu zastosowania zmian zmiennych systemowych wymagane będzie ponowne uruchomienie komputera*"],
		'errorNotFound':      ["Błąd: Typ pliku",                   "nie został znaleziony w rejestrze :("],
		'errorNotPermissions': "Błąd: Niewystarczające uprawnienia do modyfikacji rejestru. Uruchom aplikację jako administrator",
		'errorOther':          "Wystąpił jakiś nieoczekiwany błąd! Oto szczegóły:"
	},
	"bel": {
		'instruction':         "Вітаем у дадатку для паў-ручной змены абразкоў тыпаў пашырэнняў/фарматаў файлаў!\nЧасам пры працы ў мяне ўзнікалі цяжкасці, звязаныя з тым што большасць файлаў праекту ў працоўнай дырэкторыі\nадлюстроўваюцца як <не апазнаныя> ці <іншыя> тыпы файлаў.\nГэта прыкладанне створана, вядома не як панацэя, але ўсё ж часткова вырашыць праблему!\nЯк гэта працуе: Вы пішыце фармат файла, якому жадаеце абвясціць абразок, напрыклад - .py .js .java .cpp .json і іншыя. упісваеце шлях да файла, напрыклад - C\\Users\\Імя вашага карыстальніка\\Documents\\Code\\JavaScript\\icon-js.ico (можна з двукоссямі, што адбываецца пры стандартным <капіяваць як шлях>)\nВуаля! Усё працуе, толькі калі абразкі не перакрылі прыкладанні якія вы наладзілі як <адкрываць заўсёды праз>.\nКалі адбываюцца нейкія памылкі, паспрабуйце іх выправіць. Магчыма, вам усё ж давядзецца капацца ў рэгістры ўручную :(\n Але спадзяюся ў вас да гэтага не дойдзе! Дзякуй што выкарыстоўваеце мой дадатак.\n",
		'input':              ["Пашырэнне/фармат файла:", "Шлях да файла новага абразка:"],
		'success':            ["Абразок для файлаў з пашырэннем",  "паспяхова зменена!", "Для ўжывання змен сістэмных зменных запатрабуецца перазапуск кампутара*"],
		'errorNotFound':      ["Памылка: Тып файла",               "не знойдзены ў рэестры :("],
		'errorNotPermissions': "Памылка: Недастаткова правоў для змены рэестра. Запусціце дадатак ад імя адміністратара!",
		'errorOther':          "Адбылася нейкая непрадбачаная памылка! Вось яе падрабязнасці:"
	},
	"kaz": {
		'instruction':         "Кеңейтім түрлерінің/файл пішімдерінің белгішелерін жартылай қолмен өзгертуге арналған қолданбаға қош келдіңіз!\nКейде жұмыс каталогындағы жоба файлдарының көпшілігі <танылмаған> немесе <басқа> файл түрлері ретінде көрсетілетініне байланысты жұмыс кезінде қиындықтар туындады. .\nБұл қолданба, әрине, панацея ретінде жасалған жоқ, бірақ ол әлі де мәселені ішінара шешеді!\nОл қалай жұмыс істейді: Сіз белгішені жариялағыңыз келетін файл пішімін жазасыз, мысалы - .py .js .java .cpp .json және т.б..\nАл екінші жолда файлдың жолын енгізіңіз, мысалы - C\\Users\\Пайдаланушы аты\\Documents\\Code\\JavaScript\\icon-js.ico (стандартты <жол ретінде көшіру> кезінде болатын тырнақшаларды қолдануға болады)\nVoila! Барлығы белгішелер <әрдайым ашық> ретінде конфигурацияланған қолданбалармен қабаттаспаса ғана жұмыс істейді.\nҚателер орын алса, оларды түзетіп көріңіз. Сізге әлі де тізілімге қолмен кіру қажет болуы мүмкін :(\nБірақ олай болмайды деп үміттенемін! Қолданбамды пайдаланғаныңыз үшін рахмет.\n",
		'input':              ["Файл кеңейтімі/пішімі:", "Жаңа белгіше файлына жол:"],
		'success':            ["",                "кеңейтімі бар файлдардың белгішесі сәтті өзгертілді!", "Жүйе айнымалыларына өзгертулерді қолдану үшін компьютерді қайта іске қосу қажет*"],
		'errorNotFound':      ["Қате: Файл түрі", "тізілімде табылмады :("],
		'errorNotPermissions': "Қате: тізілімді өзгертуге құқықтар жеткіліксіз. Қолданбаны әкімші ретінде іске қосыңыз!",
		'errorOther':          "Күтпеген қате орын алды! Міне, оның мәліметтері:"
	},
	"che": {
		'instruction':         "Марша вогӀийла хьо ах куьйга хийцалуш йолу значкаш шуьйрачу тайпанийн/файлийн форматийн приложене!\nЦкъацкъа болх бечу хенахь халонаш хуьлу сан, белхан каталогехь йолу дукхах йолу проектан файлаш\ndisplayed <unrecognized> я <other> файлан тайпанаш санна гойтуш хилар бахьана долуш .\nThis Приложени кхоьллина, хьаха, панацея санна яц, амма цо хӀетте а цхьана декъехь проблема дӀайоккху!\nИза муха болх бо: Ахь яздо хьайна значок дӀакхайкхо лууш йолу файлан формат, масала - . .py .js .java .cpp .json а, кхин а.\nТкъа шолгӀачу могӀанехь файле боьду некъ язбе, масала - C\\Пайдаэцархой\\Хьан лелоран цӀе\\Документаш\\Код\\JavaScript\\icon-js.ico (кавычкаш лело мегар ду, иза стандартца хуьлу <copy as path>)\nVoila! Дерриге а болх беш ду, нагахь санна ахь <always open through> аьлла дӀахӀиттийначу программашна тӀехь значкаш цхьаьна ца нислахь.\nНагахь цхьа а гӀалаташ нислахь, уьш нисдан хьажа. ХӀинца а реестр чу куьйга хьакха дезаш хила тарло :(\nАмма цу тӀе ца кхачаре сатесна ву со! Баркалла хьуна сан приложени лелорна.\n",
		'input':              ["Файлан шуьйралла/формат:", "Керлачу значокийн файле кхачаран некъ:"],
		'success':            ["",                     "шуьйралла йолчу файлашна лерина значок кхиамца хийцина!", "Системан хийцамашна тӀехь хийцамаш бан хьайн компьютер юха дӀайоло еза*"],
		'errorNotFound':      ["ГӀалат: Файлан тайпа", "реестрехь ца карийна :("],
		'errorNotPermissions': "ГӀалат: Реестр хийца бакъонаш ца тоьу. Администраторан даржехь леладе приложени!",
		'errorOther':          "Цхьа дагахь доцу гӀалат даьлла! Кхузахь цуьнан детальш ю:"
	},
	"rus": {
		'instruction':         "Приветствуем в приложении для полу-ручного изменения иконок типов расширений/форматов файлов!\nИногда при работе у меня возникали трудности, связанные с тем что большинство файлов проекта в рабочей директории\nотображаются как <не опознанные> или <прочие> типы файлов.\nЭто приложение создано, конечно не как панацея, но всё же частично решить проблему!\nКак это работает: Вы пишите формат файла, которому хотите объявить иконку, например - .py .js .java .cpp .json и другие.\nА во второй строке вписываете путь к файлу, например - C\\Users\\Имя вашего пользователя\\Documents\\Code\\JavaScript\\icon-js.ico (можно с кавычками, что происходит при стандартном <копировать как путь>)\nВуаля! Всё работает, только если иконки не перекрыли приложения которые вы настроили как <открывать всегда через>.\nЕсли происходят какие то ошибки, попробуйте их исправить. Возможно, вам всё же придётся копаться в регистре вручную :(\n Но надеюсь у вас до этого не дойдет! Спасибо что используете моё приложение.\n",
		'input':              ["Расширение/формат файла:", "Путь к файлу новой иконки:"],
		'success':            ["Иконка для файлов с расширением",  "успешно изменена!", "Для применения изменений системных переменных потребуется перезапуск компьютера*"],
		'errorNotFound':      ["Ошибка: Тип файла",                "не найден в реестре :("],
		'errorNotPermissions': "Ошибка: Недостаточно прав для изменения реестра. Запустите приложение от имени администратора!",
		'errorOther':          "Произошла какая то непредвиденная ошибка! Вот её подробности:"
	},
	"fra": {
		'instruction':         "Bienvenue dans l'application permettant de modifier semi-manuellement les icônes des types/formats d'extension de fichiers !\n J'ai parfois eu des problèmes avec le fait que la plupart des fichiers de projet dans le répertoire de travail sont affichés en tant que <non reconnus> ou <autres> types de fichiers.\nCette application n'est bien sûr pas une panacée, mais elle résout quand même partiellement le problème ! \nComment ça marche : Vous écrivez le format de fichier dans lequel vous voulez déclarer l'icône, par exemple - .py .js .java .cpp .json et autres.\nEt dans la deuxième ligne écrivez le chemin vers le fichier, par exemple - C\\Users\\Votre nom d'utilisateur\\Documents\\Code\\JavaScript\\icon-js.ico (vous pouvez avec des guillemets, ce qui se produit avec le standard <copy as path>)\nVuala ! Tout fonctionne, tant que les icônes ne chevauchent pas les applications que vous avez configurées comme <ouvertes toujours à travers>.\nSi des erreurs surviennent, essayez de les corriger. Il se peut que vous deviez encore creuser l'affaire manuellement :(\n- Mais j'espère que vous n'en arriverez pas là ! Merci d'avoir utilisé mon application.\n",
		'input':              ["Extension/format du fichier:", "Chemin du fichier de la nouvelle icône:"],
		'success':            ["Icône pour les fichiers avec l'extension",  "a été modifiée avec succès!", "Un redémarrage de l'ordinateur sera nécessaire pour appliquer les modifications des variables du système*"],
		'errorNotFound':      ["Erreur : Type de fichier",                  "n'est pas trouvé dans le registre :("],
		'errorNotPermissions': "Erreur : Permissions insuffisantes pour modifier le registre. Exécutez l'application en tant qu'administrateur",
		'errorOther':          "Il y a eu une sorte d'erreur inattendue ! Voici les détails:"
	},
	"deu": {
		'instruction':         "Willkommen bei der Anwendung zum halbmanuellen Ändern von Icons für Dateierweiterungstypen/-formate! \nIch hatte manchmal Probleme mit der Tatsache, dass die meisten Projektdateien im Arbeitsverzeichnis als <unerkannte> oder <andere> Dateitypen angezeigt werden.\nDiese Anwendung ist natürlich nicht als Allheilmittel gedacht, aber dennoch löst sie das Problem teilweise! \nWie es funktioniert: Sie schreiben das Dateiformat, zu dem Sie das Icon deklarieren wollen, zum Beispiel - .py .js .java .cpp .json und andere.\nUnd in die zweite Zeile schreiben Sie den Pfad zu der Datei, zum Beispiel - C\\Users\\Ihr Nutzername\\Documents\\Code\\JavaScript\\icon-js.ico (Sie können mit Anführungszeichen, die mit dem Standard <copy as path> passiert)\nVuala! Alles funktioniert, solange sich die Icons nicht mit den Anwendungen überschneiden, die Sie als <Immer öffnen> konfiguriert haben.\nWenn es irgendwelche Fehler gibt, versuchen Sie, sie zu beheben. Es kann sein, dass du noch manuell in die Kiste greifen musst :(\n Aber ich hoffe, dass es nicht dazu kommt! Danke, dass du meine App benutzt.\n",
		'input':              ["Dateierweiterung/Format:", "Neuer Icon-Dateipfad:"],
		'success':            ["Icon für Dateien mit Endung",  "erfolgreich geändert!", "Ein Neustart des Computers ist erforderlich, um die Änderungen der Systemvariablen zu übernehmen*"],
		'errorNotFound':      ["Fehler: Dateityp",             "nicht in der Registry gefunden :("],
		'errorNotPermissions': "Fehler: Unzureichende Berechtigungen zum Ändern der Registrierung. Führen Sie die Anwendung als Administrator aus",
		'errorOther':          "Es ist ein unerwarteter Fehler aufgetreten! Hier sind die Details:"
	},
	"jpn": {
		'instruction':         "",
		'input':              ["ファイル拡張子/フォーマット:", "新しいアイコンファイルのパス:"],
		'success':            ["拡張子",           "正常に変更されました!", "システム変数の変更を適用するには、コンピュータの再起動が必要です。"],
		'errorNotFound':      ["エラー: ファイルタイプ", "レジストリで見つかりません :("],
		'errorNotPermissions': "エラー: レジストリを変更する権限が不足しています。管理者としてアプリケーションを実行してください",
		'errorOther':          "予期せぬエラーが発生しました！以下はその詳細です:"
	},
	"kor": {
		'instruction':         "",
		'input':              ["파일 확장자/형식:", "새 아이콘 파일 경로:"],
		'success':            ["확장자가 있는 파일 아이콘",  "성공적으로 변경되었습니다!", "시스템 변수 변경 사항을 적용하려면 컴퓨터를 다시 시작해야 합니다*"],
		'errorNotFound':      ["오류: 파일 형식",           "레지스트리에서 찾을 수 없습니다 :("],
		'errorNotPermissions': "오류: 레지스트리를 수정할 수 있는 권한이 부족합니다. 관리자 권한으로 애플리케이션을 실행하세요",
		'errorOther':          "예기치 않은 오류가 발생했습니다! 자세한 내용은 다음과 같습니다:"
	},
	"ita": {
		'instruction':         "",
		'input':              ["Estensione/formato del file:", "Nuovo percorso del file icona:"],
		'success':            ["Icona per i file con estensione",  " modificato con successo!", "Per applicare le modifiche alle variabili di sistema sarà necessario riavviare il computer*"],
		'errorNotFound':      ["Errore: Tipo di file",             "non trovato nel registro di sistema :("],
		'errorNotPermissions': "Errore: Autorizzazioni insufficienti per modificare il registro di sistema. Eseguire l'applicazione come amministratore",
		'errorOther':          "Si è verificato un errore imprevisto! Ecco i dettagli:"
	},
	"gre": {
		'instruction':         "",
		'input':              ["Επέκταση/μορφή αρχείου:", "Διαδρομή αρχείου νέου εικονιδίου:"],
		'success':            ["Εικονίδιο για αρχεία με επέκταση",  "άλλαξε με επιτυχία!", "Απαιτείται επανεκκίνηση του υπολογιστή για να εφαρμοστούν οι αλλαγές στις μεταβλητές του συστήματος*"],
		'errorNotFound':      ["Σφάλμα: Τύπος αρχείου",             "δεν βρέθηκε στο μητρώο :("],
		'errorNotPermissions': "Σφάλμα: Ανεπαρκή δικαιώματα για την τροποποίηση του μητρώου. Εκτελέστε την εφαρμογή ως διαχειριστής",
		'errorOther':          "Υπήρξε κάποιο απροσδόκητο σφάλμα! Ακολουθούν οι λεπτομέρειες:"
	},
	"zho trad": {
		'instruction':         "",
		'input':              ["檔案副檔名/格式:", "新圖示檔案路徑:"],
		'success':            ["副檔名為",      "的檔案圖示 成功變更!", "需要重新啟動電腦才能套用系統變數變更*"],
		'errorNotFound':      ["錯誤：檔案類型", "在註冊表中找不到 :("],
		'errorNotPermissions': "錯誤：修改註冊表的權限不足。以管理員身份執行應用程式",
		'errorOther':          "出現了某種意料之外的錯誤！以下是詳細資訊:"
	},
}



def checkLangSettingsFile() -> None:
	if not os.path.exists('.lang'):
		with open('.lang', "w") as file:
			file.write("eng")



def getLangSettings() -> str:
	with open('.lang', "r") as file:
		lang = file.readline().lower()
		return lang if lang in langs else 'eng'



def remove_unwanted_characters(inPut: str = '', dots: bool = True) -> str:
	filtr = r'[^a-zA-Z\\.\\]' if dots else r'[^a-zA-Z\\]'
	filtered = re.sub(filtr, '', inPut, flags=re.UNICODE)
	return filtered



def set_file_icon(lang: str, file_extension: str, icon_path: str) -> None:
	try:
		reg_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, f".{file_extension}", 0, reg.KEY_READ)
		file_class, _ = reg.QueryValueEx(reg_key, "")
		reg.CloseKey(reg_key)

		reg_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, f"{file_class}\\DefaultIcon", 0, reg.KEY_SET_VALUE)
		
		reg.SetValueEx(reg_key, None, 0, reg.REG_SZ, icon_path)
		reg.CloseKey(reg_key)
		
		print(f"{langs[lang]['success'][0]} <{file_extension}> {langs[lang]['success'][1]}\n{langs[lang]['success'][2]}")
		
	except FileNotFoundError:
		print(f"{langs[lang]['errorNotFound'][0]} <{file_extension}> {langs[lang]['errorNotFound'][1]}")
	except PermissionError:
		print(f"{langs[lang]['errorNotPermissions']}")
	except Exception as e:
		print(f"{langs[lang]['errorOther']} {e}")



if __name__ == "__main__":
	checkLangSettingsFile()
	lang = getLangSettings()

	print(langs[lang]['instruction'])

	while True:
		print('\n')
		set_file_icon(lang, remove_unwanted_characters(input(f'{langs[lang]['input'][0]} '), False), remove_unwanted_characters(input(f'{langs[lang]['input'][1]} ')))