# users/adminx.py

import xadmin

from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 修改title
    site_title = '德语早教后台管理界面'
    # 修改footer
    site_footer = '德语早教'
    # 收起菜单
    menu_style="accordion"



class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_type', 'send_time']

    search_fields = ['code', 'email', 'send_type']

    list_filter = ['code', 'email', 'send_type', 'send_time']

    model_icon = 'fa fa-envelope'

class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']
    model_icon = 'fa fa-picture-o'

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)