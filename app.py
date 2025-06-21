import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

st.title("📦 DC Salvage Forecasting App")
st.markdown("Forecast salvage cube volumes for Target Distribution Centers using ARIMA and Prophet models.")

# Load data
@st.cache
def load_data():
    df = pd.read_csv("salvage_data.csv", parse_dates=['week'])
    df = df[(df['DC'] == 'DC123') & (df['Disposition'] == 'Salvage')].copy()
    df.set_index('week', inplace=True)
    df = df.asfreq('W')
    df['Cube'].interpolate(inplace=True)
    return df

df = load_data()
st.subheader("📈 Salvage Volume Time Series")
st.line_chart(df['Cube'])

# Select model
model_choice = st.radio("Choose forecasting model:", ("ARIMA", "Prophet"))

if model_choice == "ARIMA":
    train = df[:-12]['Cube']
    test = df[-12:]['Cube']
    model = ARIMA(train, order=(1, 1, 1)).fit()
    forecast = model.forecast(steps=12)
    forecast.index = test.index

    st.subheader("🔮 ARIMA Forecast (Next 12 Weeks)")
    fig, ax = plt.subplots()
    ax.plot(train[-24:], label='Train')
    ax.plot(test, label='Actual')
    ax.plot(forecast, label='Forecast')
    ax.legend()
    st.pyplot(fig)

elif model_choice == "Prophet":
    prophet_df = df.reset_index()[['week', 'Cube']].rename(columns={'week': 'ds', 'Cube': 'y'})
    m = Prophet(weekly_seasonality=True, yearly_seasonality=True)
    m.fit(prophet_df[:-12])
    future = m.make_future_dataframe(periods=12, freq='W')
    forecast_df = m.predict(future)

    st.subheader("🔮 Prophet Forecast (Next 12 Weeks)")
    fig1 = m.plot(forecast_df)
    st.pyplot(fig1)

    fig2 = m.plot_components(forecast_df)
    st.pyplot(fig2)