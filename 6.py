#итоговый вариант c выбором файла.
import pandas as pd
import streamlit as st

# Заголовок приложения
st.title("Загрузка и отображение данных из CSV")

# Загрузка файла
uploaded_file = st.file_uploader("Выберите файл CSV", type=["csv"])

if uploaded_file is not None:
    # Чтение данных из файла
    data = pd.read_csv(uploaded_file)

    # Выбор колонок для отображения
    columns = st.multiselect("Выберите колонки для отображения", data.columns.tolist(), default=data.columns.tolist())

    # Фильтрация по колонкам VIP, CryoSleep, Transported, HomePlanet
    vip_filter = st.selectbox("Фильтр по VIP", ["Все", "Да", "Нет"])
    cryo_sleep_filter = st.selectbox("Фильтр по CryoSleep", ["Все", "Да", "Нет"])
    transported_filter = st.selectbox("Фильтр по Transported", ["Все", "Да", "Нет"])

    # Фильтрация по HomePlanet
    home_planet_filter = st.selectbox("Выберите домашнюю планету", ["Все"] + data['HomePlanet'].unique().tolist())

    # Фильтрация по Age
    age_min, age_max = st.slider("Выберите диапазон возраста", int(data['Age'].min()), int(data['Age'].max()),
                                 (int(data['Age'].min()), int(data['Age'].max())))

    # Применение фильтров
    filtered_data = data.copy()

    if vip_filter != "Все":
        filtered_data = filtered_data[filtered_data['VIP'] == (vip_filter == "Да")]

    if cryo_sleep_filter != "Все":
        filtered_data = filtered_data[filtered_data['CryoSleep'] == (cryo_sleep_filter == "Да")]

    if transported_filter != "Все":
        filtered_data = filtered_data[filtered_data['Transported'] == (transported_filter == "Да")]

    if home_planet_filter != "Все":
        filtered_data = filtered_data[filtered_data['HomePlanet'] == home_planet_filter]

    filtered_data = filtered_data[(filtered_data['Age'] >= age_min) & (filtered_data['Age'] <= age_max)]

    # Отображение данных
    st.write(filtered_data[columns])
