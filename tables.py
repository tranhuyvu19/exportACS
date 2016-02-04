# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AuthAssignment(Base):
    __tablename__ = 'AuthAssignment'

    itemname = Column(String(64), primary_key=True, nullable=False)
    userid = Column(String(64), primary_key=True, nullable=False)
    bizrule = Column(Text)
    data = Column(Text)


class AuthItem(Base):
    __tablename__ = 'AuthItem'

    name = Column(String(64), primary_key=True)
    type = Column(Integer, nullable=False)
    description = Column(Text)
    bizrule = Column(Text)
    data = Column(Text)


class AuthItemChild(Base):
    __tablename__ = 'AuthItemChild'

    parent = Column(String(64), primary_key=True, nullable=False)
    child = Column(String(64), primary_key=True, nullable=False, index=True)


class Right(Base):
    __tablename__ = 'Rights'

    itemname = Column(String(64), primary_key=True)
    type = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)


class ActionLog(Base):
    __tablename__ = 'action_log'

    ID = Column(Integer, primary_key=True)
    account = Column(String(64), nullable=False)
    type = Column(String(30), nullable=False)
    action = Column(String(64), nullable=False)
    description = Column(String(64))
    product_id = Column(Integer)
    Group_id = Column(Integer)
    time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    other = Column(String(100))


class CfgList(Base):
    __tablename__ = 'cfgList'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    values_array = Column(Text, nullable=False)


class Customer(Base):
    __tablename__ = 'customer'

    Mac_id = Column(Integer, primary_key=True)
    MAC_address = Column(String(64))
    Customer_ID = Column(String(255))
    Customer_Name = Column(String(255))
    Customer_Phone = Column(String(255))
    Customer_Email = Column(String(255))
    product_id = Column(Integer)


class Debug(Base):
    __tablename__ = 'debug'

    id = Column(Integer, primary_key=True)
    mac = Column(String(60, u'utf8_bin'))
    debug_time = Column(DateTime)
    debug_value = Column(String(collation=u'utf8_bin'))
    debug_type = Column(String(45, u'utf8_bin'))


class Debuglog(Base):
    __tablename__ = 'debuglog'

    id = Column(Integer, primary_key=True)
    mac = Column(String(64), nullable=False, index=True)
    log_from = Column(String(255), nullable=False, server_default=text("''"))
    info_header = Column(Text, nullable=False)
    info_body = Column(Text, nullable=False)
    info = Column(Text, nullable=False)
    bug_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ErrorLog(Base):
    __tablename__ = 'error_log'

    id = Column(Integer, primary_key=True)
    mac = Column(String(64), nullable=False, index=True, server_default=text("''"))
    faultcode = Column(String(30), nullable=False, server_default=text("''"))
    faultstring = Column(String(30), nullable=False, server_default=text("''"))
    faultcode_detail = Column(String(30), nullable=False, server_default=text("''"))
    faultstring_detail = Column(Text)
    SoftwareVersion = Column(String(30), nullable=False, server_default=text("''"))
    rpc_method = Column(String(30), nullable=False, server_default=text("''"))
    set_value = Column(Text, nullable=False)
    error_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class EventLog(Base):
    __tablename__ = 'eventLog'

    id = Column(Integer, primary_key=True)
    level = Column(String(128))
    logtime = Column(String(128))
    cpe_serial = Column(String(255))
    ip = Column(String(255))
    faultstring = Column(String(255))


class FirmwareLoadbalance(Base):
    __tablename__ = 'firmware_loadbalance'

    url = Column(String(255), primary_key=True, nullable=False, unique=True, server_default=text("''"))
    firmware = Column(String(255), primary_key=True, nullable=False, server_default=text("''"))
    Label = Column(String(100), nullable=False, server_default=text("''"))
    id = Column(Integer, nullable=False, server_default=text("'0'"))
    SoftwareVersion = Column(String(100), nullable=False, server_default=text("''"))


class FirmwareName(Base):
    __tablename__ = 'firmware_name'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    firmware = Column(String(127), nullable=False, unique=True, server_default=text("''"))
    SoftwareVersion = Column(String(100), nullable=False, server_default=text("''"))


class GroupList(Base):
    __tablename__ = 'group_list'

    Group_id = Column(Integer, primary_key=True)
    Group_name = Column(String(127), nullable=False, server_default=text("''"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    group_lock_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class GroupXCIGG93RGNewCIGG93RGProfileNew(GroupList):
    __tablename__ = 'group_X_CIG-G-93RG-New_CIG-G-93RG-Profile-New'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTW4PortWifiTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-4Port-Wifi_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTD8840TV3TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-8840T-V3_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/cpe/'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXArcherC2CIGG93RGProfileNew(GroupList):
    __tablename__ = 'group_X_Archer C2_CIG-G-93RG-Profile-New'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8901GV6TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8901G-V6_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTWVoice2TWVoiceNew(GroupList):
    __tablename__ = 'group_X_TW_Voice2_TW_Voice_new'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))


