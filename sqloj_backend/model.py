from flask_restx import fields

import enum

login_res_model = {
    'success': fields.Boolean(required=True, description="Login status"),
    'data': fields.String(required=True, description="User's role: student or teacher")
}

add_assignment_res_model = {
    'success': fields.Boolean(required=True, description="Whether the assignment is added successfully"),
    'assignment_id': fields.String(required=False, description="New assignment unique id"),
}

add_question_res_model = {
    'success': fields.Boolean(required=True, description="Whether the question is added successfully"),
    'question_id': fields.String(required=False, description="New question unique id"),
}

assignment_adding_detail = {
    'assignment_name': fields.String(required=True, description="Assignment name"),
    'assignment_start_time': fields.String(required=True, description="Assignment start time"),
    'assignment_end_time': fields.String(required=True, description="Assignment deadline")
}

assignment_detail_req_model = {'assignment_id': fields.String(required=True, description="Requested assignment id")}

assignment_detail = {
    'assignment_id': fields.String(required=True, description="Assignment unique id"),
    'assignment_name': fields.String(required=True, description="Assignment name"),
    'assignment_start_time': fields.String(required=True, description="Assignment start time"),
    'assignment_end_time': fields.String(required=True, description="Assignment deadline")
}

question_list = {
    'question_id': fields.String(required=True, description="Question unique id"),
    'question_name': fields.String(required=True, description="Question name for displaying"),
}

question_detail_req_model = {'question_id': fields.String(required=True, description="Requested question id")}

question_status = {
    'question_id': fields.String(required=True, description="Question unique id"),
    'question_name': fields.String(required=True, description="Question name for displaying"),
    'is_finished': fields.Boolean(required=True, description="Question finish status"),
}

question_detail = {
    'question_name': fields.String(required=True, description="Question name"),
    'question_description': fields.String(required=True, description="Question description"),
    'question_output': fields.String(required=True, description="Required question output"),
}

question_detail_all_model = {
    'question_id': fields.String(required=True, description="Question unique id"),
    'question_name': fields.String(required=True, description="Question name"),
    'question_description': fields.String(required=True, description="Question description"),
    'question_output': fields.String(required=True, description="Required question output"),
    'assignment_id': fields.String(required=True, description="Assignment id the question belongs to"),
    'db_id': fields.String(required=True, description="Database id the question uses"),
}

db_list_res_model = {
    "db_id": fields.String(required=True, description="Database id"),
    "db_name": fields.String(required=True, description="Database name"),
    "db_description": fields.String(required=True, description="Database description"),
    "upload_time": fields.String(required=True, description="Database uploaded time")
}

db_detail_full_model = {
    "db_id": fields.String(required=True, description="Database id"),
    "db_name": fields.String(required=True, description="Database name"),
    "db_description": fields.String(required=False, description="Database description"),
    "db_filename": fields.String(required=True, description="Database filename stored"),
    "upload_time": fields.String(required=True, description="Database uploaded time"),
}

db_add_req_model = {
    "db_name": fields.String(required=True, description="Database name"),
    "db_description": fields.String(required=True, description="Database description"),
}

db_modify_req_model = {
    "db_id": fields.String(required=True, description="Database id to modify"),
    "db_name": fields.String(required=True, description="Database name"),
    "db_description": fields.String(required=True, description="Database description"),
}

db_delete_req_model = {
    "db_id": fields.String(required=True, description="Database id to delete"),
}

add_db_res_model = {
    'success': fields.Boolean(required=True, description="Whether the database is modified successfully"),
    'db_id': fields.String(required=False, description="DB unique id"),
}



class RecordStatus(enum.Enum):
    running = "RUNNING"
    AC = "AC"
    TLE = "TLE"
    WA = "WA"


records_list = {
    'record_id': fields.String(required=True),
    'record_time': fields.String(required=True, description="Time when record submitted"),
    'assignment_id': fields.String(required=True),
    'assignment_name': fields.String(required=True),
    'question_id': fields.String(required=True),
    'question_name': fields.String(required=True),
    'record_status': fields.String(required=True, enum=[x.name for x in RecordStatus],
                                   description="Record status: RUNNING, AC, TLE, WA"),
    'running_time': fields.String(required=False, description="Run time for the code, not included if code is running")
}
