from flask import Flask, redirect, url_for, render_template, request
import smtplib
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method =='POST':
        ############ get input info ################
        sender ='aberdeensouthconcernedcitizens@gmail.com'
        letter = 'To my elected representative,\n\n I am writing to you today to express my concern regarding the proposed development of OP56 St Fitticks park which for the remainder of this email will be referred to as St Fitticks Park.\n\nIn recent years, in the name of development, Torry has lost the Victoria Road field to the Marine Centre, lost the Nigg Bay beach area to the Aberdeen Harbour Expansion Project (AHEP) and gained an incinerator.\n\nBoth developments were accepted as essential for the future prosperity of the area and we, the Community, sacrificed green space to development. It of course goes without saying that only one of these developments has been completed and the other is in a state of disrepair which has led to the temporary loss to the Community of the coastal road. Who knows when access will be returned? I am sure you will understand my surprise when I found out the council planned to develop on the lands around St Fitticks Park for an industrial area to support AHEP, which has been so disastrously implemented to date.\n\nThe proposed area of development will steal from the Community beautiful green area around peoples homes and a well-loved area locally known as the triangle where many generations of teenagers have gone to play football.\n\nThe party you represent stands on a manifesto for environmental protection and help to vulnerable communities. Do I have your assurance that you will stand by this commitment upon which you were elected? We have a city with ever increasing empty commercial lots, especially in the nearby Altens Industrial Estate, which is a more proper location for this site. The burden of transport should be placed on those using the harbour, not a burden upon the health of the Community around it.\n\nWould you attempt to justify allocating yet more space to industrial development right on peoples doorstep?\n\n\nBest Regards,'
        #citizenname = 'Neils Wood'
        #citizenpostcode = 'AB11 8BR'
        #citizenemail = 'm.maaslowit@gmail.com'
        citizenname = request.form["name"]
        citizenpostcode = request.form["postcode"]
        citizenemail = request.form["email"]
        recipients = ['nmwabz1992@gmail.com', 'neilsmckenziewood@gmail.com']
        #recipients =  ['Maureen.Watt.msp@parliament.scot', 'stephen.flynn.mp@parliament.uk', 'yallan@aberdeencity.gov.uk', 'callard@aberdeencity.gov.uk', 'audnicoll@aberdeencity.gov.uk']
        ############ email together ##############
        for i in recipients:
            fromaddr = 'From: ' + sender +'\n'
            cc = 'CC:' + citizenemail + '\n'
            toaddr = 'To: ' + i + '\n'
            subj = 'Subject: ' + 'Development of OP56 at St Fitticks park\n'
            body = fromaddr + cc + toaddr +  subj + letter + '\n\n' + citizenname + '\n' + citizenpostcode + '\n' + citizenemail
            ##############  SEND EMAIL STARTS #################
            server = smtplib.SMTP('smtp.gmail.com', port=587)
            server.ehlo()
            server.starttls()
            server.login('aberdeensouthconcernedcitizens@gmail.com', 't0rryToRRY')
            server.sendmail(sender, i, body)
            server.quit()
        return redirect(url_for("complete"))
    else:
        return render_template('index.html')
@app.route("/")
def complete():
    return f"Thanks, your email should now have been sent \
        to your representatives. Check your inbox for an email \
            you are cc'd on, if it is not there within 5 minutes \
                please repeat the process."
if __name__ == "__main__":
    app.run()
    
    

