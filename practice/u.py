import os
import numpy as np
import pandas as pd

# ==============================
# Configuration
# ==============================

NUM_SUBJECTS = 1000
FS = 125                 # Sampling frequency (Hz)
DURATION = 60            # seconds
N = FS * DURATION

OUTPUT_DIR = "Synthetic_PPG_Dataset"

os.makedirs(OUTPUT_DIR, exist_ok=True)

master = []

np.random.seed(42)

# ==============================
# Generate Dataset
# ==============================

for sid in range(1, NUM_SUBJECTS + 1):

    subject_id = f"SUB_{sid:05d}"

    age = np.random.randint(18, 80)

    height = np.random.randint(150, 191)

    weight = np.random.randint(45, 121)

    bmi = round(weight / ((height/100)**2), 2)

    pulse = np.random.randint(55, 101)

    # ---------------------------------------
    # Blood Pressure based on age and BMI
    # ---------------------------------------

    sbp = (
        95
        + 0.45*age
        + 0.55*(bmi-22)
        + np.random.normal(0,5)
    )

    dbp = (
        60
        + 0.22*age
        + 0.25*(bmi-22)
        + np.random.normal(0,3)
    )

    sbp = int(np.clip(sbp,90,190))
    dbp = int(np.clip(dbp,55,120))

    if sbp >= 140 or dbp >= 90:
        hypertension = "Yes"
    else:
        hypertension = "No"

    # ---------------------------------------
    # Time
    # ---------------------------------------

    t = np.arange(N) / FS

    f = pulse / 60

    # ---------------------------------------
    # Synthetic PPG waveform
    # ---------------------------------------

    ppg = (
        1.00*np.sin(2*np.pi*f*t)
        + 0.35*np.sin(4*np.pi*f*t)
        + 0.18*np.sin(6*np.pi*f*t)
    )

    # Respiratory modulation

    respiration = 0.12*np.sin(
        2*np.pi*0.25*t
    )

    # Baseline drift

    baseline = 0.30*np.sin(
        2*np.pi*0.05*t
    )

    # White Gaussian Noise

    noise = np.random.normal(
        0,
        0.05,
        N
    )

    raw_ppg = (
        ppg
        + respiration
        + baseline
        + noise
    )

    # ---------------------------------------
    # Save Subject CSV
    # ---------------------------------------

    df = pd.DataFrame({

        "Time_s": t,

        "Raw_PPG": raw_ppg

    })

    df.to_csv(

        os.path.join(
            OUTPUT_DIR,
            f"{subject_id}.csv"
        ),

        index=False

    )

    # ---------------------------------------
    # Master Data
    # ---------------------------------------

    master.append([

        subject_id,

        age,

        height,

        weight,

        bmi,

        pulse,

        sbp,

        dbp,

        hypertension

    ])

# ==============================
# Save Master.csv
# ==============================

master_df = pd.DataFrame(

    master,

    columns=[

        "Subject_ID",

        "Age",

        "Height_cm",

        "Weight_kg",

        "BMI",

        "Pulse",

        "SBP",

        "DBP",

        "Hypertension"

    ]

)

master_df.to_csv(

    os.path.join(
        OUTPUT_DIR,
        "Master.csv"
    ),

    index=False

)

print("Dataset Generation Completed.")
print(f"Subjects Generated : {NUM_SUBJECTS}")
print(f"Location : {OUTPUT_DIR}")