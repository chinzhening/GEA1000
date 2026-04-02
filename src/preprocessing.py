import pandas as pd

def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data = preprocess_country(data)
    data = preprocess_university(data)
    data = preprocess_gpa(data)
    data = preprocess_na(data)
    data = preprocess_bmi(data)
    data = preprocess_gender(data)
    data = preprocess_sleep(data)

    return data

def preprocess_university(data: pd.DataFrame) -> pd.DataFrame:
    # Map university names to a standardized format
    university_mapping = {
        "NTU Singapore - National Institute of Education": "NIE",
        "Universiti Putra Malaysia": "UPM",
        "University of Malaya": "UM",
        "Universitas Indonesia": "UI",
        "Universitas Gadjah Mada": "UGM",
        "Unviersitas Airlangga": "UA",
        
    }
    data["University"] = data["University"].map(university_mapping).fillna(data["University"])
    return data

def preprocess_country(data: pd.DataFrame) -> pd.DataFrame:
    # Map country names to a standardized format
    country_mapping = {
        "Singapore": "SG",
        "MALAYSIA": "MY",
        "Indonesia": "ID",
    }
    data["Country"] = data["Country"].map(country_mapping).fillna(data["Country"])
    return data

def preprocess_gpa(data: pd.DataFrame) -> pd.DataFrame:
    # use GPA - 1 for singapore universities
    data.loc[data["Country"] == "SG", "GPA"] = data.loc[data["Country"] == "SG", "GPA"] - 1.0

    # remove observations with GPA greater than 4.0
    remove_gpa = data["GPA"] > 4.0
    data = data[~remove_gpa]

    # Print the number of rows dropped
    num_rows_dropped = remove_gpa.sum()
    print(f"Dropped {num_rows_dropped} rows with GPA greater than 4.0")

    return data


def preprocess_na(data: pd.DataFrame) -> pd.DataFrame:
    # Drop rows with missing values in the columns:
    columns_to_check = [
        "PA_Days",
        "VA_Weekly_Days",
        "VA_Daily_Hours",
        "MIA_Weekly_Days",
        "MIA_Daily_Hours",
        "Relaxedness",
        "Hours_Slept",
        "BMI",
        "Fruits"
    ]

    # Print the number of rows dropped
    num_rows_dropped = data.shape[0] - data.dropna(subset=columns_to_check).shape[0]
    print(f"Dropped {num_rows_dropped} rows with missing values in columns: {columns_to_check}")

    data = data.dropna(subset=columns_to_check)

    return data

def preprocess_bmi(data: pd.DataFrame) -> pd.DataFrame:
    # remove all bmi values that are equal to zero
    bmi_zero = data["BMI"] == 0
    data = data[~bmi_zero]

    # Print the number of rows dropped
    num_rows_dropped = bmi_zero.sum()
    print(f"Dropped {num_rows_dropped} rows with BMI equal to zero")

    return data

def preprocess_gender(data: pd.DataFrame) -> pd.DataFrame:
    # Map 1 to M and 2 to F
    gender_mapping = {
        1: "M",
        2: "F"
    }

    data["Gender"] = data["Gender"].map(gender_mapping).fillna(data["Gender"])
    return data

def preprocess_sleep(data: pd.DataFrame) -> pd.DataFrame:
    # Remove outliers in Hours_Slept using the IQR method
    Q1 = data["Hours_Slept"].quantile(0.25)
    Q3 = data["Hours_Slept"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    sleep_outliers = (data["Hours_Slept"] < lower_bound) | (data["Hours_Slept"] > upper_bound)

    print(f"Dropped {sleep_outliers.sum()} rows with outliers in Hours_Slept")
    data = data[~sleep_outliers]

    return data 