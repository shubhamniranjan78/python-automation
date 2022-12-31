import os
import subprocess
from datetime import datetime, timedelta

# Configuration
REPO_DIR = "."  # Use the current directory or specify your repo's path
START_DATE = "2023-01-01"  # Start date for commits
END_DATE = "2023-12-31"  # End date for commits
MESSAGE_POOL = [
    "Refactored code for better performance",
    "Fixed a bug in the deployment script",
    "Added feature: user authentication",
    "Updated README.md with instructions",
    "Optimized API response times",
    "Wrote unit tests for new features",
    "Improved logging and error handling",
    "Cleaned up unused imports",
    "Added Docker support for project",
]

# Function to run git commands
def run_git_command(command):
    try:
        subprocess.run(command, check=True, shell=True, cwd=REPO_DIR)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Generate commits
def generate_commits(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)

    while start <= end:
        # Randomize number of commits per day (0 to 3)
        num_commits = min(3, max(0, hash(start.day) % 4))
        for _ in range(num_commits):
            message = MESSAGE_POOL[hash(str(start)) % len(MESSAGE_POOL)]
            run_git_command(f'git commit --allow-empty --date "{start.strftime("%Y-%m-%d %H:%M:%S")}" -m "{message}"')
        start += delta

# Main execution
if __name__ == "__main__":
    print(f"Generating commits from {START_DATE} to {END_DATE}...")
    generate_commits(START_DATE, END_DATE)
    run_git_command("git push origin main")  # Push changes to the remote repository
    print("Commits generated and pushed successfully!")

import os
from datetime import datetime, timedelta

# Set the start date and number of days to commit
start_date = datetime(2024, 12, 1)
days_to_commit = 30

for i in range(days_to_commit):
    commit_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit --allow-empty --date="{commit_date}" -m "Backdated commit on {commit_date}"')

os.system("git push origin main")
