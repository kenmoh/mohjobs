
from django.db import models

STATE_CHOICES = (
    ('---------', '---------'),
    ('Abuja', 'Abuja'),
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Anambra', 'Anambra'),
    ('Awka', 'Awka'),
    ('akwa ibom', 'Akwa Ibom'),
    ('Bauch', 'Bauchi'),
    ('Bayelsa', 'Bayelsa'),
    ('Benue', 'Benue'),
    ('Borno', 'Borno'),
    ('Cross river', 'Cross River'),
    ('Delta', 'Delta'),
    ('Ebonyi', 'Ebonyi'),
    ('Enugu', 'Enugu'),
    ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'),
    ('Gombe', 'Gombe'),
    ('Imo', 'Imo'),
    ('Jigawa', 'Jigawa'),
    ('Kaduna', 'Kaduna'),
    ('Kano', 'Kano'),
    ('Katsina', 'Katsina'),
    ('Kebbi', 'Kebbi'),
    ('Kogi', 'Kogi'),
    ('Kwara', 'Kwara'),
    ('Lagos', 'Lagos'),
    ('Nasarawa', 'Nasarawa'),
    ('Niger', 'Niger'),
    ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'),
    ('Osun', 'Osun'),
    ('Oyo', 'Oyo'),
    ('Plateau', 'Plateau'),
    ('Rivers', 'Rivers'),
    ('Sokoto', 'Sokoto'),
    ('Taraba', 'Taraba'),
    ('Yobe', 'Yobe'),
    ('Zamfara', 'Zamfara')
)


LOCATION_CHOICES = {
    'Abuja': 'Abuja',
    'Abia': 'Abia',
    'Adamawa': 'Adamawa',
    'Anambra': 'Anambra',
    'Awka': 'Awka',
    'akwa ibom': 'Akwa Ibom',
    'Bauch': 'Bauchi',
    'Bayelsa': 'Bayelsa',
    'Benue': 'Benue',
    'Borno': 'Borno',
    'Cross river': 'Cross River',
    'Delta': 'Delta',
    'Ebonyi': 'Ebonyi',
    'Enugu': 'Enugu',
    'Edo': 'Edo',
    'Ekiti': 'Ekiti',
    'Gombe': 'Gombe',
    'Imo': 'Imo',
    'Jigawa': 'Jigawa',
    'Kaduna': 'Kaduna',
    'Kano': 'Kano',
    'Katsina': 'Katsina',
    'Kebbi': 'Kebbi',
    'Kogi': 'Kogi',
    'Kwara': 'Kwara',
    'Lagos': 'Lagos',
    'Nasarawa': 'Nasarawa',
    'Niger': 'Niger',
    'Ogun': 'Ogun',
    'Ondo': 'Ondo',
    'Osun': 'Osun',
    'Oyo': 'Oyo',
    'Plateau': 'Plateau',
    'Rivers': 'Rivers',
    'Sokoto': 'Sokoto',
    'Taraba': 'Taraba',
    'Yobe': 'Yobe',
    'Zamfara': 'Zamfara'
}



STATUS_CHOICES = (
    ('---------', '---------'),
    ('is_employer','Employer'),
    ('is_freelancer','Freelancer/Applicant')
)


status_choices = {
    'is_employer':'Employer',
    'is_freelancer':'Freelancer/Applicant'
}


JOB_STATUS = (
    ('---------', '---------'),
    ('Draft','Draft'),
    ('publish','Publish')
    )



job_status = {
    'is_draft':'Draft',
    'is_publish':'Publish'
}

