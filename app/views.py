from django.views.generic import View
from django.shortcuts import render, redirect
from apiclient.discovery import build
from datetime import datetime, timedelta, date
from django.conf import settings
from .forms import KeywordForm
import pandas as pd


# 環境変数の読み込み
YOUTUBE_API = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)


# トップページ
class IndexView(View):
    def get(self, request, *args, **kwargs):
        # 検索フォーム
        form = KeywordForm(
            request.POST or None,
            # フォームに初期値を設定
            initial={
                'items_count': 12,  # 検索数
                'viewcount': 1000,  # 再生回数
                'order': 'viewCount',  # 並び順
                'search_start': datetime.today() - timedelta(days=30),  # 1ヶ月前
                'search_end': datetime.today(),  # 本日
            }
        )

        return render(request, 'app/index.html', {
            'form': form
        })
