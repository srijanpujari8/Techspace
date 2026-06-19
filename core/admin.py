from django.contrib import admin
from .models import Enquiry, PlacedStudent, Course, Testimonial, BlogPost, BrochureLead


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'get_course_display', 'get_branch_display', 'get_mode_display', 'is_contacted', 'created_at')
    list_filter = ('course', 'branch', 'mode', 'is_contacted', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    date_hierarchy = 'created_at'
    list_editable = ('is_contacted',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Student Info', {'fields': ('name', 'phone', 'email')}),
        ('Course Details', {'fields': ('course', 'branch', 'mode')}),
        ('Message', {'fields': ('message',)}),
        ('Status', {'fields': ('is_contacted', 'created_at')}),
    )


@admin.register(PlacedStudent)
class PlacedStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company', 'batch', 'is_active', 'order')
    list_filter = ('company', 'batch', 'is_active')
    search_fields = ('name', 'company', 'role')
    list_editable = ('is_active', 'order')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'duration', 'certificate_issued', 'is_highlighted', 'is_active', 'order')
    list_filter = ('is_active', 'is_highlighted', 'certificate_issued')
    search_fields = ('name', 'description', 'syllabus')
    list_editable = ('is_active', 'is_highlighted', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'rating', 'is_active', 'order')
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'course', 'review')
    list_editable = ('is_active', 'order')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_active')
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_active',)


@admin.register(BrochureLead)
class BrochureLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'downloaded_at')
    search_fields = ('name', 'phone', 'email')
    date_hierarchy = 'downloaded_at'
    readonly_fields = ('downloaded_at',)


# Customize admin site header
admin.site.site_header = 'TechSpace Programming Classes — Admin'
admin.site.site_title = 'TechSpace Admin'
admin.site.index_title = 'Dashboard'
