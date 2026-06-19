from django.db import models


class Enquiry(models.Model):
    COURSE_CHOICES = [
        ('software-development', 'Software Development'),
        ('data-science', 'Data Science & Analytics'),
        ('git-version-control', 'Git & Version Control'),
        ('system-architecture', 'System Architecture'),
        ('dev-tools-ides', 'Development Tools & IDEs'),
        ('cyber-security', 'Cyber Security'),
        ('cloud-computing', 'Cloud Computing'),
        ('devops', 'DevOps Engineering'),
        ('python', 'Python Programming'),
        ('fullstack', 'Full Stack Web Development'),
        ('dsa', 'DSA + Competitive Programming'),
        ('other', 'Other / Not Sure'),
    ]
    BRANCH_CHOICES = [
        ('kalamboli', 'Kalamboli'),
        ('kamothe', 'Kamothe'),
        ('panvel', 'Panvel'),
        ('any', 'Any / Nearest'),
    ]
    MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline / Classroom'),
        ('hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    course = models.CharField(max_length=60, choices=COURSE_CHOICES, default='other')
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES, blank=True, default='any')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, blank=True, default='offline')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.get_course_display()} ({self.created_at.strftime('%d %b %Y')})"


class PlacedStudent(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100, default='Software Developer')
    company = models.CharField(max_length=150, default='SP Finance')
    batch = models.CharField(max_length=20, default='2025')
    photo = models.ImageField(upload_to='placed_students/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} @ {self.company}"


class Course(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, default='fas fa-code', help_text='FontAwesome class')
    duration = models.CharField(max_length=60, default='3–6 Months')
    description = models.TextField()
    syllabus = models.TextField(help_text='Key topics, one per line')
    certificate_issued = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_highlighted = models.BooleanField(default=False, help_text='Show as featured/highlighted')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_syllabus_list(self):
        return [line.strip() for line in self.syllabus.split('\n') if line.strip()]


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    course = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.course})"


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=100, default='Omkar Jagdale')
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class BrochureLead(models.Model):
    """Gated leads captured before brochure download."""
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-downloaded_at']

    def __str__(self):
        return f"{self.name} — {self.phone}"
