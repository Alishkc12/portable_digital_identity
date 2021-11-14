from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from accounts.models import Citizen
from django.core.validators import  MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class dept_tu(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1/hseb')
    
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name_plural = 'tu_department'    


class csit_subj1(models.Model):
    student=models.OneToOneField(Citizen,on_delete=models.CASCADE,unique=True)

    phy= models.FloatField(validators=[MaxValueValidator(60)],default=0)
    phy_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)


    digitallogic= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    digitallogic_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)  



    math= models.FloatField(validators=[MaxValueValidator(80)],default=0)
    math_prac= models.FloatField(validators=[MaxValueValidator(20)],default=0)


    c_program= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    c_program_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)  




    iit= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    iit_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0) 
    
    slug=models.CharField(null=True,blank=True,max_length=10,default="")





    def save(self, *args, **kwargs):
        self.slug=self.student
       


        first_sem_total=self.phy+self.phy_prac+self.digitallogic+self.discretelogic_prac+self.math+self.math_prac+self.c_program_prac+self.c_program_prac+self.iit+self.iit_prac
        a1=first_sem_total/6



        if(self.phy>24 and self.digitallogic>24 and self.math>24 and self.c_program>24 and self.iit>8 and self.phy_prac>8 and self.digitallogic_prac>8 and self.math_prac>8 and self.c_program_prac>8and self.iit_prac>8):
            if(self.bio>24 or self.comp>24):
                if(self.bio_prac>8 or self.comp_prac>8):
                    result="pass"
                else:
                    result="fail"    
        else:
            result="fail" 
        self.percentage=a1
        self.result=result
        super(csit_subj, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural='csit subjects' 

