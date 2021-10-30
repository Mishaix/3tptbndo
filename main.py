import os
import telebot
from flask import Flask, request


rp = "1.png"

#API KEY
my_secret = os.environ['API_KEY']

#Variable to make it easier to call the bot's functions
bot = telebot.TeleBot(my_secret)

#init server with flask
server = Flask(__name__)

#Function for when the bot is started on the user's end
@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello! I'm the virtual Telegram assistant for 3 TPT BN. Which information would you like me to retrieve?\n\nDOO Reporting Procedure: /doorp\nDOO IR Templates: /temp\nCAT 1 Status: /cat1\nContacts: /cont")

#Function for when the user types or clicks on help
@bot.message_handler(commands=['temp'])
def temp(message):
  bot.reply_to(message, "*Please click the necessary templates for the relevant cases*: \n Ag+ / C+ /Agc \n HRW /hrw \n Known Contact to Ag+/ C+ /known \n Hospitalization (Non Send Out) /hos \n Ambulance (Send-Out/Hospitalization) /amb \n NCVI /nvci \n Civil Offense /civo \n Other Ad-Hoc cases /adhoc ", parse_mode='Markdown')

  #Function for when the user types or clicks on agc
@bot.message_handler(commands=['Agc'])
def Agc(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAg+/ C+\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Contact Number:*\n\n*5. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*6. Brief Description of the Incident:*\nC+\nServiceman went to (Location of Clinic/Medical Centre) on DDMMYY, HHMMhrs after developing symptoms for (Symptoms) on DDMMYY, HHMMhrs. He was administered PCR swab and was tested positive on DDMMYY, HHMMhrs.\n\nAg+\nServiceman administered ART after developing symptoms for [Symptoms] on DDMMYY, HHMMhrs and was tested positive on DDMMYY, HHMMhrs. He then went to [Medical Centre/Clinic] for PCR swab and returned [Location] for SHRO. Results are currently pending.\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.He was last in [Location of camp] on DDMMYY, HHMMhrs.\n\n*7. Follow up description:*\nWaiting for PCR swab results/ Update caa DDMMYY\n\n*8. NOK informed:*\nYes\n\n*9. Reportings:*\nIHQ:\nGSOC:\nCOVID E-Form\nAIMSIS:\nIncident Case Report No:\n\n*10. Reported by:\n", parse_mode='Markdown')

#Function for when the user types or clicks on hrw
@bot.message_handler(commands=['hrw'])
def hrw(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nHRW\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*4. Brief Description of the Incident:*\nServiceman received a HRW text and was immediately placed on SHRO at (Residence/Camp) from DDMMYY to DDMMYY. Serviceman self-administered D0 ART on DDMMYY, HHMMhrs and tested (Result).\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.\n\n*5. Follow up description:*\nAwaiting D7 result on DDMMYY/ Update caa DDMMYY\n\n*6. NOK informed:*\nYes\n\n*7. Verbal Reportings:*\nIHQ:\nGSOC:\nCOVID E-Form\n\n*8. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on known
@bot.message_handler(commands=['known'])
def known(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nKnown Contact(s) to Household/SAF Symptomatic/Asymptomatic Ag+\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*4. Brief Description of the Incident:*\nServiceman was a close contact to his/her [Known contact] that was tested positive on DDMMYY, HHMMhrs. Serviceman will be placed on SHRO at [Residence/Camp] from DDMMYY to DDMMYY. Serviceman self-administered D0 ART on DDMMYY, HHMMhrs and tested [Result].\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.\n\n*5. Follow up description:*\nAwaiting D7 result on DDMMYY/ Update caa DDMMYY\n\n*6. NOK informed:*\nYes\n\n*7. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on hos
@bot.message_handler(commands=['hos'])
def hos(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAmbulance Send-Out\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*5. Brief Description of the Incident:*\nServiceman went for XX surgery at (Location) hospital. Surgery commenced at HHMMhrs and completed at HHMMhrs. Serviceman is warded at Ward XX, Room/Bed XX.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on amb
@bot.message_handler(commands=['amb'])
def amb(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAmbulance Send-Out\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*5. Brief Description of the Incident:*\nServiceman experienced (Symptoms) and reported sick at (Location) Medical Centre at HHMMhrs. \n\nHe was accessed by the MO for (Diagnosis) and was sent to (Location) Hospital at HHMMhrs for further treatment. (Commander) is accompanying him.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')


#Function for when the user types or clicks on nvci
@bot.message_handler(commands=['nvci'])
def nvci(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\n NCVI/ CVI \n\n*2. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*3. Location of the Incident:*\nCamp/Location:\nArea:\n\n*4. Vehicles Involved:*\n\n*5. Rank & Full name of Serviceman involved:*\n\n*6. PES:*\n\n*7. Brief Description of the Incident:*\nTO was (5W1H)\n\nNo injuries to personnel.\n\n*8. IVC Footage:*\nTo be extracted\n\n*9. IVD Data:*\nTo be extracted\n\n*10. Maint Record:*\n1)Last UQM Date:\n2)Next UQM Date:\n3)Last AVI Date:\n4)Next AVI Date:\n\n*11. Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*12. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on civo
@bot.message_handler(commands=['civo'])
def civo(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nCivil Offense - (Type of Incident)\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*5. Location of the Incident:*\n\n*6. Brief Description of the Incident:*\nOn DDMMYY, HHMMhrs, (Serviceman’s Rank and Name) was (In depth details) was caught by Policemen from (Division. Subsequently, he was arrested on DDMMYY, HHMMhrs for involvement in (Offense).\n\nServiceman was released on bail on DDMMYY, HHMMhrs. His bail amount is ($$/ Any other collateral- delete whenever necessary). He will be required to report at (Location), on DDMMYY, HHMM.\n\n*7. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*8. NOK informed:*\nYes\n\n*9. Reportings:*\nGSOC:\nIHQ:\nAIMSIS:\nIncident Case Report No:\n\n*10. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on adhoc
@bot.message_handler(commands=['adhoc'])
def adhoc(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, MMHHhrs\n\n*5. Brief Description of the Incident:*\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Reportings:*\nGSOC:\nIHQ:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on cat1
@bot.message_handler(commands=['cat1'])
def cat1(message):
  bot.reply_to(message, "https://t.me/ArmyCAT1", parse_mode='Markdown')

#Function for when the user types or clicks on cat1
@bot.message_handler(commands=['doorp'])
def doorp(message):
  bot.send_photo(message.chat.id, open('1.png','rb'))

#Initiates the Bot
#bot.polling()  


# SERVER SIDE 
@server.route('/' + my_secret, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200
@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='https://thirdtptbndoo.herokuapp.com/' + my_secret)
   return "!", 200
if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))