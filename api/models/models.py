import uuid

class User:

    def __init__(self, user_id, firstname, lastname, othername, email, phone_number,
                username, registered, is_admin):
        # self.name = name 
        # self.user_id = user_id
        self.user_id = user_id 
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email 
        self.phone_number = phone_number
        self.username = username 
        self.registered = registered
        self.is_admin = is_admin


class Incident:

    def __init__(self, incident_id, created_on, created_by,
                incident_type, location, status, images,
                videos, comment):
       
        self.created_on = created_on
        self.created_by = created_by
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.location = location 
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment
        
