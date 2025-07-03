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

1. Use SSH Instead of HTTPS (No password prompts)

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

- 🔒 HTTPS with PAT

✅ Best if:

    You want quick, one-time access.

    You're using GitHub on a new device and don’t want to set up SSH yet.

    You're working behind a firewall or corporate proxy that blocks SSH.

❌ Downsides:

    You’ll need to use (or re-enter) your token often unless you cache it.

    Typing/pasting long tokens can be annoying and insecure if not managed well.

🔑 SSH

✅ Best if:

    You use GitHub regularly.

    You want passwordless, secure push/pull operations.

    You’re using automation, scripts, or working with private repos frequently.

    You want more convenience in the long term.

❌ Downsides:

    Slightly more setup at the beginning (generate and add SSH key).

    Requires adding the SSH key to GitHub and configuring the remote URL.

🌟 Recommendation: Use SSH

For developers, regular coders, or anyone managing multiple repositories, SSH is the better long-term choice — it’s more secure, easier to use after setup, and doesn’t require re-authentication.

- Testing SSH
Tip: Test SSH Connection Anytime

You can verify your connection with:

ssh -T git@github.com

- When you run:

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

It’s prompting you to specify where to save the SSH key.

- What You Should Do:

    If this is your first SSH key, just press Enter to accept the default path:

/home/yourname/.ssh/id_rsa

That will create:

    /home/yourname/.ssh/id_rsa → your private key

    /home/yourname/.ssh/id_rsa.pub → your public key (this is the one you upload to GitHub)

- After Key is Created:

    Add your SSH key to the SSH agent:

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

Copy your public key to paste into GitHub:

cat ~/.ssh/id_rsa.pub

Copy the output and add it to GitHub > Settings > SSH and GPG keys

- This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?

ChatGPT said:

That message is completely safe and expected the first time you connect to a new host (like GitHub) via SSH.
🔒 Why you're seeing this:

When you use SSH to connect to a server for the first time (e.g., git@github.com), your system has never seen that server’s public fingerprint before, so it asks:

    “Are you sure this is the server you mean to connect to?”

This is to protect against man-in-the-middle attacks.
✅ What to do:

Just type:

yes

Then hit Enter.

After this, the server's fingerprint will be saved in your ~/.ssh/known_hosts file, so the system won’t ask again next time.

Let me know if you want to confirm the GitHub fingerprint before proceeding (for security).

- 1. {{ }} is Jinja2 syntax, not raw HTML

    Jinja2 is the templating engine used by Flask.

    It allows you to write Python-like expressions inside HTML files.

2. url_for() is a Flask function, not HTML

    It's used to generate URLs dynamically.

    In this case, it finds the correct path to your static JavaScript file.

- The src attribute in an HTML <script> tag can absolutely point to a webpage if that page serves a JavaScript file.

In this case:

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

You're telling the browser:

    "Load and execute the JavaScript code that is hosted at this URL."

This is called a Content Delivery Network (CDN) link. It’s a common way to include popular libraries (like Chart.js, jQuery, etc.) without downloading them yourself. The browser fetches the JS file from the URL and uses it like any other script.
Advantages:

    No need to download or serve the file yourself.

    Often faster due to CDN caching.

    Great for quick prototyping or simple projects.

- Issue : There are duplicates being printed. Turns out that the setInterval() function (In script.js) and the schedule.run_pending() time.sleep(1) function in the Main.py file are causing a race around condition.

🧨 What's Happening:
⚙️ 1. Python: schedule.run_pending() + time.sleep(1)

    This executes the scheduled task (like generating new BPM data) once per second.

    Let's say every 1 second, your sensor appends one new BPM value to a list for a user.

🌐 2. JavaScript: setInterval(..., 1000)

    This fetches the data from the server every 1 second and updates the chart and display.

🔁 Problem: Timing Overlap

When both are synced too closely, this happens:

    At t = 2s, your Python sensor adds BPM = 90

    At the same t = 2s, the JavaScript fetch() call triggers, getting the updated array (now including 90)

    But in the next second, if your fetch() happens slightly after the next sensor update (due to processing lag, network latency, etc.), you may receive two values instead of one, or catch a partially updated list

    This can lead to:

        Duplicated BPM values displayed

        Skipped values

        Out-of-sync chart vs. text

        Appended old data repeatedly, especially if you’re tracking count and misalign due to a race condition

So what i did is just compare the time stamps and ensure that duplicates don't get printed, because the time stamps associated with the bpm remains the same throughout (the issue is being mainly caused by the js code, not the backend).

- What’s happening in each case?
✅ bpmAnomalySimulation (without parentheses)

You're passing a reference to the function, which tells the browser:

    "When this button is clicked, call this function."

So the function is called only when the event happens (on click), which is what you want.
❌ bpmAnomalySimulation() (with parentheses)

You're calling the function immediately, at the time of setting up the listener — not when the button is clicked.

And whatever value that function returns (probably undefined) is what gets passed to addEventListener. So you're effectively doing this:

anomalyButton.addEventListener("click", undefined); // <-- No function left to run

So:

    The function runs once immediately.

    After that, there's no click handler left attached.

    So nothing happens when you click the button.

🧠 Rule of Thumb

    Never use parentheses when passing a function to addEventListener.

Unless you're using an anonymous function, like this:

anomalyButton.addEventListener("click", () => bpmAnomalySimulation(uid));

This is okay if you want to pass parameters or wrap something custom.
✅ Correct Examples

// Simple reference
element.addEventListener("click", myFunction);

// Anonymous wrapper if passing arguments
element.addEventListener("click", () => myFunction(42));