class GroupXCT5624STPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_CT5624S_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTempModel1TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_Temp_Model1_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXCIGG97D2CIGG93RGProfileNew(GroupList):
    __tablename__ = 'group_X_CIG-G-97D2_CIG-G-93RG-Profile-New'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXEmilyVDSL4PortTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_EmilyVDSL4Port_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTWONTNoWifiTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW_ONT_noWifi_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXHG531V12CIGG93RGProfileNew(GroupList):
    __tablename__ = 'group_X_HG531 V1 2_CIG-G-93RG-Profile-New'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTD8840TV4TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-8840T-V4_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTXVG15306383NoWLAN(GroupList):
    __tablename__ = 'group_X_TX-VG1530_6383_noWLAN'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    NTPServer2 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))


class GroupXZyxelFSG1100HNTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_Zyxel-FSG1100HN_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTD8817V6TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-8817-V6_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTLWR841NCIGG93RGProfileNew(GroupList):
    __tablename__ = 'group_X_TL-WR841N_CIG-G-93RG-Profile-New'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXHuaweiHG610HuaweiHG610(GroupList):
    __tablename__ = 'group_X_Huawei-HG-610_Huawei-HG-610'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))


class GroupXTWEP9108WTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-EP9108W_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8901NV1TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8901N-V1_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8101GV3TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8101G-V3_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTWEP9108TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-EP9108_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTWVoice3TWVoiceNew2(GroupList):
    __tablename__ = 'group_X_TW_Voice3_TW_Voice_new2'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))


class GroupXTLWR741NDTestTLWR741NDTest(GroupList):
    __tablename__ = 'group_X_TL-WR741ND-Test_TL-WR741ND-Test'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))


class GroupXTWVoiceTWVoice(GroupList):
    __tablename__ = 'group_X_TW_voice_TW_Voice'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))


class GroupXTPLinkWR741NDTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-WR741ND_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXCT5367TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_CT5367_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXZyxelP870HWTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_Zyxel-P870HW_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8151NV3TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8151N-V3_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXZyxelP660HNT1ASimple(GroupList):
    __tablename__ = 'group_X_Zyxel-P660HN-T1A_Simple'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/cpe/'"))


class GroupXTWFP804WTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-FP804W_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8961NDV3TPLinkADSLWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8961ND-V3_TPLink_ADSL_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTD8840TV2TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-8840T-V2_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8951NDV5TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8951ND-V5_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXCIGG93RGIPCIGProfile(GroupList):
    __tablename__ = 'group_X_CIG-G-93RG-IP_CIG-Profile'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8968V1TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8968-V1_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXCTAR5378Simple(GroupList):
    __tablename__ = 'group_X_CT-AR5378_Simple'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/cpe/'"))


class GroupXTWFP801WTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-FP801W_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTLWR740NTPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TL-WR740N_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTPLinkTDW8901GV3TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8901G-V3_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXZyxelP660HT1V3STPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_Zyxel-P660H-T1-V3S_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXTWVoice1TWVoice(GroupList):
    __tablename__ = 'group_X_TW_Voice1_TW_Voice'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))


class GroupXDefaultUniversal(GroupList):
    __tablename__ = 'group_X_Default_Universal'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False)
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False)
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False)
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False)
    Connection_time = Column(String(255), nullable=False)
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))


class GroupXDefaultSimple(GroupList):
    __tablename__ = 'group_X_Default_Simple'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/cpe/'"))


class GroupXTPLinkTDW8101GV2TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TPLink-TD-W8101G-V2_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXZyxelP870HWTestZyxelP870HW(GroupList):
    __tablename__ = 'group_X_Zyxel-P870HW-Test_Zyxel-P870HW'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))


