import os
from datetime import datetime, timedelta

# Set the start date and number of days to commit
start_date = datetime(2024, 12, 1)
days_to_commit = 30

for i in range(days_to_commit):
    commit_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit --allow-empty --date="{commit_date}" -m "Backdated commit on {commit_date}"')

os.system("git push origin main")
