import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.datasets import china_smoking

data = china_smoking.load_pandas().data

data = data.reset_index()

data['Location_Group'] = data['Location'].apply(
    lambda x: 'A-R' if x[0].upper() <= 'R' else 'S-Z'
)

plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=data,
    x='smoking_yes_cancer_yes',  # Курящие с раком
    y='smoking_no_cancer_yes',   # Некурящие с раком
    hue='Location_Group',        # Разделение по группам
    palette=['navy', 'crimson'],
    s=80,
    edgecolor='black'
)

plt.title("Курение и рак по регионам Китая", fontsize=14)
plt.xlabel("Курящие с раком (случаев)", fontsize=12)
plt.ylabel("Некурящие с раком (случаев)", fontsize=12)
plt.legend(title="Группа регионов", loc='upper left')
plt.grid(linestyle='--', alpha=0.5)

plt.show()