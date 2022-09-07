
## CHATBOT
This is a chatbot which will provide answers to the student’s queries about their needs in the FSSM faculty, it could be a new student or an old one.
an example of question would be "the deadline for new student registrations?".

It based on $\color[rgb]{1,1,1}RASA_NLU$ and  $\color[rgb]{1,1,1} RASA_Core$ .

## To test the chatbot:

```
rasa train 
```

-- in another terminal :
```
rasa run actions
```
-- T run the interface :
```
rasa run -m models --enable-api --cors "*"
```
