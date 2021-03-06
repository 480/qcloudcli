# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlAddUserRequest(Request):

    def __init__(self):
        super(CdbTdsqlAddUserRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlAddUser', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)

    def get_delayThresh(self):
        return self.get_params().get('delayThresh')

    def set_delayThresh(self, delayThresh):
        self.add_param('delayThresh', delayThresh)

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_readOnly(self):
        return self.get_params().get('readOnly')

    def set_readOnly(self, readOnly):
        self.add_param('readOnly', readOnly)

    def get_sameIDC(self):
        return self.get_params().get('sameIDC')

    def set_sameIDC(self, sameIDC):
        self.add_param('sameIDC', sameIDC)

    def get_userName(self):
        return self.get_params().get('userName')

    def set_userName(self, userName):
        self.add_param('userName', userName)

    def get_watch(self):
        return self.get_params().get('watch')

    def set_watch(self, watch):
        self.add_param('watch', watch)
