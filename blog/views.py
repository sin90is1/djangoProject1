from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    context = {
        "articles": [
            {
                "title": " تیم ملی زیرورو شد؛ خداحافظی با معروف و دوستان!",
                "description": "دروازه‌بان تیم فوتبال خلیج فارس ماهشهر که تیمش توانست با درخشش او به نیمه نهایی جام حذفی برسد، از روزهای سخت پیش از این موفقیت حرف زده است.",
                "img": "https://news.varzeshe3.com/pictures/2022/04/10/B/smszcsni.jpg?w=350"

            },
            {
                "title": "مصیبت در انتظار رونالدو؛ نوجوان مضروب اوتیسم دارد (عکس)",
                "description": "تیم ملی زیرورو شد؛ خداحافظی با معروف و دوستان!",
                "img": "https://news.varzeshe3.com/pictures/2022/04/10/D/lltropm4.jpg?w=350"
            }
        ]
    }
    return render(request, "blog/home.html", context)
