import os, time, subprocess, sys


def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


try:
    install_dependencies()
except:
    pass

import requests

while True:
    try:
        url = os.environ.get("VPS_URL", "")
        cookies = os.environ.get("VPS_COOKIE", "")
        if len(url) > 5 and len(cookies) > 20:
            headers = {"Cookie": cookies}
            resp = requests.get(
                url,
                headers=headers,
            )
            print(resp.text)
    except Exception as err:
        print(f"Exception at req {err}")
    time.sleep(30)
