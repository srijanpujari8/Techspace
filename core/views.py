import os
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse, Http404
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import PlacedStudent, Course, Testimonial, Enquiry, BrochureLead
from .forms import EnquiryForm, BrochureLeadForm


# ─── Static data for placed students ──────────────────────────────────────────
PLACED_STUDENTS = [
    {'name': 'Vasudha Rathore',    'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Vaishnavi Kumbhar',  'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Rushikesh Dhumal',   'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Pranav Chavan',      'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Silviya Vellappan',  'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Samarth Shirke',     'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Asmita Dhesmane',    'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Sandhya Yele',       'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Sakshi Satre',       'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Omkar Yadav',        'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Aarti Jagtap',       'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Samiksha Sarak',     'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Roshani Sangar',     'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
    {'name': 'Sahil Ghadge',       'role': 'Software Developer', 'company': 'SP Finance', 'batch': '2025'},
]

STATIC_COURSES = [
    {'name': 'Python Programming',         'icon': 'fab fa-python',   'duration': '2–3 Months', 'highlighted': True,  'topics': ['Python Basics & OOPs', 'File Handling', 'Libraries: NumPy, Pandas', 'Flask Intro', 'Project-Based', 'Certificate Issued']},
    {'name': 'Full Stack Web Development', 'icon': 'fas fa-layer-group','duration': '4–6 Months','highlighted': False, 'topics': ['HTML5, CSS3, JS', 'React / Django', 'REST APIs', 'Database Integration', 'Deployment', 'Portfolio Project']},
    {'name': 'Data Science & Analytics',   'icon': 'fas fa-chart-bar','duration': '3–4 Months', 'highlighted': False, 'topics': ['Pandas & NumPy', 'Data Visualization', 'Machine Learning Basics', 'SQL & Databases', 'Jupyter Notebooks', 'Real Datasets']},
    {'name': 'Software Development',       'icon': 'fas fa-laptop-code','duration': '3–6 Months','highlighted': False,'topics': ['SDLC Concepts', 'OOP Principles', 'Agile & Scrum', 'Code Review', 'Git Workflow', 'Industry Practices']},
    {'name': 'DevOps Engineering',         'icon': 'fas fa-infinity',  'duration': '3 Months',  'highlighted': False, 'topics': ['CI/CD Pipelines', 'Docker & Kubernetes', 'Jenkins', 'AWS Basics', 'Linux Commands', 'Monitoring']},
    {'name': 'Cloud Computing',            'icon': 'fas fa-cloud',     'duration': '2–3 Months','highlighted': False, 'topics': ['AWS / Azure Basics', 'EC2, S3, RDS', 'Serverless Functions', 'Cloud Security', 'Cost Management', 'Certifications Guide']},
    {'name': 'Cyber Security',             'icon': 'fas fa-shield-alt','duration': '2–3 Months','highlighted': False, 'topics': ['Network Security', 'Ethical Hacking Basics', 'OWASP Top 10', 'Penetration Testing', 'Cryptography', 'Security Tools']},
    {'name': 'DSA + Competitive Programming','icon':'fas fa-sitemap', 'duration': '2–4 Months','highlighted': False, 'topics': ['Arrays, Strings, Trees', 'Sorting & Searching', 'Dynamic Programming', 'Graph Algorithms', 'LeetCode Practice', 'Contest Strategy']},
    {'name': 'Git & Version Control',      'icon': 'fab fa-git-alt',  'duration': '3–4 Weeks', 'highlighted': False, 'topics': ['Git Basics & CLI', 'Branching & Merging', 'GitHub / GitLab', 'Pull Requests', 'CI Integration', 'Team Workflows']},
    {'name': 'System Architecture',        'icon': 'fas fa-project-diagram','duration':'1–2 Months','highlighted': False,'topics': ['Design Patterns', 'Microservices', 'Load Balancing', 'Scalability', 'API Design', 'Database Sharding']},
    {'name': 'Development Tools & IDEs',   'icon': 'fas fa-tools',    'duration': '3–4 Weeks', 'highlighted': False, 'topics': ['VS Code Mastery', 'PyCharm & IntelliJ', 'Debugging Skills', 'Extensions & Plugins', 'Productivity Tips', 'Terminal Proficiency']},
]

STATIC_TESTIMONIALS = [
    {'name': 'Harshvardhan Shinde', 'course': 'Python Programming', 'rating': 5, 'review': 'TechSpace completely changed my career path. The Python course was hands-on, practical, and extremely well-structured. Omkar sir is an incredible mentor!'},
    {'name': 'Vasudha Rathore',     'course': 'Full Stack Dev',     'rating': 5, 'review': 'I got placed at SP Finance within 3 months of completing the course. The placement support and mock interviews were a game-changer.'},
    {'name': 'Rushikesh Dhumal',    'course': 'Full Stack Dev',     'rating': 5, 'review': 'The project-based curriculum at TechSpace is what sets it apart. I built a real portfolio and cracked interviews with confidence.'},
    {'name': 'Asmita Dhesmane',     'course': 'Python Programming', 'rating': 5, 'review': 'From zero coding knowledge to a Software Developer role — TechSpace made it possible. The 1:1 doubt sessions were invaluable.'},
    {'name': 'Samarth Shirke',      'course': 'Full Stack Dev',     'rating': 5, 'review': 'Best coaching institute in Navi Mumbai for programming. The trainers are experienced, approachable, and always ready to help.'},
    {'name': 'Aarti Jagtap',        'course': 'Data Science',       'rating': 5, 'review': 'Excellent curriculum, real-world projects, and a supportive learning environment. TechSpace lives up to its 100% placement promise!'},
    {'name': 'Pranav Chavan',       'course': 'Full Stack Dev',     'rating': 5, 'review': 'Flexible batch timings, recorded lectures for revision, and an amazing peer community — TechSpace is the complete package.'},
    {'name': 'Sakshi Satre',        'course': 'Python Programming', 'rating': 5, 'review': 'Omkar sir\'s teaching style is unique — he makes complex concepts simple. Highly recommend TechSpace to anyone starting their coding journey!'},
]


def home(request):
    """Render the main homepage with all sections."""
    # Try DB first, fall back to static data
    try:
        placed_students_db = list(PlacedStudent.objects.filter(is_active=True).values())
        placed_students = placed_students_db if placed_students_db else PLACED_STUDENTS
        testimonials_db = list(Testimonial.objects.filter(is_active=True).values())
        testimonials = testimonials_db if testimonials_db else STATIC_TESTIMONIALS
    except Exception:
        placed_students = PLACED_STUDENTS
        testimonials = STATIC_TESTIMONIALS

    form = EnquiryForm()
    context = {
        'form': form,
        'placed_students': PLACED_STUDENTS,  # Always use static for accuracy
        'courses': STATIC_COURSES,
        'testimonials': STATIC_TESTIMONIALS,
        'placed_count': len(PLACED_STUDENTS),
    }
    return render(request, 'index.html', context)


@require_POST
def submit_enquiry(request):
    """Handle enquiry form POST → save to DB → confirmation email → redirect."""
    form = EnquiryForm(request.POST)

    if form.is_valid():
        try:
            enquiry = form.save()
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            })

        # Send confirmation email (non-blocking, fails silently in dev)
        try:
            send_mail(
                subject='Thanks for your enquiry — TechSpace Programming Classes',
                message=f"""Hi {enquiry.name},
Thank you for your interest in TechSpace Programming Classes!

We have received your enquiry for: {enquiry.get_course_display()}
Our team will contact you shortly on: {enquiry.phone}

📍 Visit us at: Asthavinayak Building, KL 5, Sector 2, Kalamboli, Navi Mumbai – 410218
📞 Call/WhatsApp: +91 93216 74997
📧 Email: omkarcoder18@gmail.com

Warm Regards,
Omkar Jagdale
Founder & Director — TechSpace Programming Classes
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[enquiry.email] if enquiry.email else [],
                fail_silently=True,
            )
        except Exception:
            pass
        messages.success(request, f"Thank you {enquiry.name}! We'll call you within 24 hours.")
        return redirect('success')
    else:
        messages.error(request, 'Please correct the errors below.')
        context = {
            'form': form,
            'placed_students': PLACED_STUDENTS,
            'courses': STATIC_COURSES,
            'testimonials': STATIC_TESTIMONIALS,
            'placed_count': len(PLACED_STUDENTS),
            'scroll_to_contact': True,
        }
        return render(request, 'index.html', context)


@require_POST
def download_brochure(request):
    """Gate brochure download with name + phone."""
    form = BrochureLeadForm(request.POST)
    if form.is_valid():
        form.save()
        brochure_path = os.path.join(settings.MEDIA_ROOT, 'brochure', 'techspace_brochure.pdf')
        if os.path.exists(brochure_path):
            return FileResponse(
                open(brochure_path, 'rb'),
                as_attachment=True,
                filename='TechSpace_Brochure.pdf'
            )
        messages.warning(request, 'Brochure will be available soon. We\'ll WhatsApp it to you!')
        return redirect('home')
    messages.error(request, 'Please enter your name and mobile number.')
    return redirect('home')


def success(request):
    """Thank you page after enquiry submission."""
    return render(request, 'success.html')


def courses_api(request):
    """JSON API for active courses."""
    data = STATIC_COURSES
    return JsonResponse({'courses': data, 'total': len(data)})
