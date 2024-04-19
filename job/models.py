import datetime
from django.db import models
from main.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('Open', "Open"),
    ('Close',"Close")
)

JOBTYPE_CHOICES = (
    ('Full Time', "Full Time"),
    ('Part Time',"Part time"),
    ('Internship', "Internship"),
    ('Contract', "Contract")
)

JOBCATEGORY_CHOICES = (
    ('Full Stack Development', "Full Stack Development"),
    ('Marketing',"Marketing"),
    ('Accounting', "Accounting"),
    ('Design Engineering', "Design Engineering"),
    ('Matlab', "Matlab"),
)

JOB_STATUS_CHOICES = (
    ('No Offer', "No Offer"),
    ('Job Offered',"Job Offered"),
    ('Assign Task',"Assign Task"),
    ('Schedule Interview',"Schedule Interview")
)

class Job(BaseModel):  
    company = models.ForeignKey("main.Company",on_delete=models.CASCADE,limit_choices_to={'is_deleted': False}) 
    job_title = models.CharField(_('Job Title'),max_length=255)
    department = models.ForeignKey("employee.Department",on_delete=models.CASCADE,limit_choices_to={'is_deleted': False},null=True, blank=True)
    job_location = models.CharField(_('Job Location'),max_length=255,null=True, blank=True)   
    no_of_vacancies = models.CharField(_('Number Of Vacancies'),max_length=100,null=True, blank=True)
    experience = models.CharField(_("Experience"),max_length=255,null=True, blank=True)
    age = models.PositiveIntegerField(_("Age"),null=True, blank=True)
    salary_from = models.PositiveIntegerField(_("Salary From"),null=True, blank=True)
    salary_to = models.PositiveIntegerField(_("Salary To"),null=True, blank=True)
    job_type =  models.CharField(max_length=255, choices=JOBTYPE_CHOICES,null=True, blank=True)
    job_category =  models.CharField(max_length=255, choices=JOBCATEGORY_CHOICES,default='Full Stack Development')
    status =  models.CharField(max_length=255, choices=STATUS_CHOICES)
    start_date = models.DateField(_('Start Date'),help_text='start date',null=True, blank=True)    
    expired_date = models.DateField(_('Expired Date'),help_text='expired date',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

   
    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
        ordering = ['job_title']

    def __str__(self):
        return self.job_title
    

class CandidateJob(BaseModel):
    company = models.ForeignKey("main.Company",on_delete=models.CASCADE,limit_choices_to={'is_deleted': False}) 
    candidate = models.ForeignKey("candidate.Candidate",on_delete=models.CASCADE,limit_choices_to={'is_deleted': False})     
    job_title = models.CharField(_('Job Title'),max_length=255)
    job_location = models.CharField(_('Job Location'),max_length=255,null=True, blank=True)   
    description = models.TextField(null=True, blank=True)
    salary_from = models.PositiveIntegerField(_("Salary From"),null=True, blank=True)
    salary_to = models.PositiveIntegerField(_("Salary To"),null=True, blank=True)
    status =  models.CharField(max_length=255, choices=JOB_STATUS_CHOICES, default="No Offer")
    is_deleted = models.BooleanField(default=False)

   
    class Meta:
        verbose_name = _('CandidateJob')
        verbose_name_plural = _('CandidateJobs')
        ordering = ['job_title']

    def __str__(self):
        return self.job_title
    

