'''
Created on Oct 20, 2016
@author: Rohan Achar
'''
from rtypes.pcc.attributes import dimension, primarykey, predicate
from rtypes.pcc.types.subset import subset
from rtypes.pcc.types.set import pcc_set
from rtypes.pcc.types.projection import projection
from rtypes.pcc.types.impure import impure
from datamodel.search.server_datamodel import Link, ServerCopy

@pcc_set
class Luoj9Joseo1Link(Link):
    USERAGENTSTRING = "Luoj9Joseo1"

    @dimension(str)
    def user_agent_string(self):
        return self.USERAGENTSTRING

    @user_agent_string.setter
    def user_agent_string(self, v):
        # TODO (rachar): Make it such that some dimensions do not need setters.
        pass


@subset(Luoj9Joseo1Link)
class Luoj9Joseo1UnprocessedLink(object):
    @predicate(Luoj9Joseo1Link.download_complete, Luoj9Joseo1Link.error_reason)
    def __predicate__(download_complete, error_reason):
        return not (download_complete or error_reason)


@impure
@subset(Luoj9Joseo1UnprocessedLink)
class OneLuoj9Joseo1UnProcessedLink(Luoj9Joseo1Link):
    __limit__ = 1

    @predicate(Luoj9Joseo1Link.download_complete, Luoj9Joseo1Link.error_reason)
    def __predicate__(download_complete, error_reason):
        return not (download_complete or error_reason)

@projection(Luoj9Joseo1Link, Luoj9Joseo1Link.url, Luoj9Joseo1Link.download_complete)
class Luoj9Joseo1ProjectionLink(object):
    pass
