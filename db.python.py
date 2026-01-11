import psycopg2

conn = psycopg2.connect(
    dbname="EcoPackAI_Database",
    user="postgres",
    password="Gaurav@123",
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL successfully!")