import os
import telebot
from datetime import date,timedelta
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

#Testing
rp = "1.png"

#API KEY
my_secret = os.environ['API_KEY']

#Variable to make it easier to call the bot's functions
bot = telebot.TeleBot(my_secret)

#Container to hold blueops's values
blueops_dict = {}

#Blueops Class
class Blueops:
    def __init__(self,datE):
        self.datE = datE
        self.timE = None
        self.name = None
        self.contact = None
        self.location = None
        self.informe = None

#Storing today and tomorrow's dates into values
today = date.today().strftime("%d%m%y")
tow= date.today() + timedelta(days=1)
tomorrow = tow.strftime("%d%m%y")

#init server with flask
server = Flask(__name__)

#Function for when the bot is started on the user's end
@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello! I'm the virtual Telegram assistant for 3 TPT BN. Which information would you like me to retrieve?\n\nDOO Reporting Procedure: /doorp\nDOO IR Templates: /temp\nAg+ / C+ Management: /man\nContacts: /cont\nHelpful Links: /links\nOps Blue Dagger: /obd")

#Function for when the user types or clicks on help
@bot.message_handler(commands=['temp'])
def temp(message):
  bot.reply_to(message, "*Please click the necessary templates for the relevant cases*: \n Ag+ / C+ /agc \n HRW /hrw \n Known Contact to Ag+/ C+ /known \n Hospitalization (Non Send Out) /hos \n Ambulance (Send-Out/Hospitalization) /amb \n NCVI /nvci \n Civil Offense /civo \n Other Ad-Hoc cases /adhoc ", parse_mode='Markdown')

