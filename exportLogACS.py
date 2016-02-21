

#!/usr/bin/python
# -*- coding: utf-8 -*-

from tables import *
import tables
import os, sys, inspect
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, create_engine, select, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper, query, create_session,relationship, load_only
from pyExcelerator import *
from datetime import datetime, timedelta
import importlib
from itertools import ifilter
from pip.utils import logging
import multiprocessing as mp

class resultLog:
    pass



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

def countLog(listCount,mac,time):
    count = 0
    if time != None:
        for i in range(0,len(listCount)):
            if listCount[i].online_time.date() == time.date():
                if listCount[i].mac == mac:
                    count+=1
    else:
        for i in range(0,len(listCount)):
            if listCount[i].mac == mac:
                count+=1
    return count

def cleanList(listCount,mac,time):
    for row in listCount:
        if row.online_time.date() == time.date():
            if row.mac == mac:
                listCount.remove(row)
    return listCount

def checkmac(listlog,mac,time):
    for row in listlog:
        # if row['mac'] == mac and row['online_time'].date() == time.date():
        # if row['Mac ACS'] == mac:
        # print row
        # if row['MacACS'] == None:
        #     continue
        if row['Mac ACS'] == mac:
            return True
    return False

def listCountLogNormal(listlogDB,modelname,listmac):
    listlog = []
    for row in listmac:
        tmp = 0
        count = 0
        for i in range(1,8):
            dateAgo = now - timedelta(days=i)
            countlog = countLog(listlogDB,row.mac,dateAgo)
            if countlog > 9:
                tmp += countlog
                count += 1
            else:
                break
        if count < 6:
            continue
        else:
            avg = tmp / count
            if checkmac(listlog,row.mac,dateAgo) == False:
                listlog.append({
                    'Model': modelname,
                    'Group': row.Group_name,
                    'Mac ACS': row.mac,
                    'Type': 'Normal Log',
                    'AVG/Day': avg,
                })
    return listlog

def listCountLogBoot(listlogDB,modelname,listmac):
    listlog = []
    for row in listmac:
        tmp = 0
        count = 0
        for i in range(1,8):
            dateAgo = now - timedelta(days=i)
            countlog = countLog(listlogDB,row.mac,dateAgo)
            if countlog > 2:
                tmp += countlog
                count += 1
            else:
                break
        if count < 6:
            continue
        else:
            avg = tmp / count
            if checkmac(listlog,row.mac,dateAgo) == False:
                listlog.append({
                    'Model': modelname,
                    'Group': row.Group_name,
                    'Mac ACS': row.mac,
                    'Type': 'Boot Log',
                    'AVG/Day': avg,
                })
    return listlog

def exportExcel(rslist,file):
    wb = Workbook()
    ws0 = wb.add_sheet('0')

    borders = Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1

    borders_cell = Borders()
    borders_cell.right = 1

    TestNoPat = Pattern()
    TestNoPat.pattern = Pattern.SOLID_PATTERN
    TestNoPat.pattern_fore_colour = 0x07

    Alg = Alignment()
    Alg.horz = Alignment.HORZ_CENTER
    Alg.vert = Alignment.VERT_CENTER

    row_number=1
    for row in rslist:
            i=0
            for item in row:
                    val=str(row[item])
                    if row_number==1:
                            style = XFStyle()
                            style.borders = borders
                            style.pattern = TestNoPat
                            style.alignment = Alg
                            ws0.write(0,i,'', style)
                            ws0.write(0,i,item, style)
                            style = XFStyle()
                            style.borders = borders_cell
                            ws0.write(row_number,i,val, style)
                            i= i+1
                    else:
                            style = XFStyle()
                            style.borders = borders_cell
                            ws0.write(row_number,i,val, style)
                            i=i+1
            row_number=row_number+1
    wb.save('%s' %file)





engine = create_engine("mysql+pymysql://ftelacs:P@$$vv0rd:@localhost/ftelacs")

session = create_session(bind=engine)

modellist = session.query(ModelList.name,ModelList.request_log_table).all()


now = datetime.now()
aweek = now - timedelta(days=7)

# test2 = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name)\
#     .outerjoin(MacList).outerjoin(GroupList)\
#     .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT')).all()
#
# test3 = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
#                                         .outerjoin(MacList).outerjoin(GroupList)\
#                                         .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT'))\
#                                         .group_by(logClass.mac).having(func.count(logClass.mac) >= 70).all()
#
# test0 = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name)\
#     .outerjoin(MacList).outerjoin(GroupList)\
#     .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT')).all()
#
# test1 = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
#                                         .outerjoin(MacList).outerjoin(GroupList)\
#                                         .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT'))\
#                                         .group_by(logClass.mac).having(func.count(logClass.mac) >= 21).all()
#
#
#
# dayoflogNormal = listCountLogNormal(test2,'CPE',test3)
# dayoflogBoot = listCountLogBoot(test0,'CPE',test1)


rslist = list()




class_list = inspect.getmembers(sys.modules[__name__], inspect.isclass)

for model in modellist:
    for logTable in class_list:
        if logTable[0].startswith('RequestLog'):
            if model.request_log_table == str_to_class('tables','%s'%logTable[0]).__tablename__ :
                logClass = getattr(tables,'%s'%logTable[0])

                rsDBNormalLog = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name)\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT')).all()

                firstscanNormalLog = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT'))\
                                                        .group_by(logClass.mac).having(func.count(logClass.mac) >= 70).all()

                rsDBBootLog = session.query(logClass.mac,logClass.event_code,logClass.online_time,MacList.Group_id,GroupList.Group_name)\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT')).all()

                firstscanBootLog = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT'))\
                                                        .group_by(logClass.mac).having(func.count(logClass.mac) >= 21).all()

                rsNormalLog = listCountLogNormal(rsDBNormalLog,model.name,firstscanNormalLog)
                rsBootLog = listCountLogBoot(rsDBBootLog,model.name,firstscanBootLog)
                rslist += rsNormalLog
                rslist += rsBootLog

exportExcel(rslist,'LogCPE_%s.xls' %now.date())








