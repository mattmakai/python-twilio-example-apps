from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

# A list of recording objects with the properties described above
for recording in client.recordings.list():
    #print(recording.sid)
    id = recording.sid
    uri = recording.uri
    print("id  uri =", id, uri)
    #client.recordings(id).delete()


