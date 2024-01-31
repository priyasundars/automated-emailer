from jinja2 import Environment, FileSystemLoader
from utils.parse import get_rates
from utils.send_emails import send_emails


def main():
    # Step 1: Fetch data from the website
    data = get_rates()

    # Step 2: Render the data in a template
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("templates/template.html")
    rendered_html = template.render(data=data)

    # Step 3: Send the rendered HTML via email
    recipients = ["recipent1,recipient2"]
    try:
        send_emails(rendered_html, recipients)
        print("Emails sent successfully!")
    except Exception as e:
        print("Error sending emails:", str(e))

    # Step 4: Additional processing or actions
    # You can add any additional processing or actions you need here


# Call the main function
main()
