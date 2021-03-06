# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EipBmQueryTaskRequest(Request):

    def __init__(self):
        super(EipBmQueryTaskRequest, self).__init__(
            'eip', 'qcloudcliV1', 'EipBmQueryTask', 'eip.api.qcloud.com')

    def get_requestId(self):
        return self.get_params().get('requestId')

    def set_requestId(self, requestId):
        self.add_param('requestId', requestId)
