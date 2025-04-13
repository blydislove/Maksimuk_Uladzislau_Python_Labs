import matplotlib.pyplot as plt
from statsmodels.datasets import nile
import pandas as pd

# Загрузка данных
data = nile.load_pandas().data

# Проверка структуры данных
print("Структура данных:\n", data.head())
print("\nДоступные годы:", data['year'].min(), "-", data['year'].max())

# Фильтрация данных (1870–1910)
filtered_data = data[(data['year'] >= 1870) & (data['year'] <= 1910)]

# Если данных за 1870 нет, начинаем с 1871
if filtered_data.empty:
    filtered_data = data[(data['year'] >= 1871) & (data['year'] <= 1910)]

# Построение графика
plt.figure(figsize=(14, 6))
plt.plot(
    filtered_data['year'],
    filtered_data['volume'],
    color='#1f77b4',
    marker='o',
    linestyle='-',
    linewidth=1.5,
    markersize=6,
    label='Сток Нила'
)

# Настройка оформления
plt.title("Динамика стока реки Нил (1870–1910)", fontsize=16)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Объём стока (м³/с)", fontsize=12)
plt.xticks(range(1870, 1911, 5))  # Метки каждые 5 лет
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()