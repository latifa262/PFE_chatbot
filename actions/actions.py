# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import string
import psycopg2
#import re

#def replace(old, new, str, caseinsentive = False):
#        if caseinsentive:
 #           return str.replace(old, new)
  #      else:
   #         return re.sub(re.escape(old), new, str, flags=re.IGNORECASE) 
class actionmafiliere(Action):

    def name(self)-> Text:
        return "action_ma_filiere"

	
    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity']=='filiere':
                name=e['value']

            if name=="smpc":
                message="tu peux changer la filière à svtu.\nLa réclamation du changement de filière s’effectue au niveau de la plateforme au début de l’année universitaire avant le démarrage des TPs."
            if name=="svtu":
                message="tu peux changer la filière à smpc.\nLa réclamation du changement de filière s’effectue au niveau de la plateforme au début de l’année universitaire avant le démarrage des TPs."
            if name=="smia":
                message="tu peux changer la filière à svtu ou smpc.\nLa réclamation du changement de filière s’effectue au niveau de la plateforme au début de l’année universitaire avant le démarrage des TPs."

        dispatcher.utter_message(text = message)

        return []

#image_growth_up = "C:/Users/DELL/Desktop/PFE/unnamed.png"
#dispatcher.utter_template("utter_growth_up", tracker, 
#growth_amt=result,period=my_period,image_growth_up=image_growth_up) 
class actionhoraire(Action):

    def name(self)-> Text:
        return "action_horaire"

	
    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)

        for i in entities:
            if i['entity']=='horaire':
                name=i['value']
            if name=="guichet":
                message="Le service commence 09:00  jusqu'a 13:00 mais dans la period des examens il est ferme."
            if name=="infirmerie":
                message="Un médecin de la sante publique alloue à ce service trois matinée par semaine, Ce service s’occupe des affaires touchant la santé des étudiants."
            if name=="bibliotheque":
                message="L’acces a la salle de lecture est reserve aux seuls etudiants de la faculte.\nchaque jour de  08:00 a 19:00 sauf le dimanche, la biblio est Fermée."
            if name=="service des Masters":
                message="Le service des Masters commence 10:30  jusqu'a 13:30 "
        dispatcher.utter_message(text = message)

        return []	

class actionnbmodule(Action):

    def name(self)-> Text:
        return "action_nb_module"

    
    def run(self, dispatcher: CollectingDispatcher, 
       tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity']=='semestre':
                name=e['value']

            if name=="s1":
                message="cet semestre est constitué de 7 modules."
            if name=="s2":
                message="cet semestre est constitué de 7 modules."
            if name=="s3":
                message="cet semestre est constitué de 6 modules."
            if name=="s4":
                message="cet semestre est constitué de 6 modules."
            if name=="s5":
                message="cet semestre est constitué de 6 modules."
            if name=="s6":
                message="cet semestre est constitué de 6 modules."
            
        dispatcher.utter_message(text = message)

        return []  

#class action_default_fallback(Action):

#    def name(self) -> Text:
 #       return "action_default_fallback"

  #  def run(self, dispatcher: CollectingDispatcher,
   #     tracker: Tracker,
    #    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

     #   dispatcher.utter_message(text="Désolé je n'ai pas compris ce que tu as dit, s'il te plait reformule votre question.")

      #  return []
class uttertable(Action):

    def name(self) -> Text:
        return "action_utter_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        con =  psycopg2.connect(
                host = "localhost",
                database="postgres",
                user = "postgres",
                password = "123")

        
        departement = tracker.get_slot('departement')
        caract = tracker.get_slot('caract')
        departement=departement.lower();
        caract=caract.lower();
            
        cur =  con.cursor()
        cur.execute("SELECT * from chef_dep WHERE departement = %s and caract = %s ;",(departement,caract))
        rows = cur.fetchall()
        if (rows):
            for i in range(len(rows)):
                dispatcher.utter_message(text="voici l'email de {}".format(rows[i][0]))
                dispatcher.utter_message(text="{} : ".format(rows[i][1]))
                dispatcher.utter_message(text=" {}".format(rows[i][4]))
            if( (len(rows)==0)):
                    dispatcher.utter_message(text="j'ai pas compris ce que vous cherchez!!")
            cur.close()

class uttertable2(Action):

    def name(self) -> Text:
        return "action_utter_table2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        con =  psycopg2.connect(
                host = "localhost",
                database="postgres",
                user = "postgres",
                password = "123")

        
        nom = tracker.get_slot('nom')
        prenom = tracker.get_slot('prenom')
        nom=nom.lower();
        prenom=prenom.lower();
    
        cur =  con.cursor()
        cur.execute("SELECT * from chef_dep WHERE nom = %s and prenom = %s ;",(nom,prenom))
        rows = cur.fetchall()
        if (rows):
            for i in range(len(rows)):
                dispatcher.utter_message(text="voici l'email : {}".format(rows[i][4]))
            if( (len(rows)==0)):
                    dispatcher.utter_message(text="j'ai pas compris ce que vous cherchez!!")
            cur.close()     

             
            

                  