import pandas as pd

# Load your gaze data from Excel
df = pd.read_excel(r'C:\Users\aseel\OneDrive - The Pennsylvania State University\Desktop\Laparoscopic data\E1 A validation\Gaze Data 9th of April.xlsx')  # Update 'your_gaze_data.xlsx' with your file path

# Determine the downsampling factor
original_sampling_rate = 49.84
target_sampling_rate = 24.86
downsampling_factor = int(round(original_sampling_rate / target_sampling_rate))

# Downsample the data by selecting every 'downsampling_factor'-th row
downsampled_df = df.iloc[::downsampling_factor]

# Save the downsampled data to a new Excel file
downsampled_df.to_excel('downsampled_gaze_E1 9th of April.xlsx', index=False)  # Update 'downsampled_gaze_data.xlsx' with your desired output file path
