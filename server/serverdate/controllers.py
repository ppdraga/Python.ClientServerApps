from protocol import make_response
from datetime import datetime
from decorators import login_required

@login_required
def server_date_controller(request):
    return make_response(request, 200, datetime.now().timestamp())