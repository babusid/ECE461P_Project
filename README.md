# README
- You will have to download the three zip files of data from here: https://www.kaggle.com/datasets/cdminix/us-drought-meteorological-data
- After you've downloaded the data, unzip the files and place them in the "data" folder. It should be 3 CSV files. They will be very large. Run the data_converter.py script, and it will convert them into a few format that is a bit lighter weight and easier for us to use. Alternatively, use the data_weekly_averaging.ipynb script to average the original Kaggle data to weekly data. 
- Our models are in a notebook titled "regression_experiments2.ipynb" under the models folder. That notebook contains all of our final models as well as our data preprocessing based off of the weekly measurements (non-averaged)
