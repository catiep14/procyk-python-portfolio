import pandas as pd

# Load original files
true_df = pd.read_csv("True.csv")
fake_df = pd.read_csv("Fake.csv")

# Take a sample of each (adjust n as needed)
true_sample = true_df.sample(n=1000, random_state=42)
fake_sample = fake_df.sample(n=1000, random_state=42)

# Save the samples
true_sample.to_csv("True_sample.csv", index=False)
fake_sample.to_csv("Fake_sample.csv", index=False)

print("Sample files created.")