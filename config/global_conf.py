#!/usr/bin/env python
# -*- coding: utf-8 -*-

USER_TYPE = {"1":"平台", "2":"商家"}

RESULT_404 = {"status": 0, "message": "页面不存在"}

NO_PERMISSION = {"status": 0, "message": "权限不够"}

PAGE_CAPACITY = 20

PRO_PAGE_CAPACITY = 200


yes_no = {
    '0' : '否',
    '1' : '是'
}
public_status = {
    '0' : '失效',
    '1' : '<span class="green">有效</span>'
}



data = 'hbdata/',  # 项目资源文件目录 html/hbdat}
pk_os = {
    '1' : 'android',
    '2' : 'ios',
}
admin_status = {
    '0' : '正常',
    '1' : '停用',
    '2' : '<span class="red">锁定</span>'
}
user_status = {
    '0' : '非正常',
    '1' : '有效',
    '2' : '失效'
}
activity_type_option = {
    '1' : '左边',
    '2'  : '右上',
    '3'  : '右下',
}
pay_status = {
    '-1' : '作弊',
    '0'  : '非法请求',
    '1' : '待审核',
    '2'  : '审核通过',
    '3'  : '处理完成',
    '4'  : '处理出错',
    '5'  : '充值中',
    '6'  : '已退款',
    '7'  : '待退款',
    '8'  : '暂不处理'
}
pay_type = {
    '1' : '充值卡',
    '2'  : 'Q币',
    '3'  : '支付宝提现',
    '4'  : 'wifi上网券',
    '5'  : 'Q币小额兑换',

    '10'  : '兑吧',
},


ad_top = {
    '0' : '否',
    '1' : '<span class="red">是</span>'
}
ad_status = {
    '0' : '无效',
    '1' : '<span class="green">有效</span>'
}
ad_z_status = {
    '0' : '未处理',
    '1' : '已上架',
    '2' : '已下架'
}
hongbao_status = {
    '0' : '未发送',
    '1' : '<span class="red">发送失败</span>',
    '2' : '<span class="green">成功</span>',
    '3' : '<span class="red">失败</span>'
}
channel_set_status = {
    '0' : '失效',
    '1' : '<span class="green">有效</span>'
}
message_os = {
    '0' : 'android/ios',
    '1' : 'android',
    '2' : 'iOS',
}
message_status = {
    '0' : '待审核',
    '1' : '已审核',
    '2' : '<span class="green">发送成功</span>',
    '3' : '<span class="red">发送失败</span>',
    '4' : '处理成功'
}

message_notify = {
    '0' : '否',
    '1' : '<span class="green">是</span>'
}

is_public = {
    '0' : '私有',
    '1' : '公开',
}

message_type = {
    '0' : '私有',
    '1' : '公共',
}
message_detail_status = {
    '0' : '未发送',
    '1' : '<span class="green">发送成功</span>',
    '2' : '<span class="red">发送失败</span>'
}
device_modify_status = {
    '0' : '失败',
    '1' : '<span class="green">成功</span>'
}
menu_status = {
    '0' : '失效',
    '1' : '<span class="green">有效</span>'
}

public_os = {
    '0' : 'android/iOS',
    '1' : 'android',
    '2' : 'iOS',
}
jojo_status_option = {
    '0' : '待上传',
    '1' : '待审核',
    '2' : '待上线',
    '3' : '上线',
    '4' : '被下线',
    '5' : '被切',
}

