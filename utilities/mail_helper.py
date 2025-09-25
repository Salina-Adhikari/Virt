import requests
import time
import re

MAIL_BASE = "https://api.mail.tm"

class MailHelper:
    def __init__(self):
        domain_data = requests.get(f"{MAIL_BASE}/domains").json()
        domain = domain_data["hydra:member"][0]["domain"]
        self.email = f"test{int(time.time())}@{domain}"
        self.password = "Password123"

        requests.post(f"{MAIL_BASE}/accounts", json={
            "address": self.email,
            "password": self.password
        })

        login = requests.post(f"{MAIL_BASE}/token", json={
            "address": self.email,
            "password": self.password
        }).json()

        self.token = login["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def wait_for_email(self, timeout=60):
        print(f"Waiting for email at: {self.email}")

        for _ in range(timeout):
            response = requests.get(f"{MAIL_BASE}/messages", headers=self.headers).json()
            messages = response["hydra:member"]

            if messages:
                print("Email received")
                return messages[0]

            time.sleep(2)

        raise Exception("No email received")

    def get_verification_code(self, email_id):
        print(f"Reading email with ID: {email_id}")

        response = requests.get(f"{MAIL_BASE}/messages/{email_id}", headers=self.headers).json()
        body = response.get("text", "")

        match = re.search(r"\b\d{6}\b", body)
        if match:
            code = match.group(0)
            print(f"Verification code found: {code}")
            return code

        raise Exception("Verification code not found")
