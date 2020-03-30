from django.db import models

# Create your models here.

#Create a model for submission

class Submission(models.Model):
  #defines all the possible status for the papers
  SUBMITTED = 'SUB'
  REVIEWED = 'REV'
  REJECTED = 'REJ'
  ACCEPTED = 'ACC'
  
  title = models.CharField()  #paper will have a title
  slug = models.SlugField()   #paper will have a URL of somesort
  file = models.FileField() #can also add a parameter to upload it to some where
  
  
  #a dictionary object which maps the different status to strings
  STATUS_CHOICES = [
                   (SUBMITTED, 'Submitted'),
                   (REVIEWED, 'Reviewed'),
                   (ACCEPTED), 'Accepted',
                   (REJECTED, 'Rejected'),
                   ]
  
  #status of paper 
  STATUS_OF_PAPER = models.CharField(
    max_length = 3,
    choices = STATUS_CHOICES,
    default = SUBMITTED,
  )
  
  # will return paper status
  def getStatus(self):
    return self.STATUS_OF_PAPER
  
