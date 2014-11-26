from celery import task, Celery

import shout, time, sys, string

@task
def sum(a,b):
    return a+b

@task
def streaming_server_setup(username, songs):
	total = 0
	st = time.time()
	root = '/host/development/media-streaming/project/audio_streaming_app/music/static/music/songs/'
	songs = [root+'song1.ogg', root+'song2.ogg']

	s = shout.Shout()
	s.password = 'hackme'
	s.mount = username
	s.open()

	for fa in songs:
	    print "opening file %s" % fa
	    f = open(fa)
	    s.set_metadata({'song': fa})

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