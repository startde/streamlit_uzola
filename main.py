
import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from PIL import Image
#data analytics

#Тестирование 1-4
df = pd.read_excel("data/signals1-4.xlsx", engine = 'openpyxl')
table_1 = df['Отклонение от заданного числа импульсов в %']
arr = np.array_split(table_1, 3)
di_1,di_3,di_4 = arr[0], arr[1], arr[2]
di_1.tolist()
di_3.tolist()
di_4.tolist()
modules_mean = {"di_1":statistics.mean(di_1) , "di_3":statistics.mean(di_3), "di_4": statistics.mean(di_4) }
#Создание bar chart
fig = plt.figure(figsize = (4, 5))
plt.bar(list(modules_mean.keys()),
        list(modules_mean.values()),
        color ='green',
        width = 0.4)
plt.title ("Среднее отклонение по модулям в %")

#Тестирование 8
df_2 = pd.read_excel("data/signals8.xlsx", engine = 'openpyxl')
table_2 = df_2['Отклонение от заданного числа импульсов в %']
arr_2 = np.array_split(table_2, 2)
di_1_2,di_3_2= arr_2[0], arr_2[1]
di_1_2.tolist()
di_3_2.tolist()
modules_mean_2 = {"di_1":statistics.mean(di_1_2), "di_3":statistics.mean(di_3_2) }
#Создание bar chart
fig_2 = plt.figure(figsize = (10, 5))
plt.bar(list(modules_mean_2.keys()),
        list(modules_mean_2.values()),
        color ='green',
        width = 0.4)
plt.title ("Среднее отклонение по модулям в %")

#Тестирование 12
df_3 = pd.read_excel("data/signals12.xlsx", engine = 'openpyxl')
table_3 = df_3['Отклонение от заданного числа импульсов в %']
arr_3 = np.array_split(table_3, 3)
di_1_3, di_3_3, di_4_3 = arr_3[0], arr_3[1], arr_3[2]
di_1_3.tolist()
di_3_3.tolist()
di_4_3.tolist()
modules_mean_3 = {"di_1":statistics.mean(di_1_3), "di_3":statistics.mean(di_3_3), "di_4":statistics.mean(di_4_3)}
#Создание bar chart
fig_3 = plt.figure(figsize = (10, 5))
plt.bar(list(modules_mean_3.keys()),
        list(modules_mean_3.values()),
        color ='green',
        width = 0.4)
plt.title ("Среднее отклонение по модулям в %")

#Тестирование 16
df_4 = pd.read_excel("data/signals16.xlsx", engine = 'openpyxl')
table_4 = df_4['Отклонение от заданного числа импульсов в %']
arr_4 = np.array_split(table_4, 2)
arr_4_2 = np.array_split(arr_4[1], 2)
di_1_4, di_3_4, di_4_4 = arr_4[0], arr_4_2[0], arr_4_2[1]
di_1_4.tolist()
di_3_4.tolist()
di_4_4.tolist()
modules_mean_4 = {"di_1":statistics.mean(di_1_4), "di_3":statistics.mean(di_3_4), "di_4":statistics.mean(di_4_4)}
#Создание bar chart
fig_4 = plt.figure(figsize = (10, 5))
plt.bar(list(modules_mean_4.keys()),
        list(modules_mean_4.values()),
        color ='green',
        width = 0.4)
plt.title ("Среднее отклонение по модулям в %")

