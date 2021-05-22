from django.shortcuts import render
from Sabertooth_Website_App.forms import UserDetails
from django import forms
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
from email.message import EmailMessage
from .models import Job
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

key = 'abcdefghijklmnopqrstuvwxyz'


def hashed(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


def privacy(request):
    return render(request, 'main/privacy_policy.html')


def terms(request):
    return render(request, 'main/terms_&_condition.html')


def sendmail(receiver, subject, message, name='', eaddress=''):
    if receiver == 'self':
        receiver = 'hr@sabertoothtech.in'
        # receiver = 'shubhampaliwal3010@gmail.com'
        subject = 'Lead Generated from Website - ' + subject
        message = 'Name : {}'.format(name) + '\nEmail : {}\n'.format(eaddress) + 'Message : {}'.format(message)

    if message == 'default':
        message = 'Thank you {} for contacting Sabertooth Technologies. We will connect with you soon!\n\nNOTE: This is an automatic reply from an unmonitored mail. Please DO NOT REPLY to this mail.\nFor further queries, please drop a mail to hr@sabertoothtech.in. Thankyou!'.format(
            name)

    # email_adderss = "technologiessabertooth@gmail.com"
    # email_password = "sabertooth_0007"
    email_adderss = settings.EMAIL_HOST_USER
    email_password = settings.EMAIL_HOST_PASSWORD
    # print("email-address: {} + email-password: {}".format(email_adderss, email_password))

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_adderss
    msg['To'] = receiver
    msg.set_content(message)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_adderss, email_password)
        smtp.send_message(msg)


def sendmail2(receiver, subject, message, resume, name, eaddress):
    if receiver == 'self':
        receiver = 'hr@sabertoothtech.in'
        # receiver = 'shubhampaliwal3010@gmail.com'
        subject = 'Website Enquiry - ' + subject
        message = 'Name : {}'.format(name) + '\nEmail : {}\n'.format(eaddress) + 'Message : {}'.format(message)

    if message == 'default':
        message = 'Thank you {} for contacting Sabertooth Technologies. We will connect with you soon! Please find attached the Resume submitted by you!\n\nNOTE: This is an automatic reply from an unmonitored mail. Please DO NOT REPLY to this mail.\nFor further queries, please drop a mail to hr@sabertoothtech.in. Thankyou! '.format(
            name)

    # email_adderss = "technologiessabertooth@gmail.com"
    # email_password = "sabertooth_0007"
    email_adderss = settings.EMAIL_HOST_USER
    email_password = settings.EMAIL_HOST_PASSWORD
    # print("email-address: {} + email-password: {}".format(email_adderss, email_password))

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_adderss
    msg['To'] = receiver
    txt = MIMEText(message)
    msg.attach(txt)
    filename = os.path.join(settings.MEDIA_ROOT, resume)
    fo = open(filename, 'rb')
    file = email.mime.application.MIMEApplication(fo.read(), _subtype="pdf")
    fo.close()
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(file)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_adderss, email_password)
        smtp.send_message(msg)


def valid(name, email, subject, message):
    validity = True
    if name.strip() == '':
        validity = False
    if email.strip() == '':
        validity = False
    if subject.strip() == '':
        validity = False
    if message.strip() == '':
        validity = False

    return validity


def valid2(name, email, subject, message):
    validity = True
    if name.strip() == '':
        validity = False
    if email.strip() == '':
        validity = False
    if subject.strip() == '':
        validity = False
    if message.strip() == '':
        validity = False

    return validity


