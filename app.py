from flask import Flask, Response
import feedparser

app = Flask(__name__)

# Microsoft 365 Service Health RSS Feed
FEED_URL = "https://status.office365.com/api/feed"

@app.route("/")
def check_m365_status():
    feed = feedparser.parse(FEED_URL)

    if not feed.entries:
        return Response("No feed entries found", status=500)

    active_incidents = []
    for entry in feed.entries:
        title = entry.title.lower()
        if "incident" in title or "degradation" in title or "advisory" in title:
            active_incidents.append(entry.title)

    if active_incidents:
        return Response(
            f"Microsoft 365 Incident Detected: {', '.join(active_incidents)}",
            status=500
        )
    else:
        return Response("Microsoft 365 All Clear", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
