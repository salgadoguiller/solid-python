import logging
from webargs.flaskparser import parser, abort


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    """Handler toreturn a JSON error response to the client"""
    logging.debug(f'Error: {error}')
    logging.debug(f'Req: {req}')
    logging.debug(f'Schema: {schema}')
    logging.debug(f'Error status Code: {error_status_code}')
    logging.debug(f'Error headers: {error_headers}')

    abort(422, errors=error.messages)
