from PIL import Image
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, mean_squared_error, mean_absolute_error, \
    r2_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from catboost import CatBoostClassifier, CatBoostRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Учебная практика Лакизы Александра",
                   page_icon=Image.open("images/page_icon_memoji.png"))
st.title("Сравнительный анализ методов машинного обучения, применяемых "
         "для прогнозирования в задачах регрессии и классификации")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### Привет, меня зовут Александр Лакиза")
    st.markdown("#### Данное веб-приложение является частью моего задания по учебной практике в ИТМО")
with col2:
    st.image(Image.open("images/greeting_memoji.png"), width=200)

st.markdown("[Ссылка на репозиторий](https://github.com/alexanderlakiza/itmo-practice/), "
            "содержащий все материалы по данной практике")

st.markdown("### Почему я выбрал именно эту тему для практики?")
st.markdown("* Мне нравится машинное обучение, поэтому почему бы не повторить основы классического машинного обучения\n"
            "* Все остальные интересные темы разобрали")

st.markdown("### Как я распланировал свою работу?")
st.markdown("1. Сначала я целую неделю ничего не делал __(шучу)__\n"
            "2. Затем я полез искать датасеты, которые используются для задач классификации и регрессии. "
            "Я старался найти датасеты с большим количеством наблюдений\n"
            "3. Дальше я расчехлил свою "
            "[джупитерскую тетрадку](https://github.com/alexanderlakiza/itmo-practice/blob/main/ml_algorithms.ipynb)"
            " и импортировал нужные библиотеки (их оказалось не так много)\n"
            "4. После меня начали терзать мысли о том, что я слишком мало сделал для практики и мне влепят трояк, "
            "тогда мне в голову пришла гениальная идея - запилить этот сайт с помощью [Streamlit]"
            "(https://streamlit.io)\n"
            "5. Я сделал этот сайт, затем красивую презентацию в Канве, а вишенкой на торте стал "
            "15-страничный отчет по ГОСТу")
st.image(Image.open("images/shrug.png"), width=300)

st.markdown("#### Машинное обучение это огромная сфера, которая сейчас развивается как никогда стремительно")
st.image(Image.open("images/ml.jpg"))
st.markdown("Каждый день появляются новые библиотеки, фреймворки. Десятки, а то и сотни разных алгоритмов. "
            "Все их разобрать и понять - практически невозможная задача. Моя тема для практики звучит довольно "
            "объёмно: __Сравнительный анализ методов машинного обучения, применяемых для прогнозирования "
            "в задачах регрессии и классификации__, было бы странно, если б я старался затронуть все алгоритмы, "
            "которые используются в задачах регрессии и классификации, и тогда я решил, а давайте я разберу "
            "самые основы... __классическое машинное обучение__ (забегая вперёд, скажу, что мне оказалось этого мало)")
st.markdown('В итоге я поставил перед собой задачу - __разобрать базовые алгоритмы классического машинного обучения, '
            'которые применяются в задачах регрессии и классификации__. В рамках учебной практики '
            'я слегка затрону теорию, стоящую за этими алгоритмами, протестирую их в "голом виде", а также '
            'постараюсь на этом сайте объяснить их максимально просто')

st.markdown("## Ле гоу")
st.markdown("### Начнём с классификации")

col1, col2 = st.columns(2)
with col1:
    st.markdown("__Классификация__ - предсказание категории объекта.")
    st.markdown("«Разделяет объекты по заранее известному признаку."
                " Носки по цветам, документы по языкам, музыку по жанрам»")
with col2:
    st.image(Image.open("images/class.jpg"), width=200)

st.markdown("###### В качестве алгоритмов классификации для анализа я выбрал следующие:\n"
            "- Логистическая регрессия\n"
            "- k-ближайших соседей (k-NN)\n"
            "- Метод опорных векторов (SVM или SVC)\n"
            "- Наивный Байесовский классификатор\n"
            "- Случайный лес*\n"
            "- Градиентный бустинг*")

st.markdown("#### Логистическая регрессия")
st.image(Image.open("images/log_reg.png"), width=500)
st.markdown('__Логистическая регрессия__ применяется для прогнозирования вероятности возникновения '
            'некоторого события по значениям множества признаков. '
            'Для этого вводится так называемая зависимая переменная $y$, '
            'принимающая лишь одно из двух значений — как правило, это числа 0 (событие не произошло) и 1 '
            '(событие произошло), и множество независимых переменных '
            '(также называемых признаками, предикторами или регрессорами) — вещественных $x_1, x_2, x_3,..., x_n$')
st.markdown('Делается предположение о том, что вероятность наступления события $y = 1$ равна:')
st.latex(r'''{\mathbb  {P}}\{y=1\mid x\}=f(z)''')
st.latex(r'''f(z)={\frac  {1}{1+e^{{-z}}}}''')
st.latex(r''' {\displaystyle z=\theta ^{T}x=\theta _{0}+\theta _{1}x_{1}+\ldots +\theta _{n}x_{n}}''')
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(r"$x$ - вектор-столбец независимых переменных $1, x_1, x_2, ..., x_n$")
with col2:
    st.markdown(r"$\theta$ - вектор-столбец параметров (коэффициентов регрессии) $\theta_0, \theta_1, ..., \theta_n$")
with col3:
    st.markdown(r"$f(z)$ - так называемая логистическая функция (иногда также называемая сигмоидом или "
                r"логит-функцией) (см. картинку выше)")