def index(request):
    content_object = {
        "PYTHON": {'content': "Build blazing fast websites and web applications", 'image': "images/PythonLogo.jpg"},
        "DJANGO": {'content': "Ease the creation of complex, database-driven websites",
                   'image': "images/DjangoLogo.png"},
        "ANGULAR": {'content': "Maintain and create front end web framework", 'image': "images/angular.jpg"},
        "JAVASCRIPT": {'content': "Build lightweight, fast and dynamic web pages",
                       'image': "images/JavascriptLogo.jpg"},
        "NODE.JS": {'content': "Build fast and scalable network applications", 'image': "images/NodejsLogo.jpg"},
        "MONGODB": {'content': "Build schema less, document oriented, fast document database",
                    'image': "images/MongodbLogo.jpg"},
        "PYTORCH": {'content': "Deep learning and easy and fast prototyping", 'image': "images/pytorch-logo.jpg"},
        "TENSORFLOW": {'content': "Solve deep learning or machine learning problems",
                       'image': "images/TensorFlowLogo.jpg"},
        "KERAS": {'content': "Develop and evaluate deep learning models", 'image': "images/KerasLogo.jpg"},
        "SELENIUM": {'content': "Automate tests carried out on web browsers for web applications",
                     'image': "images/selenium.jpg"},
        "DOCKER": {'content': "Create, deploy, and run apps by using containers", 'image': "images/docker.jpg"},
        "and many more...": {'content': "Visit our Services Section to know more!", 'image': "images/many-more.jpg"}, }
    mydict = {"complete_records": content_object}
    return render(request, 'main/index.html', context=mydict)


def services(request):
    content_services = {
        "Web Development": {
            "image": "images/language.png",
            "desc": "You think it. We web it!",
            "anch": "main:web_development",
        },
        "Artificial Intelligence": {
            "image": "images/chip.png",
            "desc": "Take off on your own!",
            "anch": "main:artificial_intelligence",
        },
        "Application Development": {
            "image": "images/web-programming.png",
            "desc": "Well Designed & Customised.",
            "anch": "main:application_development",
        },
        "Data Services": {
            "image": "images/database.png",
            "desc": "Get. Sort. Store.",
            "anch": "main:database_management",
        },
    }
    mydict = {"service_list": content_services}
    return render(request, 'main/services.html', context=mydict)


