# MonitorHeart_POC
A POC to demonstrate a sample heart rate monitoring interface

 1. Install Git

Make sure Git is installed on your system:

git --version

If it's not, install it:

    Ubuntu/Debian: sudo apt install git

    Windows: Install Git from here

    macOS: brew install git (or use the Xcode tools)

✅ 2. Set up Git (First-time only)

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

✅ 3. Create a Python Virtual Environment

# Go to your workspace directory
cd ~/your/project/folder

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate it:
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

✅ 4. Clone a GitHub Repository

You can now clone a repository:

git clone https://github.com/username/repository.git

Example:

git clone https://github.com/pallets/flask.git

This creates a folder named flask (or the repo name).
✅ 5. Navigate to the Cloned Repo and Install Requirements

cd repository/  # replace with actual repo name

# If there's a requirements.txt
pip install -r requirements.txt

✅ 6. Make Changes and Push (Optional)

# Make changes to the code...

# Stage changes
git add .

# Commit them
git commit -m "Made some changes"

# Push (if you have write access)
git push origin main  # or 'master' depending on branch

Use SSH Instead of HTTPS (No password prompts)

    Check if you already have SSH keys

ls ~/.ssh

If you don’t have an id_rsa and id_rsa.pub, generate one:

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

Add your SSH key to GitHub

    Copy your public key:

    cat ~/.ssh/id_rsa.pub

    Go to GitHub → Settings → SSH and GPG keys → New SSH key

    Paste the key and save

Clone the repo using SSH

git clone git@github.com:username/repository.git
