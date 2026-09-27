import os

app_name = os.getenv("APP_NAME", "Secret Safe Demo")
database_url = os.getenv("DATABASE_URL")

print(f"Application: {app_name}")

if database_url:
    print("Database configuration is available.")
else:
    print("Database configuration is not set.")