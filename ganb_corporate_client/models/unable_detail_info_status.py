# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>オープンAPI仕様書（PDF版）は下記リンクをご参照ください</p> <div>   <div style='display:inline-block;'><a style='text-decoration:none; font-weight:bold; color:#00b8d4;' href='https://gmo-aozora.com/api-cooperation/api-specification.html' target='_blank'>オープンAPI仕様書</a></div><div style='display:inline-block; margin-left:2px; left:2px; width:10px; height:10px; border-top:2px solid #00b8d4; border-right:2px solid #00b8d4; transparent;-webkit-transform:rotate(45deg); transform: rotate(45deg);'></div> </div> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>共通仕様</h4> <div style='width:100%; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>＜HTTPリクエストヘッダ＞</p>   <div style='display:table; margin-left:10px; background-color:#29659b;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff;'>項目</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; color:#fff;'>仕様</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>プロトコル</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>HTTP1.1/HTTPS</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>charset</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>UTF-8</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>content-type</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>application/json</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>domain_name</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       本番環境：api.gmo-aozora.com</br>       開発環境：stg-api.gmo-aozora.com     </div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>メインURL</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       https://{domain_name}/ganb/api/corporation/{version}</br>       <span style='border-bottom:solid 1px;'>Version:1.x.x</span> の場合</br>       　https://api.gmo-aozora.com/ganb/api/corporation/<span style='border-bottom:solid 1px;'>v1</span>     </div>   </div> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜リクエスト共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <p style='padding-left:40px;'>パラメータの値が空の場合、またはパラメータ自体が設定されていない場合、どちらもNULLとして扱います</p> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜レスポンス共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <ul>     <li>レスポンスデータ</li>       <ul>         <li style='list-style-type:none;'>レスポンスデータの値が空の場合または、レスポンスデータ自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>     <li>配列</li>       <ul>         <li style='list-style-type:none;'>配列の要素の値が空の場合は「空のリスト」と記載</li>         <li style='list-style-type:none;'>配列自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>   </ul> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜更新系APIに関する注意事項＞</p>   <ul>     <li style='list-style-type:none;'>更新系処理がタイムアウトとなった場合、処理自体は実行されている可能性がありますので、</li>     <li style='list-style-type:none;'>再実行を行う必要がある場合は必ず照会系の処理で実行状況を確認してから再実行を行ってください</li>   </ul> </div>   # noqa: E501

    OpenAPI spec version: 1.15.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UnableDetailInfoStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transfer_detail_status': 'str',
        'refund_status': 'str',
        'is_repayment': 'bool',
        'repayment_date': 'str',
        'unable_reason_detail': 'UnableDetailInfoStatusUnableReasonDetail'
    }

    attribute_map = {
        'transfer_detail_status': 'transferDetailStatus',
        'refund_status': 'refundStatus',
        'is_repayment': 'isRepayment',
        'repayment_date': 'repaymentDate',
        'unable_reason_detail': 'unableReasonDetail'
    }

    def __init__(self, transfer_detail_status=None, refund_status=None, is_repayment=None, repayment_date=None, unable_reason_detail=None):  # noqa: E501
        """UnableDetailInfoStatus - a model defined in Swagger"""  # noqa: E501
        self._transfer_detail_status = None
        self._refund_status = None
        self._is_repayment = None
        self._repayment_date = None
        self._unable_reason_detail = None
        self.discriminator = None
        if transfer_detail_status is not None:
            self.transfer_detail_status = transfer_detail_status
        if refund_status is not None:
            self.refund_status = refund_status
        if is_repayment is not None:
            self.is_repayment = is_repayment
        if repayment_date is not None:
            self.repayment_date = repayment_date
        if unable_reason_detail is not None:
            self.unable_reason_detail = unable_reason_detail

    @property
    def transfer_detail_status(self):
        """Gets the transfer_detail_status of this UnableDetailInfoStatus.  # noqa: E501

        振込詳細ステータス<br>半角数字<br>1：手続済、2：手続不成立<br>手続中より前は該当する情報無しとみなし項目自体を設定しません<br>  # noqa: E501

        :return: The transfer_detail_status of this UnableDetailInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._transfer_detail_status

    @transfer_detail_status.setter
    def transfer_detail_status(self, transfer_detail_status):
        """Sets the transfer_detail_status of this UnableDetailInfoStatus.

        振込詳細ステータス<br>半角数字<br>1：手続済、2：手続不成立<br>手続中より前は該当する情報無しとみなし項目自体を設定しません<br>  # noqa: E501

        :param transfer_detail_status: The transfer_detail_status of this UnableDetailInfoStatus.  # noqa: E501
        :type: str
        """

        self._transfer_detail_status = transfer_detail_status

    @property
    def refund_status(self):
        """Gets the refund_status of this UnableDetailInfoStatus.  # noqa: E501

        組戻ステータス<br>半角数字<br>1：組戻手続中、2：組戻済、3：組戻不成立<br>組み戻しなし、および該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :return: The refund_status of this UnableDetailInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._refund_status

    @refund_status.setter
    def refund_status(self, refund_status):
        """Sets the refund_status of this UnableDetailInfoStatus.

        組戻ステータス<br>半角数字<br>1：組戻手続中、2：組戻済、3：組戻不成立<br>組み戻しなし、および該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :param refund_status: The refund_status of this UnableDetailInfoStatus.  # noqa: E501
        :type: str
        """

        self._refund_status = refund_status

    @property
    def is_repayment(self):
        """Gets the is_repayment of this UnableDetailInfoStatus.  # noqa: E501

        資金返却フラグ<br>true=あり<br>無し、および該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :return: The is_repayment of this UnableDetailInfoStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_repayment

    @is_repayment.setter
    def is_repayment(self, is_repayment):
        """Sets the is_repayment of this UnableDetailInfoStatus.

        資金返却フラグ<br>true=あり<br>無し、および該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :param is_repayment: The is_repayment of this UnableDetailInfoStatus.  # noqa: E501
        :type: bool
        """

        self._is_repayment = is_repayment

    @property
    def repayment_date(self):
        """Gets the repayment_date of this UnableDetailInfoStatus.  # noqa: E501

        資金返却日<br>半角文字<br>YYYY-MM-DD形式<br>該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :return: The repayment_date of this UnableDetailInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._repayment_date

    @repayment_date.setter
    def repayment_date(self, repayment_date):
        """Sets the repayment_date of this UnableDetailInfoStatus.

        資金返却日<br>半角文字<br>YYYY-MM-DD形式<br>該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :param repayment_date: The repayment_date of this UnableDetailInfoStatus.  # noqa: E501
        :type: str
        """

        self._repayment_date = repayment_date

    @property
    def unable_reason_detail(self):
        """Gets the unable_reason_detail of this UnableDetailInfoStatus.  # noqa: E501


        :return: The unable_reason_detail of this UnableDetailInfoStatus.  # noqa: E501
        :rtype: UnableDetailInfoStatusUnableReasonDetail
        """
        return self._unable_reason_detail

    @unable_reason_detail.setter
    def unable_reason_detail(self, unable_reason_detail):
        """Sets the unable_reason_detail of this UnableDetailInfoStatus.


        :param unable_reason_detail: The unable_reason_detail of this UnableDetailInfoStatus.  # noqa: E501
        :type: UnableDetailInfoStatusUnableReasonDetail
        """

        self._unable_reason_detail = unable_reason_detail

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UnableDetailInfoStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UnableDetailInfoStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
