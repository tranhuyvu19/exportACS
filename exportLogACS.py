

#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import tables
import inspect
from datetime import datetime, timedelta
import importlib
from multiprocessing import Process,Manager,Pool
import logging

from sqlalchemy import create_engine, func
from sqlalchemy.orm import create_session
from pyExcelerator import *

from tables import *

logger = logging.getLogger('exportACS')
hdlr = logging.FileHandler('/var/log/exportACS.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


manager = Manager()
rslist = manager.list()
threadLimiter = threading.BoundedSemaphore(40)

class MyThread(threading.Thread):
    def __init__(self, target, *args):
        super(MyThread, self).__init__()
        self._target = target
        self._args = args
    def run(self):
        threadLimiter.acquire()
        try:
            self._target(*self._args)
        finally:
            threadLimiter.release()


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

def split_processing_normal(listlogDB,modelname,listmac,num_splits=8):
    split_size = len(listmac) // num_splits
    threads = []
    for i in range(num_splits):
        # determine the indices of the list this thread will handle
        start = i * split_size
        # special case on the last chunk to account for uneven splits
        end = None if i+1 == num_splits else (i+1) * split_size
        # create the thread
        threads.append(
            # threading.Thread(target=listCountLogNormal, args=(listlogDB,modelname,listmac,start,end)))
            Process(target=listCountLogNormal, args=(listlogDB,modelname,listmac,start,end)))
        threads[-1].start() # start the thread we just created

    # wait for all threads to finish
    for t in threads:
        t.join()


def listCountLogNormal(listlogDB,modelname,listmac,start,end):
    start_time = datetime.now()
    global  rslist
    listlog = []
    for row in listmac[start:end]:
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
    logger.info('Model Name : %s\t List MAC to scan : %s\t Total Normal Log: %s\t Duration: %s' % (modelname,len(listmac[start:end]),len(listlogDB),datetime.now() - start_time))
    # return listlog
    rslist += listlog

def split_processing_boot(listlogDB,modelname,listmac,num_splits=8):
    split_size = len(listmac) // num_splits
    threads = []
    for i in range(num_splits):
        # determine the indices of the list this thread will handle
        start = i * split_size
        # special case on the last chunk to account for uneven splits
        end = None if i+1 == num_splits else (i+1) * split_size
        # create the thread
        threads.append(
            # threading.Thread(target=listCountLogBoot, args=(listlogDB,modelname,listmac,start,end)))
            Process(target=listCountLogBoot, args=(listlogDB,modelname,listmac,start,end)))
        threads[-1].start() # start the thread we just created

    # wait for all threads to finish
    for t in threads:
        t.join()

def listCountLogBoot(listlogDB,modelname,listmac,start,end):
    start_time = datetime.now()
    global rslist
    listlog = []
    for row in listmac[start:end]:
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
    logger.info('Model Name : %s\t List MAC to scan : %s\t Total Boot Log: %s\t Duration: %s' % (modelname,len(listmac[start:end]),len(listlogDB),datetime.now() - start_time))
    # return listlog
    rslist += listlog

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





engine = create_engine("mysql+pymysql://ftelacs:P@$$vv0rd:@localhost/ftelacs",pool_recycle=3600)

session = create_session(bind=engine)

modellist = session.query(ModelList.name,ModelList.request_log_table).all()

thread_list = []

pool = Pool(processes=4)

now = datetime.now()
aweek = now - timedelta(days=7)

total_log = 0

class_list = inspect.getmembers(sys.modules[__name__], inspect.isclass)

logger.info('Start Scanning %s ...' % now)

for model in modellist:
    for logTable in class_list:
        if logTable[0].startswith('RequestLog'):
            if model.request_log_table == str_to_class('tables','%s'%logTable[0]).__tablename__ :
                logClass = getattr(tables,'%s'%logTable[0])
                logger.info('Querying Database for %s' % logClass)


                firstscanNormalLog = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT'))\
                                                        .group_by(logClass.mac).having(func.count(logClass.mac) >= 70).all()

                if len(firstscanNormalLog) != 0:
                    rsDBNormalLog = session.query(logClass.mac,logClass.online_time)\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(~logClass.event_code.contains('BOOT')).all()
                    total_log += len(rsDBNormalLog)

                firstscanBootLog = session.query(logClass.mac,logClass.online_time,GroupList.Group_name,func.count(logClass.mac))\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT'))\
                                                        .group_by(logClass.mac).having(func.count(logClass.mac) >= 21).all()

                if len(firstscanBootLog) != 0:
                    rsDBBootLog = session.query(logClass.mac,logClass.online_time)\
                                                        .outerjoin(MacList).outerjoin(GroupList)\
                                                        .filter(func.DATE(logClass.online_time) >= aweek.date()).filter(logClass.event_code.contains('BOOT')).all()
                    total_log += len(rsDBBootLog)

                logger.info('Processing Scanning ... ')

                if len(firstscanNormalLog) != 0:
                    t = Process(target=split_processing_normal,args=(rsDBNormalLog,model.name,firstscanNormalLog))
                    t.start()
                    t.join()

                if len(firstscanBootLog) != 0:
                    t2 = Process(target=split_processing_boot,args=(rsDBBootLog,model.name,firstscanBootLog))
                    t2.start()
                    t2.join()






exportExcel(rslist,'LogCPE_%s.xls' %now.date())

logger.info('Total duration : %s\t Total Log: %s\t Total MAC Matched : %s' %((datetime.now() - now),total_log,len(rslist)))
logger.info('Done')








