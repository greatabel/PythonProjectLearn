from flask import Flask
from i0get_local_ssid import OperationSystemFactory


app = Flask(__name__)
app.debug = True


localservices = {
    "greatabel_old_main": """
Address: Room 1307, Block 1cm, Building 2, Shenzhen, China
Phone: +86 755 8693 4283
Province: Guangdong Province
"""
,
    "greatabel": """
Address: Room 999, China
Phone: +86 755 8693 4283
Province: Guangdong Province
"""
}
amenities = {
    "greatabel_old_main": """
Banks and post offices
Cheap and easy access to utilities such as electricity, water, natural gas and internet
Clean air
"""
,
    "greatabel": """
Banks and post house
Cheap and easy access to utilities such as electricity, water, 
natural gas and internet
Clean air
"""
}


@app.route("/")
def hello_world():
    ff = OperationSystemFactory()
    os = "Mac"
    ssid = ff.get_ssid(os)
    print("ssid=", ssid)
    result = "<b style='color:blue !important;'>" + ssid + "</b>"

    result += " say Hello, World!"
    result += "<br/><b>localservices:</b>" + localservices[ssid]+"<br/><b>amenities:</b>" + amenities[ssid]
    return "<html><body>" + result + "</body></html>"


"""
how to run:

export FLASK_APP=i1flask_api.py
export FLASK_ENV=development
python3 -m flask run

"""