def web_development(request):
    content_web = {
        "basic": {
            'CONTENT MANAGEMENT SYSTEM': {
                'image': 'images/content.png',
                'text': 'Content Management System website designing is the easiest way to add or delete content on a website without any technical training. Efficient CMS websites ease your task of modifying your website content without much dependence on anyone. We analyse and research the market trends and collaborate these with your business requirements to mould a perfect management page for you.'
            },
            'E-COMMERCE': {
                'image': 'images/ecommerce.png',
                'text': 'Custom designed E-commerce website makes you stand out from your competitors. The benefits of an advance technology have compelled businesses to obtain the web for a variety of reasons. This, in turn, calls the undeniable need for E-commerce portals to help businesses strengthen and develop at a faster rate.',

            },
            'ERP': {
                'image': 'images/erp.png',
                'text': 'Enterprise Resource Planning (ERP) software has a strategic value for your business to be a truly efficient tool that brings expected benefits, the ERP system should be customized in accordance with your specific business requirements that proves to be of great help in your operations planning, administration and to optimize internal business processes, comprising of manufacturing, supply chain, financials, customer relationship management, human resources as well as warehouse management.',
            },
        },
        "workflow": {
            'RESEARCH': {
                'image': 'images/research.png',
                'text': 'Defining and researching the UI/UX required and competitor mapping is one of the primary steps while designing. Detailed research on the scope and requirements is carried out to result in the best frontend design.',
            },
            'UI/UX DESIGN': {
                'image': 'images/userinterface.png',
                'text': 'User Interface/User Experience Design is wireframed and prototyped using the strategy developed and modified to suit any necessary changes that satisfies your user base.',
            },
            'DEVELOPMENT': {
                'image': 'images/development.png',
                'text': 'Development of the design is then carried out along with testing and making sure there are absolutely no glitches or errors and the design is user-friendly.',
            },
            'TESTING': {
                'image': 'images/testing.png',
                'text': 'To guarantee the software runs smoothly and looks exactly as the designs, we have a team experts proficient in both manual and automation testing.',
            },
            'DEPLOYMENT': {
                'image': 'images/deployment.png',
                'text': 'We make sure that the deployment of the application is smooth in terms of user accessibility and speed. The deployed application is either on a local system or the Cloud for all the users of the organization.',
            }

        },
        "techstack": {
            "HTML": {
                'image': 'images/html.jpg',
                'desc': 'Building block of a website and its related languages',
            },
            "CSS": {
                'image': 'images/css.jpg',
                'desc': 'Ease of presenting different styles to different viewers',
            },
            "JavaScript": {
                'image': 'images/javascript.jpg',
                'desc': 'Makes your website dynamic and neatly interactive',
            },
            "Angular": {
                'image': 'images/angular.png',
                'desc': 'Maintain and create front end web framework',
            },
            "Bootstrap": {
                'image': 'images/bootstrap.jpg',
                'desc': 'Build responsive, mobile-first projects on the web',
            },
            "Python": {
                'image': 'images/python.jpg',
                'desc': 'Helping you build websites and web applications',
            },
            "Django": {
                'image': 'images/django.png',
                'desc': 'Ease the creation of complex and database driven websites',
            },
            "Node.js": {
                'image': 'images/nodejs.jpg',
                'desc': 'Build fast and scalable network applications',
            },
            "Flask": {
                'image': 'images/flask.jpg',
                'desc': 'Fast and Lightweight framework for Python',
            },
            "jQuery": {
                'image': 'images/jquery.jpg',
                'desc': 'Optimize your concept to creation time with this library',
            },
            "AJAX": {
                'image': 'images/ajax.jpg',
                'desc': "Improve your customer's user experience with this library",
            },
            "MySQL": {
                'image': 'images/sql.jpg',
                'desc': 'Scalable database to add, access & managing content',
            },
            "PostgreSQL": {
                'image': 'images/postgre.jpg',
                'desc': 'Scalable database to add, access & managing content',
            },
            "Selenium": {
                'image': 'images/selenium.jpg',
                'desc': 'Automates your browser for testing',
            },
            "Docker": {
                'image': 'images/docker.jpg',
                'desc': 'Virtualization to deliver software in packages',
            },
        },
    }
    mydict = {'web_list': content_web}
    return render(request, 'main/web_development.html', context=mydict)


def artificial_intelligence(request):
    artificial_intelligence = {
        "basic": {
            'MACHINE LEARNING': {
                'image': 'images/machine-learning.png',
                'text': 'Machine learning allows computers to determine rules on how data changes without explicitly programming those rules : Study available data and analyze clients’ behaviors to discover patterns , Make predictions and decisions based on historical records , Discover similarities or anomalies in data'
            },
            'PREDICTIVE ANALYTICS': {
                'image': 'images/predictive-analysis.png',
                'text': 'Predictive analytics provides assessment on future trends. Using the available historical data, Reduces churn by identifying the clients who want to leave, Increases sales by suggesting what the client wants to buy and determines how much they will buy, Identifies employees who are likely to leave the company, Predicts demand for resources, product, and inventory, Identifies the risk of breakdowns, failures, malfunction, errors ',

            },
            'RECOMMENDATION ENGINES': {
                'image': 'images/recommendation-engines.png',
                'text': 'Recommendation engines can be utilized in a variety of areas, including movies, music, books or other products. These engines will Personalize offers basing on client’s earlier choices and review. Suggest other videos, songs, books etc. that the client will like. Increase conversion rate. Improve customer experience. Increase retention and loyalty',
            },
            'NATURAL LANGUAGE PROCESSING': {
                'image': 'images/natural-language-processing.png',
                'text': 'NLP lets companies better use language data thanks to effective processing of large amounts of voice or text messages. Natural language processing. Extracts specific data from long texts(e.g. articles, books, bills). Automatically processes invoices, orders, contractsIdentifies the writer’s emotions and recognizes hate speechImproves customer experience with chatbots and virtual assistants',
            },
            'DEEP LEARNING': {
                'image': 'images/deep-learning.png',
                'text': 'We train computer model to learn and perform classification tasks directly from images, text, or sound. Deep learning models can achieve state-of-the-art accuracy, sometimes exceeding human-level performance. Models are trained by using a large set of labeled data and neural network architectures that contain many layers',
            },
        },
        "techstack": {
            "PyTorch": {
                'image': 'images/pytorch-logo.jpg',
                'desc': 'Open Source computer vision and natural language processing library',
            },
            "Theano": {
                'image': 'images/theano.jpg',
                'desc': 'Define, optimize, & evaluate mathematical expressions',
            },
            "Caffe": {
                'image': 'images/caffe.jpg',
                'desc': 'Deep learning framework made with expression, speed & modularity',
            },
            "Python": {
                'image': 'images/python.jpg',
                'desc': 'Build state-of-the-art intelligent models with Python',
            },
            "Keras": {
                'image': 'images/keras.jpg',
                'desc': 'Deep learning and fast prototyping',
            },
            "Tensorflow": {
                'image': 'images/tensor.jpg',
                'desc': 'Solve deep learning or machine learning problems using neural networks',
            },
        },
    }
    mydict = {'ai_list': artificial_intelligence}
    return render(request, 'main/artificial_intelligence.html', context=mydict)


