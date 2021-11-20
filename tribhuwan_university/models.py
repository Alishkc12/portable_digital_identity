from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from django.utils.text import slugify
from accounts.models import Citizen
from django.core.validators import  MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



def generate_slug(text):

    new_slug = slugify(text)
    new_slug=new_slug.replace('-','_')
    return new_slug



class student_main_tu(models.Model):
    citizen_student = models.OneToOneField(Citizen,on_delete=models.CASCADE,unique=True)
    name= models.CharField(max_length=50)
    sym_no=models.CharField(max_length=50)
    # twelve_sym=models.IntegerField()
    # faculty=models.CharField(default="",max_length=20)
    faculty=models.CharField(max_length=20,default="")
    img = models.ImageField(upload_to='static/img/dept1/student_hseb')
    slug=models.SlugField(max_length=10,default="",null=True,blank=True)
    def save(self, *args, **kwargs):
        self.slug = self.citizen_student
        super(student_main_tu, self).save(*args, **kwargs)
    



    def __str__(self): 
        return self.name


    class Meta:
        verbose_name_plural='student_main_tu' 



class dept_tu(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1/hseb')
    slug=models.CharField(null=True,blank=True,max_length=10,default="")
    

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(dept_tu, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name_plural = 'tu_department'    


class csit_subj1(models.Model):
    student=models.OneToOneField(student_main_tu,on_delete=models.CASCADE,unique=True)

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
    percentage=models.CharField(null=True,blank=True,max_length=10,default="")
    result=models.CharField(null=True,blank=True,max_length=10,default="")
    result2=models.CharField(null=True,blank=True,max_length=10,default="")  
    result3=models.CharField(null=True,blank=True,max_length=10,default="")  
    result4=models.CharField(null=True,blank=True,max_length=10,default="")  
    result5=models.CharField(null=True,blank=True,max_length=10,default="")  
    result6=models.CharField(null=True,blank=True,max_length=10,default="")    
    result7=models.CharField(null=True,blank=True,max_length=10,default="")  
    result8=models.CharField(null=True,blank=True,max_length=10,default="")  





    # stat1= models.FloatField(validators=[MaxValueValidator(60)],default=0)
    # stat2_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)


    # microprocessor= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    # microprocessor_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)  



    # math1= models.FloatField(validators=[MaxValueValidator(80)],default=0)
    # math1_prac= models.FloatField(validators=[MaxValueValidator(20)],default=0)


    # discretestructure_program= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    # discretestructure_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0)  




    # oop= models.FloatField(validators=[MaxValueValidator(60)],default=0) 
    # oop_prac= models.FloatField(validators=[MaxValueValidator(40)],default=0) 

    
    # percentag2e=models.CharField(null=True,blank=True,max_length=10,default="")
    # result2=models.CharField(null=True,blank=True,max_length=10,default="")  






    def save(self, *args, **kwargs):
        self.slug=self.student
       


        first_sem_total=self.phy+self.phy_prac+self.digitallogic+self.digitallogic_prac+self.math+self.math_prac+self.c_program_prac+self.c_program_prac+self.iit+self.iit_prac
        a1=first_sem_total/6



        if(self.phy>24 and self.digitallogic>24 and self.math>24 and self.c_program>24 and self.iit>8 and self.phy_prac>8 and self.digitallogic_prac>8 and self.math_prac>8 and self.c_program_prac>8and self.iit_prac>8):
            
            result="pass"
        else:
            result="fail"    
        
        self.percentage=a1
        self.result=result
        self.result8="pass"
        self.result2="pass"
        self.result3="pass"
        self.result4="pass"
        self.result5="pass"
        self.result6="pass"
        self.result7="pass"
        super(csit_subj1, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural='csit 1st sem' 

    

