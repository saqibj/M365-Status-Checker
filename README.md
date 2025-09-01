# M365-Status-Checker

A lightweight Flask app that checks the official Microsoft 365 Service Health RSS feed and exposes an HTTP endpoint for uptime monitoring

## How it works
- Returns **200 OK** if no incidents are detected.
- Returns **500 Error** if any active incident/advisory is found.

## Deploy on Render
1. Fork this repo into your GitHub account.
2. Go to [Render.com](https://render.com).
3. Click **New + → Web Service**.
4. Connect your forked repo.
5. Set environment:
   - Runtime: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Deploy 🚀

You’ll get a free URL like:
https://m365status.onrender.com

## Add to UptimeRobot
- Create a new HTTPS monitor in UptimeRobot.
- Point it to your deployed Render URL.
- Add it to your status page.
