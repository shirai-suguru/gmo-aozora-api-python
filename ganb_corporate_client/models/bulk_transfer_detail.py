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

class BulkTransferDetail(object):
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
        'transfer_status': 'str',
        'transfer_status_name': 'str',
        'transfer_type_name': 'str',
        'remitter_code': 'str',
        'is_fee_free_use': 'bool',
        'is_fee_point_use': 'bool',
        'point_name': 'str',
        'fee_later_payment_flg': 'bool',
        'total_fee': 'str',
        'total_debit_amount': 'str',
        'transfer_applies': 'list[TransferApply]',
        'transfer_accepts': 'list[TransferAccept]',
        'bulktransfer_responses': 'list[BulkTransferResponse]'
    }

    attribute_map = {
        'transfer_status': 'transferStatus',
        'transfer_status_name': 'transferStatusName',
        'transfer_type_name': 'transferTypeName',
        'remitter_code': 'remitterCode',
        'is_fee_free_use': 'isFeeFreeUse',
        'is_fee_point_use': 'isFeePointUse',
        'point_name': 'pointName',
        'fee_later_payment_flg': 'feeLaterPaymentFlg',
        'total_fee': 'totalFee',
        'total_debit_amount': 'totalDebitAmount',
        'transfer_applies': 'transferApplies',
        'transfer_accepts': 'transferAccepts',
        'bulktransfer_responses': 'bulktransferResponses'
    }

    def __init__(self, transfer_status=None, transfer_status_name=None, transfer_type_name=None, remitter_code=None, is_fee_free_use=None, is_fee_point_use=None, point_name=None, fee_later_payment_flg=None, total_fee=None, total_debit_amount=None, transfer_applies=None, transfer_accepts=None, bulktransfer_responses=None):  # noqa: E501
        """BulkTransferDetail - a model defined in Swagger"""  # noqa: E501
        self._transfer_status = None
        self._transfer_status_name = None
        self._transfer_type_name = None
        self._remitter_code = None
        self._is_fee_free_use = None
        self._is_fee_point_use = None
        self._point_name = None
        self._fee_later_payment_flg = None
        self._total_fee = None
        self._total_debit_amount = None
        self._transfer_applies = None
        self._transfer_accepts = None
        self._bulktransfer_responses = None
        self.discriminator = None
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if transfer_status_name is not None:
            self.transfer_status_name = transfer_status_name
        if transfer_type_name is not None:
            self.transfer_type_name = transfer_type_name
        if remitter_code is not None:
            self.remitter_code = remitter_code
        if is_fee_free_use is not None:
            self.is_fee_free_use = is_fee_free_use
        if is_fee_point_use is not None:
            self.is_fee_point_use = is_fee_point_use
        if point_name is not None:
            self.point_name = point_name
        if fee_later_payment_flg is not None:
            self.fee_later_payment_flg = fee_later_payment_flg
        if total_fee is not None:
            self.total_fee = total_fee
        if total_debit_amount is not None:
            self.total_debit_amount = total_debit_amount
        if transfer_applies is not None:
            self.transfer_applies = transfer_applies
        if transfer_accepts is not None:
            self.transfer_accepts = transfer_accepts
        if bulktransfer_responses is not None:
            self.bulktransfer_responses = bulktransfer_responses

    @property
    def transfer_status(self):
        """Gets the transfer_status of this BulkTransferDetail.  # noqa: E501

        振込ステータス<br>半角数字<br>2:申請中、3:差戻、4:取下げ、5:期限切れ、8:承認取消/予約取消、<br>11:予約中、12:手続中、13:リトライ中、<br>20:手続済、30:不能・組戻あり、40:手続不成立<br>  # noqa: E501

        :return: The transfer_status of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this BulkTransferDetail.

        振込ステータス<br>半角数字<br>2:申請中、3:差戻、4:取下げ、5:期限切れ、8:承認取消/予約取消、<br>11:予約中、12:手続中、13:リトライ中、<br>20:手続済、30:不能・組戻あり、40:手続不成立<br>  # noqa: E501

        :param transfer_status: The transfer_status of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._transfer_status = transfer_status

    @property
    def transfer_status_name(self):
        """Gets the transfer_status_name of this BulkTransferDetail.  # noqa: E501

        振込ステータス名<br>全角文字<br>  # noqa: E501

        :return: The transfer_status_name of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._transfer_status_name

    @transfer_status_name.setter
    def transfer_status_name(self, transfer_status_name):
        """Sets the transfer_status_name of this BulkTransferDetail.

        振込ステータス名<br>全角文字<br>  # noqa: E501

        :param transfer_status_name: The transfer_status_name of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._transfer_status_name = transfer_status_name

    @property
    def transfer_type_name(self):
        """Gets the transfer_type_name of this BulkTransferDetail.  # noqa: E501

        種類<br>全角文字<br>総合振込　を表示<br>  # noqa: E501

        :return: The transfer_type_name of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._transfer_type_name

    @transfer_type_name.setter
    def transfer_type_name(self, transfer_type_name):
        """Sets the transfer_type_name of this BulkTransferDetail.

        種類<br>全角文字<br>総合振込　を表示<br>  # noqa: E501

        :param transfer_type_name: The transfer_type_name of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._transfer_type_name = transfer_type_name

    @property
    def remitter_code(self):
        """Gets the remitter_code of this BulkTransferDetail.  # noqa: E501

        会社コード(振込依頼人コード)<br>半角文字<br>銀行側で番号を付与している場合のみ表示<br>該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :return: The remitter_code of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._remitter_code

    @remitter_code.setter
    def remitter_code(self, remitter_code):
        """Sets the remitter_code of this BulkTransferDetail.

        会社コード(振込依頼人コード)<br>半角文字<br>銀行側で番号を付与している場合のみ表示<br>該当する情報が無い場合は項目自体を設定しません<br>  # noqa: E501

        :param remitter_code: The remitter_code of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._remitter_code = remitter_code

    @property
    def is_fee_free_use(self):
        """Gets the is_fee_free_use of this BulkTransferDetail.  # noqa: E501

        振込無料回数利用可否<br>振込利用回数の利用可否（無料回数の利用可否の設定であり、実際の利用有無ではありません）<br>総合振込では無料回数は利用できないため、常にfalse<br>  # noqa: E501

        :return: The is_fee_free_use of this BulkTransferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_fee_free_use

    @is_fee_free_use.setter
    def is_fee_free_use(self, is_fee_free_use):
        """Sets the is_fee_free_use of this BulkTransferDetail.

        振込無料回数利用可否<br>振込利用回数の利用可否（無料回数の利用可否の設定であり、実際の利用有無ではありません）<br>総合振込では無料回数は利用できないため、常にfalse<br>  # noqa: E501

        :param is_fee_free_use: The is_fee_free_use of this BulkTransferDetail.  # noqa: E501
        :type: bool
        """

        self._is_fee_free_use = is_fee_free_use

    @property
    def is_fee_point_use(self):
        """Gets the is_fee_point_use of this BulkTransferDetail.  # noqa: E501

        ポイント利用可否<br>ポイント会社の利用可否<br>  # noqa: E501

        :return: The is_fee_point_use of this BulkTransferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_fee_point_use

    @is_fee_point_use.setter
    def is_fee_point_use(self, is_fee_point_use):
        """Sets the is_fee_point_use of this BulkTransferDetail.

        ポイント利用可否<br>ポイント会社の利用可否<br>  # noqa: E501

        :param is_fee_point_use: The is_fee_point_use of this BulkTransferDetail.  # noqa: E501
        :type: bool
        """

        self._is_fee_point_use = is_fee_point_use

    @property
    def point_name(self):
        """Gets the point_name of this BulkTransferDetail.  # noqa: E501

        ポイント会社名<br>全角文字<br>  # noqa: E501

        :return: The point_name of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._point_name

    @point_name.setter
    def point_name(self, point_name):
        """Sets the point_name of this BulkTransferDetail.

        ポイント会社名<br>全角文字<br>  # noqa: E501

        :param point_name: The point_name of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._point_name = point_name

    @property
    def fee_later_payment_flg(self):
        """Gets the fee_later_payment_flg of this BulkTransferDetail.  # noqa: E501

        手数料後払区分<br>「true=後払い」以外の場合は項目自体を設定しません<br>  # noqa: E501

        :return: The fee_later_payment_flg of this BulkTransferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._fee_later_payment_flg

    @fee_later_payment_flg.setter
    def fee_later_payment_flg(self, fee_later_payment_flg):
        """Sets the fee_later_payment_flg of this BulkTransferDetail.

        手数料後払区分<br>「true=後払い」以外の場合は項目自体を設定しません<br>  # noqa: E501

        :param fee_later_payment_flg: The fee_later_payment_flg of this BulkTransferDetail.  # noqa: E501
        :type: bool
        """

        self._fee_later_payment_flg = fee_later_payment_flg

    @property
    def total_fee(self):
        """Gets the total_fee of this BulkTransferDetail.  # noqa: E501

        合計手数料<br>半角数字<br>振り込み完了時以外は、予定の手数料<br>  # noqa: E501

        :return: The total_fee of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this BulkTransferDetail.

        合計手数料<br>半角数字<br>振り込み完了時以外は、予定の手数料<br>  # noqa: E501

        :param total_fee: The total_fee of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._total_fee = total_fee

    @property
    def total_debit_amount(self):
        """Gets the total_debit_amount of this BulkTransferDetail.  # noqa: E501

        合計出金金額<br>半角数字<br>手数料+振込金額　ただし、振込完了時以外は、予定の手数料<br>  # noqa: E501

        :return: The total_debit_amount of this BulkTransferDetail.  # noqa: E501
        :rtype: str
        """
        return self._total_debit_amount

    @total_debit_amount.setter
    def total_debit_amount(self, total_debit_amount):
        """Sets the total_debit_amount of this BulkTransferDetail.

        合計出金金額<br>半角数字<br>手数料+振込金額　ただし、振込完了時以外は、予定の手数料<br>  # noqa: E501

        :param total_debit_amount: The total_debit_amount of this BulkTransferDetail.  # noqa: E501
        :type: str
        """

        self._total_debit_amount = total_debit_amount

    @property
    def transfer_applies(self):
        """Gets the transfer_applies of this BulkTransferDetail.  # noqa: E501

        振込申請情報<br>振込申請情報のリスト<br>  # noqa: E501

        :return: The transfer_applies of this BulkTransferDetail.  # noqa: E501
        :rtype: list[TransferApply]
        """
        return self._transfer_applies

    @transfer_applies.setter
    def transfer_applies(self, transfer_applies):
        """Sets the transfer_applies of this BulkTransferDetail.

        振込申請情報<br>振込申請情報のリスト<br>  # noqa: E501

        :param transfer_applies: The transfer_applies of this BulkTransferDetail.  # noqa: E501
        :type: list[TransferApply]
        """

        self._transfer_applies = transfer_applies

    @property
    def transfer_accepts(self):
        """Gets the transfer_accepts of this BulkTransferDetail.  # noqa: E501

        振込受付情報<br>振込受付情報のリスト<br>該当する情報が無い場合は空のリストを返却<br>  # noqa: E501

        :return: The transfer_accepts of this BulkTransferDetail.  # noqa: E501
        :rtype: list[TransferAccept]
        """
        return self._transfer_accepts

    @transfer_accepts.setter
    def transfer_accepts(self, transfer_accepts):
        """Sets the transfer_accepts of this BulkTransferDetail.

        振込受付情報<br>振込受付情報のリスト<br>該当する情報が無い場合は空のリストを返却<br>  # noqa: E501

        :param transfer_accepts: The transfer_accepts of this BulkTransferDetail.  # noqa: E501
        :type: list[TransferAccept]
        """

        self._transfer_accepts = transfer_accepts

    @property
    def bulktransfer_responses(self):
        """Gets the bulktransfer_responses of this BulkTransferDetail.  # noqa: E501

        総合振込レスポンス情報<br>総合振込レスポンス情報のリスト<br>該当する情報が無い場合は空のリストを返却<br>  # noqa: E501

        :return: The bulktransfer_responses of this BulkTransferDetail.  # noqa: E501
        :rtype: list[BulkTransferResponse]
        """
        return self._bulktransfer_responses

    @bulktransfer_responses.setter
    def bulktransfer_responses(self, bulktransfer_responses):
        """Sets the bulktransfer_responses of this BulkTransferDetail.

        総合振込レスポンス情報<br>総合振込レスポンス情報のリスト<br>該当する情報が無い場合は空のリストを返却<br>  # noqa: E501

        :param bulktransfer_responses: The bulktransfer_responses of this BulkTransferDetail.  # noqa: E501
        :type: list[BulkTransferResponse]
        """

        self._bulktransfer_responses = bulktransfer_responses

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
        if issubclass(BulkTransferDetail, dict):
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
        if not isinstance(other, BulkTransferDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
