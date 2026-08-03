import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# CSS Load
def load_css():
    css_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "assets",
        "style.css"
    )

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page Settings (YE YAHAN HOGA)
st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Apply
load_css()
# ==========================
# PAGE SETTINGS
# ==========================

st.markdown("""
<h1 style='font-size:50px;'>
🤖 AI Data Analysis Assistant
</h1>
<p style='font-size:20px;color:#B0B0B0'>
Analyze • Visualize • Predict • Download Reports
</p>
""", unsafe_allow_html=True)
st.write("Analyze your CSV data easily.")

# ==========================
# LOAD CSV
# ==========================

uploaded_file = st.file_uploader(
    "📂 Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

else:
    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    csv_path = os.path.join(
        BASE_DIR,
        "data",
        "sales_data.csv"
    )

    df = pd.read_csv(csv_path)

# ==========================
# DATASET
# ==========================

st.subheader("📋 Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# ==========================
# SMART DASHBOARD
# ==========================

st.header("📊 Smart Dashboard")

# Safety check
if 'filtered_df' not in locals():
    filtered_df = df

c1, c2, c3, c4 = st.columns(4)

c1.metric("Employees", len(filtered_df))
c2.metric("Average Salary", f"₹ {filtered_df['Salary'].mean():,.0f}")
c3.metric("Highest Salary", f"₹ {filtered_df['Salary'].max():,.0f}")
c4.metric("Lowest Salary", f"₹ {filtered_df['Salary'].min():,.0f}")
# ==========================
# DATASET INFO
# ==========================

st.subheader("📑 Dataset Information")

st.write("Rows :", df.shape[0])
st.write("Columns :", df.shape[1])
st.write("Column Names :")
st.write(df.columns.tolist())

st.divider()
# ==========================
# CHARTS
# ==========================

st.header("📈 Data Visualization")

col1, col2 = st.columns(2)

# --------------------------
# BAR CHART
# --------------------------
with col1:
    st.subheader("Department Wise Average Salary")

    dept_salary = df.groupby("Department")["Salary"].mean()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(dept_salary.index, dept_salary.values)
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Salary")
    ax.set_title("Average Salary by Department")

    st.pyplot(fig)

# --------------------------
# PIE CHART
# --------------------------
with col2:
    st.subheader("Employees by Department")

    dept_count = df["Department"].value_counts()

    fig2, ax2 = plt.subplots(figsize=(6, 4))

    ax2.pie(
        dept_count.values,
        labels=dept_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax2.axis("equal")

    st.pyplot(fig2)

# ==========================
# SEARCH EMPLOYEE
# ==========================

st.header("🔍 Search Employee")

name = st.text_input("Enter Employee Name")

if name:
    result = df[df["Name"].str.contains(name, case=False)]

    if result.empty:
        st.error("Employee Not Found")
    else:
        st.success("Employee Found")
        st.dataframe(result)
    if name:
        result = df[df["Name"].str.contains(name, case=False)]

        if result.empty:
            st.error("Employee Not Found")
        else:
            st.success("Employee Found")
            st.dataframe(result)

    # ==========================
    # TOP 100 HIGHEST SALARY
    # ==========================

    st.header("🏆 Top 100 Highest Salary")

    top5 = df.sort_values(by="Salary", ascending=False).head(5)

    st.dataframe(top5, use_container_width=True)

    # ==========================
    # ADVANCED ANALYTICS
    # ==========================

    st.header("📊 Advanced Analytics")

    col1, col2 = st.columns(2)

    # Histogram
    with col1:
        st.subheader("Salary Distribution")

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(df["Salary"], bins=5)
        ax.set_xlabel("Salary")
        ax.set_ylabel("Employees")
        ax.set_title("Salary Histogram")

        st.pyplot(fig)

    # Salary Trend
    with col2:
        st.subheader("Salary Trend")

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["Name"], df["Salary"], marker="o")
        ax.set_xlabel("Employee")
        ax.set_ylabel("Salary")
        ax.set_title("Salary Trend")

        plt.xticks(rotation=45)

        st.pyplot(fig)

    # ==========================
    # AGE VS SALARY
    # ==========================

    st.subheader("📈 Age vs Salary")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df["Age"], df["Salary"])

    ax.set_xlabel("Age")
    ax.set_ylabel("Salary")
    ax.set_title("Age vs Salary")

    st.pyplot(fig)

    # ==========================
    # DOWNLOAD DATA
    # ==========================

    st.header("📥 Download Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="dataset.csv",
        mime="text/csv"
    )
    # ==========================
    # SMART AI ASSISTANT
    # ==========================

    st.header("🤖 Smart AI Assistant")

    question = st.text_input("Ask anything about your dataset")

    if st.button("Ask AI"):

        q = question.lower().strip()

        if q == "":
            st.warning("Please enter a question.")

        elif "average salary" in q:
            st.success(f"Average Salary : ₹{df['Salary'].mean():,.0f}")

        elif "highest salary" in q:
            st.dataframe(df[df["Salary"] == df["Salary"].max()])

        elif "lowest salary" in q:
            st.dataframe(df[df["Salary"] == df["Salary"].min()])

        elif "total employee" in q:
            st.success(f"Total Employees : {len(df)}")

        elif "department" in q:
            st.write(df["Department"].value_counts())

        elif "youngest" in q:
            st.dataframe(df[df["Age"] == df["Age"].min()])

        elif "oldest" in q:
            st.dataframe(df[df["Age"] == df["Age"].max()])

        else:
            st.info("Sorry! I don't know this yet.")

    # ==========================
    # SIDEBAR FILTER
    # ==========================
    st.sidebar.title("⚙️ Filters")

    department = st.sidebar.selectbox(
        "Select Department",
        ["All"] + list(df["Department"].unique())
    )

    if department == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Department"] == department]

    st.write("Sidebar executed")
    st.write(filtered_df.head())
                    # ==========================
                    # SMART KPIs
                    # ==========================
st.header("📊 Smart Dashboard")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Employees", len(filtered_df))
c2.metric("Average Salary", f"₹{filtered_df['Salary'].mean():,.0f}")
c3.metric("Highest Salary", f"₹{filtered_df['Salary'].max():,.0f}")
c4.metric("Lowest Salary", f"₹{filtered_df['Salary'].min():,.0f}")

# ==========================
# AI INSIGHTS
# ==========================

st.header("🧠 AI Insights")

highest = filtered_df.loc[filtered_df["Salary"].idxmax()]
lowest = filtered_df.loc[filtered_df["Salary"].idxmin()]

st.success(f"""
✅ Total Employees : {len(filtered_df)}

💰 Average Salary : ₹ {filtered_df['Salary'].mean():,.0f}

🏆 Highest Salary : {highest['Name']} (₹ {highest['Salary']:,.0f})

📉 Lowest Salary : {lowest['Name']} (₹ {lowest['Salary']:,.0f})

🏢 Total Departments : {filtered_df['Department'].nunique()}
""")
# ==========================
# DOWNLOAD EXCEL
# ==========================

st.header("📥 Download Excel")

excel = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Excel File",
    excel,
    "employees.csv",
    "text/csv"
)
