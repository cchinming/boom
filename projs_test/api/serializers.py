from rest_framework import serializers
from api.models import records

from django.contrib.auth.models import User

Fields = ('id','owner', 'zone', 'host', 'type', 'data', 'ttl',
		'mx_priority','priority','refresh','retry','expire',
		'minimum','serial','resp_person','primary_ns')
#owner = serializers.ReadOnlyField(source = 'owner.username')
#api = serializers.PrimaryKeyRelatedField(many = True,queryset = records.objects.all())

class RecordsSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = records
        fields = ('url','id', 'zone', 'host', 'type', 'data', 'ttl',
                'mx_priority','priority','refresh','retry','expire',
                'minimum','serial','resp_person','owner','primary_ns','reg_time')

class UserSerializers(serializers.HyperlinkedModelSerializer):
    api = serializers.HyperlinkedRelatedField(many = True,view_name = 'records-detail', read_only= True)
    class Meta:
        model  = User
        fields = ('url','id','username','last_login','api')
