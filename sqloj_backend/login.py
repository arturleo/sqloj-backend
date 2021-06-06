from flask_restx import Namespace, Resource, fields

api = Namespace('login', description='User login request')

login_res = api.model('Login', {
    'success': fields.Boolean(required=True, description="Login status"),
    'data': fields.String(required=False, description="User's role: student or teacher")
})

parser = api.parser()
parser.add_argument(
    "username", type=str, required=True, help="User Name"
)
parser.add_argument(
    "password", type=str, required=True, help="Encrypted password"
)


@api.route("/")
class Login(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(login_res)
    def post(self):
        args = parser.parse_args()
        print(args["username"])
        # todo
        return {"success": True, "data": "student"}
