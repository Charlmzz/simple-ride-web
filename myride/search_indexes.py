import datetime
from haystack import indexes
from .models import Ride


# 类名必须为需要检索的Model_name+Index，这里需要检索Post，所以创建PostIndex
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # 创建一个text字段，有且只能有一个document=True
    text = indexes.CharField(document=True, use_template=True)
    # 对标题，内容进行搜索，以下两句貌似没啥用，不要也可以，我是没搞清楚
    author = indexes.CharField(model_attr='author')  # 创建一个author字段
    publish = indexes.DateTimeField(model_attr='publish')  # 创建一个publish字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return Post

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(publish__lte=datetime.datetime.now())