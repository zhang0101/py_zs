"""py_zs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

import xadmin
from home.views import HomeView, ContactView, ChangeImgsView
from news.views import NewsView, DetailView
from py_zs.settings import MEDIA_ROOT, STATIC_ROOT
from recruit.views import RecruitView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    path('', HomeView.as_view(), name='index'),

    path('index/', ChangeImgsView.as_view()),

    path('news/', NewsView.as_view(), name='news'),
    path('recruit/', RecruitView.as_view(), name='recruit'),
    path('contact/', ContactView.as_view(), name='contact'),

    re_path('detail/(?P<detail_id>.*)/', DetailView.as_view(), name='detail'),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
]