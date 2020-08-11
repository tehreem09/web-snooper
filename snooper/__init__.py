# #!/home/htf/Documents/programs/python/
#
# # from pkg_resources import get_distribution
# # from . import numberhandler
# # from .numberhandler import numbhandlerfunc, foo_out
# def __init__():
#     # __version__ = get_distribution("web-snooper").version
#     from pkg_resources import get_distribution, DistributionNotFound
#     import os.path
#
#     try:
#         _dist = get_distribution('snooper')
#         # Normalize case for Windows systems
#         dist_loc = os.path.normcase(_dist.location)
#         here = os.path.normcase(__file__)
#         if not here.startswith(os.path.join(dist_loc, 'snooper')):
#             # not installed, but there is another version that *is*
#             raise DistributionNotFound
#     except DistributionNotFound:
#         __version__ = 'Please install this project with setup.py'
#     else:
#         __version__ = _dist.version
#
#     print("hello")
# __init__()
# # print(__init__().__version__)

# import runpy
# runpy.run_module("snooper", alter_sys=True)

# nameparser-1.0.6

# hooks:
#   BeforeInstall:
#     - location: scripts/install_dependencies.sh
#       timeout: 300
#       runas: root
#   ApplicationStart:
#     - location: scripts/start_server.sh
#     - location: scripts/create_test_db.sh
#       timeout: 300
#       runas: root
#   ApplicationStop:
#     - location: scripts/stop_server.sh
#       timeout: 300
#       runas: root