import pandas as pd

def process_data(data):
    # Create a DataFrame from the entered data
    df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender', 'Diagnosis'])

    # Display general information about the data
    print("\nGeneral information about the data:")
    print(df.info())

    # Calculate the average age of patients
    average_age = df['Age'].mean()
    print(f"\nAverage age of patients: {average_age:.2f} years")

    # Count the number of patients by gender
    gender_counts = df['Gender'].value_counts()
    print("\nNumber of patients by gender:")
    print(gender_counts)

    # Group the data by diagnosis and display the average age for each diagnosis
    diagnosis_grouped = df.groupby('Diagnosis')['Age'].mean()
    print("\nAverage age of patients by diagnosis:")
    print(diagnosis_grouped)

if __name__ == "__main__":
    print("Hello! Enter patient data (type 'exit' for termination):")
    data = []

    while True:
        name = input("Patient's Name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        age = int(input("Patient's Age: "))
        gender = input("Patient's Gender (m/f): ")
        diagnosis = input("Diagnosis: ")

        data.append([name, age, gender, diagnosis])

    if data:
        process_data(data)
    else:
        print("No data entered. The program has terminated.")
