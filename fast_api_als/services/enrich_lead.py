import calendar
import time
import json
import logging
from dateutil import parser
from fast_api_als.database.db_helper import db_helper_session

from fast_api_als import constants

log = logging.getLogger(__name__)

"""
what exceptions can be thrown here?
"""


def get_enriched_lead_json(adf_json: dict) -> dict:
    try:
        json.loads(adf_json)
    except ValueError:
        raise ValueError
    if 'adf' not in adf_json:
        #field not found
        log.info("adf field is not found in adf_json object")
        raise KeyError
    
    log.info("Valid adf_json is passed as argument to get_enriched_lead_json")
    pass