st.markdown("Так как $y$ принимает лишь значения 0 и 1, то вероятность принять значение 0 равна:")
st.latex(r"{\displaystyle \mathbb {P} \{y=0\mid x\}=1-f(z)=1-f(\theta ^{T}x)}")
st.markdown(r"Нахождение вектора коэффициентов $\theta$ осуществляется с"
            r" помощью __метода максимального правдоподобия__")
st.markdown("После вычисления вероятности отнесения всех объектов к классу 1 выставляется пороговое значение, которое "
            "и определяет разбиение на классы 0 и 1")
st.caption(
    "[Википедия](https://ru.wikipedia.org/wiki/"
    "%D0%9B%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_"
    "%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F)")

st.markdown("#### k-ближайших соседей")
st.image(Image.open("images/k_nn.png"), width=375)
st.markdown("__k-ближайших соседей__ (k-NN) - метрический алгоритм для автоматической классификации объектов")
st.markdown("В случае использования метода для классификации объект присваивается тому классу, который является "
            "наиболее распространённым среди $k$ соседей данного элемента, классы которых уже известны")
st.markdown("Сам алгоритм не скрывает внутри себя никаких сложных математических вычислений. Для каждого объекта "
            "высчитывается расстояние до всех объектов, а затем проверяются классы для $k$ самых ближайших."
            "Возьмём пример с картинки: если у нас параметр $k = 3$, то зелёный кружок становится красным "
            "треугольником, если же параметр $k = 5$, то он должен стать синим квадратиком")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_"
           "k-%D0%B1%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B8%D1%85_%D1%81%D0%BE%D1%81%D0%B5%D0%B4%D0%B5%D0%B9)")

st.markdown("#### Метод опорных векторов")
st.image(Image.open("images/svm.jpg"))
st.markdown("Особым свойством __метода опорных векторов__ является непрерывное уменьшение эмпирической "
            "ошибки классификации и увеличение зазора, поэтому метод также известен как метод "
            "классификатора с максимальным зазором. Основная идея метода — перевод исходных "
            "векторов в пространство более высокой размерности и поиск разделяющей гиперплоскости с "
            "наибольшим зазором в этом пространстве. Две параллельных гиперплоскости строятся по обеим "
            "сторонам гиперплоскости, разделяющей классы. Разделяющей гиперплоскостью будет гиперплоскость, "
            "создающая наибольшее расстояние до двух параллельных гиперплоскостей. Алгоритм основан на допущении, "
            "что чем больше разница или расстояние между этими параллельными гиперплоскостями, "
            "тем меньше будет средняя ошибка классификатора")
st.markdown("__Так много слов, и всё равно ничего не понятно :/__")
col1, col2, col3 = st.columns([2, 3, 3])
with col1:
    st.empty()
with col2:
    st.image(Image.open("images/mind_blowing_memoji.png"), width=300)
with col3:
    st.empty()
st.markdown("Короче говоря, алгоритм пытается найти уравнение гиперплоскости (в случае "
            "'трёх и более'мерного пространства) или прямой (на плоскости), которое разделит пространство наблюдений "
            "с наибольшей точностью (см. на рисунок на выше)")
st.markdown("Математика за ним стоит самая что ни на есть сложная. Кратко о том, что тебе нужно знать:\n"
            "- Алгоритм, как и логистическая регрессия, относится к семейству линейных классификаторов\n"
            "- Пространство наблюдений бывает линейно разделимым и линейно неразделимым. Разумеется, "
            "второй случай куда сложнее\n"
            "- Алгоритм хорошо работает с данными небольшого объема\n"
            "- Алгоритм максимизирует разделяющую полосу, которая, как подушка "
            "безопасности, позволяет уменьшить количество ошибок классификации\n"
            "- Долгое время обучения для больших наборов данных (Я бы сказал __ооочень долгое__)")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4"
           "_%D0%BE%D0%BF%D0%BE%D1%80%D0%BD%D1%8B%D1%85_%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2)")

st.markdown("#### Наивный Байесовский классификатор")
st.image(Image.open("images/naive_bayes.jpg"))
st.markdown("__Наивный Байесовский классификатор__ простой вероятностный классификатор, основанный на применении "
            "теоремы Байеса со строгими (наивными) предположениями о независимости")
st.markdown("Формула Байеса выглядит следующим образом")
st.latex(r"P(A|B) = \frac{P(B|A) * P(A)}{P(B)}")
st.markdown("- $A$ - гипотеза\n"
            "- $B$ - событие, следующее после $A$\n"
            "- $P(A|B)$ - апостериорная вероятность\n"
            "- $P(A)$ - априорная вероятность (вероятность наступления гипотезы $A$ при наступлении события $B$)\n"
            "- $P(B|A)$ - вероятность события $B$ при истинности гипотезы $A$\n"
            "- $P(B)$ - полная вероятность наступления события $B$. Иначе можно представить в виде "
            r"$\sum P(A_i)*P(B|A_i)$")
st.markdown("После хитрых математических манипуляций формула классификации выглядит следующим образом:")
st.latex(r"{\displaystyle {\hat {y}}={\underset {k\in \{1,\ldots ,K\}}{\operatorname {argmax} }}\ "
         r"p(C_{k})\displaystyle \prod _{i=1}^{n}p(x_{i}\mid C_{k}).}")
st.markdown("Кратко я бы резюмировал этот алгоритм так: __чем чаще признак встречается в каком-то классе, тем "
            "больше вероятность того, что наблюдение с этим признаком будет в этом классе__")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/"
           "%D0%9D%D0%B0%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_"
           "%D0%B1%D0%B0%D0%B9%D0%B5%D1%81%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_"
           "%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80)")

