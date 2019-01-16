from api.models.models import User, Incident

class IncidentList:


    def __init__(self):
        self.incident_list = []
        self.user_list = []

    def fetch_all_incidence(self):
        return self.incident_list

    def add_incident(self,incident):
        new_incident = incident.__dict__
        self.incident_list.append(new_incident)

    def add_user(self, user):
        new_user = user.__dict__
        self.user_list.append(new_user)


    def retreave_incidents(self):
        return [ incidents.__dict__ for incidents in self.incident_list]

    
    def incidet_id_generator(self):
        if len(self.incident_list) == 0:
            return 1
        return len(self.incident_list)+1


    def fetch_specic_incident(self, id):
        specific_incident = [incident for incident in self.incident_list \
        if incident['incident_id']==id]
        try:
            return specific_incident[0]
        except IndexError:
            return
