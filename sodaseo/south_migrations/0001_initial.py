# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Config'
        db.create_table(u'sodaseo_config', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'sodaseo_config', to=orm['sites.Site'])),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('google_site_verification', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fb_appid', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'sodaseo', ['Config'])

        # Adding model 'Template'
        db.create_table(u'sodaseo_template', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sodaseo', ['Template'])

        # Adding model 'Url'
        db.create_table(u'sodaseo_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'sodaseo_urls', to=orm['sites.Site'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sodaseo', ['Url'])

        # Adding unique constraint on 'Url', fields ['site', 'path']
        db.create_unique(u'sodaseo_url', ['site_id', 'path'])

        # Adding model 'Var'
        db.create_table(u'sodaseo_var', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'vars', to=orm['sodaseo.Url'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sodaseo', ['Var'])

        # Adding model 'Seo'
        db.create_table(u'sodaseo_seo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sodaseo.Template'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_site_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'seo_og_image', null=True, on_delete=models.SET_NULL, to=orm['filer.Image'])),
            ('og_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('article_published_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('article_modified_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('article_section', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('article_tag', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('itemprop_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('itemprop_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('itemprop_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'seo_itemprop_image', null=True, on_delete=models.SET_NULL, to=orm['filer.Image'])),
            ('twitter_card', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_site', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_creator', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'seo_twitter_image', null=True, on_delete=models.SET_NULL, to=orm['filer.Image'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'sodaseo', ['Seo'])


    def backwards(self, orm):
        # Removing unique constraint on 'Url', fields ['site', 'path']
        db.delete_unique(u'sodaseo_url', ['site_id', 'path'])

        # Deleting model 'Config'
        db.delete_table(u'sodaseo_config')

        # Deleting model 'Template'
        db.delete_table(u'sodaseo_template')

        # Deleting model 'Url'
        db.delete_table(u'sodaseo_url')

        # Deleting model 'Var'
        db.delete_table(u'sodaseo_var')

        # Deleting model 'Seo'
        db.delete_table(u'sodaseo_seo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'all_files'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'filer.folder': {
            'Meta': {'ordering': "(u'name',)", 'unique_together': "((u'parent', u'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image'},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sodaseo.config': {
            'Meta': {'object_name': 'Config'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fb_appid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'google_site_verification': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "u'sodaseo_config'", 'to': u"orm['sites.Site']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sodaseo.seo': {
            'Meta': {'object_name': 'Seo'},
            'article_modified_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'article_published_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'article_section': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'article_tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemprop_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'itemprop_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'seo_itemprop_image'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['filer.Image']"}),
            'itemprop_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'og_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'seo_og_image'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['filer.Image']"}),
            'og_site_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'og_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sodaseo.Template']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_card': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_creator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'seo_twitter_image'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['filer.Image']"}),
            'twitter_site': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sodaseo.template': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Template'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sodaseo.url': {
            'Meta': {'ordering': "[u'path']", 'unique_together': "((u'site', u'path'),)", 'object_name': 'Url'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "u'sodaseo_urls'", 'to': u"orm['sites.Site']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sodaseo.var': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Var'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'vars'", 'to': u"orm['sodaseo.Url']"})
        }
    }

    complete_apps = ['sodaseo']