st.markdown("#### Дерево решений")
st.image(Image.open("images/dt.jpg"))
st.markdown("Структура __дерева__ представляет собой «листья» и «ветки». "
            "На рёбрах («ветках») дерева решения записаны признаки, от которых зависит целевая функция, "
            "в «листьях» записаны значения целевой функции, а в остальных узлах — признаки, по которым "
            "различаются случаи. Чтобы классифицировать новый случай, надо спуститься по дереву до листа и "
            "выдать соответствующее значение")

col1, col2 = st.columns(2)
with col1:
    st.markdown("Если говорить проще, то оно представляет из себя игру-угадайку, которая задаёт тебе вопросы, а затем "
                "по твоим ответам выдаёт тебе свой ответ. Дерево решений - интуитивно понятный подход к классификации "
                "данных, однако одного дерева может не хватит для точного анализа. Тут нам на помощь "
                "приходят __ансамбли__")
with col2:
    st.image(Image.open("images/shocked_memoji.png"), width=200)
st.markdown("###### Ансамбли деревьев решений именуют себя Случайный лес и Градиентный бустинг")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_"
           "%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9)")

st.markdown("#### Случайный лес (Random Forest)")
st.image(Image.open("images/ran_for.jpg"))
st.markdown("Начнём с того, что такое Бэггинг")
st.markdown('__Бэггинг__ (он же Bootstrap AGGregatING) - агрегирование бутстрап выборок, а если по-русски - '
            'параллельное обучение. В контексте деревьев решений, бэггинг - параллельное обучение $n$-го количества '
            'деревьев. Этот алгоритм получил название __Случайный лес__')
st.markdown("Зафиксируем - алгоритм __случайного леса__ это множество"
            " параллельно и независимо друг от друга обучающихся "
            "деревьев решений, в результате которых получается одно сильное дерево решений")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/Random_forest)")

st.markdown("#### Градиентный бустинг (Gradient Boosting)")
st.image(Image.open("images/gb.jpg"))
st.markdown("###### Мощнейшее оружие, второй и последний всадник древовидного ансамблевого апокалипсиса")
st.markdown("В __бустинге__, в отличие от бэггинга, мы обучаем алгоритмы последовательно, "
            "каждый следующий уделяет особое внимание тем случаям, на которых ошибся предыдущий. А откуда в названии "
            '"градиентный"? А дело в том, что где-то во внутренней кухне этого алгоритма, если быть точнее, при '
            'расчете коэффициентов для нового дерева скрывается градиент и его друган "градиентный'
            ' спуск". Главный плюс градиентного бустинга — неистовая, даже нелегальная в некоторых странах, '
            'точность классификации, которой позавидуют все бабушки у подъезда')
st.caption("[Википедия](https://en.wikipedia.org/wiki/Gradient_boosting)")

st.markdown("### Переходим к регрессии")
col1, col2 = st.columns(2)
with col1:
    st.markdown("__Регрессия__ — предсказание места на числовой прямой")
    st.markdown("«Нарисуй линию вдоль моих точек. Да, это машинное обучение»")
    st.markdown("Регрессия — та же классификация, только вместо категории мы "
                "предсказываем число. Стоимость автомобиля по его пробегу, количество "
                "пробок по времени суток, объем спроса на товар от роста компании и.т.д. На "
                "регрессию идеально ложатся любые задачи, где есть зависимость от времени.")
with col2:
    st.image(Image.open("images/regres.jpg"), width=250)
st.markdown("Регрессию очень любят финансисты и аналитики, она встроена даже в "
            "Excel. Внутри всё работает, опять же, банально: машина тупо пытается нарисовать "
            "линию, которая в среднем отражает зависимость. Правда, в отличии от человека с "
            "фломастером и вайтбордом, делает она это математически точно — считая среднее расстояние "
            "до каждой точки и пытаясь всем угодить")

st.markdown("###### В качестве алгоритмов регрессии для анализа я выбрал следующие (тут будут сюрпризы):\n"
            "- Линейная регрессия\n"
            "- k-ближайших соседей (k-NN)\n"
            "- Метод опорных векторов (SVM или SVR)\n"
            "- Случайный лес*\n"
            "- Градиентный бустинг*")

st.markdown("#### Линейная регрессия")
st.image(Image.open("images/lin_reg.jpg"))
st.markdown("###### Это самые основы... Все мы с неё начинали...")
st.markdown("__Линейная регрессия__ - используемая в статистике регрессионная модель "
            "зависимости одной (объясняемой, зависимой) "
            "переменной $y$ от другой или нескольких других переменных (факторов, регрессоров, независимых "
            "переменных) $x$ с линейной функцией зависимости")
st.markdown(r"Регрессионная модель имеет следующий вид: $y=f(x,b)+\varepsilon ,~E(\varepsilon )$, где $b$ — "
            r"параметры модели, $\varepsilon$  — случайная ошибка модели; называется линейной регрессией, "
            r"если функция регрессии $f(x,b)$ имеет вид:")
st.latex(r"f(x,b)=b_0+b_1 x_1+b_2 x_2+...+b_k x_k")
st.markdown(r"$b_j$ — параметры (коэффициенты) регрессии, $x_j$ — регрессоры (факторы модели), "
            r"$k$ — количество факторов модели")
st.markdown("Коэффициенты линейной регрессии показывают скорость изменения зависимой переменной по данному фактору, "
            "при фиксированных остальных факторах. Параметр $b_0$, при котором нет факторов, называют часто "
            "константой. Формально — это значение функции при нулевом значении всех факторов. "
            "Для аналитических целей удобно считать, что константа — это параметр при «факторе», "
            "равном 1 (или другой произвольной постоянной, поэтому константой называют также и этот «фактор»). "
            "В таком случае, если перенумеровать факторы и параметры исходной модели с учетом этого "
            "(оставив обозначение общего количества факторов — $k$), то линейную функцию регрессии можно "
            "записать в следующем виде, формально не содержащем константу:")
