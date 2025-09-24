# Create test_postgresql_connection.py
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        conn = psycopg2.connect(os.getenv('DB_URL'))
        cursor = conn.cursor()
        
        # Test query
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ PostgreSQL version: {version[0]}")
        
        # Test table creation
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Test query result: {result[0]}")
        
        cursor.close()
        conn.close()
        print("✅ PostgreSQL connection test successful!")
        
    except Exception as e:
        print(f"❌ PostgreSQL connection test failed: {e}")

if __name__ == "__main__":
    test_connection()