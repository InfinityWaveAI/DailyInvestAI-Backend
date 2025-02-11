from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Daily Invest AI"}

@app.post("/news")
async def getNews():
    news = [{'company name': 'IRB INFRASTRUCTURE DEVELOPERS LTD',
  'timestamp': '2025-01-09 12:44:12',
  'news': ['IRB INFRASTRUCTURE DEV: IRB INFRA AND IRB INFRASTRUCTURE TRUST (PRIVATE INVIT) TOGETHER REGISTER 19% (YOY) GROWTH TOLL COLLECTION FOR DECEMBER 2024 || DECEMBER 2024 TOLL COLLECTION IS RS. 580 CRS VS RS. 488 CRS IN DECEMBER 2023'],
  'symbol': 'IRB',
  'translation': [{'english': 'IRB INFRASTRUCTURE DEV: IRB INFRA AND IRB INFRASTRUCTURE TRUST (PRIVATE INVIT) TOGETHER REGISTER 19% (YOY) GROWTH TOLL COLLECTION FOR DECEMBER 2024 || DECEMBER 2024 TOLL COLLECTION IS RS. 580 CRS VS RS. 488 CRS IN DECEMBER 2023',
    'hindi': 'आईआरबी इन्फ्रास्ट्रक्चर विकास: आईआरबी इन्फ्रा और आईआरबी इन्फ्रास्ट्रक्चर ट्रस्ट (निजी आमंत्रण) ने मिलकर दिसंबर 2024 के लिए 19% (वर्ष-दर-वर्ष) वृद्धि टोल संग्रह दर्ज किया || दिसंबर 2024 टोल संग्रहण रु. 580 सीआरएस बनाम रु. दिसंबर 2023 में 488 करोड़',
    'telugu': 'IRB ఇన్\u200cఫ్రాస్ట్రక్చర్ DEV: IRB INFRA మరియు IRB ఇన్\u200cఫ్రాస్ట్రక్చర్ ట్రస్ట్ (ప్రైవేట్ ఆహ్వానం) కలిసి 19% నమోదు చేయండి (YOY) డిసెంబర్ 2024కి వృద్ధి టోల్ కలెక్షన్ || డిసెంబర్ 2024 టోల్ కలెక్షన్ రూ. 580 CRS VS RS. డిసెంబర్ 2023లో 488 CRS',
    'bengali': 'IRB ইনফ্রাস্ট্রাকচার ডেভ: IRB ইনফ্রা এবং IRB ইনফ্রাস্ট্রাকচার ট্রাস্ট (ব্যক্তিগত আমন্ত্রণ) একসাথে নিবন্ধন করুন 19% (YOY) গ্রোথ টোল সংগ্রহ ডিসেম্বর 2024 এর জন্য || ডিসেম্বর 2024 টোল সংগ্রহ হল রুপি। 580 CRS বনাম RS। 2023 সালের ডিসেম্বরে 488 CRS',
    'tamil': 'IRB INFRASTRUCTURE DEV: IRB INFRA மற்றும் IRB இன்ஃப்ராஸ்ட்ரக்சர் டிரஸ்ட் (தனியார் அழைப்பு) இணைந்து 19% பதிவு செய்யுங்கள் (YOY) டிசம்பர் 2024க்கான வளர்ச்சி கட்டண வசூல் || டிசம்பர் 2024 டோல் வசூல் ரூ. 580 CRS VS RS. டிசம்பர் 2023 இல் 488 CRS'}]}
    ]
    return news

@app.post("/price")
async def getPrice():
    price = [
        {'company name': 'IRB INFRASTRUCTURE DEVELOPERS LTD',
        'price': [50.10, 50.15, 50.13]}

    ]
    return price

