from google.appengine.ext import db

class Art(db.Model):

    title = db.StringProperty()
    art = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add = True)

    def getArt(self):
        return db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
