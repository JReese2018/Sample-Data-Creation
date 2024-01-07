import pandas as pd
from random import randint
from faker import Faker
fake = Faker()

### Core Balance Fake Info
df = pd.read_csv(r'C:\Users\jason\Desktop\Dummy Data\sample_balance_core_services_data.csv')

## Replacing Store code with SAMPLE
sample_store_code = []
for _ in range(157):
    sample_store_code.append('SAMPLE')
df['Fake Studio Name'] = sample_store_code

df = df.drop(columns=['Studio Name'])
df = df[['Fake Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Studio Name' : 'Studio Name'})

## Create Fake names using Faker
fake_names = []
for _ in range(157):
    fake_names.append(fake.name())
df['Full Fake Name'] = fake_names

df = df.drop(columns=['Full Name'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Fake Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Full Fake Name' : 'Full Name'})

## Creating fake emails using Faker
fake_email = []
for _ in range(157):
   fake_email.append(fake.free_email())
df['Fake Email'] = fake_email

df = df.drop(columns=['Email'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Fake Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Email' : 'Email'})

## Creating fake Phone Numbers using random
fake_number = []
for _ in range(157):
    fake_number.append(randint(1000000000,9999999999))
df['Fake Phone'] = fake_number

df = df.drop(columns=['Phone #'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Fake Phone', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Phone' : 'Phone #'})

## Creating fake Client IDs using radom
fake_id = []
for _ in range(157):
    fake_id.append(randint(0,2397847))
df['Fake Client ID'] = fake_id

df = df.drop(columns=['Client ID'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Fake Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Client ID' : 'Client ID'})

core_df = df

#core_df.to_csv('starter_sample_balance_core_services_data.csv')



### Medical Balance Fake Info
df = pd.read_csv(r'C:\Users\jason\Desktop\Dummy Data\sample_balance_medical_services_data.csv')

## Replacing Store code with SAMPLE
sample_store_code = []
for _ in range(132):
    sample_store_code.append('SAMPLE')
df['Fake Studio Name'] = sample_store_code

df = df.drop(columns=['Studio Name'])
df = df[['Fake Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Studio Name' : 'Studio Name'})

## Create Fake names using Faker
fake_names = []
for _ in range(132):
    fake_names.append(fake.name())
df['Full Fake Name'] = fake_names

df = df.drop(columns=['Full Name'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Fake Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Full Fake Name' : 'Full Name'})

## Creating fake emails using Faker
fake_email = []
for _ in range(132):
   fake_email.append(fake.free_email())
df['Fake Email'] = fake_email

df = df.drop(columns=['Email'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Fake Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Email' : 'Email'})

## Creating fake Phone Numbers using random
fake_number = []
for _ in range(132):
    fake_number.append(randint(1000000000,9999999999))
df['Fake Phone'] = fake_number

df = df.drop(columns=['Phone #'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Fake Phone', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Phone' : 'Phone #'})

## Creating fake Client IDs using radom
fake_id = []
for _ in range(132):
    fake_id.append(randint(0,2397847))
df['Fake Client ID'] = fake_id

df = df.drop(columns=['Client ID'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Fake Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Client ID' : 'Client ID'})

medical_df = df

#medical_df.to_csv('starter_sample_balance_medical_services_data.csv')



### Skin Balance Fake Info
df = pd.read_csv(r'C:\Users\jason\Desktop\Dummy Data\sample_balance_skin_services_data.csv')

## Replacing Store code with SAMPLE
sample_store_code = []
for _ in range(65):
    sample_store_code.append('SAMPLE')
df['Fake Studio Name'] = sample_store_code

df = df.drop(columns=['Studio Name'])
df = df[['Fake Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Studio Name' : 'Studio Name'})

## Create Fake names using Faker
fake_names = []
for _ in range(65):
    fake_names.append(fake.name())
df['Full Fake Name'] = fake_names

df = df.drop(columns=['Full Name'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Fake Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Full Fake Name' : 'Full Name'})

## Creating fake emails using Faker
fake_email = []
for _ in range(65):
   fake_email.append(fake.free_email())
df['Fake Email'] = fake_email

df = df.drop(columns=['Email'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Fake Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Email' : 'Email'})

## Creating fake Phone Numbers using random
fake_number = []
for _ in range(65):
    fake_number.append(randint(1000000000,9999999999))
df['Fake Phone'] = fake_number

df = df.drop(columns=['Phone #'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Client ID', 'Full Name', 'Email', 'Fake Phone', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Phone' : 'Phone #'})

## Creating fake Client IDs using random
fake_id = []
for _ in range(65):
    fake_id.append(randint(0,2397847))
df['Fake Client ID'] = fake_id

df = df.drop(columns=['Client ID'])
df = df[['Studio Name', 'Day of Issue Date', 'Day of Expire Date', 'Fake Client ID', 'Full Name', 'Email', 'Phone #', 'Business Category', 'Credit Source', 'Credit Description', 'Initial Credit Count', 'Used Credit Count', 'Remaining Credits', 'Index', 'Max date']]
df = df.rename(columns={'Fake Client ID' : 'Client ID'})

skin_df = df

#skin_df.to_csv('starter_sample_balance_skin_services_data.csv')

### 3 for 50 Fake Info

df = pd.read_csv(r'C:\Users\jason\Desktop\Dummy Data\sample_3_for_50_data.csv')

## Replacing Studio Code with SAMPLE
sample_store_code = []
for _ in range(1788):
    sample_store_code.append('SAMPLE')
df['Fake Studio Code'] = sample_store_code

df = df.drop(columns=['Studio Code'])
df = df[['Fake Studio Code', 'Purchase Date', 'Invoice ID', 'Client ID', 'First Name', 'Last Name', 'Email', 'Phone #', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake Studio Code' : 'Studio Code'})

## Creating new first name using Faker
fake_first_names = []
for _ in range(1788):
    fake_first_names.append(fake.first_name())
df['Fake First Name'] = fake_first_names

df = df.drop(columns=['First Name'])
df = df[['Studio Code', 'Purchase Date', 'Invoice ID', 'Client ID', 'Fake First Name', 'Last Name', 'Email', 'Phone #', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake First Name' : 'First Name'})

## Creating new last name using Faker
fake_last_names = []
for _ in range(1788):
    fake_last_names.append(fake.last_name())
df['Fake Last Name'] = fake_last_names

df = df.drop(columns=['Last Name'])
df = df[['Studio Code', 'Purchase Date', 'Invoice ID', 'Client ID', 'First Name', 'Fake Last Name', 'Email', 'Phone #', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake Last Name' : 'Last Name'})

## Creating new email using Faker
fake_emails = []
for _ in range(1788):
    fake_emails.append(fake.email())
df['Fake Email'] = fake_emails

df = df.drop(columns=['Email'])
df = df[['Studio Code', 'Purchase Date', 'Invoice ID', 'Client ID', 'First Name', 'Last Name', 'Fake Email', 'Phone #', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake Email' : 'Email'})

## Creating new phone number using random
fake_number = []
for _ in range(1788):
    fake_number.append(randint(1000000000,9999999999))
df['Fake Phone'] = fake_number

df = df.drop(columns=['Phone #'])
df = df[['Studio Code', 'Purchase Date', 'Invoice ID', 'Client ID', 'First Name', 'Last Name', 'Email', 'Fake Phone', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake Phone' : 'Phone #'})

## Creating new client ID using
fake_id = []
for _ in range(1788):
    fake_id.append(randint(0,2397847))
df['Fake Client ID'] = fake_id

df = df.drop(columns=['Client ID'])
df = df[['Studio Code', 'Purchase Date', 'Invoice ID', 'Fake Client ID', 'First Name', 'Last Name', 'Email', 'Phone #', 'Therapy Category', 'Business Category', 'Item', 'Sales Rep', 'Autopay Status', 'Quantity', 'Tax Amount', 'Discount', 'Credit Used', 'Unnamed: 17']]
df = df.rename(columns={'Fake Client ID' : 'Client ID'})

df_3_for_50 = df

print(df_3_for_50)

df_3_for_50.to_csv('starter_sample_3_for_50 _data.csv')