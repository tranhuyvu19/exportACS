from datetime import datetime, timedelta
import importlib
from itertools import ifilter
from pip.utils import logging

#!/usr/bin/python
from tables import *
import tables
import os, sys, inspect
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, create_engine, select, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper, query, create_session,relationship, load_only





def get_size(group_list):
    count = 0
    for row in group_list:
        count+= 1

    return count

def str_to_class(module_name, class_name):
    try:
        module_ = importlib.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)()
        except AttributeError:
            logging.error('Class does not exist')
    except ImportError:
        logging.error('Module does not exist')
    return class_ or None





engine = create_engine("mysql+pymysql://ftelacs:P@$$vv0rd:@localhost/ftelacs")
# conn = engine.connect()

session = create_session(bind=engine)
# test = select([ModelList.name])
# print conn.execute(test).rowcount

# modellist = session.query(ModelList).options(load_only(ModelList.name,ModelList.request_log_table))
modellist = session.query(ModelList.name,ModelList.request_log_table).all()




# test = session.query(MacList.Group_id,MacList.MAC_address,GroupList.Group_name,RequestLogXCIGG93RGNewCIGG93RGProfileNew.mac,RequestLogXCIGG93RGNewCIGG93RGProfileNew.event_code,RequestLogXCIGG93RGNewCIGG93RGProfileNew.online_time).outerjoin(GroupList).outerjoin(RequestLogXCIGG93RGNewCIGG93RGProfileNew).limit(100)
#test = session.query(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac,RequestLogXTW4PortWifiTPLinkADSLNoWifi.event_code,RequestLogXTW4PortWifiTPLinkADSLNoWifi.online_time,MacList.Group_id,GroupList.Group_name).outerjoin(MacList).outerjoin(GroupList).group_by(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac).having(func.count(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac) == 1)
now = datetime.now()
last_week = now - timedelta(days=6)

# test = session.query(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac,RequestLogXTW4PortWifiTPLinkADSLNoWifi.event_code,RequestLogXTW4PortWifiTPLinkADSLNoWifi.online_time,MacList.Group_id,GroupList.Group_name).outerjoin(MacList).outerjoin(GroupList).filter(RequestLogXTW4PortWifiTPLinkADSLNoWifi.online_time > last_week).filter(RequestLogXTW4PortWifiTPLinkADSLNoWifi.event_code.contains('BOOT')).group_by(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac).having(func.count(RequestLogXTW4PortWifiTPLinkADSLNoWifi.mac) > 2)
logClass = RequestLogXTW4PortWifiTPLinkADSLNoWifi
test = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name,func.count(logClass.event_code).label('count')).outerjoin(MacList).outerjoin(GroupList).filter(func.DATE(logClass.online_time) == last_week.date()).filter(~logClass.event_code.contains('BOOT')).group_by(logClass.mac).having(func.count(logClass.mac) > 9)
# test2 = test.add_column(modellist)
#test2 = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name).outerjoin(MacList).outerjoin(GroupList).filter(logClass.online_time < last_week).filter(~logClass.event_code.contains('BOOT')).group_by(logClass.mac).having(func.count(logClass.mac) > 9)
# session.query().having
# test1 = session.query(GroupList).
# print test
# test.outerjoin
# print dir(test)

print test
a = 0


for row in test:
    print dir(test)
    print row.Group_name, row.mac, row.event_code, row.online_time, row.count
    a+=1
print a



class_list = inspect.getmembers(sys.modules[__name__], inspect.isclass)

# now = datetime.now()
# for model in modellist:
#     for logTable in class_list:
#         if logTable[0].startswith('RequestLog'):
#             if model.request_log_table == str_to_class('tables','%s'%logTable[0]).__tablename__ :
#                 logClass = getattr(tables,'%s'%logTable[0])
#                 for time in range(1,8):
#                     dateAgo = now - timedelta(days=time)
#                     rs = session.query(logClass,GroupList.Group_id,GroupList.Group_name).







