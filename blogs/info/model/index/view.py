from . import index
from flask import render_template, request, jsonify
import response_code
from models import User, Blogs


def userinfo():

    user = User.query.filter(User.is_admin==True).first()
    return user

@index.route('/bogs_list')
def blogs():
    """提供主页新闻列表数据
      1.接受参数（,当前第几页，每页多少条）
      2.校验参数（判断以上参数是否是数字）
      3.根据参数查询用户需要的数据:根据博客发布时间倒叙，最后时限分页
      4.构造响应的博客数据
      5.响应博客数据
      """
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 10)

    if (type(page),  type(per_page)) != int:
        return jsonify(errno=response_code.RET.PWDERR, errmsg='参数有误')

    paginate = Blogs.query.order_by(Blogs.create_time.desc()).paginate(page, per_page,False)
    blogs_list = paginate.items
    # 4.2 获取总页数：为了实现上拉刷新
    total_page = paginate.pages
    # 4.3 当前在第几页
    current_page = paginate.page
    blogs_list_dict = []
    for blogs_dict in blogs_list:
        blogs_list_dict.append(blogs_dict.to_basic_dict())

    data = {
        'blogs_list_dict': blogs_list_dict,
        'total_page': total_page,
        'current_page': current_page
    }
    return jsonify(errno=response_code.RET.OK, errmsg='OK',data=data)

@index.route('/')
def index_view():
    user = userinfo()
    return render_template('index.html',data=user)