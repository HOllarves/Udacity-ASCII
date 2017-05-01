import os
import webapp2
import jinja2
from models.Art import Art




template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),  autoescape = True)

class Handler(webapp2.RequestHandler):

    '''
    Handler class for performing
    basic operations
    '''

    #Outputs to the browser
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    #Looks for template and add params
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    #Renders the template
    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPage(Handler):

    '''
    Home Page
    '''

    def render_index(self, title = "", art = "", error = "", arts = None):
        self.render("index.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        arts = Art().getArt()
        self.render_index(arts = arts)

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if title and art:
            a = Art(title = title, art = art)
            a.put()
            self.redirect("/")
        else:
            error = "Some fields are missing"
            self.render_index(title, art, error)


app = webapp2.WSGIApplication(
    [
    ('/', MainPage)
    ],
    debug = True)