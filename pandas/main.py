import pandas as pd
import numpy as np
import os
from faker import Faker

# Path to the input folder
input_folder = 'input'

# Create the input folder if it doesn't exist
if not os.path.exists(input_folder):
    os.makedirs(input_folder)

# Function to generate random medical records


def generate_medical_records(num_records):
    fake = Faker()

    data = {
        'PatientID': [fake.uuid4() for _ in range(num_records)],
        'Name': [fake.name() for _ in range(num_records)],
        'Age': [fake.random_int(min=18, max=80) for _ in range(num_records)],
        'Condition': [fake.random_element(elements=('Flu', 'Allergy', 'Broken Arm', 'Headache', 'Diabetes')) for _ in range(num_records)]
    }

    return pd.DataFrame(data)


# Generate 100 random medical records (you can adjust the number as needed)
num_records = 100
medical_records = generate_medical_records(num_records)

# Save the DataFrame to a CSV file in the input folder
input_file_path = os.path.join(input_folder, 'medical_data_input.csv')
medical_records.to_csv(input_file_path, index=False)

print(f"CSV file '{input_file_path}' with random medical data has been generated and placed in the 'input' folder.")
