# School_App
Task by BPK Tech, Hyderabad

Steps to execute:
1. Open Command Line Interface (Terminal in Linux, CMD prompt in windows)
2. Navigate to Project Directory
3. (Optional) Create and Activate Virtual Environment
4. Install Dependencies in requirements.txt (pip install -r requirements.txt)
5. Run app.py using coomand: flask run
6. If succesfful, message will be displayed as: * Running on http://127.0.0.1:5000
7. In Browser, provide address of server with port number displayed (Here 127.0.0.1:5000)
8. Congratulations You  can access Application.


Files descrition:
  1. app.py : Main executable file for application contains logic to handle and store data.
  2. templates/hello.html : Provide User Interface. It is default startup page.
  3. templates/base.html : Common html content of every page like Navigation bar, footer, title, etc. Used to reuse html content for every page.
  4. templates/upadte.html : You will navigate to this page when you click on Update button.
  5. static/ : This folder includes css and javascript files for additional formatting and control
  6. instance/data.db : Database file storing all the data you entered in Add Student data form. One can view this data using (https://inloop.github.io/sqlite-viewer/)
  7. Procfile : Process file indicates to run gunicorn HTTP server on application Startup
  8. requirements.txt : Required dependencies/modules to run application.
     Note: If you are using Virtual environment, ensure that all dependencies installed in virutal environment. You can check this dependencies in lib sub-directory of virtual environment directory.
