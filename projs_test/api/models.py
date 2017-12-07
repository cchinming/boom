from django.db import models
from django import forms
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments import highlight
import re
import time
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
#type data
CHOICES=(
	(u'A',u'A'),
	(u'AAAA',u'AAAA'),
	(u'CNAME',u'CNAME'),
	(u'NS',u'NS')
)
 

def create_serial():
    serial = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    return serial


class records(models.Model):

    zone = models.CharField(max_length = 255, blank = True, default = '')
    host = models.CharField(max_length = 255, blank = True , default = '')   
    type = models.CharField(max_length = 255, blank = True ,choices=CHOICES ,default = '')
    data = models.CharField(max_length = 255,blank = True , default = '')
    ttl = models.IntegerField(blank = True, default = 3600 )
    mx_priority = models.IntegerField(blank = True,null=True, default = 0 )
    priority = models.SmallIntegerField(blank = True,null=True, default = 255 )
    refresh = models.IntegerField(blank = True,null=True, default = 28800 )
    retry = models.IntegerField(blank = True,null=True, default = 14400 )
    expire = models.IntegerField(blank = True ,null=True,default = 86400 )
    minimum = models.IntegerField(blank = True,null=True, default = 86400)
    serial = models.CharField(max_length = 30,blank = True, default = create_serial())
    resp_person = models.CharField(max_length = 64, blank = True ,null=True, default = 'admin')
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)
    primary_ns = models.CharField(max_length = 64 , blank = True ,null=True, default = 'ns.admin.net')
    reg_time = models.DateTimeField(auto_now_add = True,null=True )
    

    def clean_zone(self):
        id   = self.id
        zone = self.zone
        host = self.host
        type = self.type
        data = self.data
        try:                #host,zone is it existed?
            if records.objects.get(zone=zone, host=host):
                pass
        except:
            #raise ValidationError('%s.%s is already existed!'%(host, zone))
            pass  
        else:
            try:
                if records.objects.get(id=id, zone=zone, host=host):
                    pass
            except: 
                raise ValidationError('%s.%s is already existed!'%(host,zone))
        if type =='CNAME':
           try:
               if records.objects.get(zone=zone, data=data):
                   pass
           except:
               try:
                   if records.objects.get(data=data,zone=zone):
                       pass
               except:
                   pass
               else:
                   raise ValidationError('%s.%s is already existed!'%(data,zone)) 

    def clean_data(self):
        type = self.type
        data = self.data
        data_re ={
		'A':'^(\d{1,3}\.){3}\d{1,3}$',
                'CNAME':'^[a-z]\w+$'
}
        if not re.findall(data_re[type], data):
            raise ValidationError('!!wrong')
        try:
            if records.objects.get(type):
                pass
        except:
            pass
        else:
            raise ValidationError('chongfule')


    def save(self, *args, **kwargs):
        records.clean_data(self)
        records.clean_zone(self)
        super(records,self).save(*args, **kwargs)


    class Meta:
        ordering = ('reg_time',)
    
    
