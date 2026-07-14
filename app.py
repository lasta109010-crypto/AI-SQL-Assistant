# ============================
# Import Libraries
# ============================
import streamlit as st
import sqlite3
from openai import OpenAI
import pandas as pd



client = OpenAI()
# ============================
# Database Connection
# ============================
connection = sqlite3.connect("online_store.db")
cursor = connection.cursor()

# ============================
# Streamlit User Interface
# ============================
st.tItle = ("AI SQL Assistant")

st.markdown("""
### 💡 Example Questions

- Show all customers
- Show all products
- Which customer spent the most money?
- Which country placed the most orders?
- Which product generated the most revenue?
- Show the total amount each customer has spent.
""")



question = st.text_input("Ask a question about the online store databases")

# ============================
# AI Prompt
# ============================
if st.button("Generate SQL"):
    instructions = """
    You are an expert SQLite assistant.
    Your task is to convert the user's English question into a valid SQLite query.
    
    Database schema:
    Relationships:

    orders.customer_id = customers.customer_id
    order_items.order_id = orders.order_id
    order_items.product_id = products.product_id

    Table: customers

    Columns:
    - customer_id
    - customer_name
    - country
    - email

    Table: products
    - product_id
    - product_name
    - price


    Table: orders
    - order_id
    - customer_id
    - order_date

    Table: order_items
    - order_item_id
    - order_id
    - product_id
    - quantity


    Rules:

    - Return ONLY the SQL query.
    - Do NOT use markdown.
    - Do NOT use ```sql or ``` code fences.
    - Do NOT include explanations.
    - Do NOT include comments.
    - The output must be executable SQLite code.

    """

# ============================
# Generate SQL with OpenAI
# ============================

    st.write(question)

    with st.spinner("Generating SQL..."):

        response = client.responses.create(

            model = "gpt-4.1-mini",
            input=f"""
            {instructions}

            User Question:
            {question}
            """
    )
        
# ============================
# Execute SQL
# ============================

    sql_query = response.output_text.strip()
    st.subheader("Generated SQL")
    st.code(sql_query,language="sql")
    try:

        if sql_query.upper().startswith("SELECT"):
            cursor.execute(sql_query)

            
            results = cursor.fetchall()

            if results:
                df = pd.DataFrame(results, columns=[column[0] for column in cursor.description])
                st.dataframe(df)
            else:
                 st.warning("No records found.")


    


            
          

        else:

            cursor.execute(sql_query)
            connection.commit()
            st.success("Query executed succesfully")
    except Exception as e:

        st.error(f"Could not run the query: {e}")