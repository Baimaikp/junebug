from confmodel import Config
from confmodel.fields import ConfigText, ConfigInt, ConfigDict


class JunebugConfig(Config):
    interface = ConfigText(
        "Interface to expose the API on",
        default='localhost')

    port = ConfigInt(
        "Port to expose the API on",
        default=8080)

    logfile = ConfigText(
        "File to log to or `None` for no logging",
        default=None)

    redis = ConfigDict(
        "Config to use for redis connection",
        default={
            'host': 'localhost',
            'port': 6379,
            'db': 0,
            'password': None
        })

    amqp = ConfigDict(
        "Config to use for amqp connection",
        default={
            'hostname': '127.0.0.1',
            'vhost': '/',
            'port': 5672,
            'db': 0,
            'username': 'guest',
            'password': 'guest'
        })

    inbound_message_ttl = ConfigInt(
        "Maximum time allowed to reply to messages",
        default=60)

    inbound_message_prefix = ConfigText(
        "Prefix to use for redis keys for storing inbound messages.",
        default='inbound_messages')
