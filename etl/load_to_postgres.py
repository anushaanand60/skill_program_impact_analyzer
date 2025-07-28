import pandas as pd
import psycopg2
import os
from psycopg2 import sql

# --- CONFIG ---
DB_NAME = "skill_impact"
DB_USER = "postgres"
DB_PASSWORD = "pass"
DB_HOST = "localhost"
DB_PORT = "5432"
DATA_DIR = "data"

# --- TABLE CONFIGURATION ---
TABLES = {
    "programs": ["program_name", "start_date", "end_date", "program_type", "implementing_agency", "sector", "training_duration_weeks"],
    "locations": ["state", "district", "block", "pincode", "urban_rural"],
    "training_centres": ["centre_name", "location_id", "accreditation_status", "capacity_per_batch"],
    "beneficiaries": ["aadhaar_id", "name", "age", "gender", "caste_category", "education_level", "mobile", "location_id", "program_id", "centre_id", "enrollment_date", "completion_status", "dropout_reason"],
    "employment_outcomes": ["beneficiary_id", "employed", "employment_type", "employer_name", "job_role", "salary_monthly", "employment_date", "job_duration_months"],
    "feedback": ["beneficiary_id", "feedback_text", "rating", "feedback_date", "sentiment_score"],
    "assessments": ["beneficiary_id", "pre_training_score", "post_training_score", "skill_domain", "assessment_date"]
}

def load_table(file_path, table, columns, cursor):
    print(f"\n📥 Loading: {file_path} → {table}")
    if not os.path.exists(file_path):
        print(f"❌ CSV not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    success, failed = 0, 0

    for i, row in df.iterrows():
        try:
            values = tuple(row[col] for col in columns)
            placeholders = ', '.join(['%s'] * len(columns))
            insert_stmt = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                sql.Identifier(table),
                sql.SQL(', ').join(map(sql.Identifier, columns)),
                sql.SQL(placeholders)
            )
            cursor.execute(insert_stmt, values)
            success += 1
        except Exception as e:
            print(f"❌ Row {i+1} FAILED for {table}: {e}")
            failed += 1

    print(f"✅ {success} inserted, ❌ {failed} failed for table: {table}")

def main():
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        for table, cols in TABLES.items():
            csv_path = os.path.join(DATA_DIR, f"{table}.csv")
            load_table(csv_path, table, cols, cursor)

        conn.commit()
        cursor.close()
        conn.close()
        print("\n🎉 All operations completed.")

    except Exception as e:
        print(f"❌ Database connection/load failed: {e}")

if __name__ == "__main__":
    main()