import time

def send_email(username: str):
    print(f"Sending welcome email to {username}...")
    time.sleep(10)
    print("Email sent successfully!")

def log_registration(username):
    print(f"{username} registered.")

    background_tasks.add_task(
        log_registration,
        user.username
    )