def database_management(request):
    database_management = {
        "basic": {
            'LIVE DATA API': {
                'image': 'images/api.png',
                'text': 'We turn data from multiple sources into machine-readable data feeds which can be accessed by anyone at ease. We deliver clean, structured, and organized datasets which can be integrated quickly and easily.  Experience the most advanced database management service which include Data Analysis and AI & Machine learning.'
            },
            'DATA ANALYTICS': {
                'image': 'images/data-analysis.png',
                'text': 'Our database assessment and evaluation service includes a wide range of processes followed in order to analyze the data requirement of the organization and tools for DBA Governance of database for ensuring high security, Database health checks to look for any file corruption, logical block corruption , Analyzing data for storage optimizationEvaluating DBA tools to ensure proper design & implementation of database system, Improve your predictive analytics and risk modeling using historical API data',

            },
            'CLOUD COMPUTING': {
                'image': 'images/cloud-computing.png',
                'text': 'Deploying and maintaining your applications on remote cloud servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer to increase security as well as lightning fast accessibility from all over the world',
            },
        },
        "techstack": {
            "Amazon Web Services": {
                'image': 'images/aws.jpg',
                'desc': 'World\'s largest on demand cloud computing platform',
            },
            "Google Cloud Platform": {
                'image': 'images/gcp.jpg',
                'desc': 'Suite of cloud computing services that runs on Google\'s Infrastructure',
            },
            "Microsoft Azure": {
                'image': 'images/azure.jpg',
                'desc': 'Building, Testing, Deploying, & managing applications through Microsoft managed data centers',
            },
            "MongoDB": {
                'image': 'images/MongodbLogo.jpg',
                'desc': 'Cross-platform document oriented database program',
            },
            "MySQL": {
                'image': 'images/sql.jpg',
                'desc': 'Scalable database to add, access & managing content',
            },
            "PostgreSQL": {
                'image': 'images/postgre.jpg',
                'desc': 'Scalable database to add, access & managing content',
            },
            "Tableu": {
                'image': 'images/TableauLogo.jpg',
                'desc': 'Simplify your raw data into easily understandable format',
            },
        },
    }
    mydict = {'database_list': database_management}
    return render(request, 'main/database_management.html', context=mydict)


