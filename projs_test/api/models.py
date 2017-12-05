from django.db import models
from django import forms
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments import highlight
import re
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
    serial = models.BigIntegerField(blank = True,null=True)
    resp_person = models.CharField(max_length = 64, blank = True ,null=True, default = 'admin')
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)
    primary_ns = models.CharField(max_length = 64 , blank = True ,null=True, default = 'ns.admin.net')
    reg_time = models.DateTimeField(auto_now_add = True,null=True )
    

    def clean(self):
        records.validate_zone(self)	#zone format
        records.validate_host(self)	#host format
        records.clean_type_and_data(self)	#type and data format 



    def save(self, *args, **kwargs):
        records.clean(self)
        super(records,self).save(*args, **kwargs)


    class Meta:
        ordering = ('reg_time',)
    
    

    def validate_zone(self): #判断zone 格式
        zone = self.zone
        zone_split = re.split('(\.)',zone)
        if len(zone_split) != 3:
            raise forms.ValidationError('%s 不符合域名格式。\
                                   正确格式应是：xxx.xx' % zone)
        
        error_message = ['包含非法字符，只能包含0-9a-zA-Z',
			'heihei','包含非法字符，只能包含a-z']
        
        zone_compile = ['^\w+$','\.','^[a-z]+$']
        for i in range(3):
            if re.findall(zone_compile[i],zone_split[i]):
                pass
            else:
                raise forms.ValidationError('%s  %s '% (zone_split[i],error_message[i]))
        

    def validate_host(self): #判断host格式
        host = self.host
        zone = self.zone
        if re.findall('^[A-Za-z]\w+$',host):
            pass
        else:
            raise forms.ValidationError('%s含有非法字符。 只能包含数字，字母（大小写）.' % host)
        
        try:     
            if records.objects.get(zone=zone, host=host): #若存在顺利执行try部分，执行else部分，抛出异常
                pass                                      #若不存在发生错误，不执行else部分
        except :
            pass
        else:
            raise ValidationError('%s.%s exist!'%(host, zone))
        

 
    def clean_type_and_data(self):
#"""       
#判断type与data，
#若type为A，则data为IPV4；
#若type为CNAME，则data为str；
#...

#"""       
        re_compile = {
                   'A':'^\d+\.\d+\.\d+\.\d+$',
                   'CNAME' : '^[a-zA-Z]\w+$',
                   'AAAA':'^\d+\.\d+\.\d+\.\d+$'
                          }
        type = self.type
        data = self.data

        if not re.findall(re_compile[type], data):
            raise ValidationError('type:%s data:%s no match' %(type, data))
        
        try:
            if records.objects.get(data=data):
                pass
        except:
            pass
        else:
            raise ValidationError('%s is existed!'% data)
    

