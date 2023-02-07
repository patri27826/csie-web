# %%
from django.contrib.auth.models import User
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('Member_user.xlsx')

# %%
for index, row in excel_data.iterrows():
    
    try:
        user = User.objects.create_user(username=row["username"],
                                 password=row["password"], is_staff=True)
        print(f'Add user:{row["username"]},  PW:{row["password"]}')
    except:
        print(f'Fail:{row["username"]}')
# %%
