# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Track.url'
        db.add_column(u'music_track', 'url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Track.album'
        db.alter_column(u'music_track', 'album_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Album'], null=True))

        # Changing field 'Track.duration'
        db.alter_column(u'music_track', 'duration', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Track.bitrate'
        db.alter_column(u'music_track', 'bitrate', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Track.release_year'
        db.alter_column(u'music_track', 'release_year', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Track.url'
        db.delete_column(u'music_track', 'url')


        # Changing field 'Track.album'
        db.alter_column(u'music_track', 'album_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['music.Album']))

        # Changing field 'Track.duration'
        db.alter_column(u'music_track', 'duration', self.gf('django.db.models.fields.CharField')(default=0, max_length=10))

        # Changing field 'Track.bitrate'
        db.alter_column(u'music_track', 'bitrate', self.gf('django.db.models.fields.CharField')(default=0, max_length=10))

        # Changing field 'Track.release_year'
        db.alter_column(u'music_track', 'release_year', self.gf('django.db.models.fields.IntegerField')(default=0))

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
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['music.Album']", 'null': 'True', 'blank': 'True'}),
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['music.Artist']", 'null': 'True', 'blank': 'True'}),
            'bitrate': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'release_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['music']