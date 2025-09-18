import  re

def extract_contact_info(text):
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone=re.findall(r"(?:(?:\+880)|0)?1[1-9]\d{8}", text)
    name = re.findall(r"(^[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2})", text)

    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
    }