def application_develoment(request):
    application_development = {
        "basic": {
            'USER EXPERIENCE(UX)': {
                'image': 'images/wireframe.png',
                'text': 'Intuitive designs combined with compelling user experience are what makes our apps stand ahead in the digital age. Seamless experience driven by international standards in collaboration with our out-of-the-box ideas is the specialty of Sabertooth\'s applications helping your business accomplish its goals.'
            },
            'USER INTERFACE(UI)': {
                'image': 'images/layers.png',
                'text': 'We believe that the customer always comes first - and that means exceptional products and exceptional services. Get in touch today to learn more about what we have to offer.',

            },
            'AGILE MODEL (SDLC)': {
                'image': 'images/software-development.png',
                'text': 'Incorporating Agile software development life cycle practice which promotes continuous iteration of application development and testing throughout the development lifecycle of the project. Both development and testing activities are concurrent to increase the quality of the product.',
            },
            'DEVELOPMENT': {
                'image': 'images/development.png',
                'text': 'We have always been at the forefront of creating powerful and immersive applications. Our unique approach in tandem with our bleeding-edge development techniques has helped us to build world-changing applications for people of all walks of life.',
            },
            'TESTING': {
                'image': 'images/testing.png',
                'text': 'Development of the design is then carried out along with testing and making sure there are absolutely no glitches or errors and the design is user-friendly.',
            },
            'DEPLOYMENT': {
                'image': 'images/deployment.png',
                'text': 'We make sure that the deployment of the application is smooth in terms of user accessibility and speed. The deployed application is either on a local system or the Cloud for all the users of the organization.',
            },
            'DEV OPS': {
                'image': 'images/together.png',
                'text': 'We bridge the gap between the two teams: Development and Operations by creating a collaborative work culture, which improves agility, optimize resources, allows experimentations with accelerated deliveries, faster detection, and remediation.',
            },
        },
        "techstack": {
            "Java": {
                'image': 'images/java.jpg',
                'desc': 'Build state-of-the-art intelligent models with Java',
            },
            "Python": {
                'image': 'images/python.jpg',
                'desc': 'Build state-of-the-art intelligent models with Python',
            },
            "React Native": {
                'image': 'images/react-native.jpg',
                'desc': 'Build state-of-the-art intelligent models with React Native',
            },
            "HTML": {
                'image': 'images/html.jpg',
                'desc': 'Building block of a website and its related languages',
            },
            "CSS": {
                'image': 'images/css.jpg',
                'desc': 'Ease of presenting different styles to different viewers',
            },
            "JavaScript": {
                'image': 'images/javascript.jpg',
                'desc': 'Makes your website dynamic and neatly interactive',
            },
            "Angular": {
                'image': 'images/angular.png',
                'desc': 'Maintain and create front end web framework',
            },
            "Django": {
                'image': 'images/django.png',
                'desc': 'Ease the creation of complex and database driven websites',
            },
            "Node.js": {
                'image': 'images/nodejs.jpg',
                'desc': 'Build fast and scalable network applications',
            },
            "Experience Design": {
                'image': 'images/xd.jpg',
                'desc': 'Generate wireframes and prototypes of your website',
            },
            "Illustrator": {
                'image': 'images/illu.jpg',
                'desc': 'Designing beautiful Illustrations for your brand and clients',
            },
            "Photoshop": {
                'image': 'images/photoshop-express.jpg',
                'desc': 'Create your web page design with pixel perfection',
            },
        },
    }
    mydict = {"app_list": application_development}
    return render(request, 'main/application_development.html', context=mydict)


