# importing libraries
from flask import Flask,render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "onboarding@bosscoderacademy.com"
app.config['MAIL_PASSWORD'] = 'onboard@bosscoder'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
   msg = Message(
                'Hello',
                sender ='onboarding@bosscoderacademy.com',
                recipients = ['juniorkevinu@gmail.com']
               )
   msg.body = 'Hello Flask message sent from Flask-Mail'
   msg.html = render_template('index.html')
   mail.send(msg)
   return 'Sent'
   
if __name__ == '__main__':
   app.run(debug = True)
   
   
   
   
# def sendEmail(toaddr, name, password):

#     fromaddr = "onboarding@bosscoderacademy.com"
#     msg = MIMEMultipart()
#     msg["From"] = fromaddr
#     msg["To"] = toaddr
#     msg["Subject"] = "Welcome to Bosscoder Academy! Signup now."
#     body = (
#         "Hi "
#         + name
#         + ", welcome to Bosscoder Academy. \n\nSignup now to get access to the web portal of bosscoder. \n\nBelow are the details \nWebsite: https://student.bosscoderacademy.com \nUsername: "
#         + toaddr
#         + "\nPassword: "
#         + password
#         + "\n\nThanks, Bosscoder Academy"
#     )

#     msg.attach(MIMEText(body, "plain"))

#     s = smtplib.SMTP("smtp.gmail.com", 587)

#     s.starttls()

#     s.login(fromaddr, "onboard@bosscoder")

#     text = msg.as_string()

#     s.sendmail(fromaddr, toaddr, text)

#     s.quit()