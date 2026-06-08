# Lab Take-Home Assignment: Submission Instructions

> **Module:** Advanced Python for Data Science

> **Submission Method:** Private GitHub Repository

> **Collaborator to Add:** `mobashgr`

---

## Before You Begin Read Carefully

Each student must maintain their **own individual private GitHub repository** for submitting weekly lab take-home assignments. This repository is **yours alone**. Do not share it with other students or make it **public**.

Dr. Ghadeer Mobasher will access your work by being added as a collaborator (see instructions below). 

> You may re-use the same private repository from the Python Foundations module. **However, you need to reorganise it by creating a new directory for this module**. Otherwise, please follow the instructions below.

---

## Required Repository Structure

Your repository must follow this **exact folder structure**. Each folder corresponds to one week's take-home lab assignment:

```
[your-student-id]-python-ds-labs/
│
├── README.md                              ← Brief description of your repo (see template below)
│
├── Week1-lab-take-home-assignment/
│   └── [your work files here]
│
├── Week2-lab-take-home-assignment/
│   └── [your work files here]
│
├── Week3-lab-take-home-assignment/
│   └── [your work files here]
│
├── Week4-lab-take-home-assignment/
│   └── [your work files here]
│
├── Week5-lab-take-home-assignment/
│   └── [your work files here]
│
├── Week6-lab-take-home-assignment/
   └── [your work files here]
```

> **Naming convention is strict.** Folder names must match exactly as shown above (capitalisation, hyphens, no spaces).

---

## Step-by-Step Setup Guide

Follow these steps **once at the beginning of the module** (Week 1). You will reuse this repository for all 6 weeks.

---

### Step 1: Create a GitHub Account

If you don't already have one, go to [github.com](https://github.com) and sign up for a free account. Use a professional username (e.g., your name or student ID).

---

### Step 2: Create a New Private Repository

1. Log in to GitHub and click the **`+`** icon in the top-right corner → **"New repository"**
2. Fill in the details:
   - **Repository name:** `[your-student-id]-python-ds-labs`
     *(e.g., `s12345678-python-ds-labs`)*
   - **Description:** `Lab take-home assignments for Python Foundations for Data Science`
   - **Visibility:** Select **Private**
   - **Initialise this repository with:** Tick **"Add a README file"**
3. Click **"Create repository"**
---

### Step 3: Add `mobashgr` as a Collaborator

This step is **mandatory**. Without it, your assignments cannot be accessed.

1. Go to your repository on GitHub
2. Click **"Settings"** (top navigation bar of the repository)
3. In the left sidebar, click **"Collaborators"** (under *Access*)
4. Click **"Add people"**
5. Search for **`mobashgr`** and select the correct account
6. Click **"Add mobashgr to this repository"**

> The collaborator will receive an email invitation. You do not need to do anything further.

---

### Step 4: Install Git on Your Computer

> Skip this step if Git is already installed. To check, open your terminal and run: `git --version`

