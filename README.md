# 📊 Sales Forecasting with Time Series Analysis

A dynamic web app for comparing **ARIMAX** and **LSTM** models to forecast retail sales, built using Streamlit. It enables users to explore trends, compare forecasts, and upload custom datasets for live predictions.

---

## 🔧 Features

- 📈 **Visualize** actual vs predicted sales from ARIMAX and LSTM models  
- ⚙️ **Train LSTM live** with adjustable epochs and learning rate (coming soon)  
- 🧪 **Compare models** side-by-side  
- 📁 **Upload CSVs** to test your own datasets  
- 📦 View trends of exogenous variables: `preco` (price) and `estoque` (stock)  
- 🌍 **Deployable** on [Streamlit Cloud](https://streamlit.io/cloud)  

---

## 📂 Project Structure

```
sales-forecasting/
│
├── app/
│   ├── streamlit_app.py            # Main Streamlit dashboard
│   ├── add_dummy_lstm.py           # Dummy LSTM model (for demo)
│
├── data/
│   └── arimax_forecast_output.csv  # Sample dataset with actual + forecasted values
│
├── models/                         # Folder for saving trained models (if needed)
│
└── README.md
```

---

## 🧪 Sample Dataset Format

Your CSV must include the following columns:

| Column                 | Description                         |
|------------------------|-------------------------------------|
| `date`                 | Date column (YYYY-MM-DD format)     |
| `actual_sales`         | Ground truth sales data             |
| `predicted_sales_arimax` | ARIMAX model forecast             |
| `predicted_sales_lstm`   | LSTM model forecast               |
| `preco`                | Product price                       |
| `estoque`              | Available stock                     |

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/22MH1A4242/sales-forecasting.git
   cd sales-forecasting/app
   ```

2. **Install dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📤 Upload Custom CSV

You can use the sidebar upload to visualize your own dataset. Make sure your CSV includes:

- A `date` column
- `actual_sales`, and optionally forecasts (`predicted_sales_arimax`, `predicted_sales_lstm`)
- Optionally: `preco`, `estoque`

---

## 📈 Live Training (Coming Soon)

- Set **epochs**, **learning rate**, and **hidden units**
- Train LSTM on uploaded data and visualize real-time loss and predictions

---

## 📌 Future Enhancements

- ✅ Exogenous variable visualizations (done)
- ✅ CSV upload support (done)
- 🧠 Live LSTM training
- 🧪 Model performance comparison (RMSE, MAE)
- 📦 Model download/export

---

## 🧠 Built With

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
- [TensorFlow/Keras](https://www.tensorflow.org/) *(for LSTM)*  
- [statsmodels](https://www.statsmodels.org/) *(for ARIMAX)*

---

## 📬 Contact

**Anjali Devi Medapati**  
📧 medapattanjalidevi@gmail.com  
🔗 [GitHub Profile](https://github.com/22MH1A4242)
