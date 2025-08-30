from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 👇 Owner का Email (जहां message जाएगा)
OWNER_EMAIL = "tusharku509@gmail.com"

# 👇 SMTP Server (Gmail Example)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "tusharku509@gmail.com"   # यहां अपना Gmail डालें
SMTP_PASS = "sfvytjosvgxjpvgp"      # Gmail App Password डालें (normal password नहीं चलेगा)

@app.route("/contact", methods=["POST"])
def contact():
    try:
        # Form values लेना
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # Email Body
        body = f"""
📩 New Contact Form Submission

👤 Name: {name}
📧 Email: {email}
📌 Subject: {subject}
💬 Message:
{message}
"""

        # MIME Setup
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = OWNER_EMAIL
        msg["Reply-To"] = email

        # Send Mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, OWNER_EMAIL, msg.as_string())

        # Success Response
        return render_template_string("""
            <script>alert("✅ Thank you {{name}}! Your message has been sent.");
            window.location.href="/contact.html";</script>
        """, name=name)

    except Exception as e:
        # Error Response
        return render_template_string("""
            <script>alert("❌ Sorry, your message could not be sent.");
            window.location.href="/contact.html";</script>
        """)

if __name__ == "__main__":
    app.run(debug=True)
