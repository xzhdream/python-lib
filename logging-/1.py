import logging

FORMAT = '%(asctime)-25s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.setLevel(logging.INFO)
logger.info('Protocol problem: %s', 'connection reset', extra=d)