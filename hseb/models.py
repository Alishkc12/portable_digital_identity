from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from accounts.models import Citizen
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator
def generate_slug(text):

    new_slug = slugify(text)
    new_slug=new_slug.replace('-','_')
    return new_slug

class dept_hseb(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1/hseb')
    

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(dept_hseb, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name_plural = 'hseb_department'    


class student_main(models.Model):
    citizen_student_id = models.OneToOneField(Citizen,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    eleven_sym=models.IntegerField()
    twelve_sym=models.IntegerField()
    # faculty=models.CharField(default="",max_length=20)
    faculty=models.CharField(max_length=20,default="")
    img = models.ImageField(upload_to='static/img/dept1/student_hseb')
    



    def __str__(self):
        return self.citizen_student_id


    class Meta:
        verbose_name_plural='student_main_hseb' 





     


     










   










class science_class_12(models.Model):
    student=models.OneToOneField(Citizen,on_delete=models.CASCADE)
    phy= models.FloatField(validators=[MaxValueValidator(75)])
    phy_prac= models.FloatField(validators=[MaxValueValidator(25)])
    math= models.FloatField(validators=[MaxValueValidator(75)]) 
    math_prac= models.FloatField(validators=[MaxValueValidator(25)])   
    chem= models.FloatField(validators=[MaxValueValidator(75)])  
    chem_prac= models.FloatField(validators=[MaxValueValidator(25)]) 
    english= models.FloatField(validators=[MaxValueValidator(75)])  
    english_prac= models.FloatField(validators=[MaxValueValidator(25)]) 
    nep= models.FloatField(validators=[MaxValueValidator(75)])
    nep_prac= models.FloatField(validators=[MaxValueValidator(25)])
    bio= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(75)]) 
    bio_prac= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(25)]) 
    comp= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(75)])
    comp_prac= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(25)])
    percentage=models.FloatField(null=True,blank=True)
    result=models.CharField(max_length=10,null=True,blank=True,default="")
    slug=models.CharField(null=True,blank=True,max_length=10,default="")

    def save(self, *args, **kwargs):

        self.slug=self.student
        a=self.phy+self.math+self.chem+self.english+self.nep+self.phy_prac+self.math_prac+self.chem_prac+self.english_prac+self.nep_prac
        a1=a/6
        result=""
        if(self.phy>24 and self.math>24 and self.chem>24 and self.english>24 and self.phy_prac>8 and self.math_prac>8 and self.chem_prac>8 and self.english_prac>8):
            if(self.bio>24 or self.comp>24):
                if(self.bio_prac>8 or self.comp_prac>8):
                    result="pass"
                else:
                    result="fail"    
        else:
            result="fail"            
        self.percentage=a1
        self.result=result
        super(science_class_12, self).save(*args, **kwargs)
    def clean(self):
        super(science_class_12, self).clean()
        if self.bio is None and self.comp is None:
            raise ValidationError('bio and comp one need to be filled')
        elif not (self.bio  and self.comp) is None:
            raise ValidationError('both bio and comp cant be filled..please check') 

    
        if self.comp_prac is None and self.bio_prac is None:
            raise ValidationError('bio and comp one need to be filled')
        elif not (self.bio_prac  and self.comp_prac) is None:
            raise ValidationError('both bio and comp cant be filled..please check')   
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name_plural='student hseb 12 marks'

class science_class_11(models.Model):
    student=models.OneToOneField(Citizen,on_delete=models.CASCADE)
    phy= models.FloatField(validators=[MaxValueValidator(75)])
    phy_prac= models.FloatField(validators=[MaxValueValidator(25)])
    math= models.FloatField(validators=[MaxValueValidator(75)]) 
    math_prac= models.FloatField(validators=[MaxValueValidator(25)])   
    chem= models.FloatField(validators=[MaxValueValidator(75)])  
    chem_prac= models.FloatField(validators=[MaxValueValidator(25)]) 
    english= models.FloatField(validators=[MaxValueValidator(75)])  
    english_prac= models.FloatField(validators=[MaxValueValidator(25)]) 
    nep= models.FloatField(validators=[MaxValueValidator(75)])
    nep_prac= models.FloatField(validators=[MaxValueValidator(25)])
    bio= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(75)]) 
    bio_prac= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(25)]) 
    comp= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(75)])
    comp_prac= models.FloatField(null=True,blank=True,validators=[MaxValueValidator(25)])
    percentage=models.FloatField(null=True,blank=True)
    result=models.CharField(max_length=10,null=True,blank=True,default="")
    slug=models.CharField(null=True,blank=True,max_length=10,default="")

    def save(self, *args, **kwargs):

        self.slug=self.student
        a=self.phy+self.math+self.chem+self.english+self.nep+self.phy_prac+self.math_prac+self.chem_prac+self.english_prac+self.nep_prac
        a1=a/6
        result=""
        if(self.phy>24 and self.math>24 and self.chem>24 and self.english>24 and self.phy_prac>8 and self.math_prac>8 and self.chem_prac>8 and self.english_prac>8):
            if(self.bio>24 or self.comp>24):
                if(self.bio_prac>8 or self.comp_prac>8):
                    result="pass"
                else:
                    result="fail"    
        else:
            result="fail"            
        self.percentage=a1
        self.result=result
        super(science_class_11, self).save(*args, **kwargs)
    def clean(self):
        super(science_class_11, self).clean()
        if self.bio is None and self.comp is None:
            raise ValidationError('bio and comp one need to be filled')
        elif not (self.bio  and self.comp) is None:
            raise ValidationError('both bio and comp cant be filled..please check') 

    
        if self.comp_prac is None and self.bio_prac is None:
            raise ValidationError('bio and comp one need to be filled')
        elif not (self.bio_prac  and self.comp_prac) is None:
            raise ValidationError('both bio and comp cant be filled..please check')   
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name_plural='student hseb 11 marks'

