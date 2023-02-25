import subprocess

# Run command to start the mobile hotspot
subprocess.call(
    "netsh wlan set hostednetwork mode=allow ssid=HotspotName key=Password", shell=True)
subprocess.call("netsh wlan start hostednetwork", shell=True)