st.latex(r"f(x,b)=b_1 x_1 + b_2 x_2 + \ldots + b_k x_k=\sum^k_{j=1}b_j x_j=x^Tb")
st.markdown("В основе алгоритма нахождения параметров (коэффициентов) линейной регрессии лежит "
            "__метод наименьших квадратов__")
st.markdown("У линейной регрессии есть и более сложные вариации: линейная регрессия с "
            "__L1 регуляризацией (Lasso)__, __L2 (Ridge)__ и __полиномиальная регрессия__. Первые две вещи - это "
            "способы улучшить линейную регрессию путём добавления штрафа в функцию потерь. "
            "__Полиномиальная регрессия__ - вид линейной регрессии, где $y$ равен полиному 2-ой степени и выше. "
            "Это позволяет повысить точность регрессии, но и усложняет её. Тем не менее, для неё работают такие же "
            "принципы, как и для обычной линейной регрессии")
st.image(Image.open("images/linear_example.png"), caption="Пример построения линейной регрессии с разной степенью "
                                                          "полинома")
st.markdown("На картинке выше видно, что чем выше степень полинома, тем лучше кривая описывает положение точек. "
            "(__Пы.Сы.__ Это я в домашке по [машинному обучению](https://github.com/alexanderlakiza/cs493) "
            "сам сделаль)")
st.caption("[Википедия](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F"
           "_%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F)")

st.markdown("#### k-ближайших соседей (не ждали?)")
col1, col2 = st.columns(2)
with col1:
    st.markdown("Вы наверняка в недоумении...")
    st.markdown("Саша, но ведь k-NN же используется для классификации... Да, это алгоритм классификации, но он еще "
                "может использоваться и для регрессии, а ещё и для [кластеризации](https://ru.wikipedia.org/wiki/"
                "%D0%9A%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B9_"
                "%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7) О_о")
with col2:
    st.image(Image.open("images/think.png"), width=200)
st.markdown("Нам же ничто не мешает взглянуть теперь не на классы ближайших к нашему наблюдений, а на их непрерывные "
            "значения целевой переменной и усреднить их. Так и рождается метод __регрессии k-ближайших соседей__. "
            "Так же, как и его старший брат, это довольно лёгкий в понимании и имплементации алгоритм")

st.markdown("#### Метод опорных векторов (Опять ты?!)")
st.markdown("Ты же помнишь, что метод опорных векторов ищет уравнение прямой (гиперплоскости), так зная такое"
            " уравнение, можно и задачи регрессии решать. Алгоритм ещё и использует опорные вектора для минимизации "
            "функции потерь.")
st.markdown('Что? "Как это работает с точки зрения математики?" Не спрашивайте меня, я сомневаюсь, что кто-нибудь '
            'вообще это знает')

st.markdown("#### Случайный лес и Градиентный бустинг (о, и вы тут!)")
st.markdown("Суть собственно проста. Деревья решения могут применяться не только в задачах классификации, "
            "но и в задачах регрессии. Просто в узлах вместо Gini impurity или энтропии Шеннона используется "
            "__дисперсия вокруг среднего__, формула которой выглядит следующим образом:")
st.latex(r"D = \frac{1}{l}\sum_{i = 1}^{l} (y_i - \frac{1}{l}\sum_{i = 1}^{l}y_i)")
st.markdown(" $l$ – число объектов в листе, $y_i$ – значения целевого признака. "
            "Попросту говоря, минимизируя дисперсию вокруг среднего, мы ищем признаки, "
            "разбивающие выборку таким образом, что значения целевого признака в каждом листе примерно равны")
st.markdown("А раз у нас деревья теперь предсказывают и непрерывные значения, значит, лес и градиентный бустинг уже"
            " готовы ворваться в бой")

st.markdown("### Вот мы и разобрали все самые базовые алгоритмы машинного обучения, применяемые в "
            "задачах регрессии и классификации")
col1, col2, col3 = st.columns([2, 3, 3])
with col1:
    st.empty()
with col2:
    st.image(Image.open("images/harmony.png"), caption="Вы преисполнились? Я - да", width=300)
with col3:
    st.empty()

st.markdown("---")
st.markdown('## Моя тема вообще звучит "сравнение моделей...", надо пожалуй теперь показать, как я их сравнил')
st.markdown("##### Я решил, что лучше всего будет сравнить их в полевых условиях, и нашёл для наших алгоритмов аж 4"
            " датасета...")
st.markdown("###### Ссылки на датасеты:\n"
            "* [Датасет для предсказания дохода людей]"
            "(https://www.kaggle.com/wenruliu/adult-income-dataset) (задача классификации)\n"
            "* [Датасет для предсказания выплаты кредита]"
            "(https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset) (задача классификации)\n"
            "* [Датасет для предсказания стоимости бриллиантов]"
            "(https://www.kaggle.com/shivam2503/diamonds) (задача регрессии)\n"
            "* [Датасет для предсказания стоимости домов]"
            "(https://www.kaggle.com/harlfoxem/housesalesprediction/version/1) (задача регрессии)")
st.markdown("###### Ссылка на джупитерскую тетрадку:\n"
            "* [Джупитерская тетрадка]"
            "(https://github.com/alexanderlakiza/itmo-practice/blob/main/ml_algorithms.ipynb) (да ладно?!)")
