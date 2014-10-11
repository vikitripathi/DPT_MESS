import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_id=models.CharField(max_length=10)
    item_rating=models.IntegerField(default=0)  #this has to be computed one that is mean of respected

    def __unicode__(self):  # Python 3: def __str__(self):
         return u'%s' % (self.item_name)
    

class Category(models.Model):
    item=models.ForeignKey(Item)
    items_type=models.CharField(max_length=30) 

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.items_type  
   
class User(models.Model):
    user_id=models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    tiemstamp=models.DateTimeField('date recently rated')

    def __unicode__(self):
        return u'%s %s' % (self.first_name,self.last_name)  
        #return self.email

class Rating(models.Model):
    item=models.ForeignKey(Item)
    ratings=models.IntegerField(default=0)
    timestamp=models.DateTimeField('date rated')
    user=models.ForeignKey(User)
    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'timestamp'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'    

    def __unicode__(self):
        return u'%s %s %s' % (self.item, self.user,str(self.ratings))
    
    #__unicode__ is just like toString of java  
    """
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.rate 
    """
    #return a string here ! to define the object
    #check tab error
    #python -m tabnanny admin.py

