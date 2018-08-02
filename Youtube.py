from pytube import YouTube

ytd=YouTube('https://www.youtube.com/watch?v=n2u81Ujc93g')
print ytd.title
print ytd.thumbnail_url
print ytd.streams.all()
stream=ytd.streams.first()
stream.download()
print "VIDEO DOWNLOADED SUCCESSFULLY"
