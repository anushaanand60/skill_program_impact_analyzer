import pandas as pd
import os
import random
from datetime import datetime, timedelta

os.makedirs("data", exist_ok=True)

# Seed for reproducibility
random.seed(42)

# ------------------ Programs ------------------
programs = pd.DataFrame([
    {
        "program_name": "PMKVY 4.0",
        "start_date": "2023-01-01",
        "end_date": "2025-01-01",
        "program_type": "Skill Development",
        "implementing_agency": "NSDC",
        "sector": "Retail",
        "training_duration_weeks": 12
    },
    {
        "program_name": "DDUGKY",
        "start_date": "2022-06-01",
        "end_date": "2024-06-01",
        "program_type": "Rural Youth",
        "implementing_agency": "MoRD",
        "sector": "Logistics",
        "training_duration_weeks": 10
    }
])
programs.to_csv("data/programs.csv", index=False)

# ------------------ Locations ------------------
states = ["Delhi", "Bihar", "UP", "Rajasthan", "Maharashtra", "MP", "Chhattisgarh", "Odisha"]
districts = ["North", "East", "South", "West", "Central"]
locations = []
for i in range(50):
    locations.append({
        "state": random.choice(states),
        "district": random.choice(districts),
        "block": f"Block-{i+1}",
        "pincode": str(100000 + i),
        "urban_rural": random.choice(["Urban", "Rural"])
    })
df_locations = pd.DataFrame(locations)
df_locations.to_csv("data/locations.csv", index=False)

# ------------------ Training Centres ------------------
centres = []
for i in range(20):
    centres.append({
        "centre_name": f"Training Centre {i+1}",
        "location_id": random.randint(1, 50),
        "accreditation_status": "Accredited",
        "capacity_per_batch": random.randint(25, 60)
    })
df_centres = pd.DataFrame(centres)
df_centres.to_csv("data/training_centres.csv", index=False)

# ------------------ Beneficiaries ------------------
names = ["Ravi", "Anjali", "Pooja", "Manish", "Karan", "Sneha", "Neha", "Raj", "Suman", "Divya"]
surnames = ["Kumar", "Sharma", "Verma", "Yadav", "Patel", "Gupta", "Thakur"]
genders = ["Male", "Female"]
castes = ["SC", "ST", "OBC", "General"]
edu_levels = ["10th Pass", "12th Pass", "Graduate", "Diploma"]
statuses = ["Completed", "Dropped"]
beneficiaries = []

for i in range(1, 10001):
    full_name = f"{random.choice(names)} {random.choice(surnames)}"
    status = random.choices(statuses, weights=[0.75, 0.25])[0]
    beneficiaries.append({
        "aadhaar_id": str(100000000000 + i),
        "name": full_name,
        "age": random.randint(18, 35),
        "gender": random.choice(genders),
        "caste_category": random.choices(castes, weights=[0.2, 0.1, 0.5, 0.2])[0],
        "education_level": random.choice(edu_levels),
        "mobile": str(9000000000 + i),
        "location_id": random.randint(1, 50),
        "program_id": random.randint(1, 2),
        "centre_id": random.randint(1, 20),
        "enrollment_date": (datetime(2022, 1, 1) + timedelta(days=random.randint(0, 700))).date(),
        "completion_status": status,
        "dropout_reason": "Financial issues" if status == "Dropped" else ""
    })

df_beneficiaries = pd.DataFrame(beneficiaries)
df_beneficiaries.to_csv("data/beneficiaries.csv", index=False)

# ------------------ Employment Outcomes ------------------
employed_ids = random.sample(range(1, 10001), 7000)
employed_data = []
for bid in employed_ids:
    employed_data.append({
        "beneficiary_id": bid,
        "employed": True,
        "employment_type": random.choice(["Wage", "Self"]),
        "employer_name": random.choice(["Flipkart", "Infosys", "TCS", "Local Shop", "Amazon"]),
        "job_role": random.choice(["Associate", "Driver", "Analyst", "Operator"]),
        "salary_monthly": round(random.uniform(10000, 25000), 2),
        "employment_date": (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 150))).date(),
        "job_duration_months": random.randint(6, 24)
    })
df_emp = pd.DataFrame(employed_data)
df_emp.to_csv("data/employment_outcomes.csv", index=False)

# ------------------ Feedback ------------------
feedback_data = []
for i in range(1, 10001):
    sentiment = round(random.uniform(0.3, 0.95), 2)
    rating = random.choices([2, 3, 4, 5], weights=[0.1, 0.2, 0.5, 0.2])[0]
    feedback_data.append({
        "beneficiary_id": i,
        "feedback_text": random.choice(["Very helpful", "Too fast", "Excellent content", "Could be better"]),
        "rating": rating,
        "feedback_date": datetime(2023, 6, random.randint(1, 28), random.randint(9, 18), 0).isoformat(),
        "sentiment_score": sentiment
    })
df_feedback = pd.DataFrame(feedback_data)
df_feedback.to_csv("data/feedback.csv", index=False)

# ------------------ Assessments ------------------
assessments = []
for i in range(1, 10001):
    pre = round(random.uniform(30, 65), 1)
    post = round(pre + random.uniform(10, 25), 1)
    assessments.append({
        "beneficiary_id": i,
        "pre_training_score": pre,
        "post_training_score": post,
        "skill_domain": random.choice(["Retail", "Logistics", "IT", "Data Entry"]),
        "assessment_date": (datetime(2023, 3, 1) + timedelta(days=random.randint(0, 90))).date()
    })
df_assessments = pd.DataFrame(assessments)
df_assessments.to_csv("data/assessments.csv", index=False)

print("✅ Bulk dataset generated with 10,000 rows per table. Ready to load.")