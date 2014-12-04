from celery import task, Celery
from music.models import RadioStations

import shout, time, sys, string

@task
def streaming_server_setup(username, songs, id):
	total = 0
	st = time.time()
	root = '/host/development/media-streaming/project/audio_streaming_app/music/static/music/songs/'
	song_list = []
	for i in songs:
		song_list.append(root + i + '.ogg')

	s = shout.Shout()
	s.password = 'hackme'
	s.mount = str(username)
	s.open()

	for fa in song_list:
	    print "opening file %s" % fa
	    f = open(fa)

	    nbuf = f.read(4096)
	    while 1:
	        buf = nbuf
	        nbuf = f.read(4096)
	        total = total + len(buf)
	        if len(buf) == 0:
	            break
	        s.send(buf)
	        s.sync()
	    f.close()
	    
	    et = time.time()
	    br = total*0.008/(et-st)
	    print "Sent %d bytes in %d seconds (%f kbps)" % (total, et-st, br)
	    r = RadioStations.objects.get(id = id)
	    r.active = False
	    r.save()