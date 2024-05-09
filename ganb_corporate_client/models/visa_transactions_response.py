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

class VisaTransactionsResponse(object):
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
        'date_from': 'str',
        'date_to': 'str',
        'base_date': 'str',
        'base_time': 'str',
        'has_next': 'bool',
        'next_item_key': 'str',
        'count': 'str',
        'visa_transactions': 'list[VisaTransaction]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'base_date': 'baseDate',
        'base_time': 'baseTime',
        'has_next': 'hasNext',
        'next_item_key': 'nextItemKey',
        'count': 'count',
        'visa_transactions': 'visaTransactions'
    }

    def __init__(self, account_id=None, date_from=None, date_to=None, base_date=None, base_time=None, has_next=None, next_item_key=None, count=None, visa_transactions=None):  # noqa: E501
        """VisaTransactionsResponse - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._date_from = None
        self._date_to = None
        self._base_date = None
        self._base_time = None
        self._has_next = None
        self._next_item_key = None
        self._count = None
        self._visa_transactions = None
        self.discriminator = None
        self.account_id = account_id
        self.date_from = date_from
        self.date_to = date_to
        self.base_date = base_date
        self.base_time = base_time
        self.has_next = has_next
        if next_item_key is not None:
            self.next_item_key = next_item_key
        self.count = count
        if visa_transactions is not None:
            self.visa_transactions = visa_transactions

    @property
    def account_id(self):
        """Gets the account_id of this VisaTransactionsResponse.  # noqa: E501

        口座ID<br>半角英数字<br>口座を識別するID<br>  # noqa: E501

        :return: The account_id of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this VisaTransactionsResponse.

        口座ID<br>半角英数字<br>口座を識別するID<br>  # noqa: E501

        :param account_id: The account_id of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def date_from(self):
        """Gets the date_from of this VisaTransactionsResponse.  # noqa: E501

        対象期間From<br>半角文字<br>YYYY-MM-DD形式<br>リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます<br>  # noqa: E501

        :return: The date_from of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this VisaTransactionsResponse.

        対象期間From<br>半角文字<br>YYYY-MM-DD形式<br>リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます<br>  # noqa: E501

        :param date_from: The date_from of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if date_from is None:
            raise ValueError("Invalid value for `date_from`, must not be `None`")  # noqa: E501

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this VisaTransactionsResponse.  # noqa: E501

        対象期間To<br>半角文字<br>YYYY-MM-DD形式<br>リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます<br>  # noqa: E501

        :return: The date_to of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this VisaTransactionsResponse.

        対象期間To<br>半角文字<br>YYYY-MM-DD形式<br>リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます<br>  # noqa: E501

        :param date_to: The date_to of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if date_to is None:
            raise ValueError("Invalid value for `date_to`, must not be `None`")  # noqa: E501

        self._date_to = date_to

    @property
    def base_date(self):
        """Gets the base_date of this VisaTransactionsResponse.  # noqa: E501

        基準日<br>半角文字<br>Visaデビット取引明細を照会した基準日を示します<br>YYYY-MM-DD形式<br>  # noqa: E501

        :return: The base_date of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this VisaTransactionsResponse.

        基準日<br>半角文字<br>Visaデビット取引明細を照会した基準日を示します<br>YYYY-MM-DD形式<br>  # noqa: E501

        :param base_date: The base_date of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if base_date is None:
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def base_time(self):
        """Gets the base_time of this VisaTransactionsResponse.  # noqa: E501

        基準時刻<br>半角文字<br>Visaデビット取引明細を照会した基準時刻を示します<br>HH:MM:SS+09:00形式<br>  # noqa: E501

        :return: The base_time of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_time

    @base_time.setter
    def base_time(self, base_time):
        """Sets the base_time of this VisaTransactionsResponse.

        基準時刻<br>半角文字<br>Visaデビット取引明細を照会した基準時刻を示します<br>HH:MM:SS+09:00形式<br>  # noqa: E501

        :param base_time: The base_time of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if base_time is None:
            raise ValueError("Invalid value for `base_time`, must not be `None`")  # noqa: E501

        self._base_time = base_time

    @property
    def has_next(self):
        """Gets the has_next of this VisaTransactionsResponse.  # noqa: E501

        次明細フラグ<br>・true=次明細あり<br>・false=次明細なし<br>  # noqa: E501

        :return: The has_next of this VisaTransactionsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this VisaTransactionsResponse.

        次明細フラグ<br>・true=次明細あり<br>・false=次明細なし<br>  # noqa: E501

        :param has_next: The has_next of this VisaTransactionsResponse.  # noqa: E501
        :type: bool
        """
        if has_next is None:
            raise ValueError("Invalid value for `has_next`, must not be `None`")  # noqa: E501

        self._has_next = has_next

    @property
    def next_item_key(self):
        """Gets the next_item_key of this VisaTransactionsResponse.  # noqa: E501

        次明細キー<br>半角数字<br>次明細フラグがfalseの場合は、項目自体を設定しません<br>  # noqa: E501

        :return: The next_item_key of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_item_key

    @next_item_key.setter
    def next_item_key(self, next_item_key):
        """Sets the next_item_key of this VisaTransactionsResponse.

        次明細キー<br>半角数字<br>次明細フラグがfalseの場合は、項目自体を設定しません<br>  # noqa: E501

        :param next_item_key: The next_item_key of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """

        self._next_item_key = next_item_key

    @property
    def count(self):
        """Gets the count of this VisaTransactionsResponse.  # noqa: E501

        明細取得件数<br>半角数字<br>  # noqa: E501

        :return: The count of this VisaTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VisaTransactionsResponse.

        明細取得件数<br>半角数字<br>  # noqa: E501

        :param count: The count of this VisaTransactionsResponse.  # noqa: E501
        :type: str
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def visa_transactions(self):
        """Gets the visa_transactions of this VisaTransactionsResponse.  # noqa: E501

        Visaデビット取引明細情報リスト<br>該当する情報が無い場合は空のリストを返却します<br>  # noqa: E501

        :return: The visa_transactions of this VisaTransactionsResponse.  # noqa: E501
        :rtype: list[VisaTransaction]
        """
        return self._visa_transactions

    @visa_transactions.setter
    def visa_transactions(self, visa_transactions):
        """Sets the visa_transactions of this VisaTransactionsResponse.

        Visaデビット取引明細情報リスト<br>該当する情報が無い場合は空のリストを返却します<br>  # noqa: E501

        :param visa_transactions: The visa_transactions of this VisaTransactionsResponse.  # noqa: E501
        :type: list[VisaTransaction]
        """

        self._visa_transactions = visa_transactions

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
        if issubclass(VisaTransactionsResponse, dict):
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
        if not isinstance(other, VisaTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
