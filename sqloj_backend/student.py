from flask_restx import Namespace, Resource, fields

api = Namespace('student', description="Students' manipulations")

assignment_detail = api.model('Assignment detail', {
    'assignment_id': fields.String(required=True, description="Assignment unique id"),
    'assignment_name': fields.String(required=True, description="Assignment name"),
    'assignment_start_time	': fields.String(required=True, description="Assignment start time"),
    'assignment_end_time': fields.String(required=True, description="Assignment deadline")
})

question_status = api.model('Question status', {
    'question_id': fields.String(required=True, description="Question unique id"),
    'question_name': fields.String(required=True, description="Question name for displaying"),
    'is_finished	': fields.Boolean(required=True, description="Question finish status"),
})

question_detail = api.model('Question detail', {
    'question_name': fields.String(required=True, description="Question name"),
    'question_description': fields.String(required=True, description="Question description"),
    'question_output	': fields.String(required=True, description="Required question output"),
})

submit_status = api.model('Answer submit status', {
    'success': fields.Boolean(required=True, description="whether the code uploads successfully"),
})


@api.route("/queryAssignmentList")
@api.doc(description="Get assignment list and their time span")
class AssignmentListQuery(Resource):
    @api.marshal_with(assignment_detail, as_list=True)
    def get(self):
        return [
            {
                "assignment_id": "a-066ab87a062b",
                "assignment_name": "第一次作业",
                "assignment_start_time": "June 13, 2021 11:13:00",
                "assignment_end_time": "June 20, 2021 23:59:59"
            },
            {
                "assignment_id": "a-204urhiugr9r",
                "assignment_name": "第二次作业",
                "assignment_start_time": "June 20, 2021 12:47:00",
                "assignment_end_time": "June 27, 2021 23:59:59"
            },
        ]


assignId_parser = api.parser()
assignId_parser.add_argument(
    "assignment_id", type=str, required=True, help="Requested assignment id"
)


@api.route("/selectQuestionsByAssignment")
@api.doc(description="Get question list of the requested assignment")
class QuestionListQuery(Resource):
    @api.doc(parser=assignId_parser)
    @api.marshal_with(question_status, as_list=True)
    def get(self):
        args = assignId_parser.parse_args()
        print(args["assignment_id"])
        # todo
        return [
            {
                "question_id": "q-21ru2933hui4",
                "question_name": "7-1 select查询",
                "is_finished": True,
            },
            {
                "question_id": "q-r9imvrvnq40s",
                "question_name": "7-3 delete删除",
                "is_finished": False
            },

        ]


quesId_parser = api.parser()
quesId_parser.add_argument(
    "question_id", type=str, required=True, help="Requested question id"
)


@api.route("/selectQuestionsById")
@api.doc(description="Get question detail of the requested question id")
class QuestionListQuery(Resource):
    @api.doc(parser=quesId_parser)
    @api.marshal_with(question_detail, as_list=True)
    def get(self):
        args = quesId_parser.parse_args()
        print(args["question_id"])
        # todo
        return [
            {
                "question_name": "1",
                "question_description": "2",
                "question_output": "3",
            },
            {
                "question_name": "4",
                "question_description": "5",
                "question_output": "6",
            },

        ]


answer_parser = api.parser()
answer_parser.add_argument(
    "question_id", type=str, required=True, help="Answered question id",
)
answer_parser.add_argument(
    "code", type=str, required=True, help="Sql code to execute",
)


@api.route("/submit")
@api.doc(description="Upload submitted code of the question to the judger")
class QuestionListQuery(Resource):
    @api.doc(parser=answer_parser)
    @api.marshal_with(submit_status, as_list=True)
    def post(self):
        args = answer_parser.parse_args()
        print(args["question_id"])
        # todo
        return {"success": True}
