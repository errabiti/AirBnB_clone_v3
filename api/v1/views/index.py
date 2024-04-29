sk with general routes
    routes:
        /status:    Returns "status": "OK" to indicate the system is up and running.
        /stats:     Returns the total counts for all predefined classes in storage.
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    '''
        Return JSON response indicating that the system is running.

    '''

    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def storage_counts():
    '''
        Return counts of all classes in the storage system.
    '''
    
    class_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(class_counts)
    
