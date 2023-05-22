from django.db import models

class Director(models.Model):  
    name = models.CharField(max_length=20)  
  
    def __str__(self):  
        return self.name  
      
class Movie(models.Model):  
    movie_title = models.CharField(max_length=150)  
    release_year = models.IntegerField()  
    director = models.ForeignKey(Director, on_delete = models.CASCADE, max_length=100)  
      
    def __str__(self):  
        return self.movie_title

class Teacher(models.Model):  
    teacher_name = models.CharField(max_length=200)  
  
    def __str__(self):  
        return f'{self.teacher_name}' 
class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
    teacher_name = models.ForeignKey(Teacher, blank = True, null = True, on_delete= models.CASCADE)
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)


