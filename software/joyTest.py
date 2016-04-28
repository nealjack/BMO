import xbox_read

stream = xbox_read.event_stream(deadzone=12000)
for event in stream:
	print event
