from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from utils.parse import get_rates
from utils.send_emails import send_emails

def main():
    try:
        # Step 1: Fetch data from RBI website
        rate_data = get_rates()
        print("✅ Successfully retrieved RBI rate data")
        
        # Step 2: Prepare template context
        context = {
            'data': rate_data,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M %Z")
        }

        # Step 3: Render HTML template
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("templates/template.html")
        rendered_html = template.render(**context)
        print("✨ Email template rendered successfully")

        # Step 4: Send emails
        recipients = [
            "financial.team@company.com",
            "analytics@org.in",
            "stakeholder@example.com"
        ]
        
        send_emails(
            html_content=rendered_html,
            recipients=recipients,
            subject="Latest RBI Financial Rates Update"
        )
        print(f"📨 Successfully sent to {len(recipients)} recipients")

    except Exception as e:
        print(f"❌ Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()
