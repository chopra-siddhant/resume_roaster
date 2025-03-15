from django.db import models

class Resume(models.Model):
    user_email = models.EmailField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    resume_text = models.TextField()
    roast_result = models.TextField(null=True, blank=True)
    improvement_suggestions = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Resume {self.id} - {self.user_email}"

class HRSimulator(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    hr_feedback = models.TextField()

class LinkedInFlex(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    generated_post = models.TextField()