col1, col2, col3 = st.columns([2, 3, 3])
with col1:
    st.empty()
with col2:
    st.image(Image.open("images/like.png"), width=250)
with col3:
    st.empty()

st.markdown("## Ле гоу №2")
st.markdown("Как хороший дата саентист перед обучением моделей я:\n"
            "- проверил, есть ли пропуски\n"
            "- перепичал строковые категориальные переменные в числовые\n"
            "- проверил dtypes у моих фичей\n"
            "- и пошел показывать миру, на что я способен")
st.markdown("###### Я обучил модели, а как их сравнивать? Ну, можно по времени, а ещё, "
            "разумеется, мне нужны метрики качества...")

st.markdown("##### Сравним сначала по времени обучения алгоритма на данных одного размера")

clf_times_df = pd.DataFrame.from_dict({
    'Алгоритм классификации': ["Логистическая регрессия", "k-NN", "SVM", "Naive Bayes",
                               "Случайный лес", "Градиентный бустинг"],
    '1-ый датасет': [0.445, 0.023, 55.9, 0.064, 4.17, 4.18],
    '2-ой датасет:': [0.232, 0.007, 12.3, 0.011, 5.25, 4.15]
})
st.dataframe(clf_times_df)
st.markdown("###### Самым шустрым стал k-NN")
st.markdown("###### Ансамблевые алгоритмы работают дольше классических, но не так долго, как SVM...")

reg_times_df = pd.DataFrame.from_dict({
    'Алгоритм регрессии': ["Линейная регрессия", "k-NN", "SVM", "Случайный лес", "Градиентный бустинг"],
    '1-ый датасет': [0.018, 0.00278, 8.83, 10.4, 2.24],
    '2-ой датасет': [0.0276, 0.00937, 104, 14.4, 2.7]
})
st.dataframe(reg_times_df)
st.markdown("###### Как и в классификации, ансамбелвые модели работают медленнее")
st.markdown("###### SVM на наборе данных с бриллиантами отработал совсем медленно. Наверное, ему не понравились "
            "категориальные фичи...")

st.markdown("#### Теперь взглянем на результаты метрик, но для начала я расскажу, какие метрики я использовал")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Метрики классификации:\n"
                "- Accuracy\n"
                "- ROC AUC\n"
                "- F-мера")
with col2:
    st.markdown("#### Метрики регрессии:\n"
                "- RMSE\n"
                "- MAE\n"
                "- $R^2$")
st.markdown("### Accuracy")
st.latex(r"Accuracy = \frac{TP + TN}{TP + TN + FP + FN}")
st.markdown("* $TP$ - True Positive (Классификатор верно предсказал единицу)\n"
            "* $TN$ - True Negative (Классификатор верно предсказал ноль)\n"
            "* $FP$ - False Positive (Ошибка 1-го рода или $y_{pred} = 1$, хотя $y_{true} = 0$)\n"
            "* $FN$ - False Negative (Ошибка 2-го рода или $y_{pred} = 0$, хотя $y_{true} = 1$)")
st.markdown("Измеряется от 0 до 1. Чем ближе к 1, тем лучше")

st.markdown("### ROC AUC")
st.markdown("__ROC AUC__ - это площадь под ROC-кривой (Area under ROC-curve)")
st.markdown("ROC кривая - кривая в координатах $FPR$ (False Positive Rate), $TPR$ (True Positive Rate) ")
st.markdown(r"* $FPR =  \frac{FP}{FP + TN}$ (False Positive Rate)")
st.markdown(r"* $TPR = \frac{TP}{TP + FN}$ (True Positive Rate)")
st.markdown("Измеряется от 0 до 1. Чем ближе к 1, тем лучше")

st.markdown("### F-мера (F1 score)")
st.latex(r"F1 = \frac{2 * Precision * Recall}{Precision + Recall}")
st.markdown(r"* $Precision = \frac{TP}{TP + FP}$")
st.markdown(r"* $Recall = \frac{TP}{TP + FN}$ (Recall = True Positive Rate)")
st.markdown("Измеряется от 0 до 1. Чем ближе к 1, тем лучше")

st.markdown("### Root Mean Squared Error (RMSE)")
st.latex(r"RMSE = \sqrt{\frac{1}{n} * \sum_{i=1}^{n} (y_i - \hat{y_i})^2}")
st.markdown(r"* $\hat{y_i}$ - значение целевой переменной, предсказанное регрессией")
st.markdown("* $y_i$ - истинное значение целевой переменной")
st.markdown("* $n$ - количество наблюдений")
st.markdown(r"Измеряется от 0 до $\infty$. Чем ближе к 0, тем лучше (однако стоит учитывать "
            r"истинные значения целевой переменной)")


def rmse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred) ** (1 / 2)


st.markdown("### Mean Absolute Error (MAE)")
st.latex(r"MAE = \frac{1}{n} * \sum_{i=1}^{n} \lvert{y_i - \hat{y_i}\rvert}")
st.markdown(r"Измеряется от 0 до $\infty$. Чем ближе к 0, тем лучше (однако стоит учитывать "
            r"истинные значения целевой переменной)")

st.markdown("### $R^2$")
st.latex(r"R^2 = \frac{\sum (\hat{y_i} - \bar{y})^2}{\sum (y_i - \bar{y})^2}")
st.markdown(r"* $\bar{y}$ - выборочное среднее истинных значений $y$")
st.markdown("Обычно измеряется от 0 до 1, однако может быть и отрицательным (ага, казалось бы $R$ в __квадрате__. "
            "Отрицательное значение говорит о совсем плохой модели регрессии")

