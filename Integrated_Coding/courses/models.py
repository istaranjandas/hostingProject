from django.db import models
from django.contrib.auth.models import User

class ContestQuestion(models.Model):

    difficulty = {
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard')
    }

    topic = {
        ('array','Array '),
        ('matrix','Matrix'),
        ('string','String'),
        ('searching & sorting','Searching & Sorting'),
        ('linkedlist','Linkedlist'),
        ('binary tree','Binary Tree'),
        ('binary search tree','Binary Search Tree'),
        ('greedy','Greedy'),
        ('backtracking','Backtracking'),
        ('stack & queue','Stack & Queue'),
        ('heap','Heap'),
        ('graph','Graph'),
        ('dynamic programming','Dynamic Programming'),
        ('bit maniputation','Bit Maniputaion')
    }

    question_no = models.AutoField(primary_key=True)
    question_name = models.CharField(max_length=1000)
    question_link = models.CharField(max_length=10000)
    question_difficulty = models.CharField(max_length=10, choices=difficulty, default='easy')
    question_type = models.CharField(max_length=30, choices=topic, default='array')
    is_done = models.BooleanField()
    
    def __str__(self):
        return self.question_name
 

# class Courses(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     course=models.ForeignKey(ContestQuestion,on_delete=models.CASCADE)
    
    

# class ContestQuestion(models.Model):
#     question_no = models.AutoField(primary_key=True)
#     question_name = models.CharField(max_length=1000)
#     question_link = models.CharField(max_length=10000)
#     # soution_link = models.CharField(max_length=10000)
#     is_done = models.BooleanField()
    
#     def __str__(self):
#         return self.question_name
 