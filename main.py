from flask import Flask, render_template, request, jsonify
from google.appengine.ext import ndb
import logging
import json
import uuid     


log = logging.getLogger(__name__)
app = Flask(__name__)
app.config['DEBUG'] = True

class Booking(ndb.Model):
    id = uuid
    # username = ndb.StringProperty()
    # password = ndb.StringProperty()
    moviename = ndb.StringProperty()
    tickets = ndb.IntegerProperty()
    seat = ndb.StringProperty()

class Show(ndb.Model):
    movie = ndb.StringProperty()
    screen = ndb.StringProperty()
    agerating = ndb.StringProperty()
    language = ndb.StringProperty()

@app.route("/home", methods = ["GET", "POST"])
def showhome():
    return render_template("home.html")

@app.route("/v1/bookings", methods = ["POST","GET"])
def bookticket():
    moviename = request.form.get("movieName")
    tickets = request.form.get("tickets")
    booking = Booking()
    booking.tickets = tickets
    booking.moviename = moviename
    return jsonify({"tickets":booking.tickets, "moviename":
    booking.moviename})

# @app.route("/Tickets/<id>", methods = ["GET"])
# def showtickets(id):
#     showticket = Moviee.query.get(id)
#     return user_schema.jsonify(showticket)

# @app.route("/Tickets/<id>", methods = ["PUT"])
# def updatetickets(id):
#     bookedticket = Moviee.query.get(id)
#     tickets = request.json["tickets"]
#     bookedticket.tickets = tickets
#     ndb.session.commit()
#     return user_schema.jsonify(bookedticket)

# @app.route("/Tickets/<id>", methods = ["DELETE"])
# def cancel_booking(id):
#     user = Moviee.query.get(id)
#     ndb.session.delete(user)
#     ndb.session.commit()
#     return jsonify({"sucess":True})


