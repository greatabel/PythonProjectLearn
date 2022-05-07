import os
import webapp2

import jinja2
from paste import httpserver
from paste.urlparser import StaticURLParser
from paste.cascade import Cascade
import mimetypes


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

# static_app = StaticURLParser("static/")

class StaticFileHandler(webapp2.RequestHandler):
    def get(self, path):
        abs_path = os.path.abspath(os.path.join(self.app.config.get('webapp2_static.static_file_path', 'static'), path))
        if os.path.isdir(abs_path) or abs_path.find(os.getcwd()) != 0:
            self.response.set_status(403)
            return
        try:
            f = open(abs_path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(abs_path)[0])
            self.response.out.write(f.read())
            f.close()
        except:
            self.response.set_status(404)


class MainPage(webapp2.RequestHandler):
 
  def get(self):
    template_values = {
        'name': 'Serendipo',
        'verb': 'extremely happy'
    }
    if not self.request.get('timer'):
        template = jinja_environment.get_template('index.html')
        # self.response.headers.add_header('Content-Type', mimetypes.guess_type(os.path.abspath)[0])
        # self.response.headers['Content-Type'] = mimetypes.guess_type(os.path.abspath)[0]
        self.response.out.write(template.render(template_values))
    else:
        timer= self.request.get('timer', 0)
        template_values = { 'timer' : timer }
        template = jinja_environment.get_template('timer.html')
        # self.response.headers.add_header('Content-Type', mimetypes.guess_type(os.path.abspath)[0])
        # self.response.headers['Content-Type'] = mimetypes.guess_type(os.path.abspath)[0]
        self.response.out.write(template.render(template_values))      


 
web_app = webapp2.WSGIApplication([ ('/', MainPage),
                                    (r'/static/(.+)', StaticFileHandler) ], debug=True)

# Create a cascade that looks for static files first, then tries the webapp
# app = Cascade([static_app, web_app])

def main():
    
    httpserver.serve(web_app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()