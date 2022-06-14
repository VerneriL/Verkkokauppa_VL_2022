from django.shortcuts import render

posts = [
    {
        'author': 'Me',
        'title': 'Blog Post 1',
        'content': 'First psot content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second psot content',
        'date_posted': 'August 28, 2018'
    }    
]
# Home page for the store
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

# Store page

# Test func
def about(request):
    return render(request, 'about.html', {'title': 'About'})
