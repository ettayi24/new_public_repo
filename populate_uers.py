import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'level2_pro.settings')


import django
django.setup()  # allow to us to populate database

from baseapp.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):

    for entery in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakegen.email()

        #new entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__=='__main__':
    print('populating database')
    populate(20)
    print('population completed')
