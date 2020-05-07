from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from author_service.app import app as author_service
from book_service.app import app as book_service
from customer_service.app import app as customer_service
from order_service.app import app as order_service

application = DispatcherMiddleware(
    author_service, {
    '/book': book_service,
    '/customer': customer_service,
    '/order': order_service,
})

try:
  run_simple(
    application=application,
    hostname='0.0.0.0',
    port=8080,
    use_reloader=True,
    use_debugger=True
  )
except KeyboardInterrupt:
  raise
