import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt  # Импортируем библиотеку для визуализации

# Загрузка данных
data = pd.read_csv('objects.csv', delimiter=';')

# Отделяем целевую переменную
target = data['Стоимость (т.руб.)']
data = data.drop('Стоимость (т.руб.)', axis=1)

# Разделяем на числовые и категориальные признаки
categorical_cols = ['Район', 'Тип планировки', 'Первый/Последний этаж', 'Наличие агенства', 'Состояние']
numerical_cols = ['Общая площадь (м2)', 'Жилая площадь (м2)', 'Площадь кухни (м2)']

# Кодирование категориальных признаков
categorical = pd.get_dummies(data[categorical_cols], drop_first=True)  # drop_first, чтобы избежать избыточности

# Нормализация числовых признаков
scaler = MinMaxScaler()
numerical = scaler.fit_transform(data[numerical_cols])
numerical = pd.DataFrame(numerical, columns=numerical_cols)  # Восстанавливаем названия столбцов

# Объединение данных
data = pd.concat([numerical, categorical], axis=1)

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Преобразование в тензоры TensorFlow
X_train = tf.convert_to_tensor(X_train, dtype=tf.float32)
X_test = tf.convert_to_tensor(X_test, dtype=tf.float32)
y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
y_test = tf.convert_to_tensor(y_test, dtype=tf.float32)

# Создание модели
inputs = tf.keras.Input(shape=(X_train.shape[1],))  # Используем Input для входного слоя
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Компиляция модели
model.compile(optimizer='adam', loss='mean_squared_error')

# Обучение модели
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))

# Оценка модели
eval_result = model.evaluate(X_test, y_test)
print(f'Оценка модели: {eval_result}')

# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Преобразуем y_test и y_pred в numpy массивы для корректного сравнения
y_test = y_test.numpy()
y_pred = y_pred.flatten()  # Преобразуем в одномерный массив

# Разделение данных на группы выше и ниже идеальной линии
above_line = y_pred > y_test
below_line = y_pred <= y_test

# Построение диаграммы разброса (scatter plot)
plt.figure(figsize=(8, 6))
plt.scatter(y_test[above_line], y_pred[above_line], color='blue', label='Выше линии')  # Точки выше линии
plt.scatter(y_test[below_line], y_pred[below_line], color='green', label='Ниже линии')  # Точки ниже линии
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', label='Идеальная линия')  # Прямая

# Оформление графика
plt.xlabel('Реальная стоимость (т.руб.)')
plt.ylabel('Предсказанная стоимость (т.руб.)')
plt.title('Сравнение реальной и предсказанной стоимости')
plt.grid(True)
plt.legend()
plt.show()

# Предсказание для нового объекта
new_house_data = {
    'Общая площадь (м2)': [100],
    'Жилая площадь (м2)': [80],
    'Площадь кухни (м2)': [20],
    'Район': ['Центр'],  # Пример значений для категориальных признаков
    'Тип планировки': ['Студия'],
    'Первый/Последний этаж': ['Нет'],
    'Наличие агенства': ['Нет'],
    'Состояние': ['Хорошее']
}

# Создаем DataFrame
new_house_df = pd.DataFrame(new_house_data)

# Повторяем обработку данных
new_numerical = scaler.transform(new_house_df[numerical_cols])
new_categorical = pd.get_dummies(new_house_df[categorical_cols], drop_first=True)

# Добавляем недостающие столбцы после get_dummies, если таковые имеются
for col in categorical.columns:
    if col not in new_categorical:
        new_categorical[col] = 0

# Соединяем обработанные данные
new_house_processed = pd.concat([pd.DataFrame(new_numerical, columns=numerical_cols), new_categorical], axis=1)

# Предсказание
new_house_tensor = tf.convert_to_tensor(new_house_processed, dtype=tf.float32)
prediction = model.predict(new_house_tensor)
print(f'Предсказание: {prediction[0][0]}')