st.markdown("## Теперь пообучаем модельки")
st.markdown("#### Начнём с [датасета про доход людей](https://www.kaggle.com/wenruliu/adult-income-dataset)")
st.markdown("Нам надо предсказать зарабатывает ли человек больше 50 тысяч $ в год")


@st.cache(ttl=864000)
def get_dfs():
    adult_df = pd.read_csv('data/adult.csv')
    credit_df = pd.read_csv('data/UCI_Credit_Card.csv')
    diam_df = pd.read_csv('data/diamonds.csv')
    house_df = pd.read_csv('data/kc_house_data.csv')

    credit_df = pd.DataFrame(credit_df.drop("ID", axis=1))
    diam_df = pd.DataFrame(diam_df.drop("Unnamed: 0", axis=1))

    adult_df['income'] = adult_df['income'].map({'<=50K': 0, '>50K': 1})
    adult_df['gender'] = adult_df['gender'].map({'Male': 1, 'Female': 0})

    return adult_df, credit_df, diam_df, house_df


adult_df, credit_df, diam_df, house_df = get_dfs()


@st.cache(ttl=864000)
def prepare_adults(adult_df):
    X = pd.concat(
        [adult_df[['age', 'capital-gain', 'capital-loss', 'fnlwgt', 'educational-num', 'gender', 'hours-per-week']],
         pd.get_dummies(adult_df['workclass'], prefix='work'),
         pd.get_dummies(adult_df['education'], prefix='edu'),
         pd.get_dummies(adult_df['marital-status']),
         pd.get_dummies(adult_df['occupation'], prefix='job'),
         pd.get_dummies(adult_df['relationship']),
         pd.get_dummies(adult_df['race']),
         pd.get_dummies(adult_df['native-country'], prefix='nation')], axis=1)
    y = adult_df['income']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


X_train_adult, X_test_adult, y_train_adult, y_test_adult = prepare_adults(adult_df)
adults_results = {'classifier': ['Log-Reg', 'k-NN', 'SVM', 'Naive-Bayes', 'Random-Forest', 'Grad-Boost'],
                  'accuracy': [],
                  'roc auc': [],
                  'f1': []}


def vis_clf_metrics(ac, ra, f):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='Accuracy', value=ac)
    with col2:
        st.metric(label='ROC AUC', value=ra)
    with col3:
        st.metric(label='F1', value=f)


def plot_cm(cf_matrix, colormap='Blues'):
    fig, ax = plt.subplots()
    ax = sns.heatmap(cf_matrix, annot=True, cmap=colormap, fmt='.0f', )

    ax.set_title('Confusion Matrix\n')
    ax.set_xlabel('\nПредсказанные значения')
    ax.set_ylabel('Истинные значения')

    ax.xaxis.set_ticklabels(['0', '1'])
    ax.yaxis.set_ticklabels(['0', '1'])

    additional_texts = ['(True Negative)', '(False Positive)', '(False Negative)', '(True Positive)']
    for text_elt, additional_text in zip(ax.texts, additional_texts):
        ax.text(*text_elt.get_position(), '\n' + additional_text, color=text_elt.get_color(),
                ha='center', va='top', size=10)

    return fig


def make_clf1_result(ac, ra, f):
    adults_results['accuracy'].append(ac)
    adults_results['roc auc'].append(ra)
    adults_results['f1'].append(f)


@st.cache(ttl=864000)
def log_clf(X_train, X_test, y_train, y_test):
    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    log_reg_preds = log_reg.predict(X_test)
    return (str(round(accuracy_score(y_test, log_reg_preds), 3)), str(round(roc_auc_score(y_test, log_reg_preds), 3)),
            str(round(f1_score(y_test, log_reg_preds), 3)), confusion_matrix(y_test, log_reg_preds))


acc, roc_auc, f1, cm = log_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### Логистическая регрессия")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))


@st.cache(ttl=864000)
def knn_clf(X_train, X_test, y_train, y_test):
    knn_clf = KNeighborsClassifier()
    knn_clf.fit(X_train, y_train)
    preds = knn_clf.predict(X_test)
    return (str(round(accuracy_score(y_test, preds), 3)), str(round(roc_auc_score(y_test, preds), 3)),
            str(round(f1_score(y_test, preds), 3)), confusion_matrix(y_test, preds))


acc, roc_auc, f1, cm = knn_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### k-ближайших соседей")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))


@st.cache(ttl=864000)
def svm_clf(X_train, X_test, y_train, y_test):
    clf = SVC()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    return (str(round(accuracy_score(y_test, preds), 3)), str(round(roc_auc_score(y_test, preds), 3)),
            str(round(f1_score(y_test, preds), 3)), confusion_matrix(y_test, preds))


acc, roc_auc, f1, cm = svm_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### Метод опорных векторов")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))


@st.cache(ttl=864000)
def bayes_clf(X_train, X_test, y_train, y_test):
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    return (str(round(accuracy_score(y_test, preds), 3)), str(round(roc_auc_score(y_test, preds), 3)),
            str(round(f1_score(y_test, preds), 3)), confusion_matrix(y_test, preds))


acc, roc_auc, f1, cm = bayes_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### Наивный Байесовский классификатор")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))


