# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'music_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('img', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'music', ['Artist'])

        # Adding model 'Album'
        db.create_table(u'music_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('release_year', self.gf('django.db.models.fields.IntegerField')()),
            ('img', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'music', ['Album'])

        # Adding model 'Track'
        db.create_table(u'music_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Album'])),
            ('img', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bitrate', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('release_year', self.gf('django.db.models.fields.IntegerField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'music', ['Track'])

        # Adding M2M table for field artist on 'Track'
        m2m_table_name = db.shorten_name(u'music_track_artist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('track', models.ForeignKey(orm[u'music.track'], null=False)),
            ('artist', models.ForeignKey(orm[u'music.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['track_id', 'artist_id'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'music_artist')

        # Deleting model 'Album'
        db.delete_table(u'music_album')

        # Deleting model 'Track'
        db.delete_table(u'music_track')

        # Removing M2M table for field artist on 'Track'
        db.delete_table(db.shorten_name(u'music_track_artist'))


    models = {
        u'music.album': {
            'Meta': {'object_name': 'Album'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'music.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'music.track': {
            'Meta': {'object_name': 'Track'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['music.Album']"}),
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['music.Artist']", 'symmetrical': 'False'}),
            'bitrate': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'release_year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['music']