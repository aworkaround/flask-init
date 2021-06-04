## FLASK-INIT

- It is a advanced Blueprint structure of a flask application.
- Can be used as ready to use Flask Hello World Application.
- Ready to deploy complex Flask Web applictions.
- Bootstrap version - v5.0.0-beta1
- Jquery version - 3.5.1
- Please refer requirements.txt for python modules versions.

## Start with this App

- Install python from https://www.python.org/downloads/  (use **sudo apt install python3 -y** on Linux[Ubuntu])
- Download git from https://git-scm.com/downloads  (use **sudo install git -y** on Linux[Ubuntu])
- Go to Windows PowerShell or Command Prompt on your Windows device.  (use Terminal/konsole on linux device)
- Type **git clone https://github.com/9app/flask-init.git** and hit enter.
- Type **cd flask-init**
- Type **pipenv install**
- Type **pipenv shell**
- Type **python ./run.py** and now you can lauch the application on http://localhost:5000 or http://localhost:8080 depending on DEBUG_MODE ENV variable value.


## Please check below folders and files structure -  

**flask-init**  
├── app  
│   ├── __init__.py  
│   ├── config.py  
│   ├── main  
│   │   ├── __init__.py  
│   │   └── routes.py  
│   ├── static  
│   │   ├── css  
│   │   │   └── main.css  
│   │   ├── fonts  
│   │   ├── icons  
│   │   ├── js  
│   │   │   └── main.js  
│   │   └── vendor  
│   │       ├── bootstrap  
│   │       │   ├── bootstrap.min.css  
│   │       │   └── bootstrap.min.js  
│   │       └── jquery  
│   │           └── jquery.min.js  
│   └── templates  
│       ├── base.html  
│       └── main  
│           └── index.html  
├── requirements.txt  
└── run.py  
