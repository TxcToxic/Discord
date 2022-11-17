import pypresence
import time

time = time.time()
clientID = 123
rpc = pypresence.Presence(clientID)
rpc.connect()

rpc.update(details="Top Text", state="Low Text", large_image="NAME", large_text="Large Image Text", start=time, buttons=[{"label": "Website", "url": "https://cft-devs.xyz"}, {"label": "Clicker", "url": "https://cft-devs.xyz/clicker"}])

while True:
    time.sleep(30) # Can only update rich presence every 15 seconds
