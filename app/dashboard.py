import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# --- PostgreSQL connection ---
@st.cache_resource
def get_conn():
    return psycopg2.connect(
        database="skill_impact",
        user="postgres",
        password="pass",  # CHANGE if needed
        host="localhost",
        port="5432"
    )

conn = get_conn()

st.set_page_config(layout="wide")
st.title("📊 Skill Program Impact Analyzer")

# --- Filters (Sidebar) ---
with st.sidebar:
    st.header("🔍 Filters")
    states = pd.read_sql("SELECT DISTINCT state FROM locations ORDER BY state", conn)["state"].tolist()
    programs = pd.read_sql("SELECT DISTINCT program_name FROM programs", conn)["program_name"].tolist()
    selected_state = st.selectbox("Filter by State", ["All"] + states)
    selected_program = st.selectbox("Filter by Program", ["All"] + programs)

# --- Base Query ---
query = """
SELECT b.*, l.state, p.program_name, eo.salary_monthly, eo.employment_type
FROM beneficiaries b
JOIN locations l ON b.location_id = l.location_id
JOIN programs p ON b.program_id = p.program_id
LEFT JOIN employment_outcomes eo ON b.beneficiary_id = eo.beneficiary_id
"""

df = pd.read_sql(query, conn)

# --- Apply Filters ---
if selected_state != "All":
    df = df[df["state"] == selected_state]
if selected_program != "All":
    df = df[df["program_name"] == selected_program]

# --- KPI Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Beneficiaries", len(df))
col2.metric("✅ Completed", df[df["completion_status"] == "Completed"].shape[0])
col3.metric("📉 Dropouts", df[df["completion_status"] == "Dropped"].shape[0])

st.markdown("---")

# --- Gender Distribution ---
if not df.empty:
    st.subheader("🧑‍🤝‍🧑 Gender-wise Participation")
    fig1 = px.histogram(df, x="gender", color="gender", title="Gender Distribution", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

# --- Dropout vs Completion ---
status_counts = df["completion_status"].value_counts().reset_index()
status_counts.columns = ["completion_status", "count"]
fig2 = px.pie(status_counts, names="completion_status", values="count", title="Training Status")
st.subheader("📉 Completion vs Dropout Rate")
st.plotly_chart(fig2, use_container_width=True)

# --- Salary by Program ---
salary_df = df[df["salary_monthly"].notnull()]
if not salary_df.empty:
    avg_salary = salary_df.groupby("program_name")["salary_monthly"].mean().reset_index()
    fig3 = px.bar(avg_salary, x="program_name", y="salary_monthly", title="💰 Average Salary by Program")
    st.subheader("💼 Salary Insights")
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No salary data available for selected filters.")

# --- Completion by Caste ---
st.subheader("📚 Completion Status by Caste Category")
caste_chart = df.groupby(["caste_category", "completion_status"]).size().reset_index(name="count")
fig4 = px.bar(caste_chart, x="caste_category", y="count", color="completion_status", barmode="group")
st.plotly_chart(fig4, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤ using Streamlit + PostgreSQL | Skill Program Impact Analyzer | 2025")