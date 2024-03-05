import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API SE OCULTA POR SEGURIDAD 
ckey = "########################"
csecret = "########################"
atoken = "########################-kyuyyls0BxT7I4m0MlQjS3wUhNvbotn"
asecret = "########################"
#####################################


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Cristian:123456@localhost:5984/')  
try:
    db = server.create('pichincha')
except:
    db = server('pichincha')


twitterStream.filter(locations=[-79.3709,-0.7211,-77.8397,0.3273])    
#CRITERIO DE FILTRACIÓN
twitterStream.filter(track=['Rafael Correa','2024','presidente','REVOLUCION'])
