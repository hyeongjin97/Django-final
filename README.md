# Django-final

<h1>filter+pagination 병함</h1>

<h3>blog/view.py</h3>
 
 ~~~ python
 def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs2 = Blog.objects.exclude(writer=author)
        paginator = Paginator(blogs2,3)
        page = request.GET.get('page')
        blogs2 = paginator.get_page(page)
        return render(request,'home.html', {'blogs2':blogs2})
~~~

<h3>blog/templates/home.html</h3>

~~~ html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Document</title>

</head>
<body style="text-align: center;">
    

    {%extends 'base.html'%}

    {%block content%}
    {% if user.is_authenticated %}
    {{user.location}}에 사는 {{user.university}}에 다니는 {{user.nickname}}님 안녕하세요
    <a href="?search=true&writer={{user.nickname}}">내가 쓴 글</a>
    {% endif %}
    
    <h1>Blog Project</h1>
       
    <div class="container">
        {% for blog in blogs%}
           <div> 
            <h3>제목:{{ blog.title }}</h3>
            작성자:{{ blog.writer }}<br>
            내용:{{ blog.summary }}<a href="{%url 'detail' blog.id%}">...more</a><br><br>
           </div>
        {% endfor %}
        {% for blog in blogs2%}
           <div> 
            <h3>{{ blog.title }}</h3>
            {{ blog.writer }}
            {{ blog.summary }} <a href="{%url 'detail' blog.id%}">...more</a>
           </div>
        {% endfor %}
    </div>
    {% if blogs.has_previous %}
    
    <a href="?page=1">처음</a>
    <a href="?page={{blogs.previous_page_number}}">이전</a>
    
    {% endif %}

    {% if blogs2.has_previous  %}
    <a href="?search=true&writer={{user.nickname}}&page=1">첫페이지</a>
    <a href="?search=true&writer={{user.nickname}}&page={{blogs.previous_page_number}}">이전페이지</a>
    {% endif %}
    
    <span>{{blogs.number}}</span>
    <span>{{blogs2.number}}</span>
    <span>of</span>
    <span>{{blogs.paginator.num_pages}}</span>
    <span>{{blogs2.paginator.num_pages}}</span>
    
    {% if blogs.has_next %}
    <a href="?page={{blogs.next_page_number}}">다음</a>
    <a href="?page={{blogs.paginator.num_pages}}">마지막</a>
    {% endif %}

    {% if blogs2.has_next %}
    <a href="?search=true&writer={{user.nickname}}&page={{blogs2.next_page_number}}">다음페이지</a>
    <a href="?search=true&writer={{user.nickname}}&page={{blogs2.paginator.num_pages}}">마지막페이지</a>
    {% endif %}

    {%endblock%}
 
</body>
</html>
~~~
  
