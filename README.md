
## CHATBOT
This is a chatbot which will provide answers to the student’s queries about their needs in the FSSM faculty, it could be a new student or an old one.
an example of question would be "the deadline for new student registrations?".
It based on RASA NLU and RASA Core.

## to test the chatbot:

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
