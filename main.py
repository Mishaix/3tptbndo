import os
import telebot
from datetime import date,timedelta
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

#Testing
rp = "6.jpg"

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
  bot.reply_to(message, "Hello! I'm the virtual Telegram assistant for 3 TPT BN. Which information would you like me to retrieve?\n\nDOO Reporting Procedure: /doorp\nDOO IR Templates: /temp\nContacts: /cont\nHelpful Links: /links\nOps Blue Dagger: /obd")

#Function for when the user types or clicks on help
@bot.message_handler(commands=['temp'])
def temp(message):
  bot.reply_to(message, "*Please click the necessary templates for the relevant cases*: \n HA-ART Ag+/ PCR+ /agc \n HRN /hrn \n Known Contact to Ag+/ C+ /known \n Hospitalization (Non Send Out) /hos \n Ambulance (Send-Out/Hospitalization) /amb \n NCVI /nvci \n Civil Offense /civo \n Other Ad-Hoc cases /adhoc ", parse_mode='Markdown')

#Function for when the user types or clicks on agc
@bot.message_handler(commands=['agc'])
def agc(message):
  bot.reply_to(message, "Incident Reporting \n\n*From Unit, Coy/Node:*\n3 Tpt Bn, (Coy/Node)\n\n*a. Nature of Activity:*\nHA-ART Ag+\n\n*b. Brief Description of the Incident:*\nOn (DDMMYY, HHMMhrs), Serviceman experienced (Symptoms) and did a SA-ART. The result returned Ag+. Serviceman then reported sick at (Location of Clinic) on (HHMMhrs) for HA-ART. The result returned Ag+.\n\nServiceman is given XX days MC from DDMMYY to DDMMYY. Serviceman was last in (Camp) on (DDMMYY, HHMMhrs). \n\n*c. Unit Follow Up Actions:*\nServiceman is on MC till DDMMYY. Unit to track serviceman till he is tested Ag- without symptoms. \n\n???????????????????????????????????????\n*Incident Reporting:*\n\n1.Type of Service:\n2. Rank:\n3. Unit: 3 Tpt Bn\n4. Name:\n5. Status: SA-ART Ag+, HA-ART Ag+\n6. Personnel Camp Location:\n7. Swab Location:\n8. Swab Result Date: DD/MM/YYYY\n9. Swab Result Time: HHMMhrs\n10. Follow up Swab Date: NA\n11. Incident Date: DD/MM/YYYY\n12. Incident Time/Time of info received: HHMMhrs\n13. Quarantine/MC Start: DD/MM/YYYY\n14. Quarantine Location: \n15. SAF Close Contact:\n16. Date of Contact: \n17. Vaccination completed? Yes/No\n18. 2nd Vaccination & Booster Date\nDD/MM/YYYY, DD/MM/YYYY\n19. Last Date in Camp: DD/MM/YYYY, HHMMhrs\n20. Symptoms: \n\nIHQ:\nGSOC:\nCOVID E-Form\n ", parse_mode='Markdown')

