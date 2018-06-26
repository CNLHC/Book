
# 豆瓣api中正常返回的信息
normal = '{"rating":{"max":10,"numRaters":10,"average":"6.2","min":0},"subtitle":"","author":["钟锡华","周岳明"],"pubdate":"2010-2","tags":[{"count":5,"name":"物理","title":"物理"},{"count":2,"name":"教材","title":"教材"},{"count":1,"name":"物理-大學","title":"物理-大學"},{"count":1,"name":"普通物理","title":"普通物理"},{"count":1,"name":"啊啊啊","title":"啊啊啊"},{"count":1,"name":"北大","title":"北大"}],"origin_title":"","image":"https://img1.doubanio.com\\/view\\/subject\\/m\\/public\\/s4598157.jpg","binding":"","translator":[],"catalog":"","pages":"325","images":{"small":"https://img1.doubanio.com\\/view\\/subject\\/s\\/public\\/s4598157.jpg","large":"https://img1.doubanio.com\\/view\\/subject\\/l\\/public\\/s4598157.jpg","medium":"https://img1.doubanio.com\\/view\\/subject\\/m\\/public\\/s4598157.jpg"},"alt":"https:\\/\\/book.douban.com\\/subject\\/4717389\\/","id":"4717389","publisher":"","isbn10":"7301160976","isbn13":"9787301160978","title":"大学物理通用教程普通高等教育十一五国家级规划教材·大学物理通用教程","url":"https:\\/\\/api.douban.com\\/v2\\/book\\/4717389","alt_title":"","author_intro":"","summary":"《大学物理通用教程普通高等教育十一五国家级规划教材·大学物理通用教程:力学(第2版)》内容简介：全套教程包括《力学》、《热学》、《电磁学》、《光学》、《近代物理》和《习题指导》。\\n《力学》一书包括质点运动学、牛顿力学基本定律、动量定理、机械能定理、角动量定理、质心力学定理、刚体力学、振动、波动、流体力学和哈密顿原理，共计十一章，并配有181道习题。《大学物理通用教程普通高等教育十一五国家级规划教材·大学物理通用教程:力学(第2版)》以力学基本规律和概念、典型现象和应用为主体内容，同时注重知识的扩展和适度的深化，包括学科发展前沿评介、某些历史背景和注记，以及对学生在学习上的指导。崇尚结构、承袭传统、力求平实、注重扩展是《大学物理通用教程普通高等教育十一五国家级规划教材·大学物理通用教程:力学(第2版)》的特色。这是一本通用教程，大体上与讲授36课时相匹配，适合于理、工、农、医和师范院系使用。","series":{"id":"33145","title":"大学物理通用教程"},"price":"20.00元"}'

# 豆瓣api中的错误信息
error = """{ "code":113, "msg":"required_parameter_is_missing: client_id", "request":"GET /shuo/statuses/232323" } """

# 错误格式的json
error_json = """"cde:113, "msg":"required_parameter_is_missing: client_id", "request":"GET /shuo/statuses/232323" } """


class url():
    Wrong_URL = 1
    Wrong_Json = "wrong_json_url"
    normal = "normal_url"
    Exceed_limtation = "exceed_limation_url"


def get(*args, **kwargs):
    class fake_get_method():
        def __init__(self, text, status_code=200):
            self.text = text
            self.status_code = status_code

    # 注意函数会改变传入基地址，所以此处需要检查子串
    if url.Wrong_Json in args[0]:
        return fake_get_method(text=error_json)

    elif url.normal in args[0]:
        return fake_get_method(text=normal, status_code=200)

    elif url.Exceed_limtation in args[0]:
        return fake_get_method(text=error, status_code=403)
