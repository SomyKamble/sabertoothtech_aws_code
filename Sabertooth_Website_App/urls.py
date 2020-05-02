from django.urls import path
from Sabertooth_Website_App import views

app_name='main'

urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('services/web_development',views.web_development,name='web_development'),
    path('services/artificial_intelligence',views.artificial_intelligence,name='artificial_intelligence'),
    path('services/application_development',views.application_develoment,name='application_development'),
    path('services/database_management',views.database_management,name='database_management'),
    path('products/',views.product,name='product'),
    path('products/fintech',views.product_fintech,name='product_fintech'),
    path('products/insight',views.product_insight,name='product_insight'),
    path('products/neural_network',views.product_neural_network,name='product_neural_network'),
    path('products/database_management',views.product_database_management,name='product_database_management'),
    path('about/',views.about,name='about'),
    path('career/',views.career,name='career'),
    path('contact/',views.contact,name='contact'),
    path('reachout/',views.reachout,name='reachout'),
    path('SubmitQuery/',views.SubmitQuery,name='SubmitQuery'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('video_calling/',views.video_calling,name='video_calling'),
    path('video_chatbot_calling/',views.video_chatbot_calling,name='video_chatbot_calling'),
]


