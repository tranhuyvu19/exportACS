import importlib
from itertools import ifilter
from pip.utils import logging

#!/usr/bin/python
from tables import *
import tables
import os, sys, inspect
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, create_engine, select
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

modellist = session.query(ModelList).options(load_only(ModelList.name,ModelList.request_log_table))


class_list = inspect.getmembers(sys.modules[__name__], inspect.isclass)


for model in modellist:
    for logTable in class_list:
        if logTable[0].startswith('RequestLog'):
            if model.request_log_table == str_to_class('tables','%s'%logTable[0]).__tablename__ :
                rs = session.query(getattr(tables,'%s'%logTable[0])).whereclause()










#for i in testlist:
#    print i.Group_name

