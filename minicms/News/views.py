# coding=utf-8
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpResponse
from models import Article


class ArticleDetailView(DetailView):
    model = Article  # 要显示详情内容的类

    template_name = 'article_detail.html'
    # 模板名称，默认为 应用名/类名_detail.html（即 app/modelname_detail.html）

    # 在 get_context_data() 函数中可以用于传递一些额外的内容到网页
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def A(request):
    # request.session['has_commented'] = True
    # request.session['name'] = "yin"
    # request.session['age'] = "12"
    # return HttpResponse('Thanks for your comment!')
    # username = request.session.get("name","False")
    # return render(request, 'article_detail.html',{"username":username})
    return render(request, 'article_detail.html')

     # if request.session.get('has_commented', False):
     #    username = request.session.get("name","False")
     #    return HttpResponse(username)