import pandas as pd
import numpy as np

# Load existing CSV
df = pd.read_csv("data/arimax_forecast_output.csv")

# Add dummy LSTM predictions (e.g., ARIMAX + random noise)
np.random.seed(42)
df['predicted_sales_lstm'] = df['predicted_sales_arimax'] + np.random.normal(0, 20, size=len(df))

# Save back to the same file
df.to_csv("data/arimax_forecast_output.csv", index=False)

print("✅ Dummy LSTM predictions added.")
