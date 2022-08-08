import pypresence
import time

time = time.time()
clientID = 123
rpc = pypresence.Presence(clientID)
rpc.connect()

while True:
    rpc.update(details="Top Text", state="Low Text", large_image="NAME", large_text="Large Image Text", start=time)
