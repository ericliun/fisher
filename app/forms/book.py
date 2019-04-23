#BookForm.py
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length, NumberRange,DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1,max=30),DataRequired()])
    #DataRequired()方法要求用户必须输入，且不能为空格
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)