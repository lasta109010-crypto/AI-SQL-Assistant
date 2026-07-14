# ============================
# Import Libraries
# ============================
import streamlit as st
import sqlite3
from openai import OpenAI
import pandas as pd


# ============================
# Database Connection
# ============================
client = OpenAI()

connection = sqlite3.connect("statistics_canada.db")
cursor = connection.cursor()

# 
# ==========================================
# THE TITLE
# ==========================================
st.title("CA AI Statistics Canada Data Explorer")
st.caption(
    "Ask questions in plain English and explore Canadian public statistics using AI-generated SQL."
)
st.markdown("""
### Explore Canadian Statistics

#### Demographics
- Population
- Immigration
- Life Expectancy

#### Economy
- Income
- Wages
- Employment and Unemployment
- GDP

#### Housing and Cost
- Housing
- Consumer Spending
- Poverty

#### Society
- Healthcare
- Education
- Crime and Public Safety
""")

# ==========================================
# AI Instructions
# ==========================================
instructions = """
You are an SQLite expert.

Convert the user's question into valid SQLite SQL.

Return ONLY the SQL query.

Database Schema:
Relationships:
All statistics tables are related using:
- province
- year

When a question requires data from multiple tables, join them using BOTH columns.

Example:
population.province = income.province
AND population.year = income.year

Table: population
Columns:
- id
- province
- year
- population

Table: income
Columns:
- id
- province
- year
- median_income

Table: housing
Columns:
- id
- province
- year
- average_house_price

Table: employment
Columns:
- id
- province
- year
- employment_rate
- unemployment_rate

Table: healthcare
Columns:
- id
- province
- year
- physicians_per_1000
- healthcare_spending

Table: immigration
Columns:
- id
- province
- year
- immigrants

Table: life_expectancy
Columns:
- id
- province
- year
- life_expectancy

Table: education
Columns:
- id
- province
- year
- university_graduation_rate

Table: gdp
Columns:
- id
- province
- year
- gdp_billions

Table: crime
Columns:
- id
- province
- year
- crime_rate

Table: wages
Columns:
- id
- province
- year
- average_hourly_wage

Table: poverty
Columns:
- id
- province
- year
- poverty_rate

Table: consumer_spending
Columns:
- id
- province
- year
- average_annual_spending

"""





# ==========================================
# OpenAI API
# ==========================================

question = st.text_input("Ask a question about Canadian statistics")

if st.button("🔍 Analyze Data"):

    with st.spinner("Analyzing Canadian statistics..."):

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
{instructions}

User Question:
{question}
"""
        )

        sql_query = response.output_text.strip()
        sql_query = sql_query.replace("```sql", "")
        sql_query = sql_query.replace("```", "")
        sql_query = sql_query.strip()

        

        

        
        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        # ==========================================
        # Execute SQL
        # ==========================================

        try:

            if sql_query.upper().startswith("SELECT"):

                cursor.execute(sql_query)

                results = cursor.fetchall()

                if results:

                    df = pd.DataFrame(
                        results,
                        columns=[column[0] for column in cursor.description]
                    )

                    st.dataframe(df)

                else:

                    st.warning("No records found.")

            else:

                st.error("Only SELECT queries are allowed.")

        except Exception as e:

            st.error(f"Could not run the query: {e}")