#Function for when the user types or clicks on hrn
@bot.message_handler(commands=['hrn'])
def hrw(message):
  bot.reply_to(message, "Incident Reporting \n\n*From Unit, Coy/Node:*\n3 Tpt Bn, (Coy/Node)\n\n*a. Nature of Activity:*\nHousehold/Non-Household KC (DDMMYY), HRN (DDMMYY)\n\n*b. Brief Description of the Incident:*\nServiceman was a known contact to his/her (Known contact) that was tested (SA-ART Ag+/ HA-ART Ag+/ PCR+) on DDMMYY, HHMMhrs. Serviceman did D1 SA-ART on DDMMYY, HHMMhrs and tested (Result).\n\n Serviceman was last in (Camp) on (DDMMYY, HHMMhrs).\n\nFollow up report:\nServiceman was issued a HRN from DDMMYY to DDMMYY.\n\n*c. Unit Follow Up Actions:*\nAwaiting D5 ART on (DDMMYY)\n\n???????????????????????????????????????\n*Incident Reporting:*\n\n1.Type of Service:\n2. Rank:\n3. Unit: 3 Tpt Bn\n4. Name:\n5. Status: Household/Non-Household KC, SA-ART Ag- (DDMMYY), HRN (DDMMYY)\n6. Personnel Camp Location:\n7. Swab Location:\n8. Swab Result Date: DD/MM/YYYY\n9. Swab Result Time: HHMMhrs\n10. Follow up Swab Date: DD/MM/YYYY\n11. Incident Date: DD/MM/YYYY (KC), DD/MM/YYYY (HRN)\n12. Incident Time/Time of info received: HHMMhrs\n13. Quarantine/MC Start: DD/MM/YYYY\n14. Quarantine Location: \n15. SAF Close Contact:\n16. Date of Contact: \n17. Vaccination completed? Yes/No\n18. 2nd Vaccination & Booster Date\nDD/MM/YYYY, DD/MM/YYYY\n19. Last Date in Camp: DD/MM/YYYY, HHMMhrs\n20. Symptoms: \n\nIHQ:\nGSOC:\nCOVID E-Form\n ", parse_mode='Markdown')

#Function for when the user types or clicks on known
@bot.message_handler(commands=['known'])
def known(message):
  bot.reply_to(message, "Incident Reporting \n\n*From Unit, Coy/Node:*\n3 Tpt Bn, (Coy/Node)\n\n*a. Nature of Activity:*\nHousehold/Non-Household KC (DDMMYY)\n\n*b. Brief Description of the Incident:*\nServiceman was a known contact to his/her (Known contact) that was tested (SA-ART Ag+/ HA-ART Ag+/ PCR+) on DDMMYY, HHMMhrs. Serviceman did D1 SA-ART on DDMMYY, HHMMhrs and tested (Result). \n\n Serviceman was last in (Camp) on (DDMMYY, HHMMhrs).\n\n*c. Unit Follow Up Actions:*\nAwaiting D5 ART on (DDMMYY)\n\n???????????????????????????????????????\n*Incident Reporting:*\n\n1.Type of Service:\n2. Rank:\n3. Unit: 3 Tpt Bn\n4. Name:\n5. Status: Household/Non-Household KC, SA-ART Ag-\n6. Personnel Camp Location:\n7. Swab Location:\n8. Swab Result Date: DD/MM/YYYY\n9. Swab Result Time: HHMMhrs\n10. Follow up Swab Date: DD/MM/YYYY\n11. Incident Date: DD/MM/YYYY (KC), DD/MM/YYYY (HRN)\n12. Incident Time/Time of info received: HHMMhrs\n13. Quarantine/MC Start: DD/MM/YYYY\n14. Quarantine Location: \n15. SAF Close Contact:\n16. Date of Contact: \n17. Vaccination completed? Yes/No\n18. 2nd Vaccination & Booster Date\nDD/MM/YYYY, DD/MM/YYYY\n19. Last Date in Camp: DD/MM/YYYY, HHMMhrs\n20. Symptoms: \n\nIHQ:\nGSOC:\nCOVID E-Form\n ", parse_mode='Markdown')

