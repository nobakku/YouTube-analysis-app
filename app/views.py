from django.shortcuts import render, redirect
from django.views.generic import View
from apiclient.discovery import build
from datetime import datetime, timedelta, date
from django.conf import settings
from .forms import KeywordForm
import pandas as pd


# 環境変数の読み込み
YOUTUBE_API = build('youtube', 'v3', developerkey=settings.YOUTUBE_API_KEY)


# トップページ
class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = KeywordForm(
            request.POST or None,
            initial={
                'items_count': 12,
                'viewcount': 1000,
                'order': 'viewCount',
                'search_start': datetime.today() - timedelta(days=30),
                'search_end': datetime.today(),
            }
        )

        return render(request, 'app/index.html', {
            'form': form,
        })
