# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseModel'
        db.create_table(u'projects_basemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'projects', ['BaseModel'])

        # Adding model 'Company'
        db.create_table(u'projects_company', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.BaseModel'], unique=True, primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=6000, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=120, null=True, blank=True)),
            ('employees', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('profile_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('profile_background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Company'])

        # Adding model 'User'
        db.create_table(u'projects_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_company', null=True, to=orm['projects.Company'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'projects_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'projects.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'projects_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'projects.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.BaseModel'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 3, 0, 0))),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default='10:00')),
            ('bounty', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('sample_screenshot', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('finished_screenshot', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'Developer'
        db.create_table(u'projects_developer', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.BaseModel'], unique=True, primary_key=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=6000, null=True, blank=True)),
            ('profile_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('profile_background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('portfolio_site', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.User'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Developer'])


    def backwards(self, orm):
        # Deleting model 'BaseModel'
        db.delete_table(u'projects_basemodel')

        # Deleting model 'Company'
        db.delete_table(u'projects_company')

        # Deleting model 'User'
        db.delete_table(u'projects_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'projects_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'projects_user_user_permissions'))

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'Developer'
        db.delete_table(u'projects_developer')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'projects.company': {
            'Meta': {'object_name': 'Company', '_ormbases': [u'projects.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            'employees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profile_background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'projects.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'projects.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '6000', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'portfolio_site': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'profile_background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project', '_ormbases': [u'projects.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'bounty': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 3, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'finished_screenshot': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sample_screenshot': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': "'10:00'"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        u'projects.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_company'", 'null': 'True', 'to': u"orm['projects.Company']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']