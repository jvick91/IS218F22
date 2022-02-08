from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
#<<<<<<< HEAD
        name = "Joe V"
#=======
        #name = "kwilliam"
#>>>>>>> 7570df10deaf35c3a683e5de7121debeb5df4f75
        return render_template('index.html', name=name)
