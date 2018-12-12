var cur_page = 1; // 当前页
var total_page = 1;  // 总页数
var data_querying = true;   // 是否正在向后台获取数据。为true时不能上拉刷新。反之，可以上拉刷新


$(function () {
    // 当主页加载完成后，立即主动的获取新闻列表数据
    updateNewsData();

    //页面滚动加载相关
    $(window).scroll(function () {

        // 浏览器窗口高度
        var showHeight = $(window).height();

        // 整个网页的高度
        var pageHeight = $(document).height();

        // 页面可以滚动的距离
        var canScrollHeight = pageHeight - showHeight;

        // 页面滚动了多少,这个是随着页面滚动实时变化的
        var nowScroll = $(document).scrollTop();

        if ((canScrollHeight - nowScroll) < 100) {
            // TODO 判断页数，去更新博客数据
            if (!data_querying) {
                // 加载下一页数据
                data_querying = true; // 表示正在加载数据
                cur_page += 1;

                // 判断是否是最后一页，如果不是最后一页可以继续加载下一页
                if (cur_page < total_page) {
                    updateNewsData()
                }
            }
        }
    })
})

function updateNewsData() {
    // TODO 更新博客数据
    var params = {

        'page': cur_page
        // 不需要传入per_page,因为默认10
    };

    $.get('/index/bogs_list', params, function (response) {
        // 能够执行到这里说明数据加载完成，有可能失败，有可能成功
        data_querying = false; // 表示没有正在加载数据,可以上拉

        if (response.errno == '0') {
            // 在响应成功后，需要记录分页之后的总页数（服务器告诉前端一共多少页）
            total_page = response.data.total_page;

            // 清空第一页数据:为了不让前一个分类的第一页数据追加到下一个分类中
            if (cur_page == 1) {
                $(".list_con").html("");
            }

            // 获取数据成功，使用新的数据渲染界面
            for (var i = 0; i < response.data.blogs_list_dict.length; i++) {
                var blogs = response.data.blogs_list_dict[i]

                var content2 = '<li class="index_arc_item">'
                content2 += '<a href="#" class="pic"> <img class="lazyload" data-original="temp/art.jpg" alt="应该选"/></a>'
                content2 += '<h4 class="title"><a href="article_detail.html">'+blogs.title+'</a></h4>'
                content2 += '<div class="date_hits">'
                content2 += '<span>老王</span> <span>2017-02-24</span><span><a href="/article-lists/10.html">程序人生</a></span>'
                content2 += '<p class="hits"><i class="Hui-iconfont" title="点击量">&#xe6c1;</i>'+blogs.clicks+'° </p>'
                content2 += '<p class="commonts"><i class="Hui-iconfont" title="点击量">&#xe622;</i> <span class="cy_cmt_count">20</span> </p>'
                content2 += '</div>'
                content2 += '<div class="desc">'+blogs.content+'</div>'
                content2 += ' </li>'

                // append表示将新的数据追加到旧的数据的后面；html表示将新的数据替换到旧的数据的后面；
                $(".index_arc").append(content)
            }
        } else {
            alert(response.errmsg);
        }
    });
}
