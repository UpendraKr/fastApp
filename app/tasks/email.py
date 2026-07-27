def send_email(to, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        to (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Here you would implement the actual email sending logic,
    # such as using an SMTP server or an email-sending service.
    try:
        # Example placeholder for sending email logic
        print(f"--------------------->Sending email to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # Assume email is sent successfully
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False