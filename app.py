from flask import Flask, render_template, jsonify
from newsfetch.news import Newspaper  # استدعاء الكود الذي أرسلته
import json

app = Flask(__name__)

@app.route('/')
def index():
    # هنا سنقوم بتجربة سحب خبر حقيقي باستخدام المحرك الخاص بك
    # سنستخدم الرابط الموجود في عينة البيانات التي أرسلتها كمثال
    [span_0](start_span)test_url = "https://www.thehindu.com/news/national/jammu-and-kashmir/militants-killed-in-encounter-in-jks-anantnag/article68822224.ece"[span_0](end_span)
    
    try:
        # استخدام كلاس Newspaper من ملفاتك لسحب البيانات
        news = Newspaper(test_url)
        article_data = {
            "headline": news.headline,
            "image": news.image_url,
            "summary": news.description,
            "source": news.publication
        }
    except:
        # [span_1](start_span)في حال فشل السحب، نستخدم بيانات احتياطية من ملف sample.json[span_1](end_span)
        article_data = {
            "headline": "عذراً، تعذر سحب الخبر حالياً",
            "image": "https://via.placeholder.com/1200x600",
            "summary": "تأكد من تثبيت المكتبات المطلوبة في requirements.txt",
            "source": "نظام الطوارئ"
        }

    return render_template('index.html', article=article_data)

if __name__ == '__main__':
    app.run(debug=True)
