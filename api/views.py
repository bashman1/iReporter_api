from flask import Blueprint, jsonify, abort, request, make_response, json
from api.models.incidents import IncidentList
from api.models.models import Incident
from api.models.validators import Validator


appblueprint = Blueprint('api',__name__)
incident = IncidentList()
is_valid = Validator()

@appblueprint.route('/')
def index():
    return "welcome to iReporter"


@appblueprint.route('/incidents')
def fetch_all_incidents():
    return jsonify({"incidents":incident.fetch_all_incidence()})


@appblueprint.route('/incidents', methods=['POST'])
def report_incident():
    if not request.json or not request.get_json()['created_on'] or not \
    request.get_json()['created_by'] or not request.get_json()['incident_type'] \
    or not request.get_json()['location'] or not request.get_json()['status'] or not \
    request.get_json()['images'] or not request.get_json()['videos'] or not \
    request.get_json()['comment']:
        abort (400)

    created_on, created_by, incident_type, location, status, images, videos, comment = request.get_json()['created_on'], \
    request.get_json()['created_by'], request.get_json()['incident_type'], request.get_json()['location'], \
    request.get_json()['status'], request.get_json()['images'], request.get_json()['videos'], request.get_json()['comment']

    # if not is_valid.input_fields(incident_type, location, status, images, videos, comment):
    #     return jsonify({"Error":"Ooops, one of the input fields is not in order"}), 400

    incident_id = incident.incidet_id_generator()
    new_incident = Incident(incident_id, created_on, created_by, incident_type, location, status, images, videos, comment)
    incident.add_incident(new_incident)
    return jsonify({"incident":incident.incident_list[-1]}), 201 


@appblueprint.route('/red-flags/<int:redflag_id>', methods=['GET'])
def fetch_specific_red_flag(redflag_id):
    if not incident.fetch_specic_incident(redflag_id):
        return jsonify({"Error":"The red-flag is not found"})
    return jsonify({"Red-Flag": incident.fetch_specic_incident(redflag_id)})


@appblueprint.route('/red-flags/<int:redflag_id>/location', methods=['PATCH'])
def patch_red_flag_location(redflag_id):
    redflag = incident.fetch_specic_incident(redflag_id)
    if redflag:
        location = request.get_json()['location']
        new_location = location
        redflag['location'] = new_location
        return jsonify({"incident":redflag})
    else:
        return jsonify({
            "status":200,
            "message":"red-flag does not exist"
        })


@appblueprint.route('/red-flag/<int:redflag_id>/comment', methods=['PATCH'])
def patch_red_flag_comment(redflag_id):
    redflag = incident.fetch_specic_incident(redflag_id)
    if redflag:
        comment = request.get_json()['comment']
        new_comment = comment
        redflag['comment'] = new_comment
        return jsonify({"incident":redflag})
    else:
        return jsonify({
            "status":200,
            "message":"red-flag does not exist"
        })


@appblueprint.route('/red-flags/<int:redflag_id>', methods=['DELETE'])
def delete_spacific_redflag(redflag_id):
    redflag = incident.fetch_specic_incident(redflag_id)
    if redflag:
        pass

    else:
        return jsonify({
            "status":200,
            "message":"red-flag does not exist"
        })