#Function for when the user types or clicks on hos
@bot.message_handler(commands=['hos'])
def hos(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nAmbulance Send-Out\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman went for XX surgery at (Location) hospital. Surgery commenced at HHMMhrs and completed at HHMMhrs. Serviceman is warded at Ward XX, Room/Bed XX.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on amb
@bot.message_handler(commands=['amb'])
def amb(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / (Training/Non-Training related)\n\n*1. Nature of Activity:*\nAmbulance Send-Out due to (Reason)\n\n*2. Rank & Full name of Serviceman involved:*\nRank & Full Name (Capitalized)\n\n*3. PES:*\nXX\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Brief Description of the Incident:*\nServiceman experienced (Symptoms) and reported sick at (Location) Medical Centre at HHMMhrs. \n\nHe was accessed by the MO for (Diagnosis) and was sent to (Location) Hospital at HHMMhrs for further treatment. (Commander) is accompanying him.\n\n*6. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*7. NOK informed:*\nYes\n\n*8. Verbal Reportings:*\nIHQ\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*9. Reported by:*\nRank & Full Name (Capitalized)", parse_mode='Markdown')


#Function for when the user types or clicks on nvci
@bot.message_handler(commands=['nvci'])
def nvci(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\n NCVI/ CVI \n\n*2. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*3. Location of the Incident:*\nCamp/Location:\nArea:\n\n*4. Vehicles Involved:*\n\n*5. Rank & Full name of Serviceman involved:*\nTO/DV\nVC (If necessary)\nFP (If necessary)\n\n*6. PES:*\n\n*7. Brief Description of the Incident:*\nOn DDMMYY at HHMMhrs, (Name of TO or DV) was driving MIDXXXXX (State Vehicle Type) in (Location of Camp Location or Road Location) for (Purpose). He was executing a XXXX (state what type of vehicle movement Right Turn/Left Turn/Reverse) and came into contact with (Object/Vehicle that came into contact).\n\nVehicle suffered (details of damage to vehicle). (Object/Vehicle that came into contact) was seen to have sustained (details of damages)\n\nState If any injuries to military or civilian personnel. \n\n*8. IVC Footage:*\nTo be extracted\n\n*9. IVD Data:*\nTo be extracted\n\n*10. Maint Record:*\n1)Last UQM Date:\n2)Next UQM Date:\n3)Last AVI Date:\n4)Next AVI Date:\n\n*11. Reportings:*\nIHQ:\nGSOC:\nAIMSIS:\nIncident Case Report No:\n\n*12. Reported by:*\n", parse_mode='Markdown')

#Function for when the user types or clicks on civo
@bot.message_handler(commands=['civo'])
def civo(message):
  bot.reply_to(message, "Incident Reporting \n\n*From / Category of Incident / Type of Training*:\n3 Tpt Bn, (Coy/Node) / Non-Training related\n\n*1. Nature of Activity:*\nCivil Offense - (Type of Incident)\n\n*2. Rank & Full name of Serviceman involved:*\n\n*3. PES:*\n\n*4. Date & Time of Incident:*\nDDMMYY, HHMMhrs\n\n*5. Location of the Incident:*\n\n*6. Brief Description of the Incident:*\nOn DDMMYY, HHMMhrs, (Serviceman???s Rank and Name) was (In depth details) was caught by Policemen from (Division. Subsequently, he was arrested on DDMMYY, HHMMhrs for involvement in (Offense).\n\nServiceman was released on bail on DDMMYY, HHMMhrs. His bail amount is ($$/ Any other collateral- delete whenever necessary). He will be required to report at (Location), on DDMMYY, HHMM.\n\n*7. Follow up description:*\nInitial Reporting/ Update caa DDMMYY\n\n*8. NOK informed:*\nYes\n\n*9. Reportings:*\nGSOC:\nIHQ:\nAIMSIS:\nIncident Case Report No:\n\n*10. Reported by:*\n", parse_mode='Markdown')

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
  bot.send_photo(message.chat.id, open('6.jpg','rb'))

#Function for when the user types or clicks on cont
@bot.message_handler(commands=['cont'])
def cont(message):
  bot.reply_to(message, "*3 TPT Ops Room*: 67494444\n*3 TPT DOO Phone*: 89408249 \n*SBC Guardroom*: 67964358\n*SBMC*: 67964402\n*IHQ*: 63074506\n*GSOC*: 67684844\n*CTN*: 65444567\n*TTN*: 68642909\n*CLN*: 65597877", parse_mode='Markdown')

  #deprecated function #IGNORE
#Function for when the user types or clicks on man
#@bot.message_handler(commands=['man'])
#def man(message):
  #bot.send_photo(message.chat.id, open('2.png','rb'))


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