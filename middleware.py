from tyk.decorators import *
from gateway import TykGateway as tyk

@Hook
def RedirectHook(request, session, spec):
  print("RedirectHook is called")
  request.object.return_overrides.response_code = 301
  request.object.return_overrides.headers["Location"] = "http://newurl.com/"
  return request, session
