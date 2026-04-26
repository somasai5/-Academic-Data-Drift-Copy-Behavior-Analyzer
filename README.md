# 📊 Academic Data Drift & Copy Behavior Analyzer

## 📘 Overview

This project analyzes how student academic data behaves when **Shallow Copy** and **Deep Copy** are used in Python.

It demonstrates how improper copying can lead to **data drift** and unintended changes, especially when working with **nested data structures**.

---

## 🎯 Objectives

* Understand shallow vs deep copy behavior
* Work with nested data (list of dictionaries)
* Apply controlled mutation on selected records
* Perform statistical analysis using NumPy and Pandas
* Detect data drift and classify system behavior

---

## 📂 Data Structure

Each student record is stored as:

```python
{
    "id": int,
    "marks": int,
    "attendance": int,
    "scores": [internal, assignment]
}
```

---

## ⚙️ Key Features

* Dynamic data generation (10–15 students)
* Data stored as list of dictionaries (nested)
* Conversion to Pandas DataFrame
* Statistical analysis using NumPy
* Manual mean calculation (without NumPy)
* Controlled mutation using personalization logic
* Drift detection and classification

---

## 🧠 Personalization Logic

```python
divisor = roll_number % 3 or 3
```

Mutation applied only to:

```python
index % divisor == 0
```

---

## 🔧 Mutation Logic

Mutation is applied **only on copied data**.

* **Marks Update:**

  ```python
  marks = marks + sqrt(marks)
  ```

  (rounded to maintain consistency)

* **Attendance Update:**
  Increased using a small random value.

* **Scores Update (Nested List):**
  Both elements in `scores` are incremented using random values.

---

## 🔄 Copy Behavior

### 🔴 Shallow Copy

* Copies only outer structure
* Nested data is shared
* Changes affect original dataset

### 🟢 Deep Copy

* Creates completely independent copy
* No shared references
* Original data remains unchanged

---

## 📊 Analysis Performed

* **Manual Mean** (without NumPy)

* **NumPy Mean, Median, Standard Deviation**

* **Drift Calculation:**

  ```python
  drift = |original_mean - modified_mean|
  ```

* **Normalization:**
  Marks are scaled between 0 and 1 before mutation.

---

## 🚦 Pattern Detection

The system classifies results into:

* **Copy Failure Detected** → Original data changed unexpectedly
* **Critical Drift** → Drift exceeds threshold
* **Minor Drift** → Moderate variation
* **Stable Data** → Minimal variance

---

## 📌 Output Includes

* Original DataFrame
* Shallow copy result
* Original after shallow copy
* Deep copy result
* Original after deep copy
* Drift value
* Tuple → `(mean, drift, std_dev)`
* Final classification

---

## 🧾 Key Observation

Shallow copy caused unintended data drift because nested lists (`scores`) were shared between original and copied data.

Deep copy avoided this issue by creating fully independent objects.

---

## ▶️ How to Run

```bash
python main.py
```

---

## 👨‍💻 Author

**SomaSaish Kona**
Register Number: 24110011658

---

## 📌 Note

This project uses controlled mutation, personalization logic, and statistical analysis to ensure originality and demonstrate clear differences between shallow and deep copy behavior.