- **Windows:** Download from [git-scm.com](https://git-scm.com/downloads) and follow the installer
- **macOS:** Run `xcode-select --install` in the Terminal, or download from [git-scm.com](https://git-scm.com/downloads)
- **Linux (Ubuntu/Debian):** Run `sudo apt install git` in the terminal

After installing, configure your identity (run these once):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-github-email@example.com"
```

---

### Step 5: Clone Your Repository to Your Local Machine

"Cloning" downloads your GitHub repository to your computer so you can work on it locally.

1. Go to your repository on GitHub
2. Click the green **`<> Code`** button
3. Copy the **HTTPS** URL (it will look like `https://github.com/your-username/your-repo-name.git`)
4. Open your **Terminal** (macOS/Linux) or **Git Bash** (Windows)
5. Navigate to where you want to store your work, for example:

```bash
cd ~/Documents/Masters/
```

6. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

7. Move into the newly created folder:

```bash
cd your-repo-name
```

---

### Step 6: Create the Weekly Folders

Inside your cloned repository folder, create all 6 weekly folders at once. Run the following in your terminal:

```bash
mkdir Week1-lab-take-home-assignment
mkdir Week2-lab-take-home-assignment
mkdir Week3-lab-take-home-assignment
mkdir Week4-lab-take-home-assignment
mkdir Week5-lab-take-home-assignment
mkdir Week6-lab-take-home-assignment
```

> **GitHub does not track empty folders. Add a placeholder file to each so they appear in your repository**:
### Linux or macOS (Bash)
```bash
for i in 1 2 3 4 5 6; do
  touch "Week${i}-lab-take-home-assignment/.gitkeep"
done
```
### Windows: Option (1)
If you are using Git Bash (installed with Git), you can run the same command as above:
```bash
for i in 1 2 3 4 5 6; do
  touch "Week${i}-lab-take-home-assignment/.gitkeep"
done
```
### Windows: Option (2)
If you are using Command Prompt
```bash
for %i in (1 2 3 4 5 6) do type nul > Week%i-lab-take-home-assignment\.gitkeep
```

### Windows: Option (3)
If you are using PowerShell
```bash
1..6 | ForEach-Object {
    New-Item "Week$_-lab-take-home-assignment/.gitkeep" -ItemType File
}
```
Then push the structure to GitHub (see the next section for a full explanation of each command):

```bash
git add .
git commit -m "Initial setup: added all 6 weekly lab folders"
git push origin main
```

---

## How to Submit Each Week's Assignment

At the end of each week, follow these steps to submit your completed lab work.

### Step 1: Add your completed files to the correct week's folder

Place your `.ipynb` notebook (and any supporting files) inside the corresponding weekly folder. For example, for Week 3:

```
Week3-lab-take-home-assignment/
└── Week3_lab_solution.ipynb
```

### Step 2: Open your terminal and navigate to your repository

```bash
cd ~/Documents/Masters/your-repo-name
```

### Step 3: Stage your changes

This tells Git which files you want to include in the next save point (commit):

```bash
git add Week3-lab-take-home-assignment/
```

Or to stage all changes at once:

```bash
git add .
```

### Step 4: Commit your changes

A commit is a labelled save point with a message describing what changed:

```bash
git commit -m "Submit Week 3 lab take-home assignment"
```

> **Good commit messages** are short and descriptive. They help you (and the marker) understand what was submitted and when.

### Step 5: Push to GitHub

This uploads your commit from your local machine to GitHub, making it visible to the teaching team:

```bash
git push origin main
```

> If prompted, enter your GitHub username and password. If GitHub asks for a token instead of a password, see [Creating a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

### Step 6: Verify your submission

1. Go to your repository on GitHub in your browser
2. Navigate to the correct weekly folder
3. Confirm your files are visible and up to date

> If your files appear on GitHub, your submission is complete. No additional form or email is required.

---

## Quick Reference: Weekly Submission Cheatsheet

```bash
# 1. Navigate into your repo
cd ~/path/to/your-repo-name

# 2. Stage your work
git add Week[N]-lab-take-home-assignment/

# 3. Commit with a clear message
git commit -m "Submit Week [N] lab take-home assignment"

# 4. Push to GitHub
git push origin main
```

---

## Common Issues & Fixes

| Problem | Likely Cause | Fix |
|--------|-------------|-----|
| `git: command not found` | Git not installed | Follow Step 4 above |
| `Permission denied` | Wrong repository URL or not logged in | Check your GitHub login; use HTTPS not SSH |
| `fatal: not a git repository` | You're in the wrong folder | Run `cd your-repo-name` first |
| `rejected — non-fast-forward` | Changes exist on GitHub, not on your machine | Run `git pull origin main` first, then push again |
| Files not showing on GitHub | You forgot to push | Run `git push origin main` |
| Collaborator can't see your repo | Invite not accepted or wrong username | Re-check `mobashgr` is added under Settings → Collaborators |

---

## Repository README Template

Replace the contents of the `README.md` in **your submission repository** with the following:

```markdown
# Python Foundations for Data Science: Lab Take-Home Assignments

**Student Name:** [Your Full Name]
**Student ID:** [Your Student ID]
---

## Repository Structure

This private repository contains my individual lab take-home assignment submissions
for the module *Python Foundations for Data Science*.

| Folder | Contents |
|--------|---------|
| Week1-lab-take-home-assignment | Week 1 lab submission |
| Week2-lab-take-home-assignment | Week 2 lab submission |
| Week3-lab-take-home-assignment | Week 3 lab submission |
| Week4-lab-take-home-assignment | Week 4 lab submission |
| Week5-lab-take-home-assignment | Week 5 lab submission |
| Week6-lab-take-home-assignment | Week 6 lab submission |

---

> This repository is private. Collaborator access has been granted to the module instructor.
```

---

## Submission Deadlines

| Assignment | Deadline |
|------------|----------|
| Week 1 Lab Take-Home |TBD|
| Week 2 Lab Take-Home |TBD|
| Week 3 Lab Take-Home |TBD |
| Week 4 Lab Take-Home |TBD |
| Week 5 Lab Take-Home |TBD |
| Week 6 Lab Take-Home |TBD|

> The timestamp of your **last commit before the deadline** will be used as your submission time.

---

*For questions about submissions, contact [Ghadeer Mobasher](mailto:ghadeer.mobasher@srh-hochschulen.de).*
