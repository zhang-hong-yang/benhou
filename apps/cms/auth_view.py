from apps.cms import cms_bp


@cms_bp.route("/", endpoint="index")
def index():
	return "this is a test message"