notification_status = {
    '0' : '待审核',
    '1' : '已审核',
    '2' : '处理成功',
    '3' : '发送成功',
    '4' : '发送失败'
}
exchange_select = {
    '1' : '用户ID',
    '2' : '兑换ID',
    '3' : '手机号',
    '4' : '物品ID',
    '5' : '设备ID',
    '6' : '交易IP',
    '7' : '操作人',
}
is_images = {
    '0' : '否',
    '1' : '是'
}
pk_status = {
    '0' : '待审核',
    '1' : '<span class="green">已审核</span>'
}
pk_scale = {
    '1' : '10%',
    '2' : '20%',
    '3' : '30%',
    '4' : '40%',
    '5' : '50%',
    '6' : '60%',
    '7' : '70%',
    '8' : '80%',
    '9' : '90%',
    '10' : '100%'
}
version_status = {
    '0' : '待审核',
    '1' : '<span class="green">已审核</span>'
}
o_product_status = {
    '0' : '待上架',
    '1' : '<span class="green">已上架</span>',
    '2' : '<span class="red">已下架</span>'
}
o_product_lottery_status = {
    '0' : '未开始',
    '1' : '<span class="green">进行中</span>',
    '2' : '<span class="blue">倒计时</span>',
    '3' : '<span class="brown">已揭晓</span>',
    '4' : '<span class="red">已下线</span>',
}
o_luck_user_status = {
    '0' : '未填写',
    '1' : '<span class="green">待发货</span>',
    '2' : '<span class="brown">已发货</span>',
    '3' : '<span class="blue">已收货</span>',
    '4' : '<span class="yellow">已晒单</span>',
}
o_logistics_option = {
    '1' : '申通快递',
    '10' : '优速快递',
    '11' : '京东',
    '2' : '顺丰快递',
    '3' : '圆通快递',
    '4' : '韵达快递',
    '5' : '汇通快递',
    '6' : '天天快递',
    '7' : 'EMS快递',
    '9' : '虚拟物品',
}
o_logistics_key_value = {
    '申通快递' : 'shentong',
    '优速快递' : 'youshuwuliu',
    '顺丰快递' : 'shunfeng',
    '圆通快递' : 'yuantong',
    '韵达快递' : 'yunda',
    '汇通快递' : 'huitongkuaidi',
    '天天快递' : 'tiantian',
    'EMS快递' : 'ems',
}
o_activity_type_option = {
    #// '1' : '未中奖比例返现',
    '4' : '充值送夺宝币',
    '5' : '未中奖随机返现',
    #// '2' : '同商品购买N次赠M次',
    #// '3' : '购买主商品赠送其他商品夺宝号码',
}
o_activity_limit_type_option = {
    '1' : '总人次上限',
    '2' : '用户数上限',
    '3' : '单笔订单赠送上限',
    '4' : '单个用户赠送上限',
    '5' : '无上限',
}
o_pay_back_rate_option = {

    '0.01' : '1%',
    '0.02' : '2%',
    '0.03' : '3%',
    '0.04' : '4%',
    '0.05' : '5%',
    '0.06' : '6%',
    '0.07' : '7%',
    '0.08' : '8%',
    '0.09' : '9%',

    '0.10' : '10%',
    '0.11' : '11%',
    '0.12' : '12%',
    '0.13' : '13%',
    '0.14' : '14%',
    '0.15' : '15%',
    '0.16' : '16%',
    '0.17' : '17%',
    '0.18' : '18%',
    '0.19' : '19%',

    '0.20' : '20%',
    '0.21' : '21%',
    '0.22' : '22%',
    '0.23' : '23%',
    '0.24' : '24%',
    '0.25' : '25%',
    '0.26' : '26%',
    '0.27' : '27%',
    '0.28' : '28%',
    '0.29' : '29%',
}
o_present_rate_option = {
    '1:1' : '1:1',
    '2:1' : '2:1',
    '3:1' : '3:1',
    '4:1' : '4:1',
    '5:1' : '5:1',
    '6:1' : '6:1',
    '7:1' : '7:1',
    '8:1' : '8:1',
    '9:1' : '9:1',
    '10:1' : '10:1',
    '11:1' : '11:1',
    '12:1' : '12:1',
    '13:1' : '13:1',
    '14:1' : '14:1',
    '15:1' : '15:1',
    '16:1' : '16:1',
    '17:1' : '17:1',
    '18:1' : '18:1',
    '19:1' : '19:1',
    '20:1' : '20:1',
}
pay_back_status_option = {
    '2' : '返现成功',
    '3' : '返现失败',
    '4' : '消息发送成功',
    '5' : '消息发送失败',
}
one_order_status_option = {
    '0' : '待付款',
    '1' : '付款完毕且已经处理',
    '-1' : '异常订单 扣款失败',
    '-2' : '订单取消',
}
honbao_type_option = {
    '1' : '奖励',
    '2' : '补偿',
}
share_remark_option = {
    '1' : '[请上传清晰的奖品实拍照片]',
    '2' : '[请上传充值到账截图]'
}
share_pay_back_option = {
    '0' : '0元',
    '1' : '1元',
    '2' : '2元',
    '3' : '3元',
    '4' : '4元',
    '5' : '5元',
    '6' : '6元',
    '7' : '7元',
    '8' : '8元',
    '9' : '9元',
}
od_provider_option = {
    'gongying1' : '供应商1',
    'gongying2' : '供应商2',
    'gongying3' : '供应商3',
}
