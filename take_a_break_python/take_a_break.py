import webbrowser
import time
import random
time_between_breaks=5 #in seconds
number_of_breaks=3
music_to_play=["https://www.youtube.com/watch?v=zFt0tO4Op14",
				"https://www.youtube.com/watch?v=GoCOg8ZzUfg",
				"https://youtu.be/otCpCn0l4Wo?t=14s"]
random.shuffle(music_to_play)
for i in range (0,number_of_breaks):
	time.sleep(time_between_breaks)
	index= i
	if (index==len(music_to_play)-1):
		index=0
	webbrowser.open(music_to_play[index])

