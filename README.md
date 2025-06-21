# 🧠 DC Salvage Forecasting

Forecasting salvage and return-to-vendor (RTV) volumes at Target's Distribution Centers using time series techniques.

## 📌 Project Goal

To build accurate time series models that forecast the cube volume of salvage and RTV items 3 months into the future, supporting reverse logistics planning.

---

## 📁 Repository Structure

```
dc-salvage-forecasting/
│
├── data/
│   ├── salvage_data.csv              # Full dataset
│   ├── salvage_data_train.csv        # Training data (till 2022)
│   └── salvage_data_test.csv         # Testing data (2023)
│
├── notebooks/
│   ├── 01_eda_arima_modeling.ipynb   # EDA + ARIMA baseline model
│   └── 02_model_comparison.ipynb     # ARIMA, SARIMAX, Prophet comparison
│
├── README.md                         # Project overview and instructions
```

---

## 🛠️ Models Implemented

| Model     | When to Use                           | Why It Works Well                    |
|-----------|----------------------------------------|--------------------------------------|
| ARIMA     | Stationary series, no seasonality      | Simple, interpretable                |
| SARIMAX   | Weekly/seasonal effects present        | Captures seasonality, external vars |
| Prophet   | Irregular, multiple seasonalities      | Handles holidays, flexible trends   |
| LSTM*     | Complex, nonlinear patterns            | Neural model, captures long memory  |

> *LSTM implementation is optional and not included in the notebook due to complexity and compute needs.

---

## 📊 Evaluation Metric

- **MAPE** (Mean Absolute Percentage Error) used to compare model performance.

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/dc-salvage-forecasting.git
cd dc-salvage-forecasting
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn statsmodels prophet scikit-learn
```

### 3. Run Notebooks

- `01_eda_arima_modeling.ipynb` for initial data exploration and ARIMA
- `02_model_comparison.ipynb` for comparing ARIMA, SARIMAX, and Prophet

---

## 📞 Contact

For questions or collaboration:
**Nayan Dharviya**  
📧 Nayan.Dharviya@target.com

---

## 📌 Note

This project is a demo built on synthetic data for showcasing forecasting capabilities. Not for production use.
