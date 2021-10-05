from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class dept_hseb(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1/hseb')
    
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name_plural = 'hseb_department'    


class student_main(models.Model):
	citizen_student_id = models.CharField(max_length=10)
	name= models.CharField(max_length=50)
	eleven_sym=models.IntegerField()
	twelve_sym=models.IntegerField()
	img = models.ImageField(upload_to='static/img/dept1/student_hseb')


	def __str__(self):
		return self.citizen_student_id


	class Meta:
		verbose_name_plural='student_main_hseb'	



class student_marks_eleven(models.Model):

	student=models.ForeignKey(student_main,on_delete=models.CASCADE) 
	phy= models.FloatField()
	math= models.FloatField()   
	chem= models.FloatField()  
	english= models.FloatField()  
	nep= models.FloatField()
	bio= models.FloatField()  
	comp= models.FloatField()  

	def __str_(self):
		return self.student  


class student_marks_twelve(models.Model):

	student=models.ForeignKey(student_main,on_delete=models.CASCADE) 
	phy= models.FloatField()
	math= models.FloatField()   
	chem= models.FloatField()  
	english= models.FloatField()  
	nep= models.FloatField()
	bio= models.FloatField()  
	comp= models.FloatField()  

	def __str_(self):
		return self.student  
        