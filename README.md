# 🌱 Crop Recommendation System

A machine learning project that recommends the best crop to grow based on soil and environmental conditions using Random Forest Classification.

## 📊 Features

- Predicts optimal crops based on:
  - Nitrogen (N), Phosphorus (P), Potassium (K) levels
  - Temperature, Humidity, pH
  - Rainfall
- Achieves **99.3% accuracy** on test data
- Supports 22 different crop types
- Interactive visualization with confusion matrix

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd ml
```

2. Create a virtual environment:
```bash
python -m venv myenv
```

3. Activate the virtual environment:
```bash
# Windows
myenv\Scripts\activate

# Linux/Mac
source myenv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the main script:
```bash
python ml1.py
```

## 📈 Model Performance

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 99.31%
- **Dataset**: 2200 samples with 7 features
- **Crops Supported**: rice, maize, chickpea, kidneybeans, pigeonpeas, mothbeans, mungbean, blackgram, lentil, pomegranate, banana, mango, grapes, watermelon, muskmelon, apple, orange, papaya, coconut, cotton, jute, coffee

## 🧪 Example Prediction

Input: `[60, 50, 50, 20.0, 50.0, 7.0, 100.0]`
- N: 60, P: 50, K: 50
- Temperature: 20°C, Humidity: 50%
- pH: 7.0, Rainfall: 100mm

**Predicted Crop: Maize** 🌽

## 📁 Project Structure

```
ml/
├── ml1.py                    # Main script with enhanced output
├── Crop_recommendation.csv   # Dataset
├── requirements.txt          # Dependencies
├── README.md                # This file
└── .gitignore               # Git ignore rules
```

## 🛠️ Technologies Used

- **Python 3.13**
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **matplotlib/seaborn**: Data visualization
- **numpy**: Numerical computations

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---
Made with ❤️ for sustainable agriculture