@st.cache(ttl=864000)
def rf_clf(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    return (str(round(accuracy_score(y_test, preds), 3)), str(round(roc_auc_score(y_test, preds), 3)),
            str(round(f1_score(y_test, preds), 3)), confusion_matrix(y_test, preds))


acc, roc_auc, f1, cm = rf_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### Случайный лес")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))


@st.cache(ttl=864000)
def gb_clf(X_train, X_test, y_train, y_test):
    clf = CatBoostClassifier(random_seed=42, verbose=False)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    return (str(round(accuracy_score(y_test, preds), 3)), str(round(roc_auc_score(y_test, preds), 3)),
            str(round(f1_score(y_test, preds), 3)), confusion_matrix(y_test, preds))


acc, roc_auc, f1, cm = gb_clf(X_train_adult, X_test_adult, y_train_adult, y_test_adult)
make_clf1_result(acc, roc_auc, f1)
st.markdown("#### Градиентный бустинг")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm))

st.markdown("##### Сводная таблица по метрикам классификации")
st.table(adults_results)

st.markdown("#### Теперь [датасет с предсказанием выплат по кредиту]"
            "(https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset)")
st.markdown("Здесь нам необходимо предсказать сможет ли клиент выплатить в следующем месяце ежемесячную норму по "
            "кредиту")


@st.cache(ttl=864000)
def prepare_credit(credit_df):
    X = credit_df.drop('default.payment.next.month', axis=1)
    y = credit_df['default.payment.next.month']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


X_train_cre, X_test_cre, y_train_cre, y_test_cre = prepare_credit(credit_df)
credit_results = {'classifier': ['Log-Reg', 'k-NN', 'SVM', 'Naive-Bayes', 'Random-Forest', 'Grad-Boost'],
                  'accuracy': [],
                  'roc auc': [],
                  'f1': []}


def make_clf2_result(ac, ra, f):
    credit_results['accuracy'].append(ac)
    credit_results['roc auc'].append(ra)
    credit_results['f1'].append(f)


acc, roc_auc, f1, cm = log_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### Логистическая регрессия")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

acc, roc_auc, f1, cm = knn_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### k-ближайших соседей")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

acc, roc_auc, f1, cm = svm_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### Метод опорных векторов")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

acc, roc_auc, f1, cm = bayes_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### Наивный Байесовский классификатор")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

acc, roc_auc, f1, cm = rf_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### Случайный лес")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

acc, roc_auc, f1, cm = gb_clf(X_train_cre, X_test_cre, y_train_cre, y_test_cre)
make_clf2_result(acc, roc_auc, f1)
st.markdown("#### Градиентный бустинг")
vis_clf_metrics(acc, roc_auc, f1)
st.pyplot(plot_cm(cm, "flare"))

st.markdown("##### Сводная таблица по метрикам классификации")
st.table(credit_results)

st.markdown("### Теперь перейдём к регрессии")
st.markdown("#### Начнём с [датасета про предсказание стоимости бриллиантов]"
            "(https://www.kaggle.com/shivam2503/diamonds)")


@st.cache(ttl=864000)
def prepare_diamonds(diam_df):
    X = pd.concat([diam_df[['depth', 'table', 'x', 'y', 'z']],
                   pd.get_dummies(diam_df['cut']),
                   pd.get_dummies(diam_df['color']),
                   pd.get_dummies(diam_df['clarity'])], axis=1)
    y = diam_df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


X_train_d, X_test_d, y_train_d, y_test_d = prepare_diamonds(diam_df)
diam_results = {'classifier': ['Lin-Reg', 'k-NN', 'SVM', 'Random-Forest', 'Grad-Boost'],
                'RMSE': [],
                'MAE': [],
                'R^2': []}


def vis_reg_metrics(rm, mae, f):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='RMSE', value=rm)
    with col2:
        st.metric(label='MAE', value=mae)
    with col3:
        st.metric(label='R^2', value=f)


def make_reg1_result(ac, ra, f):
    diam_results['RMSE'].append(ac)
    diam_results['MAE'].append(ra)
    diam_results['R^2'].append(f)


@st.cache(ttl=864000)
def lin(X_train, X_test, y_train, y_test):
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    return (str(round(rmse(y_test, preds), 3)), str(round(mean_absolute_error(y_test, preds), 3)),
            str(round(r2_score(y_test, preds), 3)))


@st.cache(ttl=864000)
def knn_reg(X_train, X_test, y_train, y_test):
    reg = KNeighborsRegressor()
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    return str(round(rmse(y_test, preds), 3)), str(round(mean_absolute_error(y_test, preds), 3)), str(
        round(r2_score(y_test, preds), 3))


@st.cache(ttl=864000)
def svm_reg(X_train, X_test, y_train, y_test):
    reg = SVR()
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    return (str(round(rmse(y_test, preds), 3)), str(round(mean_absolute_error(y_test, preds), 3)),
            str(round(r2_score(y_test, preds), 3)))


@st.cache(ttl=864000)
def rf_reg(X_train, X_test, y_train, y_test):
    reg = RandomForestRegressor(random_state=42)
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    return (str(round(rmse(y_test, preds), 3)), str(round(mean_absolute_error(y_test, preds), 3)),
            str(round(r2_score(y_test, preds), 3)))


@st.cache(ttl=864000)
def gb_reg(X_train, X_test, y_train, y_test):
    reg = CatBoostRegressor(random_seed=42, verbose=False)
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    return (str(round(rmse(y_test, preds), 3)), str(round(mean_absolute_error(y_test, preds), 3)),
            str(round(r2_score(y_test, preds), 3)), preds)


def vis_diam_reg(df, preds):
    X = pd.concat([diam_df[['depth', 'table', 'x', 'y', 'z']],
                   pd.get_dummies(diam_df['cut']),
                   pd.get_dummies(diam_df['color']),
                   pd.get_dummies(diam_df['clarity'])], axis=1)
    y = diam_df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    yyy = [x for _, x in sorted(zip(X_test['x'], preds))]
    xxx = [y for y, _ in sorted(zip(X_test['x'], preds))]

    fig = px.scatter(x=X_test['x'], y=y_test, opacity=0.25,
                     labels=dict(x="Координата X", y="Стоимость"),
                     title="Предсказание стоимость бриллианта с помощью CatBoostRegressor")
    fig.add_traces(go.Scatter(x=xxx, y=yyy, name='Предсказанная<br>стоимость'))
    return fig


