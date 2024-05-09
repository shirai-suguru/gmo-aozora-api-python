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

class TransferCancelResponse(object):
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
        'account_id': 'str',
        'cancel_target_key_class': 'str',
        'result_code': 'str',
        'apply_no': 'str',
        'apply_end_datetime': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'cancel_target_key_class': 'cancelTargetKeyClass',
        'result_code': 'resultCode',
        'apply_no': 'applyNo',
        'apply_end_datetime': 'applyEndDatetime'
    }

    def __init__(self, account_id=None, cancel_target_key_class=None, result_code=None, apply_no=None, apply_end_datetime=None):  # noqa: E501
        """TransferCancelResponse - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._cancel_target_key_class = None
        self._result_code = None
        self._apply_no = None
        self._apply_end_datetime = None
        self.discriminator = None
        self.account_id = account_id
        self.cancel_target_key_class = cancel_target_key_class
        self.result_code = result_code
        self.apply_no = apply_no
        if apply_end_datetime is not None:
            self.apply_end_datetime = apply_end_datetime

    @property
    def account_id(self):
        """Gets the account_id of this TransferCancelResponse.  # noqa: E501

        口座ID<br>半角英数字<br>口座を識別するID<br>  # noqa: E501

        :return: The account_id of this TransferCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransferCancelResponse.

        口座ID<br>半角英数字<br>口座を識別するID<br>  # noqa: E501

        :param account_id: The account_id of this TransferCancelResponse.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def cancel_target_key_class(self):
        """Gets the cancel_target_key_class of this TransferCancelResponse.  # noqa: E501

        取消対象キー区分<br>半角英数値<br>1:振込申請取消　2:振込受付取消　3:総合振込申請取消　4:総合振込受付取消<br>  # noqa: E501

        :return: The cancel_target_key_class of this TransferCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._cancel_target_key_class

    @cancel_target_key_class.setter
    def cancel_target_key_class(self, cancel_target_key_class):
        """Sets the cancel_target_key_class of this TransferCancelResponse.

        取消対象キー区分<br>半角英数値<br>1:振込申請取消　2:振込受付取消　3:総合振込申請取消　4:総合振込受付取消<br>  # noqa: E501

        :param cancel_target_key_class: The cancel_target_key_class of this TransferCancelResponse.  # noqa: E501
        :type: str
        """
        if cancel_target_key_class is None:
            raise ValueError("Invalid value for `cancel_target_key_class`, must not be `None`")  # noqa: E501

        self._cancel_target_key_class = cancel_target_key_class

    @property
    def result_code(self):
        """Gets the result_code of this TransferCancelResponse.  # noqa: E501

        結果コード<br>半角数字<br>1:完了　2：未完了<br>  # noqa: E501

        :return: The result_code of this TransferCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this TransferCancelResponse.

        結果コード<br>半角数字<br>1:完了　2：未完了<br>  # noqa: E501

        :param result_code: The result_code of this TransferCancelResponse.  # noqa: E501
        :type: str
        """
        if result_code is None:
            raise ValueError("Invalid value for `result_code`, must not be `None`")  # noqa: E501

        self._result_code = result_code

    @property
    def apply_no(self):
        """Gets the apply_no of this TransferCancelResponse.  # noqa: E501

        受付番号（振込申請番号）<br>半角数字<br>取り消し対象の番号<br>  # noqa: E501

        :return: The apply_no of this TransferCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._apply_no

    @apply_no.setter
    def apply_no(self, apply_no):
        """Sets the apply_no of this TransferCancelResponse.

        受付番号（振込申請番号）<br>半角数字<br>取り消し対象の番号<br>  # noqa: E501

        :param apply_no: The apply_no of this TransferCancelResponse.  # noqa: E501
        :type: str
        """
        if apply_no is None:
            raise ValueError("Invalid value for `apply_no`, must not be `None`")  # noqa: E501

        self._apply_no = apply_no

    @property
    def apply_end_datetime(self):
        """Gets the apply_end_datetime of this TransferCancelResponse.  # noqa: E501

        振込依頼完了日時<br>半角文字<br>YYYY-MM-DDTHH:MM:SS+09:00形式<br>結果コードが、1:完了のときのみセット<br>このリクエストの依頼が完了した日時を返却<br>それ以外は項目自体を設定しません<br>  # noqa: E501

        :return: The apply_end_datetime of this TransferCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._apply_end_datetime

    @apply_end_datetime.setter
    def apply_end_datetime(self, apply_end_datetime):
        """Sets the apply_end_datetime of this TransferCancelResponse.

        振込依頼完了日時<br>半角文字<br>YYYY-MM-DDTHH:MM:SS+09:00形式<br>結果コードが、1:完了のときのみセット<br>このリクエストの依頼が完了した日時を返却<br>それ以外は項目自体を設定しません<br>  # noqa: E501

        :param apply_end_datetime: The apply_end_datetime of this TransferCancelResponse.  # noqa: E501
        :type: str
        """

        self._apply_end_datetime = apply_end_datetime

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
        if issubclass(TransferCancelResponse, dict):
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
        if not isinstance(other, TransferCancelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
