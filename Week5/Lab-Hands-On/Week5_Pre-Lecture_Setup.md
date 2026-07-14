# Week 5 Pre-Lecture Setup

Week 5 covers web development and API design, including building and containerizing a small web service. To spend our class time on the material instead of software installation, please complete the steps below before the lecture,
---

## Step 1: Install Python 3.11 or newer

Check whether you already have a suitable version:

```bash
python3 --version
```

If this returns 3.11 or higher, you are done with this step.

If it returns an older version, or the command is not found, install a current version from [python.org/downloads](https://www.python.org/downloads/). Windows users, during installation, make sure to check the box labeled "Add Python to PATH" before clicking install, this is easy to miss and causes problems later.

Confirm the install:

```bash
python3 --version
pip3 --version
```

Both should return version numbers without errors.

---

## Step 2: Install Docker

Docker lets us package an application together with everything it needs to run, so it behaves the same on every machine. We will use it heavily in this lecture.

### macOS

1. Go to docker.com and download Docker Desktop for Mac, choosing the version that matches your chip (Apple Silicon or Intel, check under the Apple menu, "About This Mac" if you are unsure).
2. Open the downloaded file and drag Docker to your Applications folder.
3. Launch Docker Desktop from Applications. The first launch can take a minute or two. You will know it is ready when the whale icon in your menu bar stops animating.

### Windows

1. Docker Desktop on Windows requires WSL2 (Windows Subsystem for Linux). Open [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6) **as Administrator** and run:
   ```powershell
   wsl --install
   ```
   If it is already installed, this command will tell you so, that is fine.
2. Restart your computer if prompted.
3. Go to docker.com and download Docker Desktop for Windows.
4. Run the installer. Keep the default option to use the WSL2 based engine when asked.
5. Launch Docker Desktop and wait for it to report that it is running.

### Linux

Steps vary slightly by distribution. For Ubuntu or Debian based systems:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

If you are on Fedora, RHEL, Arch, or another distribution, search "install Docker Engine" plus your distribution name for the current official instructions, the overall steps are similar.

Then add yourself to the `docker` group so you do not need `sudo` for every command:

```bash
sudo usermod -aG docker $USER
```

Log out and back in (or restart) for this change to take effect.

---

## Step 3: Verify Docker is working

Run this from any terminal:

```bash
docker run hello-world
```

You should see a message starting with "Hello from Docker!" along with a short explanation of what just happened. If you see that message, Docker is installed and working correctly.

Also confirm Docker Compose is available (it is bundled with current Docker installs, no separate install needed):

```bash
docker compose version
```

This should return a version number.

---

## Docker GPU support

Skip this entire section unless you have been specifically told you will need it, or you know you have an NVIDIA GPU and want to follow along with the GPU portion of the lecture on your own machine.

This requires, in order:

1. An NVIDIA GPU with a current driver installed on your machine (confirm with `nvidia-smi` in a terminal, it should print a status table)
2. The NVIDIA Container Toolkit installed (Linux) or a current NVIDIA driver with WSL2 GPU support (Windows)
3. Verification that Docker can see the GPU:
   ```bash
   docker run --rm --gpus all nvidia/cuda:12.4.1-runtime-ubuntu22.04 nvidia-smi
   ```
   This should print the same GPU status table as running `nvidia-smi` directly.

> This is not supported on Mac, Apple Silicon Macs do not have NVIDIA GPUs. If you are on a Mac, you can still follow the GPU concepts covered in the lecture.

---

## Quick checklist before the lecture

Run these three commands. If all three succeed, you are fully ready.

```bash
python3 --version
pip3 --version
docker run hello-world
```

---