import re
from urllib.parse import urlparse
from email import message_from_string

class PhishingTriageToolkit:
    def __init__(self, target_company_domain: str):
        self.target_domain = target_company_domain.lower()
        self.suspicious_keywords = r"(urgent|immediately|suspended|verify your password|click here|action required|wire transfer|security alert)"
        self.dangerous_extensions = ('.exe', '.js', '.scr', '.iso', '.bat', '.vbs', '.html')

    def analyze_text(self, email_body: str) -> bool:
        matches = re.findall(self.suspicious_keywords, email_body, re.IGNORECASE)
        return len(matches) > 0

    def analyze_url(self, url: str) -> bool:
        try:
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname
            if not hostname:
                return True
                
            hostname = hostname.lower()
            domain_parts = hostname.split('.')
            
            if len(domain_parts) >= 2:
                root_domain = ".".join(domain_parts[-2:])
            else:
                root_domain = hostname

            if self.target_domain in hostname and root_domain != self.target_domain:
                return True 
                
            return False
        except Exception:
            return True

    def analyze_attachments(self, msg_object) -> bool:
        for part in msg_object.walk():
            filename = part.get_filename()
            if filename:
                filename = filename.lower()
                if filename.endswith(self.dangerous_extensions):
                    return True 
        return False

    def process_triage(self, raw_email_string: str, extracted_url: str) -> str:
        risk_score = 0
        msg = message_from_string(raw_email_string)
        
        sender_header = msg.get('From', '').lower()
    
        if self.target_domain in sender_header and "@" in sender_header:
            domain_of_sender = sender_header.split('@')[-1].strip('>')
            if self.target_domain not in domain_of_sender:
                risk_score += 5 

        email_body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_body += part.get_payload()
        else:
            email_body = msg.get_payload()

        if self.analyze_text(email_body):
            risk_score += 2 

        if extracted_url and self.analyze_url(extracted_url):
            risk_score += 4 

        if self.analyze_attachments(msg):
            risk_score += 4

        print(f"\n--- Triage Report ---")
        print(f"Calculated Threat Risk Score: {risk_score} / 15")

        if risk_score >= 7:
            return "RESULT: [MALICIOUS] -> Action: Block Domain & Escalate to SOC team."
        elif risk_score >= 3:
            return "RESULT: [SUSPICIOUS] -> Action: Warn User & Move to Quarantine."
        else:
            return "RESULT: [SAFE] -> Action: Close Ticket."
        
if __name__ == "__main__":
    print("==================================================")
    print("🛡️  Welcome to the Interactive Phishing Triage Tool 🛡️")
    print("Please copy your suspicious email into a .txt file and provide the path to analyze it from your email account.")
    print("==================================================")
    company_domain = input("🏢 Enter your company's legitimate domain (e.g., company.com): ").strip()
    
    if not company_domain:
        print("❌ Error: Company domain cannot be empty. Setting default to 'decodelabs.tech'")
        company_domain = "decodelabs.tech"

    triage_tool = PhishingTriageToolkit(target_company_domain=company_domain)

    print("\n--------------------------------------------------")

    email_file_path = input("📂 Enter the path to the suspicious email file (.txt): ").strip('\'"')

    print("\n--------------------------------------------------")

    user_url = input("🔗 Enter the URL found in the email (Press Enter to extract automatically): ").strip('\'"')

    try:
        with open(email_file_path, "r", encoding="utf-8") as file:
            real_raw_email = file.read()
        if not user_url:
            print("🔍 No URL entered. Automatically searching inside the email file...")
            url_match = re.search(r'https?://[^\s<>"]+', real_raw_email)
            extracted_url = url_match.group(0) if url_match else ""
        else:
            extracted_url = user_url
        
        if extracted_url:
            print(f"🎯 URL Selected for Analysis: {extracted_url}")
        else:
            print("🎯 No URLs detected or provided.")

        final_decision = triage_tool.process_triage(real_raw_email, extracted_url)
        print(final_decision)

    except FileNotFoundError:
        print(f"❌ Error: Could not find the email file at: {email_file_path}")
        print("Please check the path and try again.")
        
    print("==================================================")