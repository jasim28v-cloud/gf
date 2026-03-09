# استيراد الأدوات التي أرسلتها لي
from newsfetch.news import Newspaper
from newsfetch.helpers import clean_text
import json

def start_scraping(url):
    print(f"جاري سحب الخبر من: {url} ...")
    
    # استخدام كود Newspaper الذي أرسلته
    try:
        news = Newspaper(url)
        
        # تجهيز البيانات المستخرجة
        article_data = {
            "headline": news.headline,
            "image_url": news.image_url,
            "description": news.description,
            "publication": news.publication,
            "summary": news.summary,
            "authors": news.authors
        }
        
        # حفظ النتيجة في ملف sample.json لكي يقرأها الموقع
        with open('sample.json', 'w', encoding='utf-8') as f:
            json.dump(article_data, f, ensure_ascii=False, indent=4)
            
        print("تم سحب الخبر وحفظه بنجاح في ملف sample.json!")
        
    except Exception as e:
        print(f"حدث خطأ أثناء السحب: {e}")

if __name__ == "__main__":
    # يمكنك وضع أي رابط خبر هنا لتجربة السحب
    target_url = "https://www.thehindu.com/news/national/jammu-and-kashmir/militants-killed-in-encounter-in-jks-anantnag/article68822224.ece"
    start_scraping(target_url)
