'''This script is used to convert the raw data into a few formats that are lighter, and can be used by the model.'''


import pandas as pd

print("Reading csvs....")
train = pd.read_csv('train_timeseries.csv')
test = pd.read_csv('test_timeseries.csv')
validation = pd.read_csv('validation_timeseries.csv')
print("Reading complete!")

print("Dropping non-scored rows...")
train_with_score = train.dropna()
train_with_score.to_csv('train_with_raw_score.csv', index=False)
test_with_score = test.dropna()
test_with_score.to_csv('test_with_raw_score.csv', index=False)
validation_with_score = validation.dropna()
validation_with_score.to_csv('validation_with_raw_score.csv', index=False)
print("Dropping complete!")


print("Rounding scores...")
train_with_score['score'] = train_with_score['score'].round().astype(int)
test_with_score['score'] = test_with_score['score'].round().astype(int)
validation_with_score['score'] = validation_with_score['score'].round().astype(int)
train_with_score.to_csv('train_with_rounded_score.csv', index=False)
test_with_score.to_csv('test_with_rounded_score.csv', index=False)
validation_with_score.to_csv('validation_with_rounded_score.csv', index=False)
print("Rounding complete!")

print("Converting scores to binary...")
train_with_score['score'] = train_with_score['score'].astype(bool).astype(int)
test_with_score['score'] = test_with_score['score'].astype(bool).astype(int)
validation_with_score['score'] = validation_with_score['score'].astype(bool).astype(int)
train_with_score.to_csv('train_with_binary_score.csv', index=False)
test_with_score.to_csv('test_with_binary_score.csv', index=False)
validation_with_score.to_csv('validation_with_binary_score.csv', index=False)
print("Conversion complete!")
