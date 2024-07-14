from flask import Blueprint, render_template, request, jsonify
from flask_mail import Message, Mail
from flask_babel import _
from os import getenv
from datetime import datetime
from src.models import Event, Guide

router = Blueprint('router', __name__)
mail = Mail()


@router.route("/<lang>/")
def index(lang):
    events = Event.query.all()

    context = {
        "title": _("Find Your Guide | Home Page"),
        "events": events
    }
    return render_template("index.html", **context)


@router.route("/<lang>/about")
def about(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | About")
    })
    return render_template("about.html", **context)


@router.route("/<lang>/contact")
def contact(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | Contact")
    })
    return render_template("contact.html", **context)


@router.route("/<lang>/guides")
def guides(lang):
    guides = Guide.query.all()  # Fetch all guides from the database

    locations = {guide.location for guide in guides}
    languages = {
        language for guide in guides for language in guide.languages.split(', ')}

    context = {
        "title": _("Find Your Guide | Guides"),
        "guides": guides,
        "languages": sorted(languages),
        "locations": sorted(locations),
        # Add WhatsApp number from environment variables
        "whatsapp_number": getenv("WHATSAPP_NUMBER")
    }
    return render_template("guides.html", **context)


@router.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json()
    contact_info = data.get('contact')

    if not contact_info:
        return jsonify({'success': False, 'message': 'No contact info provided'})

    html_content = f"""
    <html>
      <body>
        <h2 style="color: #2E86C1;">Find Your Guide | Contact Info</h2>
        <p>We have received the following contact info:</p>
        <div style="border: 1px solid #ddd; padding: 10px; background-color: #f9f9f9;">
          {contact_info}
        </div>
      </body>
    </html>
    """

    msg = Message(
        'Find Your Guide | Contact Info',
        recipients=[getenv("TO_EMAIL")],
        html=html_content
    )

    try:
        mail.send(msg)
        print(f'Received contact info: {contact_info}')
        return jsonify({'success': True})
    except Exception as e:
        print(f'Error sending email: {e}')
        return jsonify({'success': False, 'message': 'Failed to send email'})


@router.route('/api/contact_form', methods=['POST'])
def api_contact_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'success': False, 'message': _('All fields are required')})

    html_content = f"""
    <html>
    <head>
        <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}
        .header {{
            background-color: #2E86C1;
            color: #ffffff;
            padding: 10px 0;
            text-align: center;
            border-radius: 5px 5px 0 0;
        }}
        .header h2 {{
            margin: 0;
            font-size: 24px;
        }}
        .content {{
            padding: 20px;
        }}
        .content p {{
            margin: 10px 0;
        }}
        .content .label {{
            font-weight: bold;
            color: #2E86C1;
        }}
        .footer {{
            text-align: center;
            padding: 10px 0;
            font-size: 12px;
            color: #777777;
            border-top: 1px solid #e0e0e0;
            margin-top: 20px;
        }}
        </style>
    </head>
    <body>
        <div class="container">
        <div class="header">
            <h2>Find Your Guide | New Contact Message</h2>
        </div>
        <div class="content">
            <p>You have received a new message from your website contact form:</p>
            <p><span class="label">Name:</span> {name}</p>
            <p><span class="label">Email:</span> {email}</p>
            <p><span class="label">Message:</span> {message}</p>
        </div>
        <div class="footer">
            <p>&copy; {datetime.now().year} Find Your Guide. All rights reserved.</p>
        </div>
        </div>
    </body>
    </html>
    """

    msg = Message(
        'Find Your Guide | New Contact Message',
        recipients=[getenv("TO_EMAIL")],
        html=html_content
    )

    try:
        mail.send(msg)
        print(f'Received contact form message from: {name} ({email})')
        return jsonify({'success': True, 'message': _('Your message has been sent successfully.')})
    except Exception as e:
        print(f'Error sending email: {e}')
        return jsonify({'success': False, 'message': _('Failed to send message')})
