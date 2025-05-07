import pandas as pd

# Load original large datasets
true_df = pd.read_csv("True.csv")
fake_df = pd.read_csv("Fake.csv")

# Sample a smaller subset (adjust size as needed)
sample_size = 5000

true_sample = true_df.sample(n=min(sample_size, len(true_df)), random_state=42)
fake_sample = fake_df.sample(n=min(sample_size, len(fake_df)), random_state=42)

# Save to smaller CSVs
true_sample.to_csv("True_sample.csv", index=False)
fake_sample.to_csv("Fake_sample.csv", index=False)

print("✅ Sample files saved as 'True_sample.csv' and 'Fake_sample.csv'")