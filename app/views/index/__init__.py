from flask.blueprints import Blueprint
from app.views.index.views import IndexView

index_bp = Blueprint('index', __name__,
                     template_folder='index')

index_bp.add_url_rule('/', view_func=IndexView.as_view('index'))

