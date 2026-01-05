import re

def extract_emails(input_file, output_file):
    with open(input_file, "r") as file:
        text = file.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    return len(emails)

def run_email_extractor():
    input_file = "input.txt"
    output_file = "emails.txt"

    count = extract_emails(input_file, output_file)

    print("Email Extraction Completed")
    print("Total emails found:", count)
    print("Saved in:", output_file)


run_email_extractor()