#Добавление скриншотов
image_1 = Image.open("data/di_1.png")
image_2 = Image.open("data/di_2.png")
image_3 = Image.open("data/di_2_1.png")
image_4 = Image.open("data/di_3.png")
image_5 = Image.open("data/di_4.png")
image_6 = Image.open("data/di_5.png")
image_7 = Image.open("data/ai_1.png")
image_8 = Image.open("data/ai_2.png")
image_9 = Image.open("data/ro_1.png")
image_10 = Image.open("data/axiscada_1.png")
image_11 = Image.open("data/codesys_modbus.png")
#Блок streamlit
st.title ("Отчет о тестировании контроллера UZOLA PRO100")
with st.sidebar:
    selected = option_menu (
    menu_title = "Главное меню",
    options = ["Дискретные входы","Аналоговые входы","Релейные выходы", "Совместимость с AxiScada", "Выводы"],
    #icons = ["house","gear","activity","snowflake","envelope"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)

if selected == "Дискретные входы":
    option = st.selectbox(
    'Выберите тестирование',
    ('4 входа', '8 входов', '12 входов', '16 входов', '32 входа'))
    if option == "4 входа":
            # st.write('You selected:', option)
        st.header('Тестирование четырех входов одновременно')
        # Create a row layout
        txt_1 = st.container()
        c1 = st.container()
        #c1.write("Таблица тестирования четырех входов одновременно")
        with txt_1:
            st.markdown("Были настроены модули DI-321 (1 шт.), DO-321 (1 шт.).")
            st.markdown("Проверена связь по протоколу ModBus.")
            st.markdown("После загрузки некорректной программы ПЛК завис. Ошибку можно было устранить, лишь подключившись по SSH.")
            st.markdown("**Отсутствует кнопка сброса до заводских настроек.**")
            st.markdown("1 – 8 дискретные входы модуля ПЛК могут быть настроены в качестве счетчиков. Далее были добавлены модули DI-321 (2 шт.) для проверки счетных входов ПЛК. "
            "Для проверки были выбраны 3 частоты – 5, 40 и 80 кГц. Для каждой частоты было совершено по 3 пуска – по 420 000 импульсов в каждом пуске. "
            "Итоговое значение на счетном входе должно было равняться 260 000 (в виду ограничения в 1 000 000 импульсов за один пуск на генераторе)")
            st.image(image_1)
        with c1:
            #chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
            #st.area_chart(chart_data)
            st.dataframe(df)
            st.pyplot(fig)
            st.markdown("На каждом модуле не было выявлено проблем при тестировании четырех входов одновременно. Небольшие погрешности появлялись при частоте 80 кГц")
    if option == "8 входов":
        st.header('Тестирование восьми входов одновременно')
        txt_2 = st.container()
        c2 = st.container()
        with txt_2:
            st.markdown("При тестировании двух модулей одновременно (по 4 входа на каждом) периодически стала появляться **следующая ошибка**, "
                        "но на точность подсчета при частотах 5 и 40 кГц она не повлияла. При 80 кГц отклонение составило 0,4%.")
            st.image(image_2, caption = "Ошибка запуска шины CAN")
        with c2:
            #chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
            #st.area_chart(chart_data)
            st.dataframe(df_2)
            st.pyplot(fig_2)
            st.image(image_3, caption = 'Ошибка в подсчете импульсов')
    if option == "12 входов":
        st.header('Тестирование двенадцати входов одновременно')
        txt_3 = st.container()
        c3 = st.container()
        with txt_3:
            st.markdown(
                "При тестировании трех модулей одновременно (по 4 входа на каждом) ошибка “Шина не запущена” стала появляться чаще. "
                "В данной конфигурации тестирования при частотах 40 и 80 кГц вход №3 на первом модуле начал считать с погрешность 75% и 99% соответственно. "
                "На остальных входах подобных отклонений замечено не было. При частоте 80 кГц отклонение на остальных входах модулей выросло, но все равно оставалось на уровне 0,5 -0,9 % ")
            st.image(image_4, caption="Ошибка в подсчете импульсов")
        with c3:
            st.dataframe(df_3)
            st.pyplot(fig_3)
    if option == "16 входов":
        st.header("Тестирование шестнадцати входов одовременно")
        txt_4 = st.container()
        c4 = st.container()
        with txt_4:
            st.markdown(
                "При тестировании трех модулей одновременно (8 входов на первом, по 4 входа на остальных) ошибка “Шина не запущена” не исчезала. "
                "Перестали считать вход №3 на первом модуле и вход №1 на 4 модуле. На частотах 5 и 40 кГц отклонения на остальных входах колебались в районе 1%. "
                "При частоте 80 кГц хуже всех показал себя первый модуль в виду своей загруженности. Далее было проведено еще два тестирования – 3 и 4 модули были по очереди максимально нагружены. "
                "Результат был аналогичен первому модулю – отказ как минимум одного счетного входа, высокие отклонения на остальных входах. ")
            st.image(image_4, caption="Ошибка в подсчете импульсов")
        with c4:
            st.dataframe(df_4)
            st.pyplot(fig_4)
    if option == '32 входа':
        st.header("Тестирование всех дискретных модулей ПЛК")
        st.markdown("Затем было проведено тестирование всех входов дискретных модулей ПЛК и были получены следующие результаты:")
        st.markdown("•	После “горячей” замены модули 230012, 230014, 230007 настраивались несколько минут. В то время как остальным было достаточно до 30 секунд. "
                    "Так же периодически приходилось переводить тумблер в положение “Stop” для того, чтобы продолжить работу, так как замененный модуль не выходил на связь более 5 минут.")
        st.markdown("•	Счетные входы модуля 230012 не всегда работали корректно. При первичном тестировании импульсы считали лишь 2 и 6 входы. "
                    "После некоторого времени было решено протестировать данный модуль еще раз, и счетные входы стали работать корректно. "
                    "Настройки генератора импульсов при этом не менялись.")
        st.markdown("•	Дискретные входы 1-32 работали исправно на всех модулях. Индикация показывала на какие входы подаётся сигнал.")
        st.image(image_6, caption="Ошибка в подсчете импульсов")
        st.markdown("При одновременной работе 7 дискретных модулей некоторые входы не досчитывали до заданного значения. "
                    "При этом при повторном запуске генератора импульсов , входы начинали считать с верных значений. ")
if selected == "Аналоговые входы":
    st.header("Тестирование аналоговых входов")
    st.markdown("Были протестированы два аналоговых модуля 230015, 230018. "
                "Были проверены все аналоговые входы по току и напряжению в соответствующих режимах: ")
    st.markdown("•	измерение напряжения от минус 10 до 10 вольт,")
    st.markdown("•	измерение напряжения от минус 5 до 5 вольт,")
    st.markdown("•	измерение напряжения от 0 до 10 вольт,")
    st.markdown("•	измерение напряжения от 0 до 5 вольт,")
    st.markdown("•	измерение тока от 0 до 20 миллиампер,")
    st.markdown("•	измерение тока от 4 до 20 миллиампер")
    st.markdown("Было замечено, что если входы 1, 4, 5, 8, 9, 12, 13, 16 (измеряют ток и напряжение)  не задействованы, "
                "то “Текущее значение” при настройке на измерение напряжения равняется 2, а при настройке на ток равняется 10.")
    st.markdown("Необходимо замыкать шунтирующий резистор, для того чтобы показания на входе равнялись 0, когда ко входу ничего не подключено.")    
    st.markdown("При подключении реостата или потенциометра к данным входам “Текущее значение” значение становится равным 0.~."
                "Во всех режимах отклонение было в пределах 0.005 – 0.01.")
    st.image(image_7)
    st.markdown("Была проверена одновременная работа 8 входов модулей. Добавлена логика на включение/выключение дискретных выходов в зависимости от напряжения, измеряемых на аналоговых входах. "
                "Ошибок не было обнаружено, программа работала корректно. Горячая замена работает корректно.")
    st.image(image_8, caption = "Код программы")
if selected == "Релейные выходы":
    st.header("Тестирование релейных выходов")
    st.markdown("Был протестирован релейный модуль. Был написан алгоритм срабатывания релейных выходов. "
                "Во время подачи единицы на первый дискретный вход появились искры. "
                "После этого контроллер продолжил работу. "
                "Алгоритм был протестирован, релейные выходы и их индикация срабатывали исправно, задержка на включение релейных выходов практически отсутствовала. ")
    st.markdown("Спустя некоторое время при подаче единицы на второй вход дискретного модуля индикация на модулях стала красной, контроллер отсоединился от Codesys. "
                "После этого “LNK” на всех модулях стала красной,  “RUN” стала мигать зеленым. "
                "Перестала запускаться шина CAN, все модули перестали выходить на связь. На ЦПУ контроллера индикация не свидетельствовала об ошибках. "
                "Модуль перестал реагировать на команду “ADDR” ЦПУ.")
    st.image(image_9, caption = "Ошибка чтения модуля")
if selected == "Совместимость с AxiScada":
    st.header("Тестирование совместимости с AxiScada")
    st.markdown ("Была протестирована связь с AxiScada по протоколу Modbus.")
    st.markdown("Максимальная частота опроса – 1 с.")
    st.markdown("Данные передаются без задержек. Можно записать значения с панели в контроллер. Ошибок не было обнаружено.")    
    st.image (image_10, caption = "Тест совместимости с AxiScada")
    st.image (image_11, caption = "Данные в Codesys")
if selected == "Выводы":
    st.header("Выводы")
    st.markdown("После диагностики неисправности сотрудниками Uzola было выявлено, что на микросхеме перегорел преобразователь CAN.")
    st.markdown("Uzola выслали отремонтированный ЦПУ и “крышку шасси”.")
    st.markdown("Таким образом , можно сделать следующие выводы по модулям ПЛК:")
    st.markdown("•	Дискретные модули работают исправно, но с увеличением нагрузки – количество ошибок и отклонения возрастают. Сотрудникам Uzola не удалось выявить причины ошибок.")
    st.markdown("•	Аналоговые входы работают исправно.")
    st.markdown("•	Релейный модуль работает исправно.")
    st.markdown("•	Связь с AxiScada протестирована по протоколу ModBus – ошибок не обнаружено.")
