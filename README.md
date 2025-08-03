# 🛒 Retail Sales Forecasting App

A user-friendly and interactive Streamlit web app for sales forecasting and customer analysis. Supports both regression (for continuous targets) and classification (for categorical targets) with options to upload custom CSVs, explore visualizations, and make predictions.

## 🚀 Features

- 📂 Upload your own CSV datasets (limit: 200MB)
- 🔧 Choose Target (y) and Feature (X) variables from the UI
- 🤖 Supports **Regression** (e.g., predicting sales amount) and **Classification** (e.g., predicting customer gender)
- 📈 Model training with performance metrics:
  - RMSE, MAE, R² for Regression
  - Accuracy for Classification
- 🔍 Auto-detection of categorical vs numerical targets
- 📊 Data visualization:
  - Seaborn plots (distribution, correlation heatmap)
  - 3D plots for numeric features (e.g., Age vs Income vs Spending Score)
- 🔁 Map encoded target labels back to original names (e.g., 0 → Female)
- 🌐 Deployable on Streamlit Cloud
- 📤 Upload test data and download predictions

---

## 🖥️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Scikit-learn, Pandas, Numpy
- **Visualization**: Matplotlib, Seaborn, Plotly (for 3D)
- **Modeling**: LinearRegression, LogisticRegression

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sales-forecasting.git
   cd sales-forecasting
   ```

2. **Create a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app/streamlit_app.py
   ```

---

## 📂 Sample Dataset

You can use the included sample file:
- [`Mall_Customers.csv`](./data/Mall_Customers.csv)

or upload your own CSV.

---

## 📌 How to Use

1. Upload your dataset.
2. Preview the data and select the target and features from the sidebar.
3. App detects classification vs regression.
4. Model is trained automatically.
5. See evaluation metrics and visualizations.
6. (Optional) Upload test data for predictions.
7. Download results if needed.

---

## 🧪 Example Use Cases

- Predict customer spending or sales based on demographic data
- Classify customers into segments (e.g., gender, age group)
- Analyze trends using uploaded retail datasets

---

## 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and set the entry point to `app/streamlit_app.py`

---

## 👤 Author

**Anjali Devi Medapati**  
📧 medapattanjalidevi@gmail.com  
🔗 [GitHub](https://github.com/22MH1A4242)

---

## 📄 License

This project is open-source and free to use under the MIT License.

