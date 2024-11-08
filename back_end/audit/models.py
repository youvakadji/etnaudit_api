from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir une adresse email")
        if not username:
            raise ValueError("L'utilisateur doit avoir un nom d'utilisateur")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Notification(models.Model):
    IMPORTANCE_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    message = models.TextField()
    importance_level = models.CharField(max_length=20, choices=IMPORTANCE_CHOICES)

    def __str__(self):
        return self.message

class Audit(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.audit_type.name} ({self.status})"


class Audit_Result(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    issues_type = models.CharField(max_length=100)
    result = models.TextField()
    severity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.issues_type} ({self.severity})"

class Log(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    log_message = models.TextField()

    def __str__(self):
        return self.log_message

class Report(models.Model):
    audit_result = models.ForeignKey(Audit_Result, on_delete=models.CASCADE)
    analysis = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.analysis
    
class Prompt(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    prompt_text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.prompt_text[:50]}"

class AI_Recommendation(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    recommendation = models.TextField()
    applied = models.BooleanField(default=False)

    def __str__(self):
        return self.recommendation
