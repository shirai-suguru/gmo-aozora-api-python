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

class DebitsDetail(object):
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
        'debit_id': 'str',
        'card_brand_type_code': 'str',
        'debit_status': 'str',
        'debit_expire_date': 'str',
        'debit_amount_cumulative': 'DebitsDetailDebitAmountCumulative',
        'debit_amount_possible': 'DebitsDetailDebitAmountPossible',
        'debit_amount_limit': 'DebitsDetailDebitAmountLimit'
    }

    attribute_map = {
        'debit_id': 'debitId',
        'card_brand_type_code': 'cardBrandTypeCode',
        'debit_status': 'debitStatus',
        'debit_expire_date': 'debitExpireDate',
        'debit_amount_cumulative': 'debitAmountCumulative',
        'debit_amount_possible': 'debitAmountPossible',
        'debit_amount_limit': 'debitAmountLimit'
    }

    def __init__(self, debit_id=None, card_brand_type_code=None, debit_status=None, debit_expire_date=None, debit_amount_cumulative=None, debit_amount_possible=None, debit_amount_limit=None):  # noqa: E501
        """DebitsDetail - a model defined in Swagger"""  # noqa: E501
        self._debit_id = None
        self._card_brand_type_code = None
        self._debit_status = None
        self._debit_expire_date = None
        self._debit_amount_cumulative = None
        self._debit_amount_possible = None
        self._debit_amount_limit = None
        self.discriminator = None
        if debit_id is not None:
            self.debit_id = debit_id
        if card_brand_type_code is not None:
            self.card_brand_type_code = card_brand_type_code
        if debit_status is not None:
            self.debit_status = debit_status
        if debit_expire_date is not None:
            self.debit_expire_date = debit_expire_date
        if debit_amount_cumulative is not None:
            self.debit_amount_cumulative = debit_amount_cumulative
        if debit_amount_possible is not None:
            self.debit_amount_possible = debit_amount_possible
        if debit_amount_limit is not None:
            self.debit_amount_limit = debit_amount_limit

    @property
    def debit_id(self):
        """Gets the debit_id of this DebitsDetail.  # noqa: E501

        半角数字<br>デビットカードを識別するID<br>  # noqa: E501

        :return: The debit_id of this DebitsDetail.  # noqa: E501
        :rtype: str
        """
        return self._debit_id

    @debit_id.setter
    def debit_id(self, debit_id):
        """Sets the debit_id of this DebitsDetail.

        半角数字<br>デビットカードを識別するID<br>  # noqa: E501

        :param debit_id: The debit_id of this DebitsDetail.  # noqa: E501
        :type: str
        """

        self._debit_id = debit_id

    @property
    def card_brand_type_code(self):
        """Gets the card_brand_type_code of this DebitsDetail.  # noqa: E501

        半角英数字<br>・01=visa<br>・02＝master<br>  # noqa: E501

        :return: The card_brand_type_code of this DebitsDetail.  # noqa: E501
        :rtype: str
        """
        return self._card_brand_type_code

    @card_brand_type_code.setter
    def card_brand_type_code(self, card_brand_type_code):
        """Sets the card_brand_type_code of this DebitsDetail.

        半角英数字<br>・01=visa<br>・02＝master<br>  # noqa: E501

        :param card_brand_type_code: The card_brand_type_code of this DebitsDetail.  # noqa: E501
        :type: str
        """

        self._card_brand_type_code = card_brand_type_code

    @property
    def debit_status(self):
        """Gets the debit_status of this DebitsDetail.  # noqa: E501

        半角英数字<br>・01=利用中<br>・02=有効期限切れ<br>・09=解約<br>  # noqa: E501

        :return: The debit_status of this DebitsDetail.  # noqa: E501
        :rtype: str
        """
        return self._debit_status

    @debit_status.setter
    def debit_status(self, debit_status):
        """Sets the debit_status of this DebitsDetail.

        半角英数字<br>・01=利用中<br>・02=有効期限切れ<br>・09=解約<br>  # noqa: E501

        :param debit_status: The debit_status of this DebitsDetail.  # noqa: E501
        :type: str
        """

        self._debit_status = debit_status

    @property
    def debit_expire_date(self):
        """Gets the debit_expire_date of this DebitsDetail.  # noqa: E501

        半角文字<br>デビットカードの有効期限を返却します<br>YYYY-MM形式<br>  # noqa: E501

        :return: The debit_expire_date of this DebitsDetail.  # noqa: E501
        :rtype: str
        """
        return self._debit_expire_date

    @debit_expire_date.setter
    def debit_expire_date(self, debit_expire_date):
        """Sets the debit_expire_date of this DebitsDetail.

        半角文字<br>デビットカードの有効期限を返却します<br>YYYY-MM形式<br>  # noqa: E501

        :param debit_expire_date: The debit_expire_date of this DebitsDetail.  # noqa: E501
        :type: str
        """

        self._debit_expire_date = debit_expire_date

    @property
    def debit_amount_cumulative(self):
        """Gets the debit_amount_cumulative of this DebitsDetail.  # noqa: E501


        :return: The debit_amount_cumulative of this DebitsDetail.  # noqa: E501
        :rtype: DebitsDetailDebitAmountCumulative
        """
        return self._debit_amount_cumulative

    @debit_amount_cumulative.setter
    def debit_amount_cumulative(self, debit_amount_cumulative):
        """Sets the debit_amount_cumulative of this DebitsDetail.


        :param debit_amount_cumulative: The debit_amount_cumulative of this DebitsDetail.  # noqa: E501
        :type: DebitsDetailDebitAmountCumulative
        """

        self._debit_amount_cumulative = debit_amount_cumulative

    @property
    def debit_amount_possible(self):
        """Gets the debit_amount_possible of this DebitsDetail.  # noqa: E501


        :return: The debit_amount_possible of this DebitsDetail.  # noqa: E501
        :rtype: DebitsDetailDebitAmountPossible
        """
        return self._debit_amount_possible

    @debit_amount_possible.setter
    def debit_amount_possible(self, debit_amount_possible):
        """Sets the debit_amount_possible of this DebitsDetail.


        :param debit_amount_possible: The debit_amount_possible of this DebitsDetail.  # noqa: E501
        :type: DebitsDetailDebitAmountPossible
        """

        self._debit_amount_possible = debit_amount_possible

    @property
    def debit_amount_limit(self):
        """Gets the debit_amount_limit of this DebitsDetail.  # noqa: E501


        :return: The debit_amount_limit of this DebitsDetail.  # noqa: E501
        :rtype: DebitsDetailDebitAmountLimit
        """
        return self._debit_amount_limit

    @debit_amount_limit.setter
    def debit_amount_limit(self, debit_amount_limit):
        """Sets the debit_amount_limit of this DebitsDetail.


        :param debit_amount_limit: The debit_amount_limit of this DebitsDetail.  # noqa: E501
        :type: DebitsDetailDebitAmountLimit
        """

        self._debit_amount_limit = debit_amount_limit

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
        if issubclass(DebitsDetail, dict):
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
        if not isinstance(other, DebitsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