def product(request):
    product_content = {
        "DATA MANAGEMENT":
            {
                'content': "Harnessing the power of data to build impactful solutions through Data Mining, Data Extraction, Web Scraping and other data driven techniques. ",
                'image': 'images/DataApiLogo.jpg',
                'anch': 'main:product_database_management'},
        "DEEP LEARNING":
            {'content': "Building Tech of the Future, in the present, with Deep Learning knowledge and expertise.",
             'image': 'images/DeepLearningLogo.jpg',
             'anch': 'main:product_neural_network'},
        "FINTECH":
            {
                'content': "Powering exponential growth in the financial world by changing the game through innovation and technology.",
                'image': 'images/FintechLogo.jpg',
                'anch': 'main:product_fintech'},
        # "CLOUD":
        # {'content': "Cloud designed for your business needs",
        #  'image': "images/CloudLogo.jpg",
        #  'anch': 'main:product_cloud'},
        "INSIGHTS":
            {
                'content': "Running ahead of the competiton using a high functioning system that predicts the impact of news on stock prices.",
                'image': "images/InsightsLogo.jpg",
                'anch': 'main:product_insight'}
    }

    # anchors = [
    #     'https://github.com/Sabertoothtech',
    #     'https://github.com/Sabertoothtech',
    #     'https://github.com/Sabertoothtech',
    #     'https://github.com/Sabertoothtech',
    #     'https://public.tableau.com/profile/adil.warsi#!/vizhome/NIFTYNEWSANDSTOCKDATAPUBLIC/Dashboard1?publish=yes'

    # ]
    # i = 0
    # for ele in product_content.keys():
    #     product_content[ele]['anch'] = anchors[i]
    #     i += 1

    mydict = {"product_list": product_content}
    return render(request, 'main/product.html', context=mydict)


def product_database_management(request):
    return render(request, 'main/product_database_management.html')


def product_fintech(request):
    return render(request, 'main/product_fintech.html')


def product_insight(request):
    return render(request, 'main/product_insight.html')


def product_neural_network(request):
    return render(request, 'main/product_neural_network.html')


def about(request):
    return render(request, 'main/about.html')


def career(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        resume = request.FILES.get('myfile')
        print(filename)

        if valid2(name, email, subject, message):
            sendmail2('self', subject, message, filename, name, email)
            sendmail2(email, 'Welcome To Sabertooth Technologies!', 'default', filename, name, email)

        job = Job.objects.all()
        args = {'jobs': job}
        return render(request, 'main/career.html', args)

    job = Job.objects.all()
    args = {'jobs': job}
    return render(request, 'main/career.html', args)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        if valid(name, email, subject, message):
            sendmail('self', subject, message, name, email)
            sendmail(email, 'Welcome To Sabertooth Technologies!', 'default', name)
    return render(request, 'main/contact.html')


def reachout(request):
    return render(request, 'main/reachout.html')


@csrf_exempt
def SubmitQuery(request):
    cname = request.POST.get("name")
    cemail = request.POST.get("email")
    cquery = request.POST.get("query")

    # receiver = 'contact@sabertoothtech.in'
    receiver = 'hr@sabertoothtech.in'
    # receiver = 'shubhampaliwal3010@gmail.com'
    subject = 'Lead Generated from Website'
    message = 'Lead Generated from the Website --- \n' + 'Name : {}'.format(cname) + '\nEmail : {}\n'.format(
        cemail) + 'Message : {}'.format(cquery)

    # email_adderss = hashed(5, 'yjhmstqtlnjxxfgjwyttym@lrfnq.htr')
    # email_password = 'S'+hashed(5, 'fgjwyttymyjhm_0007')
    # email_adderss = "technologiessabertooth@gmail.com"
    # email_password = "sabertooth_0007"
    email_adderss = settings.EMAIL_HOST_USER
    email_password = settings.EMAIL_HOST_PASSWORD
    # print("email-address: {} + email-password: {}".format(email_adderss, email_password))

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_adderss
    msg['To'] = receiver
    msg.set_content(message)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_adderss, email_password)
        smtp.send_message(msg)

    return render(request, 'main/reachout.html')


def chatbot(request):
    return render(request, "main/chatbot_index.html")


# Create your views here.
def video_calling(request):
    return render(request, 'main/video_calling.html')


# Create your views here.
def video_chatbot_calling(request):
    return render(request, 'main/video_chatbot_calling.html')


# Create your views here.
def webrtc(request):
    return render(request, 'main/webrtc.html')
