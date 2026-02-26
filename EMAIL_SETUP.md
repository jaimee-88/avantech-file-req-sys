# Email Setup Instructions

## Overview
Email sending functionality has been added to your Django application. The system uses Django's built-in email backend with SMTP.

## Configuration

### 1. Install `.env` File
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

### 2. Configure Email Settings
Edit the `.env` file with your email provider credentials:

**For Gmail:**
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

**To use Gmail:**
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Use the app password in `EMAIL_HOST_PASSWORD`

### 3. For Other Email Providers

**Outlook/Hotmail:**
```
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

**SendGrid:**
```
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
```

**AWS SES:**
```
EMAIL_HOST=email-smtp.region.amazonaws.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

## Contact Form

The contact form is available at: `/contact/`

### Features:
- Form validation (name, email, subject, message)
- Email sending to your configured email address
- Success/error messages displayed to the user
- CSRF protection
- Bootstrap styling

## Testing Email in Development

You can test email sending without a real email provider using Django's console backend:

Add to your `.env` file:
```
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

This will print emails to the console instead of sending them.

## Files Modified/Created:

- `myproject/settings.py` - Email configuration added
- `demo/forms.py` - ContactForm created
- `demo/views.py` - contact view added
- `demo/urls.py` - contact URL pattern added
- `templates/contact.html` - Contact form template
- `templates/home.html` - Updated with contact link
- `.env.example` - Email configuration template

## Security Notes

- Never commit the `.env` file to version control
- Always use App Passwords for Gmail, not your actual password
- Disable "Less secure app access" if not using App Passwords
- In production, use environment variables or AWS Secrets Manager

## Troubleshooting

### "SMTPAuthenticationError"
- Verify your email credentials
- For Gmail, ensure you're using an App Password, not your regular password
- Check that you've enabled 2FA on your Gmail account

### "SMTPException: SMTP AUTH extension not supported"
- Your email provider may not support SMTP
- Try a different SMTP server

### Emails not sending in production
- Check firewall/port settings (port 587 should be open)
- Some hosting providers block outgoing SMTP - consider using SendGrid or AWS SES
- Enable debug mode temporarily to see error messages
