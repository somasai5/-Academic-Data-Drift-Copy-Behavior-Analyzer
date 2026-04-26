import copy
import random
import math
import numpy as np
import pandas as pd


# ---------------- 1. DATA GENERATION ----------------
def generate_data(n):
    data = []
    for i in range(n):
        data.append({
            "id": 1001 + i,
            "marks": random.randint(40, 95),
            "attendance": random.randint(60, 100),
            "scores": [
                random.randint(10, 25),
                random.randint(10, 25)
            ]
        })
    return data


# ---------------- 2. DISPLAY ----------------
def display(title, data):
    print("\n" + "="*60)
    print(title)
    print("="*60)
    df = pd.DataFrame(data)
    print(df)


# ---------------- 3. NORMALIZATION ----------------
def normalize_marks(data):
    marks = [d["marks"] for d in data]
    min_m = min(marks)
    max_m = max(marks)

    for d in data:
        if max_m - min_m == 0:
            d["marks"] = 0
        else:
            d["marks"] = round((d["marks"] - min_m) / (max_m - min_m), 3)
    return data


# ---------------- 4. MUTATION ----------------
def apply_mutation(data, roll_number):
    divisor = roll_number % 3 or 3   # Anti-AI rule

    for i in range(len(data)):
        if i % divisor == 0:   # Personalization
            d = data[i]

            # Required sqrt logic (slightly modified for originality)
            d["marks"] = round(d["marks"] + math.sqrt(d["marks"]), 3)

            # Attendance change
            d["attendance"] += random.randint(3, 8)

            # Nested modification (IMPORTANT)
            d["scores"][0] += random.randint(1, 3)
            d["scores"][1] += random.randint(1, 3)

    return data


# ---------------- 5. MANUAL MEAN (NO NUMPY) ----------------
def manual_mean(data):
    total = 0
    for d in data:
        total += d["marks"]
    return total / len(data)


# ---------------- 6. NUMPY STATS ----------------
def compute_stats(data):
    marks = [d["marks"] for d in data]
    return np.mean(marks), np.median(marks), np.std(marks)


# ---------------- 7. DRIFT ----------------
def compute_drift(original, modified):
    return abs(manual_mean(original) - manual_mean(modified))


# ---------------- 8. PATTERN DETECTION ----------------
def detect_pattern(drift, original_changed):
    threshold = 0.2   # Custom threshold

    if original_changed:
        return "Copy Failure Detected"
    elif drift > threshold:
        return "Critical Drift"
    elif drift > threshold / 2:
        return "Minor Drift"
    else:
        return "Stable Data"


# ---------------- MAIN PROGRAM ----------------

# Step 1: Generate data
data = generate_data(random.randint(10, 15))

# Normalize
data = normalize_marks(data)

# Save original safely
original_before = copy.deepcopy(data)

roll_number = 24110011658

# ORIGINAL
display("ORIGINAL DATA", data)


# -------- SHALLOW COPY --------
shallow_copy = copy.copy(data)
apply_mutation(shallow_copy, roll_number)

display("SHALLOW COPY RESULT", shallow_copy)
display("ORIGINAL AFTER SHALLOW COPY (CHANGED)", data)


# -------- DEEP COPY --------
fresh_data = copy.deepcopy(original_before)

deep_copy = copy.deepcopy(fresh_data)
apply_mutation(deep_copy, roll_number)

display("DEEP COPY RESULT", deep_copy)
display("ORIGINAL AFTER DEEP COPY (UNCHANGED)", fresh_data)


# -------- ANALYSIS --------
mean_val = round(manual_mean(deep_copy), 3)   # Manual (required)
np_mean, np_median, np_std = compute_stats(deep_copy)

drift_val = round(compute_drift(original_before, deep_copy), 3)

print("\nDRIFT VALUE:", drift_val)

print("\nTUPLE OUTPUT (mean, drift, std_dev):")
print((mean_val, drift_val, round(np_std, 3)))


# -------- COPY FAILURE CHECK --------
original_changed = data != original_before


# -------- FINAL CLASSIFICATION --------
result = detect_pattern(drift_val, original_changed)

print("\nFINAL CLASSIFICATION:")
print(result)


# -------- EXPLANATION (MANDATORY) --------
print("\nEXPLANATION:")
print("Shallow copy caused drift because nested lists (scores) are shared.")
print("When scores were modified in shallow copy, original data also changed.")
print("Deep copy created independent objects, so original data remained unchanged.")
# Shallow copy creates a new outer structure but keeps references to nested objects such as lists. When mutation is applied to nested elements like scores, both the shallow copy and original data are affected. This leads to unintended data drift.
