pip install -r requirements.txt

在virtual environment里面把/lib/python3.9/site-packages/django/forms/widgets.py 里面build_attrs()加上一个**kwargs
把ckeditor目录下，widget.py里面render()加上一个renderer=None
