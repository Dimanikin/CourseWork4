from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from parsers import page_parser


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        filters = page_parser.parse_args()
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        b = movie_service.get_one(mid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200
