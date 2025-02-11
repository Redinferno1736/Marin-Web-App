# Marin Web App

**Marin** is a personal assistant web application that allows users to perform tasks like searching the web, playing YouTube videos, opening apps/folders, and controlling system settings (volume and brightness) using text or voice commands.

---

## Table of Contents
1. [Features](#features)
2. [How to Access the Website](#how-to-access-the-website)
3. [How to Use the Website](#how-to-use-the-website)
   - [Text Commands](#text-commands)
   - [Voice Commands](#voice-commands)
4. [Deployment](#deployment)
5. [Local Setup](#local-setup)
6. [Dependencies](#dependencies)

---

## Features
- **Search the Web**: Perform Google searches directly from the app.
- **Play YouTube Videos**: Search and play YouTube videos.
- **Open Apps/Folders**: Launch built-in Windows apps or open folders on your system.
- **Control System Settings**: Adjust system volume and screen brightness.
- **User Authentication**: Register, log in, and log out securely.

---

## How to Access the Website
1. **Deployed Version**:
   - Visit the deployed website on Render: [Marin Web App](#) (replace with your Render URL).
   - Register a new account or log in with existing credentials.

2. **Local Setup**:
   - Follow the [Local Setup](#local-setup) instructions to run the app on your machine.

---

## How to Use the Website

### Text Commands
1. **Search the Web**:
   - Type: `Search for [query]`
   - Example: `Search for Python programming`

2. **Play YouTube Videos**:
   - Type: `Play [video name]`
   - Example: `Play Arcade by Duncan Laurence`

3. **Open Apps**:
   - Type: `Open [app name]`
   - Example: `Open Notepad`

4. **Open Folders**:
   - Type: `Open [folder name] folder`
   - Example: `Open Downloads folder`

5. **Set Volume**:
   - Type: `Set volume to [level]`
   - Example: `Set volume to 50`

6. **Set Brightness**:
   - Type: `Set brightness to [level]`
   - Example: `Set brightness to 70`

---

### Voice Commands
1. **Search the Web**:
   - Say: `Search for [query]`
   - Example: `Search for Flask documentation`

2. **Play YouTube Videos**:
   - Say: `Play [video name]`
   - Example: `Play Bohemian Rhapsody`

3. **Open Apps**:
   - Say: `Open [app name]`
   - Example: `Open Calculator`

4. **Open Folders**:
   - Say: `Open [folder name] folder`
   - Example: `Open Documents folder`

5. **Set Volume**:
   - Say: `Set volume to [level]`
   - Example: `Set volume to 30`

6. **Set Brightness**:
   - Say: `Set brightness to [level]`
   - Example: `Set brightness to 80`

---

## Deployment
To deploy the app on **Render**:
1. Fork this repository and push it to your GitHub account.
2. Go to [Render](https://render.com/) and create a new **Web Service**.
3. Connect your GitHub repository to Render.
4. Set the following configurations:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variables (if any) in the Render dashboard.
6. Deploy the app.

---

## Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/marin-web-app.git
   cd marin-web-app