#Function for when the user types or clicks on agc
@bot.message_handler(commands=['agc'])
def agc(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAg+/ C+\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Contact Number:*\n\n*5. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*6. Brief Description of the Incident:*\nC+\nServiceman went to (Location of Clinic/Medical Centre) on DDMMYY, HHMMhrs after developing symptoms for (Symptoms) on DDMMYY, HHMMhrs. He was administered PCR swab and was tested positive on DDMMYY, HHMMhrs.\n\nAg+\nServiceman administered ART after developing symptoms for (Symptoms) on DDMMYY, HHMMhrs and was tested positive on DDMMYY, HHMMhrs. He then went to (Medical Centre/Clinic) for PCR swab and returned (Location) for SHRO. Results are currently pending.\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.He was last in (Location of camp) on DDMMYY, HHMMhrs.\n\n*7. Follow up description:*\nWaiting for PCR swab results/ Update caa DDMMYY\n\n*8. NOK informed:*\nYes\n\n*9. Reportings:*\nIHQ:\nGSOC:\nCOVID E-Form\nAIMSIS:\nIncident Case Report No:\n\n*10. Reported by:*\n ", parse_mode='Markdown')

#Function for when the user types or clicks on hrw
@bot.message_handler(commands=['hrw'])
def hrw(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nHRW\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman received a HRW text and was immediately placed on SHRO at (Residence/Camp) from DDMMYY to DDMMYY. Serviceman self-administered D0 ART on DDMMYY, HHMMhrs and tested (Result).\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.\n\n*6. Follow up description:*\nAwaiting D7 result on DDMMYY/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ:\nGSOC:\nCOVID E-Form\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on known
@bot.message_handler(commands=['known'])
def known(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nKnown Contact to Household/SAF Symptomatic/Asymptomatic Ag+/ C+\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman was a known contact to his/her (Known contact) that was tested (ART/PCR) positive on DDMMYY, HHMMhrs. Serviceman will be placed on SHRO at (Residence/Camp) from DDMMYY to DDMMYY. Serviceman self-administered D0 ART on DDMMYY, HHMMhrs and tested (Result). Serviceman currently (have/ do not have) flu symptoms.\n\nServiceman is fully/not vaccinated. First Dose on DDMMYY and Second Dose on DDMMYY.\n\n*6. Follow up description:*\nAwaiting D7 result on DDMMYY/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8.Reportings:*\nIHQ:\nGSOC:\nCOVID E-Form:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on hos
@bot.message_handler(commands=['hos'])
def hos(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAmbulance Send-Out\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman went for XX surgery at (Location) hospital. Surgery commenced at HHMMhrs and completed at HHMMhrs. Serviceman is warded at Ward XX, Room/Bed XX.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on amb
@bot.message_handler(commands=['amb'])
def amb(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAmbulance Send-Out\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman experienced (Symptoms) and reported sick at (Location) Medical Centre at HHMMhrs. \n\nHe was accessed by the MO for (Diagnosis) and was sent to (Location) Hospital at HHMMhrs for further treatment. (Commander) is accompanying him.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')


#Function for when the user types or clicks on nvci
@bot.message_handler(commands=['nvci'])
def nvci(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\n NCVI/ CVI \n\n*2. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*3. Location of the Incident:*\nCamp/Location:\nArea:\n\n*4. Vehicles Involved:*\n\n*5. Rank & Full name of Serviceman involved:*\nTO/DV\nVC (If necessary)\nFP (If necessary)\n\n*6. PES:*\n\n*7. Brief Description of the Incident:*\nOn DDMMYY at HHMMhrs, (Name of TO or DV) was driving MIDXXXXX (State Vehicle Type) in (Location of Camp Location or Road Location) for (Purpose). He was executing a XXXX (state what type of vehicle movement Right Turn/Left Turn/Reverse) and came into contact with (Object/Vehicle that came into contact).\n\nVehicle suffered (details of damage to vehicle). (Object/Vehicle that came into contact) was seen to have sustained (details of damages)\n\nState If any injuries to military or civilian personnel. \n\n*8. IVC Footage:*\nTo be extracted\n\n*9. IVD Data:*\nTo be extracted\n\n*10. Maint Record:*\n1)Last UQM Date:\n2)Next UQM Date:\n3)Last AVI Date:\n4)Next AVI Date:\n\n*11. Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*12. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on civo
@bot.message_handler(commands=['civo'])
def civo(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nCivil Offense - (Type of Incident)\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Location of the Incident:*\n\n*6. Brief Description of the Incident:*\nOn DDMMYY, HHMMhrs, (Serviceman’s Rank and Name) was (In depth details) was caught by Policemen from (Division. Subsequently, he was arrested on DDMMYY, HHMMhrs for involvement in (Offense).\n\nServiceman was released on bail on DDMMYY, HHMMhrs. His bail amount is ($$/ Any other collateral- delete whenever necessary). He will be required to report at (Location), on DDMMYY, HHMM.\n\n*7. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*8. NOK informed:*\nYes\n\n*9. Reportings:*\nGSOC:\nIHQ:\nAIMSIS:\nIncident Case Report No:\n\n*10. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on adhoc
@bot.message_handler(commands=['adhoc'])
def adhoc(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Reportings:*\nGSOC:\nIHQ:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on links
@bot.message_handler(commands=['links'])
def links(message):
  bot.reply_to(message, "*Cat 1 Status:*\nhttps://t.me/ArmyCAT1", parse_mode='Markdown')

#Function for when the user types or clicks on doorp
@bot.message_handler(commands=['doorp'])
def doorp(message):
  bot.send_photo(message.chat.id, open('1.png','rb'))

#Function for when the user types or clicks on cont
@bot.message_handler(commands=['cont'])
def cont(message):
  bot.reply_to(message, "*3 TPT Ops Room*: 67494444\n*3 TPT DOO Phone*: 89408249 \n*SBC Guardroom*: 67964358\n*SBMC*: 67964402\n*IHQ*: 63074506\n*GSOC*: 67684844\n*CTN*: 65444567\n*TTN*: 68642909\n*CLN*: 65597877", parse_mode='Markdown')

#Function for when the user types or clicks on man
@bot.message_handler(commands=['man'])
def man(message):
  bot.send_photo(message.chat.id, open('2.png','rb'))


# Handle '/obd'
@bot.message_handler(commands=['obd'])
def opsbluedagger(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(str(today),str(tomorrow))
    msg = bot.reply_to(message, "What is the date to activate?",reply_markup=markup)
    bot.register_next_step_handler(msg, process_date_step)

def process_date_step(message):
    try:
        chat_id = message.chat.id
        datE = message.text
        datE = Blueops(datE)
        blueops_dict[chat_id] = datE
        msg = bot.reply_to(message, 'What time will it be activating?')
        bot.register_next_step_handler(msg, process_time_step)
    except Exception as e:
        bot.reply_to(message, 'Error')

def process_time_step(message):
    try:
        chat_id = message.chat.id
        timE = message.text
        user = blueops_dict[chat_id]
        user.timE = timE
        msg = bot.reply_to(message, 'Who is the POC?')
        bot.register_next_step_handler(msg, process_name_step)
    except Exception as e:
        bot.reply_to(message, 'Error')

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = blueops_dict[chat_id]
        user.name = name
        msg = bot.reply_to(message, 'What is his contact?')
        bot.register_next_step_handler(msg, process_contact_step)
    except Exception as e:
        bot.reply_to(message, 'Error')

def process_contact_step(message):
    try:
        chat_id = message.chat.id
        contact = message.text
        if not contact.isdigit():
            msg = bot.reply_to(message, 'Enter the proper number without spacing')
            bot.register_next_step_handler(msg, process_contact_step)
            return
        elif len(contact)> 8:
           msg = bot.reply_to(message, 'Contact number is not more than 8!')
           bot.register_next_step_handle(msg, process_contact_step)
           return
        user = blueops_dict[chat_id]
        user.contact = contact
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('180SQN TO W PIER', 'W PIER TO 180SQN')
        msg = bot.reply_to(message, 'Location: (Click 1)', reply_markup=markup)
        bot.register_next_step_handler(msg, process_location_step)
    except Exception as e:
        bot.reply_to(message, 'Error')

def process_location_step(message):
    try:
        chat_id = message.chat.id
        location = message.text
        user = blueops_dict[chat_id]
        if (location == u'180SQN TO W PIER') or (location == u'W PIER TO 180SQN'):
            user.location = location
        else:
            raise Exception("Unknown location")
        msg = bot.reply_to(message, 'What time was TTN informed?')
        bot.register_next_step_handler(msg, process_informe_step)
    except Exception as e:
        bot.reply_to(message, 'Error')

def process_informe_step(message):
    try:
        chat_id = message.chat.id
        informe = message.text
        user = blueops_dict[chat_id]
        user.informe = informe
        bot.send_message(chat_id, 'Ops Blue Dagger will be activated at:\n\n' + user.datE + ',' + user.timE+'\n\nPOC:'+ user.name+'\nHP:'+ str(user.contact)+'\nLocation:' + user.location+'\n\nUpdated TTN @ ' + user.informe)
    except Exception as e:
        bot.reply_to(message, 'Error')


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