from klein import Klein

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.web.server import Site


class ToyServer(object):
    @inlineCallbacks
    def setup(self, app=None):
        if app is None:
            app = Klein()

        self.app = app
        self.server = yield reactor.listenTCP(0, Site(self.app.resource()))
        addr = self.server.getHost()
        self.url = "http://%s:%s" % (addr.host, addr.port)

    def teardown(self):
        self.server.loseConnection()

    @classmethod
    @inlineCallbacks
    def from_test(cls, test, app=None):
        server = cls()
        yield server.setup(app)
        test.addCleanup(server.teardown)
        returnValue(server)


def conjoin(a, b):
    result = {}
    result.update(a)
    result.update(b)
    return result


def omit(collection, *fields):
    return dict((k, v) for k, v in collection.iteritems() if k not in fields)
