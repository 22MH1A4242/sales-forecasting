import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set Streamlit page config
st.set_page_config(page_title="Sales Forecasting", layout="centered")

# Load data
file_path = '../data/arimax_forecast_output.csv'


if not os.path.exists(file_path):
    st.error(f"❌ File not found at path: {file_path}")
    st.stop()

df = pd.read_csv(file_path)

# Generate proper datetime range if missing
if 'date' not in df.columns or not pd.api.types.is_datetime64_any_dtype(df['date']):
    df['date'] = pd.date_range(start='2016-05-01', periods=len(df), freq='D')
else:
    df['date'] = pd.to_datetime(df['date'])

# Add dummy preco and estoque columns if not present
if 'preco' not in df.columns:
    df['preco'] = np.random.randint(50, 200, size=len(df))
if 'estoque' not in df.columns:
    df['estoque'] = np.random.randint(100, 500, size=len(df))

# Title and instructions
st.title("📊 Sales Forecasting: ARIMAX vs LSTM")
st.caption("Compare actual sales with model forecasts (ARIMAX / LSTM)")

# Show available columns
st.markdown("✅ **Available columns in data:**")
st.json(list(df.columns))

# Forecast model selection
model = st.radio("📌 Choose Forecasting Model:", ["ARIMAX", "LSTM"], horizontal=True)

# Forecast plot
st.subheader("📈 Forecast vs Actual Sales")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['date'], df['actual_sales'], label='Actual Sales', color='blue')

if model == "ARIMAX":
    if 'predicted_sales_arimax' in df.columns:
        ax.plot(df['date'], df['predicted_sales_arimax'], label='ARIMAX Forecast', color='green')
    else:
        st.warning("⚠️ ARIMAX forecast column missing in CSV.")
        st.stop()
elif model == "LSTM":
    if 'predicted_sales_lstm' in df.columns:
        ax.plot(df['date'], df['predicted_sales_lstm'], label='LSTM Forecast', color='orange')
    else:
        st.warning("⚠️ LSTM forecast column missing in CSV.")
        st.stop()

ax.set_title(f"Actual vs {model} Forecasted Sales")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Optional: Show raw data
if st.checkbox("📂 View Raw Data"):
    st.dataframe(df)

# Preco and Estoque trends
st.subheader("📦 Price (preco) and Stock (estoque) Trends")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df['date'], df['preco'], label='Preco (Price)', color='purple')
ax2.plot(df['date'], df['estoque'], label='Estoque (Stock)', color='brown')
ax2.set_title("Preco and Estoque Over Time")
ax2.set_xlabel("Date")
ax2.set_ylabel("Value")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)
# --- New Section: Live LSTM Training ---
st.subheader("🧠 Train LSTM Live (Advanced)")

with st.expander("⚙️ Configure LSTM Training"):
    epochs = st.slider("Epochs", min_value=5, max_value=100, value=20)
    units = st.slider("LSTM Units", min_value=10, max_value=100, value=50)
    look_back = st.slider("Look-back Window", min_value=1, max_value=30, value=7)

if st.button("🚀 Train LSTM Model"):
    from sklearn.preprocessing import MinMaxScaler
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense

    st.info("Training LSTM model...")

    sales_data = df[['actual_sales']].values.astype(float)
    scaler = MinMaxScaler()
    sales_scaled = scaler.fit_transform(sales_data)

    # Create LSTM dataset
    X, y = [], []
    for i in range(look_back, len(sales_scaled)):
        X.append(sales_scaled[i - look_back:i])
        y.append(sales_scaled[i])
    X, y = np.array(X), np.array(y)

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model_lstm = Sequential()
    model_lstm.add(LSTM(units=units, input_shape=(X.shape[1], 1)))
    model_lstm.add(Dense(1))
    model_lstm.compile(loss='mean_squared_error', optimizer='adam')
    history = model_lstm.fit(X, y, epochs=epochs, batch_size=16, verbose=0)

    # Predict
    predictions = model_lstm.predict(X)
    predictions_rescaled = scaler.inverse_transform(predictions)

    df['lstm_live_forecast'] = np.nan
    df['lstm_live_forecast'].iloc[look_back:] = predictions_rescaled[:, 0]

    # Plot
    st.success("✅ LSTM model trained!")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(df['date'], df['actual_sales'], label="Actual Sales", color="blue")
    ax3.plot(df['date'], df['lstm_live_forecast'], label="Live LSTM Forecast", color="red")
    ax3.set_title("Live LSTM Forecast vs Actual")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Sales")
    ax3.legend()
    st.pyplot(fig3)

# --- New Section: CSV Upload Demo ---
st.subheader("📁 Upload Your CSV for Demo")

uploaded_file = st.file_uploader("Upload your sales data CSV", type=["csv"])

if uploaded_file is not None:
    try:
        demo_df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(demo_df.head())
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
