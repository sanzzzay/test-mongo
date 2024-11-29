from mongo_manager.base import MongoManager
from datetime import datetime, timedelta
import random


def generate_sample_users(count: int) -> list:
    """Generate sample user data"""
    departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
    cities = ["New York", "London", "Tokyo", "Paris", "Singapore"]

    users = []
    for i in range(count):
        user = {
            "employee_id": f"EMP{i + 1:03d}",
            "name": f"User {i + 1}",
            "email": f"user{i + 1}@example.com",
            "age": random.randint(22, 60),
            "department": random.choice(departments),
            "city": random.choice(cities),
            "salary": random.randint(50000, 150000),
            "join_date": (datetime.now() - timedelta(days=random.randint(0, 1000))).strftime("%Y-%m-%d"),
            "is_active": random.choice([True, False]),
            "projects": random.sample(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
                                      random.randint(1, 3))
        }
        users.append(user)
    return users


def main():
    # Initialize MongoDB manager
    mongo_manager = MongoManager(
        host="localhost",
        port=27017,
        database="company_db"
    )

    try:
        # Generate and insert 100 users
        print("Generating and inserting 100 user records...")
        users = generate_sample_users(100)
        inserted_ids = mongo_manager.insert_many("employees", users)
        print(f"Successfully inserted {len(inserted_ids)} records\n")

        # Perform various queries
        print("Performing sample queries:")

        # 1. Find all employees in Engineering department
        engineering_employees = mongo_manager.find_many("employees",
                                                        {"department": "Engineering"})
        print(f"\n1. Number of Engineering employees: {len(engineering_employees)}")
        print("Sample Engineer:", engineering_employees[0] if engineering_employees else "None")

        # 2. Find employees with salary > 100000
        high_salary_employees = mongo_manager.find_many("employees",
                                                        {"salary": {"$gt": 100000}})
        print(f"\n2. Number of high salary employees: {len(high_salary_employees)}")

        # 3. Find specific employee by ID
        employee = mongo_manager.find_one("employees", {"employee_id": "EMP001"})
        print("\n3. Found employee EMP001:", employee["name"] if employee else "Not found")

        # 4. Find employees in specific cities
        tokyo_employees = mongo_manager.find_many("employees", {"city": "Tokyo"})
        print(f"\n4. Number of employees in Tokyo: {len(tokyo_employees)}")

        # 5. Find active employees working on Project Alpha
        active_alpha_employees = mongo_manager.find_many("employees",
                                                         {"is_active": True,
                                                          "projects": "Alpha"})
        print(f"\n5. Number of active employees on Project Alpha: {len(active_alpha_employees)}")

        # Update some records
        print("\nPerforming updates:")

        # 1. Give 10% raise to Engineering department
        update_count = mongo_manager.update_many(
            "employees",
            {"department": "Engineering"},
            {"salary": 110000}
        )
        print(f"Updated {update_count} Engineering employee salaries")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up
        mongo_manager.close()


if __name__ == "__main__":
    main()