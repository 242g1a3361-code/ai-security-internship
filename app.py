# Task 4 - Secure Agentic AI App - Fake Data Only
# Author: Tejaswi | YGF NGO Internship
import re, time
ALLOWED_FILES = ["safe_data/test.txt"]
ALLOWED_URLS = ["https://example.com/api"]
BLOCKED_WORDS = ["ignore previous", "reveal secret", "SECRET-FLAG-123", "/etc/passwd", "os.system", "delete all"]
request_count = 0
def is_safe_input(user_input):
    low = user_input.lower()
    for word in BLOCKED_WORDS:
        if word.lower() in low:
            return False, f"Blocked: Contains forbidden pattern '{word}'"
    if ".." in user_input or "/etc/" in user_input:
        return False, "Blocked: Path traversal detected"
    return True, "Safe"
def file_read_tool(filename):
    if filename not in ALLOWED_FILES:
        return "BLOCKED: File not in allow-list. Only safe_data/test.txt allowed."
    return "Fake file content: Hello, this is test data. No real secrets here."
def email_tool(to_email, message):
    if not to_email.endswith("@example.com"):
        return "BLOCKED: Only @example.com allowed for testing."
    print(f"[APPROVAL NEEDED] Send email to {to_email}? Type YES to approve.")
    approval = input("Approve? ")
    if approval.upper() != "YES":
        return "Cancelled by user."
    return f"Fake email sent to {to_email} (Simulation only, no real email sent)"
def http_tool(url):
    if url not in ALLOWED_URLS:
        return "BLOCKED: URL not in allow-list. SSRF protection active."
    return "Fake API response: {status: ok, data: test}"
def chatbot():
    global request_count
    print("=== Secure AI Agent Started (Fake Data Only) ===")
    print("Try: read safe_data/test.txt | send email | call api | exit")
    while True:
        request_count += 1
        if request_count > 10:
            print("Rate limit: Max 10 requests. Please wait.")
            time.sleep(2)
            request_count = 0
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Agent: Bye! Stay safe.")
            break
        safe, reason = is_safe_input(user_input)
        if not safe:
            print(f"Agent: {reason} - I cannot follow that instruction.")
            continue
        if "read" in user_input.lower():
            print("Agent:", file_read_tool("safe_data/test.txt"))
        elif "email" in user_input.lower():
            print("Agent:", email_tool("test@example.com", "Hello test"))
        elif "api" in user_input.lower() or "http" in user_input.lower():
            print("Agent:", http_tool("https://example.com/api"))
        else:
            print("Agent: I can help with file read, fake email, or safe API call only.")
if __name__ == "__main__":
    chatbot()
