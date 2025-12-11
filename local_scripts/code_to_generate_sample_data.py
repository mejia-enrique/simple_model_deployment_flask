import numpy as np
import pandas as pd

np.random.seed(42)  # For reproducibility

N = 500

# Predictors
education = np.random.randint(0, 4, N)
years_of_experience = np.random.randint(1, 31, N) 
# team_members: Mostly low numbers, but some high numbers
team_members = np.clip(np.random.lognormal(mean=1.0, sigma=1.5, size=N).astype(int), 0, 150)


# Target Variable Income which is a function of features + noise.
base_income = 0 
income_prediction = (
    base_income +
    (education * 9765) +           
    (years_of_experience * 1965) +  
    (team_members * 1346) +       
    np.random.normal(0, 15432, N)   # Noise 
)

# Apply the required range (6K to 250K) and convert to integer
income = np.clip(income_prediction, 8000, 250000).round(0).astype(int)

# Creating dataframe and saving to csv
data = pd.DataFrame({
    'education': education,
    'years_of_experience': years_of_experience,
    'team_members': team_members,
    'income': income
})

# Export
data.to_csv('income_sample_data.csv', index=False)
