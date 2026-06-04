#BUG1
import requests

API_BASE_URL = "https://hr-internal.company.com/api"
API_TOKEN = "your_api_token_here"

def get_employee(employee_id):
    url = f"{API_BASE_URL}/employees/{employee_id}"

    # Added Authorization header with Bearer token to fix 401 Unauthorized
    response = requests.get(url, headers={"Authorization": f"Bearer {API_TOKEN}"})
    
    if response.status_code == 404:
        return None
    
    data = response.json()

    # Safely access "employee" key to avoid KeyError when response is 404
    return data.get("employee")

#BUG2
def get_monthly_attendance(conn, employee_id, month, year):
    # Changed LEFT JOIN to INNER JOIN to ensure only matching employee records are returned
    # Added employee_id filter to restrict results to the given employee
    query = """
        SELECT a.date, a.check_in, a.check_out, e.name
        FROM attendance a
        INNER JOIN employees e
        ON a.employee_id = e.id
        WHERE a.employee_id = ?
        AND a.month = ?
        AND a.year = ?
        ORDER BY a.date ASC
    """
    cursor = conn.cursor()
    cursor.execute(query, (employee_id, month, year))
    return cursor.fetchall()

#BUG3
from datetime import datetime

WORK_START = "09:00"
LATE_THRESHOLD_MINUTES = 15

def calculate_hours(check_in: str, check_out: str):
    fmt = "%H:%M"
    ci = datetime.strptime(check_in, fmt)
    co = datetime.strptime(check_out, fmt)

    # Corrected subtraction order to compute positive work duration (check_out - check_in)
    duration = co - ci
    hours_worked = duration.seconds / 3600

    start = datetime.strptime(WORK_START, fmt)
    late_by = (ci - start).seconds // 60

    # Changed condition to >= so exactly 15 minutes late is also flagged
    is_late = late_by >= LATE_THRESHOLD_MINUTES

    return round(hours_worked, 2), is_late

#BUG4
def generate_summary(records):
    total_hours = 0
    late_days = 0

    # Fixed loop range to prevent IndexError (removed +1)
    for i in range(len(records)):
        record = records[i]
        total_hours += record["hours"]
        if record["is_late"]:
            late_days += 1

    # Handled empty list to avoid division by zero when calculating average
    avg_hours = total_hours / len(records) if len(records) > 0 else 0

    return {
        "total_hours": round(total_hours, 2),
        "avg_hours": round(avg_hours, 2),
        "late_days": late_days,
        "days_present": len(records)
    }

MIN_DAYS_REQUIRED = 20
MAX_LATE_DAYS = 3

#BUG5
def check_attendance_policy(summary):
    days_present = summary["days_present"]
    late_days = summary["late_days"]

    # Corrected comparison to flag employees with fewer than minimum required days
    below_minimum = days_present < MIN_DAYS_REQUIRED

    # Changed condition to >= so exactly max late days also triggers warning
    exceeded_late = late_days >= MAX_LATE_DAYS

    if below_minimum or exceeded_late:
        return {
            "warning": True,
            "reason": []
              + (["Below minimum attendance"] if below_minimum else [])
              + (["Exceeded late check-ins"] if exceeded_late else [])
        }
    return {"warning": False, "reason": []}