rms, mae, r_two = lin(X_train_d, X_test_d, y_train_d, y_test_d)
make_reg1_result(rms, mae, r_two)
st.markdown("#### Линейная регрессия")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = knn_reg(X_train_d, X_test_d, y_train_d, y_test_d)
make_reg1_result(rms, mae, r_two)
st.markdown("#### k-ближайших соседей")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = svm_reg(X_train_d, X_test_d, y_train_d, y_test_d)
make_reg1_result(rms, mae, r_two)
st.markdown("#### Метод опорных векторов")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = rf_reg(X_train_d, X_test_d, y_train_d, y_test_d)
make_reg1_result(rms, mae, r_two)
st.markdown("#### Случайный лес")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two, predictions = gb_reg(X_train_d, X_test_d, y_train_d, y_test_d)
make_reg1_result(rms, mae, r_two)
st.markdown("#### Градиентный бустинг")
vis_reg_metrics(rms, mae, r_two)
st.plotly_chart(vis_diam_reg(diam_df, predictions))
st.markdown("Для задач регрессии довольно трудно построить график, отражающий результаты работы модели. Однако, "
            "смотря на метрики, мы понимаем, что наши модели машинного обучения довольно хорошо справились с задачей")
st.table(diam_results)

st.markdown("#### Последний датасет на сегодня - "
            "[датасет со стоимостью домов](https://www.kaggle.com/harlfoxem/housesalesprediction/version/1)")
st.markdown("Тут всё очевидно, необходимо по характеристике дома предсказать его стоимость")


@st.cache(ttl=864000)
def prepare_houses(house_df):
    X = house_df.drop(['id', 'date', 'price'], axis=1)
    y = house_df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


X_train_h, X_test_h, y_train_h, y_test_h = prepare_houses(house_df)
house_results = {'classifier': ['Lin-Reg', 'k-NN', 'SVM', 'Random-Forest', 'Grad-Boost'],
                 'RMSE': [],
                 'MAE': [],
                 'R^2': []}


def make_reg2_result(ac, ra, f):
    house_results['RMSE'].append(ac)
    house_results['MAE'].append(ra)
    house_results['R^2'].append(f)


def vis_house_reg(df, preds):
    X = df.drop(['id', 'date', 'price'], axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    yyy = [x for _, x in sorted(zip(X_test['sqft_living'], preds))]
    xxx = [y for y, _ in sorted(zip(X_test['sqft_living'], preds))]

    fig = px.scatter(x=X_test['sqft_living'], y=y_test, opacity=0.25,
                     title="Предсказание стоимость жилья с помощью CatBoostRegressor",
                     labels=dict(x="Площадь помещения", y="Стоимость"))
    fig.add_traces(go.Scatter(x=xxx, y=yyy, name='Предсказанная<br>стоимость'))
    return fig


rms, mae, r_two = lin(X_train_h, X_test_h, y_train_h, y_test_h)
make_reg2_result(rms, mae, r_two)
st.markdown("#### Линейная регрессия")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = knn_reg(X_train_h, X_test_h, y_train_h, y_test_h)
make_reg2_result(rms, mae, r_two)
st.markdown("#### k-ближайших соседей")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = svm_reg(X_train_h, X_test_h, y_train_h, y_test_h)
make_reg2_result(rms, mae, r_two)
st.markdown("#### Метод опорных векторов")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two = rf_reg(X_train_h, X_test_h, y_train_h, y_test_h)
make_reg2_result(rms, mae, r_two)
st.markdown("#### Случайный лес")
vis_reg_metrics(rms, mae, r_two)

rms, mae, r_two, predictions = gb_reg(X_train_h, X_test_h, y_train_h, y_test_h)
make_reg2_result(rms, mae, r_two)
st.markdown("#### Градиентный бустинг")
vis_reg_metrics(rms, mae, r_two)
st.plotly_chart(vis_house_reg(house_df, predictions))

st.table(house_results)

st.markdown("### Какие выводы можем сделать?")
st.markdown("* Мне совсем не нравится метод опорных векторов, долгий, результаты плохие показал...")
st.markdown("* Бустинги как всегда впереди планеты всей, но на то они и ансамбли. Хотя лес недалеко отстал "
            "от них")
st.markdown("* В задаче регрессии, где числовых признаков было больше, чем категориальных, k-NN справился лучше "
            "линейной регрессии. Метрический алгоритм он и в Африке метрический алгоритм")
st.markdown("* В одной из двух задач классификации линейные алгоритмы (SVC, Логистическая регрессия) отметили "
            "все наблюдения на тестовой выборке за нули. Это значит, что для таких алгоритм гораздо важнее "
            "правильно подбирать порог отсечения")
st.markdown("* Разумеется, по 2 датасета на классификацию и регрессию совсем мало для полного анализа алгоритмов. "
            "Но в принципе этого хватает, чтобы уловить какие-то признаки каждого из базовых алгоритмов")

st.markdown("##### Фух, вроде всё... Теперь пойду чилить...")
col1, col2, col3 = st.columns([2, 3, 3])
with col1:
    st.empty()
with col2:
    st.image(Image.open("images/love_memoji.png"), caption="From Sanya with <3")
with col3:
    st.empty()
