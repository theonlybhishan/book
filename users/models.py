from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AgentProfile(models.Model):
    DOCUMENT_CHOICES=(
    ('DN','Darta_Number'),
    # ('V_ID','Vehicle_Id'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    agent_name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    # slug = models.SlugField(unique=True)
    contact_number = models.IntegerField()
    address = models.TextField(max_length=150)
    photo = models.ImageField(upload_to ='agent')
    document_id = models.PositiveBigIntegerField()
    document_type = models.CharField(choices =DOCUMENT_CHOICES,default='DN',max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comission = models.SmallIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name}+{self.last_name}'
