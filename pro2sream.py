import streamlit as st
import pandas as pd
import mysql.connector


st.set_page_config(page_title="Internation Debt report Analysis",
                   page_icon="📈",
                   layout="wide")

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="international_debt_analysis",
    autocommit=True
)

mycursor=conn.cursor()

def queries():
    st.header("International Debt Analysis")
    st.subheader("Queries and answers")


    select_query=st.selectbox("Options",[
                "Select any Query",
                "Retrieve all distinct country names from the dataset",
                "Count the total number of countries available",
                "Find the total number of indicators present",
                "Display the first 10 records of the dataset",
                "Calculate the total global debt",
                "List all unique indicator names",
                "Find the number of records for each country",
                "Display all records where debt is greater than 1 billion USD",
                "Find the minimum, maximum, and average debt values",
                "Count total number of records in the dataset",
                "Find the total debt for each country",
                "Display the top 10 countries with the highest total debt",
                "Find the average debt per country",
                "Calculate total debt for each indicator",
                "Identify the indicator contributing the highest total debt",
                "Find the country with the lowest total debt",
                "Calculate total debt for each country and indicator combination",
                "Count how many indicators each country has",
                "Display countries whose total debt is above the global average",
                "Rank countries based on total debt (highest to lowest)",
                "Find the top 5 indicators contributing most to global debt",
                "Calculate percentage contribution of each country to total global debt",
                "Identify the top 3 countries for each indicator based on debt",
                "Find the difference between maximum and minimum debt for each country",
                "Create a view for the top 10 countries with highest debt,Categorize countries into:High Debt,Medium Debt,Low Debt",
                "Use window functions to calculate cumulative debt per country",
                "Find indicators where average debt is higher than overall average debt",
                "Identify countries contributing more than 5% of global debt",
                "Find the most dominant indicator (highest contribution) for each country"
    ])

    if select_query == "Retrieve all distinct country names from the dataset":
        st.code("SELECT DISTINCT long_name FROM meta;", language  ="sql")
        query1 = "SELECT DISTINCT long_name FROM meta;"
        df=pd.read_sql(query1, conn)
        st.dataframe(df, width="stretch")
        
    elif select_query== "Count the total number of countries available":
        st.code("select count(country_code) from meta", language = "sql")
        query2="select count(country_code) from meta;"
    
        mycursor.execute(query2)
        result = mycursor.fetchone()

        st.metric("Total Number of Countries", result[0])

    elif select_query== "Find the total number of indicators present":
        st.code("SELECT COUNT(DISTINCT indicator_name) FROM ids_data", language="sql")
        query3 = "SELECT COUNT(DISTINCT indicator_name) FROM ids_data;"
        mycursor.execute(query3)
        result = mycursor.fetchone()
        st.write("Total number of indicators:", result[0])

    elif select_query=="Display the first 10 records of the dataset":
        st.code("select * from all_country limit 10;", language="sql")
        query4="select * from all_country limit 10;"
        mycursor.execute(query4)
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif select_query=="Calculate the total global debt":
        st.code("select sum(debt_amt) from all_country", language= "sql")
        query5 = "select sum(debt_amt) from all_country;"
        mycursor.execute(query5)
        result=mycursor.fetchone()
        st.metric("Total Global Debt", f"{result[0]:,.2f}")

    elif select_query=="List all unique indicator names":
        st.code("select distinct indicator_name from ids_data", language = "sql")
        query6="select distinct indicator_name from ids_data;"
        df=pd.read_sql(query6, conn)
        st.dataframe(df, width="stretch")

    elif select_query== "Find the number of records for each country":
        st.code("SELECT country_name, COUNT(*) AS record_count FROM all_country GROUP BY country_name", language = "sql")
        query7 = "SELECT country_name, COUNT(*) AS record_count FROM all_country GROUP BY country_name;"
        df= pd.read_sql(query7, conn)
        st.dataframe(df, width="stretch")

    elif select_query == "Display all records where debt is greater than 1 billion USD":
        st.code("SELECT country_name, country_code, debt_amt FROM all_country WHERE debt_amt > 1000000000 ORDER BY debt_amt DESC;", language="sql")
        query8="SELECT country_name, country_code, debt_amt FROM all_country WHERE debt_amt > 1000000000 ORDER BY debt_amt DESC;"
        df=pd.read_sql(query8, conn)
        st.dataframe(df, width="stretch")

    elif select_query=="Find the minimum, maximum, and average debt values":
        st.code("select min(debt_amt), max(debt_amt), avg(debt_amt) from all_country;", language = "sql")
        query9="select min(debt_amt), max(debt_amt), avg(debt_amt) from all_country;"
        st.code(query, language="sql")

        df = pd.read_sql(query, conn)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Minimum Debt",
            f"{df.iloc[0]['minimum_debt']:,.2f}"
        )

        col2.metric(
            "Maximum Debt",
            f"{df.iloc[0]['maximum_debt']:,.2f}"
        )

        col3.metric(
            "Average Debt",
            f"{df.iloc[0]['average_debt']:,.2f}"
        )

    elif select_query == "Count total number of records in the dataset":
        st.code("select count(*) from all_country;", language="sql")
        query10 = "select count(*) from all_country;"
        mycursor.execute(query10)
        result= mycursor.fetchone()
        st.write("Total number of records:", result)

    elif select_query== "Find the total debt for each country":
        st.code("select country_code, country_name, sum(debt_amt) as total_debt from all_country group by country_name,country_code order by total_debt desc", language="sql")
        query11="select country_code, country_name, sum(debt_amt) as total_debt from all_country group by country_name,country_code order by total_debt desc;"
        df=pd.read_sql(query11, conn)
        st.write(df)

    elif select_query == "Display the top 10 countries with the highest total debt":
        st.code("select country_name, country_code, sum(debt_amt) as debt_value from all_country group by country_name, country_code order by debt_value desc limit 10;", language ="sql")
        query12="select country_name, country_code, sum(debt_amt) as debt_value from all_country group by country_name, country_code order by debt_value desc limit 10;"
        df=pd.read_sql(query12, conn)
        st.write(df)

    elif select_query == "Find the average debt per country":
        st.code("select country_name, avg(debt_amt) as Average_debt from all_country group by country_name order by Average_debt;", language = "sql")
        query13 = "select country_name, avg(debt_amt) as Average_debt from all_country group by country_name order by Average_debt;"
        df=pd.read_sql(query13, conn)
        st.write(df)

    elif select_query == "Calculate total debt for each indicator":
        st.code(
            "select ac.series_code, ids.indicator_name, sum(ac.debt_amt) as total_debt_value from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ids.indicator_name order by total_debt_value desc;", language= "sql")
        query14="select ac.series_code, ids.indicator_name, sum(ac.debt_amt) as total_debt_value from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ids.indicator_name order by total_debt_value desc;"
        df=pd.read_sql(query14, conn)
        st.write(df)

    elif select_query == "Identify the indicator contributing the highest total debt":
        st.code("select ac.series_code, sum(ac.debt_amt) as maximum_debt, ids.indicator_name from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ids.indicator_name order by maximum_debt desc limit 1;", language= "sql")
        query15="""select ac.series_code, sum(ac.debt_amt) as maximum_debt, ids.indicator_name
        from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code
        group by ac.series_code, ids.indicator_name
        order by maximum_debt desc limit 1;"""
        df= pd.read_sql(query15, conn)
        st.write(df)
    
    elif select_query == "Find the country with the lowest total debt":
        st.code("select country_code, country_name, min(debt_amt) as lowest_debt from all_country group by country_code, country_name order by lowest_debt desc limit 1;", language = "sql")
        query16="select country_code, country_name, min(debt_amt) as lowest_debt from all_country group by country_code, country_name order by lowest_debt desc limit 1;"
        df=pd.read_sql(query16, conn)
        st.write(df)

    elif select_query == "Calculate total debt for each country and indicator combination":
        st.code("select ac.series_code, ac.country_name, ids.indicator_name, sum(ac.debt_amt) as total_debt from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ac.country_name, ids.indicator_name order by total_debt asc;", language = "sql")
        query17= "select ac.series_code, ac.country_name, ids.indicator_name, sum(ac.debt_amt) as total_debt from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ac.country_name, ids.indicator_name order by total_debt asc;"
        df= pd.read_sql(query17, conn)
        st.write(df)

    elif select_query == "Count how many indicators each country has":
        st.code("select ac.series_code, ac.country_name, count(ids.indicator_name) as indicators from all_country as ac inner join ids_data as ids on ac.series_code = ids.series_code group by ac.series_code, ac.country_name order by indicators desc;", language = "sql")
        query18="select ac.series_code, ac.country_name, count(ids.indicator_name) as indicators from all_country as ac inner join ids_data as ids on ac.series_code = ids.series_code group by ac.series_code, ac.country_name order by indicators desc;"
        df=pd.read_sql(query18, conn)
        st.write(df)

    elif select_query ==  "Display countries whose total debt is above the global average":
        st.code("select country_code, country_name, sum(debt_amt) as debt from all_country group by country_code, country_name having sum(debt_amt) > (select avg(debt_amt) from all_country) order by debt desc;", language = "sql")
        query19 = "select country_code, country_name, sum(debt_amt) as debt from all_country group by country_code, country_name having sum(debt_amt) > (select avg(debt_amt) from all_country) order by debt desc;"
        df=pd.read_sql(query19, conn)
        st.write(df)

    elif select_query == "Rank countries based on total debt (highest to lowest)":
        st.code("SELECT country_name, country_code,SUM(debt_amt) AS total_debt,RANK() OVER (ORDER BY SUM(debt_amt) DESC) AS debt_rank FROM all_country GROUP BY country_name, country_code ORDER BY debt_rank;", language = "sql")
        query20="""SELECT country_name, country_code,SUM(debt_amt) AS total_debt,RANK() OVER (ORDER BY SUM(debt_amt) DESC) AS debt_rank FROM all_country GROUP BY country_name, country_code ORDER BY debt_rank;"""
        df=pd.read_sql(query20, conn)
        st.write(df)

    elif select_query == "Find the top 5 indicators contributing most to global debt":
        st.code("select ac.series_code, sum(ac.debt_amt) as maximum_debt, ids.indicator_name from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ids.indicator_name order by maximum_debt desc limit 5;", language = "sql")
        query21="""select ac.series_code, sum(ac.debt_amt) as maximum_debt, ids.indicator_name from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ids.indicator_name order by maximum_debt desc limit 5;"""
        mycursor.execute(query21)
        result= mycursor.fetchall()
        st.write(result)

    elif select_query =="Calculate percentage contribution of each country to total global debt":
        st.code("select country_name, sum(debt_amt) as total_debt, round((sum(debt_amt)/(select sum(debt_amt) from all_country)) * 100,2) as debt_percent from all_country group by country_name order by debt_percent desc;", language = "sql")
        query22= """select country_name, sum(debt_amt) as total_debt, round((sum(debt_amt)/(select sum(debt_amt) from all_country)) * 100,2) as debt_percent from all_country group by country_name order by debt_percent desc;"""
        df=pd.read_sql(query22, conn)
        st.write(df)

    elif select_query  ==  "Identify the top 3 countries for each indicator based on debt":
        st.code("select ac.country_name, ac.series_code, ids.indicator_name, sum(ac.debt_amt) as total_debt from all_country as ac inner join ids_data as ids on ac.series_code=ids.series_code group by ac.series_code, ac.country_name, ids.indicator_name order by total_debt desc limit 3;", language ="sql")
        query23 = """select ac.country_name, ac.series_code, ids.indicator_name, 
            sum(ac.debt_amt) as total_debt from all_country as ac inner join ids_data as ids
            on ac.series_code=ids.series_code group by ac.series_code,
            ac.country_name, ids.indicator_name
            order by total_debt desc limit 3;"""

        df=pd.read_sql(query23, conn)
        st.write(df)

    elif select_query== "Find the difference between maximum and minimum debt for each country":
        st.code ("select country_name, country_code, min(debt_amt) as min_debt, max(debt_amt) as max_debt, max(debt_amt) - min(debt_amt) as differnce from all_country group by country_code, country_name order by differnce desc;", language = "sql")
        query24 = """
        SELECT country_name,
            country_code,
            MIN(debt_amt) AS min_debt,
            MAX(debt_amt) AS max_debt,
            MAX(debt_amt) - MIN(debt_amt) AS difference
        FROM all_country
        GROUP BY country_code, country_name
        ORDER BY difference DESC;
        """     
        df=pd.read_sql(query24, conn)
        st.write(df)

    elif select_query == "Create a view for the top 10 countries with highest debt,Categorize countries into:High Debt,Medium Debt,Low Debt":
        st.code("CREATE VIEW IF NOT EXISTS country_debt_cat AS SELECT country_name, country_code, SUM(debt_amt) AS total_debt, CASE WHEN SUM(debt_amt) >= 4.10000 THEN 'High Debt' when SUM(debt_amt) >= 1.87931 THEN 'Medium Debt' ELSE 'Low Debt' END AS debt_category FROM all_country GROUP BY country_name, country_code;", language = "sql")
        query25 = "CREATE VIEW IF NOT EXISTS country_debt_cat AS SELECT country_name, country_code, SUM(debt_amt) AS total_debt, CASE WHEN SUM(debt_amt) >= 4.10000 THEN 'High Debt' when SUM(debt_amt) >= 1.87931 THEN 'Medium Debt' ELSE 'Low Debt' END AS debt_category FROM all_country GROUP BY country_name, country_code;"
        mycursor.execute(query25)
        conn.commit()

        st.write("View created successfully")

    elif select_query == "Use window functions to calculate cumulative debt per country":
        query26 = """
        SELECT country_name,
            country_code,
            series_code,
            year,
            debt_amt,
            SUM(debt_amt) OVER (
                PARTITION BY country_code, series_code
                ORDER BY year
            ) AS cumulative_debt
        FROM all_country
        ORDER BY country_code, series_code, year;
        """
        st.code(query26, language = "sql")
        df = pd.read_sql(query26, conn)
        st.write(df)

    elif select_query == "Find indicators where average debt is higher than overall average debt":
        st.code("select avg(debt_amt) from all_country;", language = "sql")
        query = "select avg(debt_amt) from all_country;"
        df=pd.read_sql(query, conn)
        st.write(df)

    elif select_query ==  "Identify countries contributing more than 5% of global debt":
        st.code("select country_code, countyr_name, sum(debt_amt) as t_debt from all_country;", language = "sql")
        query29 = "select country_code, countyr_name, sum(debt_amt) as t_debt from all_country;"
        df=pd.read_sql(query29, conn)
        st.write(df)


queries()


# =========================================================
# FILE PATHS
# =========================================================
country_path=r"C:\Users\Dhanalakshmi\Desktop\GUVI PRACTICE\Projects\Project 2\SQL insert\country_data.csv"
ids_path=r"C:\Users\Dhanalakshmi\Desktop\GUVI PRACTICE\Projects\Project 2\SQL insert\ids_data.csv"
meta_path=r"C:\Users\Dhanalakshmi\Desktop\GUVI PRACTICE\Projects\Project 2\SQL insert\meta_data.csv"

st.header("Country wise debt report")
country_file="select * from all_country;"
df=pd.read_sql(country_file, conn)
st.dataframe(df, width="stretch")

st.header("Indicators data report")
ids_file="select * from ids_data;"
df=pd.read_sql(ids_file, conn)
st.dataframe(df, width="stretch")

st.header("Meta data report")
meta_file= "select * from meta;"
df=pd.read_sql(meta_file, conn)
st.dataframe(df, width="stretch")







