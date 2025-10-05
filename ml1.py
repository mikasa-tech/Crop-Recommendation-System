import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Display first few rows
print("📊 Sample Data:")
print(df.head())

# Features and target
X = df.drop('label', axis=1)  # Features
y = df['label']               # Target

# Split into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy}")

# Confusion Matrix
plt.figure(figsize=(12, 6))
sns.heatmap(pd.crosstab(y_test, y_pred), annot=True, fmt='d', cmap='YlGnBu')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Predict for new input
sample_input = [[60, 50, 50, 20.0, 50.0, 7.0, 100.0]]  # [N, P, K, temperature, humidity, ph, rainfall]
predicted_crop = model.predict(sample_input)

print("\n🧪 Input Data:", sample_input[0])
print("🌱 Recommended Crop:", predicted_crop[0])