class GroupXTWFP504TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_TW-FP504_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class GroupXDraytek2910TPLinkADSLNoWifi(GroupList):
    __tablename__ = 'group_X_Draytek-2910_TPLink_ADSL_No_Wifi'

    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), primary_key=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    Group_name = Column(String(255), nullable=False, server_default=text("''"))
    firmware_id = Column(Integer, nullable=False, server_default=text("'0'"))
    groupcfg_value = Column(Text, nullable=False)
    cfg_md5 = Column(String(32), nullable=False, server_default=text("''"))
    IPPingDiagnostics_DiagnosticsState = Column(String(255), nullable=False, server_default=text("'None'"))
    IPPingDiagnostics_Host = Column(String(255), nullable=False, server_default=text("''"))
    IPPingDiagnostics_Timeout = Column(String(255), nullable=False, server_default=text("'17000'"))
    IPPingDiagnostics_DataBlockSize = Column(String(255), nullable=False, server_default=text("'42'"))
    IPPingDiagnostics_DSCP = Column(Integer, nullable=False, server_default=text("'0'"))
    Provision_period = Column(String(255), nullable=False, server_default=text("'10800'"))
    Application_file_name = Column(String(255), nullable=False, server_default=text("''"))
    Connection_time = Column(String(255), nullable=False, server_default=text("''"))
    Provision_code1 = Column(String(32), nullable=False, server_default=text("'123456789012345678901234567890AB'"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("'http://acs2.fpt.net/acs/cwmp'"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'0'"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("'0000-00-00T00:00:00'"))


class MacList(Base):
    __tablename__ = 'mac_list'

    Mac_id = Column(Integer, primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(ForeignKey(u'group_list.Group_id', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    hardware_version = Column(String(255), nullable=False, server_default=text("''"))
    sofeware_version = Column(String(255), nullable=False, server_default=text("''"))
    dsp_code = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    debug_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    lock_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip2long = Column(BigInteger, nullable=False, index=True)
    note = Column(Text)

    Group = relationship(u'GroupList')


class MacXTPLinkTDW8968V1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8968-V1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTWFP801WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-FP801W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8968V1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8968-V1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXCIGG97D2CIGG93RGProfileNew(MacList):
    __tablename__ = 'status_X_CIG-G-97D2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXHG531V12CIGG93RGProfileNew(MacList):
    __tablename__ = 'mac_X_HG531 V1 2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTempModel1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_Temp_Model1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8951NDV5TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8951ND-V5_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTWONTNoWifiTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW_ONT_noWifi_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTLWR741NDTestTLWR741NDTest(MacList):
    __tablename__ = 'mac_X_TL-WR741ND-Test_TL-WR741ND-Test'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXArcherC2CIGG93RGProfileNew(MacList):
    __tablename__ = 'status_X_Archer C2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkTDW8961NDV3TPLinkADSLWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8961ND-V3_TPLink_ADSL_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkWR741NDTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-WR741ND_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWVoiceTWVoice(MacList):
    __tablename__ = 'status_X_TW_voice_TW_Voice'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SIP1OutboundProxy = Column(String(255), nullable=False, server_default=text("'sbc01.fpt.net'"))
    SIP1OutboundProxyPort = Column(String(5), nullable=False, server_default=text("'5060'"))
    SIP1Enabled = Column(String(10), nullable=False, server_default=text("'Disabled'"))
    SIP1Number = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthUserName = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthPassword = Column(String(255), nullable=False, server_default=text("'S1changeme'"))


class StatusXTLWR740NTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TL-WR740N_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkTD8840TV4TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-8840T-V4_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXHuaweiHG610HuaweiHG610(MacList):
    __tablename__ = 'mac_X_Huawei-HG-610_Huawei-HG-610'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTWEP9108TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-EP9108_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXDefaultSimple(MacList):
    __tablename__ = 'mac_X_Default_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXEmilyVDSL4PortTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_EmilyVDSL4Port_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTW4PortWifiTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-4Port-Wifi_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXCIGG93RGIPCIGProfile(MacList):
    __tablename__ = 'status_X_CIG-G-93RG-IP_CIG-Profile'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ManufacturerOUI = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ProvisioningCode = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_DeviceLog = Column(Text, nullable=False)
    InterfaceConfig_EnabledForInternet = Column(String(255), nullable=False, server_default=text("''"))
    InterfaceConfig_WANAccessType = Column(String(255), nullable=False, server_default=text("''"))
    InterfaceConfig_Layer1UpstreamMaxBitRate = Column(String(255), nullable=False, server_default=text("''"))
    InterfaceConfig_Layer1DownstreamMaxBitRate = Column(String(255), nullable=False, server_default=text("''"))
    InterfaceConfig_PhysicalLinkStatus = Column(String(255), nullable=False, server_default=text("''"))
    DeviceSummary = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_SpecVersion = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    ModemFirmwareVersion = Column(String(255), nullable=False, server_default=text("''"))


class MacXTWFP804WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-FP804W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTD8840TV2TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-8840T-V2_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8901GV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8901G-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTPLinkTDW8151NV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8151N-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkTDW8901GV6TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8901G-V6_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXCIGG97D2CIGG93RGProfileNew(MacList):
    __tablename__ = 'mac_X_CIG-G-97D2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXZyxelP870HWTestZyxelP870HW(MacList):
    __tablename__ = 'mac_X_Zyxel-P870HW-Test_Zyxel-P870HW'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTWEP9108WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-EP9108W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTD8817V6TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-8817-V6_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTPLinkTDW8901NV1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8901N-V1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXDefaultSimple(MacList):
    __tablename__ = 'status_X_Default_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))


class MacXTW4PortWifiTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-4Port-Wifi_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTWVoiceTWVoice(MacList):
    __tablename__ = 'mac_X_TW_voice_TW_Voice'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTLWR740NTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TL-WR740N_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTD8840TV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-8840T-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXHuaweiHG610HuaweiHG610(MacList):
    __tablename__ = 'status_X_Huawei-HG-610_Huawei-HG-610'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXCIGG93RGNewCIGG93RGProfileNew(MacList):
    __tablename__ = 'mac_X_CIG-G-93RG-New_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTempModel1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_Temp_Model1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXZyxelFSG1100HNTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_Zyxel-FSG1100HN_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTWEP9108WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-EP9108W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXEmilyVDSL4PortTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_EmilyVDSL4Port_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXZyxelP870HWTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_Zyxel-P870HW_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTWFP504TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-FP504_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTD8840TV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-8840T-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXZyxelP870HWTestZyxelP870HW(MacList):
    __tablename__ = 'status_X_Zyxel-P870HW-Test_Zyxel-P870HW'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTLWR841NCIGG93RGProfileNew(MacList):
    __tablename__ = 'status_X_TL-WR841N_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTLWR741NDTestTLWR741NDTest(MacList):
    __tablename__ = 'status_X_TL-WR741ND-Test_TL-WR741ND-Test'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ManufacturerOUI = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_SerialNumber = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ProvisioningCode = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_DeviceLog = Column(Text, nullable=False)
    DeviceInfo_Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_SpecVersion = Column(String(255), nullable=False, server_default=text("''"))
    ManagementServer_ParameterKey = Column(String(255), nullable=False, server_default=text("''"))
    ManagementServer_ManageableDeviceNumberOfEntries = Column(String(255), nullable=False, server_default=text("''"))
    ACS_URL = Column(String(255), nullable=False, server_default=text("''"))
    NTPServer1 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    NTPServer2 = Column(String(255), nullable=False, server_default=text("'pool.ntp.org'"))
    LocalTimeZone = Column(String(255), nullable=False, server_default=text("''"))
    LocalTimeZoneName = Column(String(255), nullable=False, server_default=text("''"))
    PeriodicInformTime = Column(String(255), nullable=False, server_default=text("''"))
    KickURL = Column(String(255), nullable=False, server_default=text("''"))
    ManageableDeviceNotificationLimit = Column(String(255), nullable=False, server_default=text("''"))
    UpgradesManaged = Column(Integer, nullable=False, server_default=text("'1'"))
    ModemFirmwareVersion = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTPLinkTD8840TV2TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-8840T-V2_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWONTNoWifiTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW_ONT_noWifi_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXZyxelP660HT1V3STPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_Zyxel-P660H-T1-V3S_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWVoice2TWVoiceNew(MacList):
    __tablename__ = 'status_X_TW_Voice2_TW_Voice_new'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkTDW8901GV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8901G-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTLWR841NCIGG93RGProfileNew(MacList):
    __tablename__ = 'mac_X_TL-WR841N_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8101GV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8101G-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXZyxelP660HNT1ASimple(MacList):
    __tablename__ = 'mac_X_Zyxel-P660HN-T1A_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTD8817V6TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-8817-V6_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTDW8951NDV5TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8951ND-V5_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXCT5624STPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_CT5624S_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXHG531V12CIGG93RGProfileNew(MacList):
    __tablename__ = 'status_X_HG531 V1 2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWFP504TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-FP504_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTWEP9108TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TW-EP9108_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXDraytek2910TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_Draytek-2910_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTWVoice1TWVoice(MacList):
    __tablename__ = 'mac_X_TW_Voice1_TW_Voice'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXZyxelP660HNT1ASimple(MacList):
    __tablename__ = 'status_X_Zyxel-P660HN-T1A_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTPLinkTDW8101GV2TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8101G-V2_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXCIGG93RGIPCIGProfile(MacList):
    __tablename__ = 'mac_X_CIG-G-93RG-IP_CIG-Profile'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8901GV6TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8901G-V6_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWFP804WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-FP804W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXDefaultUniversal(MacList):
    __tablename__ = 'mac_X_Default_Universal'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True)
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False)
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False)
    ConnectionRequestURL = Column(String(255), nullable=False)
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXZyxelP660HT1V3STPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_Zyxel-P660H-T1-V3S_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTDW8101GV2TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8101G-V2_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTDW8151NV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8151N-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXDraytek2910TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_Draytek-2910_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTXVG15306383NoWLAN(MacList):
    __tablename__ = 'status_X_TX-VG1530_6383_noWLAN'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_UpstreamCurrRate = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_DownstreamCurrRate = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_UpstreamMaxRate = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_DownstreamMaxRate = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_UpstreamNoiseMargin = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_DownstreamNoiseMargin = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_UpstreamAttenuation = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_DownstreamAttenuation = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_UpstreamPower = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLInterfaceConfig_DownstreamPower = Column(String(255), nullable=False, server_default=text("''"))


class StatusXCIGG93RGNewCIGG93RGProfileNew(MacList):
    __tablename__ = 'status_X_CIG-G-93RG-New_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWVoice1TWVoice(MacList):
    __tablename__ = 'status_X_TW_Voice1_TW_Voice'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SIP1OutboundProxy = Column(String(255), nullable=False, server_default=text("'sbc01.fpt.net'"))
    SIP1OutboundProxyPort = Column(String(5), nullable=False, server_default=text("'5060'"))
    SIP1Enabled = Column(String(10), nullable=False, server_default=text("'Disabled'"))
    SIP1Number = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthUserName = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthPassword = Column(String(255), nullable=False, server_default=text("'S1changeme'"))


class MacXTWVoice3TWVoiceNew2(MacList):
    __tablename__ = 'mac_X_TW_Voice3_TW_Voice_new2'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTXVG15306383NoWLAN(MacList):
    __tablename__ = 'mac_X_TX-VG1530_6383_noWLAN'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXZyxelFSG1100HNTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_Zyxel-FSG1100HN_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWVoice3TWVoiceNew2(MacList):
    __tablename__ = 'status_X_TW_Voice3_TW_Voice_new2'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    SIP1OutboundProxy = Column(String(255), nullable=False, server_default=text("'sbc01.fpt.net'"))
    SIP1OutboundProxyPort = Column(String(5), nullable=False, server_default=text("'5060'"))
    SIP1Enabled = Column(String(10), nullable=False, server_default=text("'Disabled'"))
    SIP1Number = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthUserName = Column(String(255), nullable=False, server_default=text("'S1changeme'"))
    SIP1AuthPassword = Column(String(255), nullable=False, server_default=text("'S1changeme'"))


class StatusXDefaultUniversal(MacList):
    __tablename__ = 'status_X_Default_Universal'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True)
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False)
    OUI = Column(String(6), nullable=False)
    ProductClass = Column(String(255), nullable=False)
    HardwareVersion = Column(String(255), nullable=False)
    SoftwareVersion = Column(String(255), nullable=False)
    ConnectionService_WANConnectionService = Column(String(255), nullable=False)
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False)
    WANDSLLink_Name = Column(String(255), nullable=False)
    DeviceInfo_ModelName = Column(String(255), nullable=False)
    InterfaceConfig_Layer1UpstreamMaxBitRate = Column(String(255), nullable=False)
    InterfaceConfig_Layer1DownstreamMaxBitRate = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_UpstreamCurrRate = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_DownstreamCurrRate = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_UpstreamMaxRate = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_DownstreamMaxRate = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_UpstreamNoiseMargin = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_DownstreamNoiseMargin = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_UpstreamAttenuation = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_DownstreamAttenuation = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_UpstreamPower = Column(String(255), nullable=False)
    WANDSLInterfaceConfig_DownstreamPower = Column(String(255), nullable=False)
    SSID = Column(String(255), nullable=False)
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    WLANConfiguration_Status = Column(String(255), nullable=False)


