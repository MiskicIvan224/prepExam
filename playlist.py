playlist = dict(Title = "Patagonia Bus", author = "Colt Steele", 
                
				songs = [
                    dict(title = "song1", artist = ["Ivan"], duration = 2.5),
					dict(title = "song2", artist = ["Ivann", "Ivannakvadrat"], duration = 2.6),
                    dict(title = "song3", artist = ["Ivannn"], duration = 2.7)
				])


counter = 0.0
for durations in playlist["songs"]:
    duration_times = durations.get("duration")
    counter+=duration_times
print(counter)
   