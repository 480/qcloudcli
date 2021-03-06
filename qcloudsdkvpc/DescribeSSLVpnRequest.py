# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSSLVpnRequest(Request):

    def __init__(self):
        super(DescribeSSLVpnRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeSSLVpn', 'vpc.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderDirection(self):
        return self.get_params().get('orderDirection')

    def set_orderDirection(self, orderDirection):
        self.add_param('orderDirection', orderDirection)

    def get_orderField(self):
        return self.get_params().get('orderField')

    def set_orderField(self, orderField):
        self.add_param('orderField', orderField)

    def get_sslVpnId(self):
        return self.get_params().get('sslVpnId')

    def set_sslVpnId(self, sslVpnId):
        self.add_param('sslVpnId', sslVpnId)

    def get_sslVpnName(self):
        return self.get_params().get('sslVpnName')

    def set_sslVpnName(self, sslVpnName):
        self.add_param('sslVpnName', sslVpnName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
