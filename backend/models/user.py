from mongoengine import Document, StringField, BooleanField, ValidationError
import re

# Custom validators for email and roll number
def email_validator(value):
    if value and not re.match(r"^\S+@\S+\.\S+$", value):
        raise ValidationError(f"{value} is not a valid email format!")

def roll_number_validator(value):
    if value and not re.match(r"^\d+$", value):
        raise ValidationError(f"{value} is not a valid roll number format!")

# User model
class User(Document):
    email = StringField(unique=True, sparse=True, validators=[email_validator])
    rollNumber = StringField(unique=True, sparse=True, validators=[roll_number_validator])
    password = StringField(required=True)
    
    meta = {
        'timestamps': True
    }
