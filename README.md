# 使用过的模块名

1：urllib2 只是python内部自带的

2：beautifulsoup

3：yolk 查看本地安装了那些第三方模块

4：pylint 代码检查

5：pymysql 连接mysql的

6：Django python的web高级框架



## 鸡杂面

1：

```
__init__.py 文件是用来声明模块的文件，有了它 就能将文件夹声明为一个模块，可以直接在代码中引用，内容一般为空。
```

- 常见应用

  ```
  python manage.py startapp blog
  ```

  ​

2：python   templates    学习使用自带的DLT，  还有比较流行的jinja2。

- render(request, 'index.html', argument3)
  - argument3  支持一个dict类型的参数

3：Models

- 封装了操作数据库 的SQL语句
- 可以操作数据库

4：2017-07-11， 今天遇到一个问题，想使用Django链接 mysql，但是配置完 settings.py文件后，

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
```

执行：

python manage.py shell

命令报错：

```
Unhandled exception in thread started by <function wrapper at 0x030376B0>
Traceback (most recent call last):
  File "C:\Python27\lib\site-packages\django\utils\autoreload.py", line 226, in
wrapper
    fn(*args, **kwargs)
  File "C:\Python27\lib\site-packages\django\core\management\commands\runserver.
py", line 113, in inner_run
    autoreload.raise_last_exception()
  File "C:\Python27\lib\site-packages\django\utils\autoreload.py", line 249, in
raise_last_exception
    six.reraise(*_exception)
  File "C:\Python27\lib\site-packages\django\utils\autoreload.py", line 226, in
wrapper
    fn(*args, **kwargs)
  File "C:\Python27\lib\site-packages\django\__init__.py", line 27, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Python27\lib\site-packages\django\apps\registry.py", line 108, in pop
ulate
    app_config.import_models(all_models)
  File "C:\Python27\lib\site-packages\django\apps\config.py", line 199, in impor
t_models
    self.models_module = import_module(models_module_name)
  File "C:\Python27\lib\importlib\__init__.py", line 37, in import_module
    __import__(name)
  File "C:\Python27\lib\site-packages\django\contrib\auth\models.py", line 4, in
 <module>
    from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
  File "C:\Python27\lib\site-packages\django\contrib\auth\base_user.py", line 52
, in <module>
    class AbstractBaseUser(models.Model):
  File "C:\Python27\lib\site-packages\django\db\models\base.py", line 119, in __
new__
    new_class.add_to_class('_meta', Options(meta, app_label))
  File "C:\Python27\lib\site-packages\django\db\models\base.py", line 316, in ad
d_to_class
    value.contribute_to_class(cls, name)
  File "C:\Python27\lib\site-packages\django\db\models\options.py", line 214, in
 contribute_to_class
    self.db_table = truncate_name(self.db_table, connection.ops.max_name_length(
))
  File "C:\Python27\lib\site-packages\django\db\__init__.py", line 33, in __geta
ttr__
    return getattr(connections[DEFAULT_DB_ALIAS], item)
  File "C:\Python27\lib\site-packages\django\db\utils.py", line 211, in __getite
m__
    backend = load_backend(db['ENGINE'])
  File "C:\Python27\lib\site-packages\django\db\utils.py", line 115, in load_bac
kend
    return import_module('%s.base' % backend_name)
  File "C:\Python27\lib\importlib\__init__.py", line 37, in import_module
    __import__(name)
  File "C:\Python27\lib\site-packages\django\db\backends\mysql\base.py", line 28
, in <module>
    raise ImproperlyConfigured("Error loading MySQLdb module: %s" % e)
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No mo
dule named MySQLdb
```

##### 想办法解决哇：

首先想到google错文， "Error loading MySQLdb module: %s" % e

搜索结果大概是：

I had the same error and `pip install MySQL-python` solved it for me.

大概意思应该是需要下载一个第三方模块来链接mysql，但是我在我的cmd里面执行：

```
pip install MySQL-python
```

也是报错：

```
C:\Users\Administrator\Desktop\django\myblog>pip install MySQL-pythoner
Collecting MySQL-pythoner
  Could not find a version that satisfies the requirement MySQL-pythoner (from v
ersions: )
No matching distribution found for MySQL-pythoner
```

这里我记得之前装过**MySQL-python**，但是装不上，是版本的问题，我python版本是2.7.13

后来装了一个**pymysql**代替，后面又google：

看到这个搜索结果，感觉应该是对了

In settings.py, add following just below `import os`.

```
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass
```

#### ------------------------------------最后成功解决问题----------------------------

```
$ python manage.py makemigrations
$ python manage.py migrate
```

最后 创建好数据库 中的表。