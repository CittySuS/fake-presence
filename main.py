from pypresence import Presence
import time

RPC = Presence('856194108506112061')
RPC.connect()

RPC.update(state = "Watching: Gohar Khan",
			large_image = 'FR',
			large_text = 'studying',
			buttons = [
						{
						"label": "Join",
						"url": "https://www.youtube.com/watch?v=gk5FEFf8Guo"
						}
					  ],
			start = time.time()
		   )

loop = RPC.get_event_loop()
loop.run_forever()
