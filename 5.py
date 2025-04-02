# просто загрузка таблицы из файла
#
import pandas as pd
import streamlit as st

# Задайте путь к файлу CSV
file_path = 'C:/Users/1111/PycharmProjects/pythonStreamlit/train.csv'  # Замените на путь к Вашему файлу

data = pd.read_csv(file_path)

st.write(data)

