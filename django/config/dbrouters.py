import random


class MyDBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        print(f'{model._meta.app_label}, {model._meta.model_name}')
        if model._meta.model_name == "posttrash": # 모델명으로 구분
            return 'external'
        if model._meta.app_label == 'blog': # app 이름으로 구분
            return 'default'
        return 'default'
        # 아래 처럼 랜덤하게 접속 DB를 바꿔 버릴 수도 있음
        # return random.choice(['default', 'external'])

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.model_name == "posttrash": # 모델명으로 구분
            return 'external'
        if model._meta.app_label == 'blog': # app 이름으로 구분
            return 'default'
        return 'default'
        # return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        # if obj1._meta.app_label == 'blog' or \
        #         obj2._meta.app_label == '':
        #     return True
        # return None
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'blog' and model_name == 'posttrash':
            return db == 'external'
        else:
            return db == 'default'
        return None
