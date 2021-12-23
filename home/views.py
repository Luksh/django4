from django.http import request
from django.shortcuts import render
from home.models import Blog, Contact, Feedback, Information

# Create your views here.

def home(request):
    review = {}
    review['comment'] = Feedback.objects.all()
    return render(request,'index.html',review)

def about(request):
    review = {}
    review['comment'] = Feedback.objects.all()
    return render(request,'about.html',review)

def services(request):
    review = {}
    review['comment'] = Feedback.objects.all()
    return render(request,'services.html',review)

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        message = {'success':'The form is submitted'}
        return render(request,'contact.html',message)

    content = {}
    content['info'] = Information.objects.all()
    return render(request,'contact.html',content)



    return render(request,'contact.html')



def blog(request):

    blog_view = {}
    blog_view['blogs'] = Blog.objects.all()

    return render(request,'blog-home.html',blog_view)





def blog_single(request):
    return render(request,'blog-single.html')


def elements(request):
    return render(request,'elements.html')

def blog_detail(request,slug):
    blog_detail = {}
    blog_detail['blog_details'] = Blog.objects.filter(slug = slug)
    return render(request,'blog-single.html',blog_detail)