class StatusXZyxelP870HWTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_Zyxel-P870HW_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkWR741NDTPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-WR741ND_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTWVoice2TWVoiceNew(MacList):
    __tablename__ = 'mac_X_TW_Voice2_TW_Voice_new'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXTPLinkTDW8101GV3TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8101G-V3_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTDW8961NDV3TPLinkADSLWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-W8961ND-V3_TPLink_ADSL_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceSummary = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    SSID = Column(String(255), nullable=False, server_default=text("''"))
    Channel = Column(String(255), nullable=False, server_default=text("'0'"))
    Enable_Wireless = Column(Integer, nullable=False, server_default=text("'0'"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXArcherC2CIGG93RGProfileNew(MacList):
    __tablename__ = 'mac_X_Archer C2_CIG-G-93RG-Profile-New'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXCTAR5378Simple(MacList):
    __tablename__ = 'status_X_CT-AR5378_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))


class MacXTPLinkTDW8901NV1TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_TPLink-TD-W8901N-V1_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXCT5367TPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_CT5367_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class MacXCTAR5378Simple(MacList):
    __tablename__ = 'mac_X_CT-AR5378_Simple'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class StatusXTPLinkTD8840TV4TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TPLink-TD-8840T-V4_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXCT5367TPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_CT5367_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class StatusXTWFP801WTPLinkADSLNoWifi(MacList):
    __tablename__ = 'status_X_TW-FP801W_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    Manufacturer = Column(String(255), nullable=False, server_default=text("''"))
    OUI = Column(String(6), nullable=False, server_default=text("''"))
    ProductClass = Column(String(255), nullable=False, server_default=text("''"))
    HardwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    SoftwareVersion = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionService_WANConnectionService = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_DestinationAddress = Column(String(255), nullable=False, server_default=text("''"))
    WANDSLLink_Name = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_ModelName = Column(String(255), nullable=False, server_default=text("''"))
    DeviceInfo_UpTime = Column(String(255), nullable=False, server_default=text("''"))
    PPPoEUsername = Column(String(255), nullable=False, server_default=text("''"))


class MacXCT5624STPLinkADSLNoWifi(MacList):
    __tablename__ = 'mac_X_CT5624S_TPLink_ADSL_No_Wifi'

    Mac_id = Column(ForeignKey(u'mac_list.Mac_id', ondelete=u'CASCADE'), primary_key=True)
    ip2long = Column(BigInteger, nullable=False)
    MAC_address = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    Group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    product_id = Column(Integer, nullable=False, server_default=text("'1'"))
    SN = Column(String(255), nullable=False, server_default=text("''"))
    ACS_UserName = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    ACS_PassWord = Column(String(255), nullable=False, server_default=text("'acstr69'"))
    connRequest_UserName = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    connRequest_PassWord = Column(String(255), nullable=False, server_default=text("'cpetr69'"))
    delete_default_WAN_conn = Column(Integer, nullable=False, server_default=text("'0'"))
    maccfg_value = Column(Text, nullable=False)
    maccfg_flag = Column(Integer, nullable=False, server_default=text("'0'"))
    seachablePhoneNumber = Column(String(255), nullable=False, server_default=text("''"))
    ConnectionRequestURL = Column(String(255), nullable=False, server_default=text("''"))
    valuesChanged = Column(Text, nullable=False)
    parameter_control = Column(Text, nullable=False)
    Provision_code2 = Column(String(32), nullable=False, server_default=text("'abc56789'"))


class ModelList(Base):
    __tablename__ = 'model_list'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, server_default=text("''"))
    isVoIP = Column(Integer, nullable=False, server_default=text("'0'"))
    PhoneNums = Column(Integer, nullable=False, server_default=text("'0'"))
    profile_id = Column(Integer, nullable=False, server_default=text("'0'"))
    group_table = Column(String(255), nullable=False, server_default=text("''"))
    mac_table = Column(String(255), nullable=False, server_default=text("''"))
    status_table = Column(String(255), nullable=False, server_default=text("''"))
    history_status_table = Column(String(255), nullable=False, server_default=text("''"))
    portMapping_table = Column(String(255), nullable=False, server_default=text("''"))
    request_log_table = Column(String(255), nullable=False, server_default=text("''"))
    wan_conn_table = Column(String(255), nullable=False, server_default=text("''"))
    status_conf = Column(String(255), nullable=False, server_default=text("''"))
    mapping_conf = Column(String(255), nullable=False, server_default=text("''"))
    voip_conf = Column(String(255), nullable=False, server_default=text("''"))
    ipping_conf = Column(String(255), nullable=False, server_default=text("''"))
    firm_DelaySeconds = Column(Integer, nullable=False, server_default=text("'5'"))
    MAC_EX = Column(String(255), nullable=False, server_default=text("''"))
    Log_nums = Column(Integer, nullable=False, server_default=text("'100'"))
    default_pvcode = Column(String(255), nullable=False, server_default=text("''"))
    default_vpi = Column(Integer, nullable=False, server_default=text("'0'"))
    default_vci = Column(Integer, nullable=False, server_default=text("'33'"))
    default_connection_type = Column(String(255), nullable=False, server_default=text("''"))
    default_link_type = Column(String(255), nullable=False, server_default=text("'EoA'"))
    cfg_id = Column(Integer, nullable=False, server_default=text("'0'"))
    description = Column(Text, nullable=False)
    WANSetup = Column(String(4), nullable=False, server_default=text("'Hide'"))
    PortMapping = Column(String(4), nullable=False, server_default=text("'Hide'"))
    MACFiltering = Column(String(4), nullable=False, server_default=text("'Hide'"))
    IPFiltering = Column(String(4), nullable=False, server_default=text("'Hide'"))
    VirtualServers = Column(String(4), nullable=False, server_default=text("'Hide'"))
    StaticRoute = Column(String(4), nullable=False, server_default=text("'Hide'"))
    RPCGet = Column(Integer, nullable=False, server_default=text("'20'"))
    RPCSet = Column(Integer, nullable=False, server_default=text("'20'"))
    ImageFile = Column(String(128), nullable=False)


class ParameterList(Base):
    __tablename__ = 'parameter_list'

    id = Column(Integer, primary_key=True)
    tr069_para = Column(String(255), nullable=False, server_default=text("''"))
    db_s_name = Column(String(255), nullable=False, server_default=text("''"))
    db_s_alias = Column(String(255), nullable=False, server_default=text("''"))
    para_type = Column(String(255), nullable=False, server_default=text("''"))
    sql_type = Column(String(255), nullable=False, server_default=text("''"))
    value_type = Column(String(255), nullable=False, server_default=text("''"))
    value_obj = Column(String(255), nullable=False, server_default=text("''"))
    default_value = Column(String(255), nullable=False, server_default=text("''"))
    is_hidden = Column(Integer, nullable=False, server_default=text("'0'"))
    must_table = Column(String(255), nullable=False, server_default=text("''"))
    user_defined = Column(Integer, nullable=False, server_default=text("'0'"))


class ParameterMapping(Base):
    __tablename__ = 'parameter_mapping'

    id = Column(Integer, primary_key=True)
    tr069_para = Column(String(255), nullable=False, server_default=text("''"))
    db_s_name = Column(String(255), nullable=False, server_default=text("''"))
    db_s_alias = Column(String(255), nullable=False, server_default=text("''"))
    para_type = Column(String(255), nullable=False, server_default=text("''"))
    sql_type = Column(String(255), nullable=False, server_default=text("''"))
    value_type = Column(String(255), nullable=False, server_default=text("''"))
    value_obj = Column(String(255), nullable=False, server_default=text("''"))
    default_value = Column(String(255), nullable=False, server_default=text("''"))
    is_hidden = Column(Integer, nullable=False, server_default=text("'0'"))
    must_table = Column(String(255), nullable=False, server_default=text("''"))
    user_defined = Column(Integer, nullable=False, server_default=text("'0'"))


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    values_array = Column(Text, nullable=False)


class RequestLogXArcherC2CIGG93RGProfileNew(Base):
    __tablename__ = 'request_log_X_Archer C2_CIG-G-93RG-Profile-New'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCIGG93RGIPCIGProfile(Base):
    __tablename__ = 'request_log_X_CIG-G-93RG-IP_CIG-Profile'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCIGG93RGNewCIGG93RGProfileNew(Base):
    __tablename__ = 'request_log_X_CIG-G-93RG-New_CIG-G-93RG-Profile-New'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCIGG97D2CIGG93RGProfileNew(Base):
    __tablename__ = 'request_log_X_CIG-G-97D2_CIG-G-93RG-Profile-New'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCTAR5378Simple(Base):
    __tablename__ = 'request_log_X_CT-AR5378_Simple'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCT5367TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_CT5367_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXCT5624STPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_CT5624S_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXDefaultSimple(Base):
    __tablename__ = 'request_log_X_Default_Simple'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXDefaultUniversal(Base):
    __tablename__ = 'request_log_X_Default_Universal'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXDraytek2910TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_Draytek-2910_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXEmilyVDSL4PortTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_EmilyVDSL4Port_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXHG531V12CIGG93RGProfileNew(Base):
    __tablename__ = 'request_log_X_HG531 V1 2_CIG-G-93RG-Profile-New'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXHuaweiHG610HuaweiHG610(Base):
    __tablename__ = 'request_log_X_Huawei-HG-610_Huawei-HG-610'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTLWR740NTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TL-WR740N_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTLWR741NDTestTLWR741NDTest(Base):
    __tablename__ = 'request_log_X_TL-WR741ND-Test_TL-WR741ND-Test'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTLWR841NCIGG93RGProfileNew(Base):
    __tablename__ = 'request_log_X_TL-WR841N_CIG-G-93RG-Profile-New'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTD8817V6TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-8817-V6_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTD8840TV2TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-8840T-V2_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTD8840TV3TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-8840T-V3_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTD8840TV4TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-8840T-V4_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8101GV2TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8101G-V2_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8101GV3TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8101G-V3_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8151NV3TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8151N-V3_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8901GV3TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8901G-V3_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8901GV6TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8901G-V6_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8901NV1TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8901N-V1_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8951NDV5TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8951ND-V5_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8961NDV3TPLinkADSLWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8961ND-V3_TPLink_ADSL_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkTDW8968V1TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-TD-W8968-V1_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTPLinkWR741NDTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TPLink-WR741ND_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTW4PortWifiTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-4Port-Wifi_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWEP9108WTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-EP9108W_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWEP9108TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-EP9108_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWFP504TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-FP504_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWFP801WTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-FP801W_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWFP804WTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW-FP804W_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWONTNoWifiTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_TW_ONT_noWifi_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWVoice1TWVoice(Base):
    __tablename__ = 'request_log_X_TW_Voice1_TW_Voice'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWVoice2TWVoiceNew(Base):
    __tablename__ = 'request_log_X_TW_Voice2_TW_Voice_new'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWVoice3TWVoiceNew2(Base):
    __tablename__ = 'request_log_X_TW_Voice3_TW_Voice_new2'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTWVoiceTWVoice(Base):
    __tablename__ = 'request_log_X_TW_voice_TW_Voice'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTXVG15306383NoWLAN(Base):
    __tablename__ = 'request_log_X_TX-VG1530_6383_noWLAN'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXTempModel1TPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_Temp_Model1_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXZyxelFSG1100HNTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_Zyxel-FSG1100HN_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXZyxelP660HT1V3STPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_Zyxel-P660H-T1-V3S_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXZyxelP660HNT1ASimple(Base):
    __tablename__ = 'request_log_X_Zyxel-P660HN-T1A_Simple'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXZyxelP870HWTestZyxelP870HW(Base):
    __tablename__ = 'request_log_X_Zyxel-P870HW-Test_Zyxel-P870HW'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class RequestLogXZyxelP870HWTPLinkADSLNoWifi(Base):
    __tablename__ = 'request_log_X_Zyxel-P870HW_TPLink_ADSL_No_Wifi'

    id = Column(Integer, primary_key=True)
    mac = Column(ForeignKey(u'mac_list.MAC_address', ondelete=u'CASCADE'), nullable=False, index=True, server_default=text("''"))
    online_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    event_code = Column(String(255), nullable=False, server_default=text("''"))

    mac_list = relationship(u'MacList')


class Schedule(Base):
    __tablename__ = 'schedule'

    mac = Column(String(64), primary_key=True, nullable=False, server_default=text("''"))
    action = Column(String(30), primary_key=True, nullable=False, server_default=text("''"))
    addtime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    schedule_data = Column(String)


class SessionLog(Base):
    __tablename__ = 'sessionLog'

    id = Column(Integer, primary_key=True)
    level = Column(String(128))
    logtime = Column(String(128))
    cpe_serial = Column(String(255))
    ip = Column(String(255))
    eventcode = Column(String(255))


class SystemLog(Base):
    __tablename__ = 'system_log'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, index=True, server_default=text("''"))
    faultcode = Column(String(30), nullable=False, server_default=text("''"))
    faultstring = Column(String(255), nullable=False)
    faultcode_detail = Column(String(255), nullable=False, server_default=text("''"))
    faultstring_detail = Column(String(255), nullable=False, server_default=text("''"))
    action_desc = Column(String(30), nullable=False, server_default=text("''"))
    set_value = Column(Text, nullable=False)
    ip = Column(String(15), nullable=False)
    created_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_trouble_shooting = Table(
    'trouble_shooting', metadata,
    Column('Mac_id', Integer, nullable=False),
    Column('MAC_address', String(64), nullable=False),
    Column('Group_id', Integer, nullable=False),
    Column('product_id', Integer, nullable=False),
    Column('send_time', DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('CR_result', String(255)),
    Column('Ping_result', Text),
    Column('IPPing_result', Text),
    Column('Status_result', Text)
)


class UserProfile(Base):
    __tablename__ = 'user_profiles'

    user_id = Column(Integer, primary_key=True)
    lastname = Column(String(50), nullable=False, server_default=text("''"))
    firstname = Column(String(50), nullable=False, server_default=text("''"))


class UserProfilesField(Base):
    __tablename__ = 'user_profiles_fields'
    __table_args__ = (
        Index('varname', 'varname', 'widget', 'visible'),
    )

    id = Column(Integer, primary_key=True)
    varname = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    field_type = Column(String(50), nullable=False)
    field_size = Column(Integer, nullable=False, server_default=text("'0'"))
    field_size_min = Column(Integer, nullable=False, server_default=text("'0'"))
    required = Column(Integer, nullable=False, server_default=text("'0'"))
    match = Column(String(255), nullable=False, server_default=text("''"))
    range = Column(String(255), nullable=False, server_default=text("''"))
    error_message = Column(String(255), nullable=False, server_default=text("''"))
    other_validator = Column(String(5000), nullable=False, server_default=text("''"))
    default = Column(String(255), nullable=False, server_default=text("''"))
    widget = Column(String(255), nullable=False, server_default=text("''"))
    widgetparams = Column(String(5000), nullable=False, server_default=text("''"))
    position = Column(Integer, nullable=False, server_default=text("'0'"))
    visible = Column(Integer, nullable=False, server_default=text("'0'"))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    activkey = Column(String(128), nullable=False, server_default=text("''"))
    createtime = Column(Integer, nullable=False, server_default=text("'0'"))
    lastvisit = Column(Integer, nullable=False, server_default=text("'0'"))
    superuser = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    status = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
