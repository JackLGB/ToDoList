def Singleton(cls):
    """
    单例装饰器
    :param cls:
    :return:
    """
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton
